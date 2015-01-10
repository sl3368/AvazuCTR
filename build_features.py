__author__ = 'Sameer Lal'
import time
from collections import defaultdict


#TODO: Include special features for when device id and device ip
class feature_builder:

    def construct_feature_dict(self,feature_list):
        feature_dict=defaultdict(bool)
        for feature in feature_list:
            feature_dict[feature]=True
        return feature_dict

    def __init__(self,feature_list=None):
        self.feature_dict={}

        #if the list of features is none, then do all
        if feature_list is None:
            self.feature_dict=defaultdict(lambda: True)
        else:
            self.feature_dict=self.construct_feature_dict(feature_list)

        #self.ad_id=set()
        self.hour=set()
        self.c1=set()
        self.banner_position=set()
        self.site_id=set()
        self.site_domain=set()
        self.site_category=set()
        self.app_id=set()
        self.app_domain=set()
        self.app_category=set()
        self.device_id=set()
        self.device_ip=set()
        self.device_model=set()
        self.device_type=set()
        self.device_conn_type=set()
        self.c14=set()
        self.c15=set()
        self.c16=set()
        self.c17=set()
        self.c18=set()
        self.c19=set()
        self.c20=set()
        self.c21=set()

        #dictionaries
        #self.ad_id_map={}
        self.hour_map={}
        self.c1_map={}
        self.banner_position_map={}
        self.site_id_map={}
        self.site_domain_map={}
        self.site_category_map={}
        self.app_id_map={}
        self.app_domain_map={}
        self.app_category_map={}
        self.device_id_map={}
        self.device_ip_map={}
        self.device_model_map={}
        self.device_type_map={}
        self.device_conn_type_map={}
        self.c14_map={}
        self.c15_map={}
        self.c16_map={}
        self.c17_map={}
        self.c18_map={}
        self.c19_map={}
        self.c20_map={}
        self.c21_map={}

        #length
        self.length=0

        #Building Sets
        print 'BUILDING SETS..'
        i=0
        start=time.time()
        with open('train') as f:
            for line in f:
                if i==0:
                    i+=1
                    continue
                comps=line.rstrip().split(',')
                #self.ad_id.update([comps[0]])
                if self.feature_dict['hour']:
                    self.hour.update([comps[2][6:]])
                if self.feature_dict['c1']:
                    self.c1.update([comps[3]])
                if self.feature_dict['banner']:
                    self.banner_position.update([comps[4]])
                if self.feature_dict['siteid']:
                    self.site_id.update([comps[5]])
                if self.feature_dict['sitedomain']:
                    self.site_domain.update([comps[6]])
                if self.feature_dict['sitecategory']:
                    self.site_category.update([comps[7]])
                if self.feature_dict['appid']:
                    self.app_id.update([comps[8]])
                if self.feature_dict['appdomain']:
                    self.app_domain.update([comps[9]])
                if self.feature_dict['appcategoy']:
                    self.app_category.update([comps[10]])
                if self.feature_dict['deviceid']:
                    self.device_id.update([comps[11]])
                if self.feature_dict['deviceip']:
                    self.device_ip.update([comps[12]])
                if self.feature_dict['devicemodel']:
                    self.device_model.update([comps[13]])
                if self.feature_dict['devicetype']:
                    self.device_type.update([comps[14]])
                if self.feature_dict['deviceconntype']:
                    self.device_conn_type.update([comps[15]])
                if self.feature_dict['c14']:
                    self.c14.update([comps[16]])
                if self.feature_dict['c15']:
                    self.c15.update([comps[17]])
                if self.feature_dict['c16']:
                    self.c16.update([comps[18]])
                if self.feature_dict['c17']:
                    self.c17.update([comps[19]])
                if self.feature_dict['c18']:
                    self.c18.update([comps[20]])
                if self.feature_dict['c19']:
                    self.c19.update([comps[21]])
                if self.feature_dict['c20']:
                    self.c20.update([comps[22]])
                if self.feature_dict['c21']:
                    self.c21.update([comps[23]])

                i+=1
                if i%10000000==0:
                    print 'PARSED '+str(i)+' LINES....'

        print 'FINISHED PARSING TRAINING FILE FOR SETS....TOOK: '+str(time.time()-start)

        print 'BUILDING DICTIONARIES...'
        start=time.time()

        #hour
        for h in self.hour:
            if self.feature_dict['hour']:
                self.hour_map[h]=self.length
                self.length+=1
        #c1
        for c in self.c1:
            if self.feature_dict['c1']:
                self.c1_map[c]=self.length
                self.length+=1
        #banner
        for ban in self.banner_position:
            if self.feature_dict['banner']:
                self.banner_position_map[ban]=self.length
                self.length+=1
        #site_id
        for sid in self.site_id:
            if self.feature_dict['siteid']:
                self.site_id_map[sid]=self.length
                self.length+=1
        #site_domain
        for sdom in self.site_domain:
            if self.feature_dict['sitedomain']:
                self.site_domain_map[sdom]=self.length
                self.length+=1
        #site_category
        for scat in self.site_category:
            if self.feature_dict['sitecategory']:
                self.site_category_map[scat]=self.length
                self.length+=1
        #app_id
        for aid in self.app_id:
            if self.feature_dict['appid']:
                self.app_id_map[aid]=self.length
                self.length+=1
        #app_domain
        for apdom in self.app_domain:
            if self.feature_dict['appdomain']:
                self.app_domain_map[apdom]=self.length
                self.length+=1
        #app_category
        for apcat in self.app_category:
            if self.feature_dict['appcategory']:
                self.app_category_map[apcat]=self.length
                self.length+=1
        #device_id
        for did in self.device_id:
            if self.feature_dict['deviceid']:
                self.device_id_map[did]=self.length
                self.length+=1
        #device_ip
        for dip in self.device_ip:
            if self.feature_dict['deviceip']:
                self.device_ip[dip]=self.length
                self.length+=1
        #device_model
        for devmod in self.device_model:
            if self.feature_dict['devicemodel']:
                self.device_model_map[devmod]=self.length
                self.length+=1
        #device_type
        for devtype in self.device_type:
            if self.feature_dict['devicetype']:
                self.device_type_map[devtype]=self.length
                self.length+=1
        #device connect
        for devcon in self.device_conn_type:
            if self.feature_dict['deviceconntype']:
                self.device_conn_type_map[devcon]=self.length
                self.length+=1
        #c14
        for c in self.c14:
            if self.feature_dict['c14']:
                self.c14_map[c]=self.length
                self.length+=1
        #c15
        for c in self.c15:
            if self.feature_dict['c15']:
                self.c15_map[c]=self.length
                self.length+=1
        #c16
        for c in self.c16:
            if self.feature_dict['c16']:
                self.c16_map[c]=self.length
                self.length+=1
        #c17
        for c in self.c17:
            if self.feature_dict['c17']:
                self.c17_map[c]=self.length
                self.length+=1
        # #c18
        for c in self.c18:
            if self.feature_dict['c18']:
                self.c18_map[c]=self.length
                self.length+=1
        # #c19
        for c in self.c19:
            if self.feature_dict['c19']:
                self.c19_map[c]=self.length
                self.length+=1
        # #c20
        for c in self.c20:
            if self.feature_dict['c20']:
                self.c20_map[c]=self.length
                self.length+=1
        # #c21
        for c in self.c21:
            if self.feature_dict['c21']:
                self.c21_map[c]=self.length
                self.length+=1

        print 'FINISHED CONSTRUCTING DICTIONARIES...TOOK: '+str(time.time()-start)
        print 'FINGERPRINT LENGTH: '+str(self.length)

    #Get fingerprint for Train or Prediction Sets, based on previously set features
    def get_fingerprint(self,comps,Train=1):
        feature_vector=[0]*(self.length+1)
        if self.feature_dict['hour']:
            feature_vector[self.hour_map[comps[1+Train][6:]]]=1
        if self.feature_dict['c1']:
            feature_vector[self.c1_map[comps[2+Train]]]=1
        if self.feature_dict['banner']:
            feature_vector[self.banner_position_map[comps[3+Train]]]=1
        if self.feature_dict['siteid']:
            feature_vector[self.site_id_map[comps[4+Train]]]=1
        if self.feature_dict['sitedomain']:
            feature_vector[self.site_domain_map[comps[4+Train]]]=1
        if self.feature_dict['sitecategory']:
            feature_vector[self.site_category_map[comps[6+Train]]]=1
        if self.feature_dict['appid']:
            feature_vector[self.app_id_map[comps[7+Train]]]=1
        if self.feature_dict['appdomain']:
            feature_vector[self.app_domain_map[comps[8+Train]]]=1
        if self.feature_dict['appcategory']:
            feature_vector[self.app_category_map[comps[9+Train]]]=1
        if self.feature_dict['deviceid']:
            feature_vector[self.device_id_map[comps[10+Train]]]=1
        if self.feature_dict['deviceip']:
            feature_vector[self.device_ip_map[comps[11+Train]]]=1
        if self.feature_dict['devicemodel']:
            feature_vector[self.device_model_map[comps[12+Train]]]=1
        if self.feature_dict['devicetype']:
            feature_vector[self.device_type_map[comps[13+Train]]]=1
        if self.feature_dict['deviceconntype']:
            feature_vector[self.device_conn_type_map[comps[14+Train]]]=1
        if self.feature_dict['c14']:
            feature_vector[self.c14_map[comps[15+Train]]]=1
        if self.feature_dict['c15']:
            feature_vector[self.c15_map[comps[16+Train]]]=1
        if self.feature_dict['c16']:
            feature_vector[self.c16_map[comps[17+Train]]]=1
        if self.feature_dict['c17']:
            feature_vector[self.c17_map[comps[18+Train]]]=1
        if self.feature_dict['c18']:
            feature_vector[self.c18_map[comps[19+Train]]]=1
        if self.feature_dict['c19']:
            feature_vector[self.c19_map[comps[20+Train]]]=1
        if self.feature_dict['c20']:
            feature_vector[self.c20_map[comps[21+Train]]]=1
        if self.feature_dict['c21']:
            feature_vector[self.c21_map[comps[22+Train]]]=1
        return feature_vector
