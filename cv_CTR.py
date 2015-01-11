__author__ = 'Lal'

import random
import time

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import log_loss
from pybrain.datasets import ClassificationDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import SoftmaxLayer

from AvazuCTR.AvazuCTR.build_features import feature_builder


def map_to_features(comps,train):
    feature_vector=[0]*15

    banner=int(comps[3+train])
    #banner
    if banner==0:
        feature_vector[0]=1
    elif banner==1:
        feature_vector[1]=1
    elif banner==2:
        feature_vector[2]=1
    elif banner==3:
        feature_vector[3]=1
    elif banner==4:
        feature_vector[4]=1
    elif banner==5:
        feature_vector[5]=1
    elif banner==7:
        feature_vector[6]=1

    c18=int(comps[19+train])
    #c18
    if c18==0:
        feature_vector[7]=1
    elif c18==1:
        feature_vector[8]=1
    elif c18==2:
        feature_vector[9]=1
    elif c18==3:
        feature_vector[10]=1

    did=comps[10+train]
    #device id
    if did=='a99f214a':
        feature_vector[11]=1
    elif did=='c357dbff':
        feature_vector[12]=1
    elif did=='936e92fb':
        feature_vector[13]=1
    else:
        feature_vector[14]=1

    return feature_vector

def train_nn(train_features,train_targets):
    nn=buildNetwork(15,15,2,outclass=SoftmaxLayer)
    training_set=ClassificationDataSet(15,1)

    for k in range(len(train_targets)):
        training_set.appendLinked(train_features[k],[train_targets[k]])
    training_set._convertToOneOfMany()
    print 'TRAINING NEURAL NET...'
    start=time.time()
    trainer=BackpropTrainer(nn,training_set)
    trainer.train()
    print 'FINISHED TRAINING...TOOK: '+str(time.time()-start)
    return trainer

def get_data_from_nn(trainer,test_features,test_targets):
    test_set=ClassificationDataSet(15)
    for k in range(len(test_features)):
        test_set.appendLinked(test_features[k],[test_targets[k]])
    return trainer.testOnClassData(dataset=test_set,return_probs=True)


def small_test():

    mapper=feature_builder()

    start=time.time()
    print 'PARSING TRAINING FILE...'
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
            if random.random()<=.025:
                comps=line.rstrip().split(',')
                #features=map_to_features(comps,1)
                features=mapper.get_fingerprint(comps)
                target=int(comps[1])
                training_features.append(features)
                training_targets.append(target)
    print 'FINISHED PARSING TRAINING FILE...TOOK: '+str(time.time()-start)
    print 'Training Set Size: '+str(len(training_targets))

    #nn_trainer=train_nn(training_features,training_targets)


    start=time.time()
    print 'TRAINING RF MODEL...'
    RF=RandomForestClassifier(n_estimators=35)
    RF.fit(training_features,training_targets)
    #rf_scores=cross_val_score(RF,training_features,training_targets,cv=4)
    print 'TRAINED MODEL...TOOK: '+str(time.time()-start)

    print 'PERFORMING VALIDATION TESTS...'
    start=time.time()
    log_errors=[]
    nn_errors=[]
    for cv in range(5):
        print 'DOING VALIDATION: '+str(cv+1)
        testing_features=[]
        testing_targets=[]
        i=0
        with open('train') as f:
            for line in f:
                i+=1
                if i==1:
                    continue
                if i%10000000==0:
                    print 'PARSED...'+str(i)
                    #break
                if random.random()<=.01:
                    comps=line.rstrip('\n').split(',')
                    #features=map_to_features(comps,1)
                    features=mapper.get_fingerprint(comps)
                    target=int(comps[1])
                    testing_features.append(features)
                    testing_targets.append(target)
        print 'TESTING SET SIZE: '+str(len(testing_targets))
        probs=RF.predict_proba(testing_features)
        loss=log_loss(testing_targets,probs)
        print 'RF LOSS: '+str(loss)
        log_errors.append(loss)
        #probability=get_data_from_nn(nn_trainer,testing_features,testing_targets)
        #nn_loss=log_loss(testing_targets,probability)
        #nn_errors.append(nn_loss)
        #print 'NN LOSS: '+str(nn_loss)
        print 'TOOK: '+str(time.time()-start)


    print 'AVERAGE RF: '+str((sum(log_errors)/float(len(log_errors))))
    print 'AVERAGE NN: '+str((sum(nn_errors)/float(len(nn_errors))))
    print 'TOOK '+str(time.time()-start)

    #print str(rf_scores)
    #print("Accuracy: %0.2f (+/- %0.2f)" % (rf_scores.mean(), rf_scores.std() * 2))

    print 'DONE!'

small_test()
