__author__ = 'Sameer Lal'
import time
import random

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from pybrain.datasets import ClassificationDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import SoftmaxLayer
from sklearn.metrics import log_loss

from AvazuCTR.AvazuCTR.build_features import feature_builder


#TODO: Run models on more balanced training set
#TODO: Isolate where errors are being made
def write_to_submission(ids,probs):
    print 'WRITING TO FILE...'
    out=open('predict.txt','w')
    out.write('id,click\n')
    for i in range(len(ids)):
        prob=probs[i][1]
        out.write(ids[i]+','+str(prob)+'\n')
    print 'WROTE TO: prediction.txt'

def get_probs_from_nn(trainer,test_features,fp_length):
    test_set=ClassificationDataSet(fp_length)
    for k in range(len(test_features)):
        test_set.appendLinked(test_features[k])
    return trainer.testOnClassData(dataset=test_set,return_probs=True)

def create_model_list(RF,EF,NN):
    model_list=[]
    if RF:
        model_list.append('RF')
    if EF:
        model_list.append('ET')
    if NN:
        model_list.append('NN')

def create_training_set(mapper,TrainingPercent):
    start=time.time()
    print 'PARSING FILE AND BUILDING SET...'
    #Build Training Set from sup Sampling
    training_features=[]
    training_targets=[]
    i=0
    with open('train') as f:
        for line in f:
            i+=1
            if i==1:
                continue
            if i%10000000==0:
                print 'PARSED...'+str(i)
                #break
            if random.random()<=TrainingPercent:
                comps=line.rstrip().split(',')
                features=mapper.get_fingerprint(comps)
                target=int(comps[1])
                training_features.append(features)
                training_targets.append(target)
    print 'FINISHED PARSING FILE...TOOK: '+str(time.time()-start)
    print 'SET SIZE: '+str(len(training_targets))
    return training_features,training_targets

def nn_train_full(training_features,training_targets,fp_length,hidden_layer=None):
    if hidden_layer is None:
        hidden_layer=fp_length
    nn=buildNetwork(fp_length,hidden_layer,2,outclass=SoftmaxLayer)
    training_set=ClassificationDataSet(fp_length,1)

    for k in range(len(training_targets)):
        training_set.appendLinked(training_features[k],[training_targets[k]])
    training_set._convertToOneOfMany()
    print 'TRAINING NEURAL NET...'
    start=time.time()
    trainer=BackpropTrainer(nn,training_set)
    trainer.train()
    print 'FINISHED TRAINING...TOOK: '+str(time.time()-start)
    return trainer

def nn_train_online(training_features,training_targets,fp_length,hidden_layer=None):
    if hidden_layer is None:
        hidden_layer=fp_length
    nn=buildNetwork(fp_length,hidden_layer,2,outclass=SoftmaxLayer)
    start=time.time()
    print 'TRAINING NEURAL NET...'
    for k in range(len(training_targets)):
        training_set=ClassificationDataSet(fp_length,1)
        training_set.appendLinked(training_features[k],[training_targets[k]])
        training_set._convertToOneOfMany()
        trainer=BackpropTrainer(nn,training_set)
        trainer.train()

    print 'FINISHED TRAINING...TOOK: '+str(time.time()-start)
    return trainer

def get_test_features(mapper):
    start=time.time()
    print 'PARSING TEST FILE...'
    test_cases=[]
    test_id=[]
    j=0
    with open('test') as f_test:
        for line in f_test:
            j+=1
            if j==1:
                continue
            if j%1000000==0:
                print 'PARSED...'+str(j)
            comps=line.rstrip('\n').split(',')
            features=mapper.get_fingerprint(comps,Train=0)
            test_cases.append(features)
            test_id.append(comps[0])
    print 'DONE PARSING TEST FILE...TOOK: '+str(time.time()-start)
    print 'Testing Set Size: '+str(len(test_cases))
    return test_id , test_cases

def perform_cv(mapper,TestingPercent,CV_Number,RF_Trained=None,ET_Trained=None,NN_Trained=None):

    RF_ERROR=[]
    ET_ERROR=[]
    NN_ERROR=[]

    for j in range(CV_Number):
        print 'PERFORMING VALIDATION '+str(j+1)+'...'
        start=time.time()
        testing_features,testing_targets=create_training_set(mapper,TestingPercent)
        print 'FINISHED BUILDING TEST SET...'

        #computing log loss on test set for RF
        if RF_Trained is not None:
            RF_probs=RF_Trained.predict_proba(testing_features)
            rferror=log_loss(testing_targets,RF_probs)
            print 'RANDOM FOREST ERROR: '+str(rferror)
            RF_ERROR.append(rferror)

        #computing log loss on test set for ET
        if ET_Trained is not None:
            ET_probs=ET_Trained.predict_proba(testing_features)
            eterror=log_loss(testing_targets,ET_probs)
            print 'EXTRA TREES ERROR: '+str(eterror)
            ET_ERROR.append(eterror)

        #computing log loss on test set for NN
        if NN_Trained is not None:
            NN_probs=get_probs_from_nn(NN_Trained,testing_features)
            nnerror=log_loss(testing_targets,NN_probs)
            print 'NN LOSS: '+str(nnerror)
            NN_ERROR.append(nnerror)
        print 'VALIDATION TOOK: '+str(time.time()-start)

    #Printing Averages
    if RF_Trained is not None:
        print 'RF AVERAGE ERROR: '+str((sum(RF_ERROR)/float(len(RF_ERROR))))
    if ET_Trained is not None:
        print 'ET AVERAGE ERROR: '+str((sum(ET_ERROR)/float(len(ET_ERROR))))
    if NN_Trained is not None:
        print 'NN AVERAGE ERROR: '+str((sum(NN_ERROR)/float(len(NN_ERROR))))





def build_and_run_model(CV=True,CV_Number=5,RandomForest=True,RF_Estimators=25,ExtraTrees=False,NeuralNet=False,NeuralNetTraining='Full',
                        TrainingPercent=.3,TestingPercent=.1,WriteOutput=False,WriteOutputType=None,FingerPrint=None):

    #CV=If Running CV Validation
    #CV_Number=Number of Validation Tests
    #Random Forest=Build Random Forest Model for validation or prediction
    #ExtraForest=Build Extra Forest Model for validation or prediction
    #NueralNet=Build Nueral Net
    #NueralNetTraining='Full' to train with mini-batch, 'Iterative' to train online
    #TrainingPercent=Percentage of Trainig Set (40M) to use in model training
    #TestingPercent=Percent of Training Set to make test validation sets
    #WriteOutput=Whether to print out output for submission using trained model
    #WriteOutputType=Which trained model to print
    #Fingerprint=Attributes for fingerprinting to use (see build_features.py for more details)

    #time
    process_start=time.time()

    #Default Fingerprint
    if FingerPrint==None:
        FingerPrint=['banner','c18','c15']
    elif FingerPrint=='all':
        FingerPrint=None

    #Setup Feature Mapper (maps categories for each click/non-click to a binary feature vector)
    mapper=feature_builder(FingerPrint)
    fplength=mapper.length

    #Build Training Set
    print 'BUILDING TRAINING SET...'
    training_features,training_targets=create_training_set(mapper,TrainingPercent)
    print 'FINISHED BUILDING TRAINING SET...'

    #create Model List
    RF=None
    ET=None
    nn_trainer=None

    #Train the Various Models
    if RandomForest:
        print 'TRAINING RANDOM FOREST...'
        rf_start=time.time()
        RF=RandomForestClassifier(n_estimators=RF_Estimators)
        RF.fit(training_features,training_targets)
        print 'DONE TRAINING MODEL...TOOK: '+str(time.time()-rf_start)
    if ExtraTrees:
        print 'TRAINING EXTRA TREES MODEL...'
        etstart=time.time()
        ET=ExtraTreesClassifier()
        ET.fit(training_features,training_targets)
        print 'DONE TRAINING MODEL...TOOK: '+str(time.time()-etstart)
    if NeuralNet:
        print 'TRAINING NEURAL NET...'
        nnstart=time.time()
        if NeuralNetTraining=='Full':
            nn_trainer=nn_train_full(training_features,training_targets,fplength)
        else:
            nn_trainer=nn_train_online(training_features,training_targets,fplength)
        print 'DONE TRAINING MODEL...TOOK: '+str(time.time()-nnstart)

    #Perform CV on Trained Models and Find Error
    if CV:
        print 'PERFORMING CROSS VALIDATIONS...'
        cv_start=time.time()
        perform_cv(mapper,TestingPercent,CV_Number,RF_Trained=RF,ET_Trained=ET,NN_Trained=nn_trainer)
        print 'FINISHED PERFORMING CV...TOOK: '+str(time.time()-cv_start)

    #If Writing the output
    if WriteOutput:
        'PERFORMING SUBMISSION PROCEDURE...'
        #Get Test Data
        test_ids, cases=get_test_features(mapper)

        #Checks to make sure model training has occurred
        if WriteOutputType=='RF':
            if RF is None:
                print 'DID NOT TRAIN RF MODEL!'
                exit(137)
            else:
                print 'PREDICTING ON CASES...'
                rfprobs=RF.predict_proba(cases)
                write_to_submission(test_ids,rfprobs)
        elif WriteOutputType=='ET':
            if ET is None:
                print 'DID NOT TRAIN ET MODEL!'
                exit(137)
            else:
                print 'PREDICTING ON CASES...'
                etprobs=ET.predict_proba(cases)
                write_to_submission(test_ids,etprobs)
        elif WriteOutputType=='NN':
            if nn_trainer is None:
                print 'DID NOT TRAIN NN MODEL!'
                exit(137)
            else:
                print 'PREDICTING ON CASES...'
                nnprobs=get_probs_from_nn(nn_trainer,cases,fplength)
                write_to_submission(test_ids,nnprobs)

    print '.......FINISHED.....'
    print 'TOTAL TIME USED: '+str(time.time()-process_start)


build_and_run_model(RandomForest=False,NeuralNet=True,NeuralNetTraining='online',TrainingPercent=.1,TestingPercent=.01,FingerPrint=['banner','c18','c19'])