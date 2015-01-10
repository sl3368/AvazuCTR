__author__ = 'Lal'

import time
from collections import defaultdict


def get_features_from_set():

    #sets
    ad_id=set()
    click=set()
    hour=set()
    day=set()
    month=set()
    c1=set()
    banner_position=set()
    site_id=set()
    site_domain=set()
    site_category=set()
    app_id=set()
    app_domain=set()
    app_category=set()
    device_id=set()
    device_ip=set()
    device_model=set()
    device_type=set()
    device_conn_type=set()
    c14=set()
    c15=set()
    c16=set()
    c17=set()
    c18=set()
    c19=set()
    c20=set()
    c21=set()

    #dictionaries
    ad_id_clicked=defaultdict(int)
    ad_id_not_clicked=defaultdict(int)
    banner_position_clicked=defaultdict(int)
    banner_position_not_clicked=defaultdict(int)
    c1_clicked=defaultdict(int)
    c1_not_clicked=defaultdict(int)
    c15_clicked=defaultdict(int)
    c15_not_clicked=defaultdict(int)
    c16_clicked=defaultdict(int)
    c16_not_clicked=defaultdict(int)
    c18_clicked=defaultdict(int)
    c18_not_clicked=defaultdict(int)
    c19_clicked=defaultdict(int)
    c19_not_clicked=defaultdict(int)
    device_id_clicked=defaultdict(int)
    device_id_not_clicked=defaultdict(int)

    count_click=0

    i=0
    start=time.time()

    with open('train') as f:
        for line in f:
            if i==0:
                i=i+1
                continue
            comps=line.rstrip().split(',')
            ad_id.update([comps[0]])
            click.update([comps[1]])

            #format date
            hour.update([comps[2][6:]])
            day.update([comps[2][4:6]])
            month.update([comps[2][2:4]])

            #c1, etc.
            c1.update([comps[3]])
            banner_position.update([comps[4]])
            site_id.update([comps[5]])
            site_domain.update([comps[6]])
            site_category.update([comps[7]])
            app_id.update([comps[8]])
            app_domain.update([comps[9]])
            app_category.update([comps[10]])
            #device_id.update([comps[11]])
            #device_ip.update([comps[12]])
            device_model.update([comps[13]])
            device_type.update([comps[14]])
            device_conn_type.update([comps[15]])
            c14.update([comps[16]])
            c15.update([comps[17]])
            c16.update([comps[18]])
            c17.update([comps[19]])
            c18.update([comps[20]])
            c19.update([comps[21]])
            c20.update([comps[22]])
            c21.update([comps[23]])

            # if int(comps[1])==1:
            #     count_click=count_click+1
            #     ad_id_clicked[comps[0]]=ad_id_clicked[comps[0]]+1
            #     banner_position_clicked[comps[4]]=banner_position_clicked[comps[4]]+1
            #     c1_clicked[comps[3]]=c1_clicked[comps[3]]+1
            #     c15_clicked[comps[17]]=c15_clicked[comps[17]]+1
            #     c16_clicked[comps[18]]=c16_clicked[comps[18]]+1
            #     c18_clicked[comps[20]]+=1
            #     c19_clicked[comps[21]]+=1
            #     device_id_clicked[comps[11]]+=1
            # else:
            #     ad_id_not_clicked[comps[0]]=ad_id_clicked[comps[0]]+1
            #     banner_position_not_clicked[comps[4]]=banner_position_not_clicked[comps[4]]+1
            #     c1_not_clicked[comps[3]]=c1_clicked[comps[3]]+1
            #     c15_not_clicked[comps[17]]=c15_clicked[comps[17]]+1
            #     c16_not_clicked[comps[18]]=c16_clicked[comps[18]]+1
            #     device_id_not_clicked[comps[11]]+=1
            #     c18_not_clicked[comps[20]]+=1
            #     c19_not_clicked[comps[21]]+=1

            i=i+1

            if i%5000000==0:
                print 'PARSED '+str(i)+' LINES....'

            # if i==15000000:
            #     break

    print 'TOTAL: '+str(i)
    print 'FINISHED PARSING TOOK '+str(time.time()-start)+'....'
    print '\n\n'
    print 'NOW SHOWING FEATURES\' SETS'
    print '\n\n'

    print 'ID....'+str(len(app_id))
    # for d in ad_id:
    #     print d
    #print '\n\n'

    print 'CLICK...'+str(len(click))
    # for c in click:
    #     print c
    #print '\n\n'

    print 'HOUR...'+str(len(hour))
    # for h in hour:
    #     print h
    #print '\n\n'

    print 'DAY...'+str(len(day))
    # for y in day:
    #     print y
    #print '\n\n'

    print 'MONTH..'+str(len(month))
    for th in month:
        print th
    #print '\n\n'

    print 'C1..'+str(len(c1))
    # for anon in c1:
    #     print anon
    #print '\n\n'

    print 'BANNER POSITION...'+str(len(banner_position))
    # for pos in banner_position:
    #     print pos
    #print '\n\n'

    print 'SITE ID...'+str(len(site_id))
    # for sid in site_id:
    #     print sid
    #print '\n\n'

    print 'SITE DOMAIN..'+str(len(site_domain))
    # for dom in site_domain:
    #     print dom
    #print '\n\n'

    print 'SITE CATEGORY...'+str(len(site_category))
    # for scat in site_category:
    #     print scat
    #print '\n\n'

    print 'APP ID...'+str(len(app_id))
    # for apid in app_id:
    #     print apid
    #print '\n\n'

    print 'APP DOMAIN...'+str(len(app_domain))
    # for apdom in app_domain:
    #     print apdom
    #print '\n\n'

    print 'APP CATEGORY...'+str(len(app_category))
    # for cat in app_category:
    #     print cat
    #print '\n\n'

    print 'DEVICE ID...'+str(len(device_id))
    # for did in device_id:
    #     print did
    #print '\n\n'

    print 'DEVICE IP...'+str(len(device_ip))
    # for dip in device_ip:
    #     print dip
    #print '\n\n'

    print 'DEVICE MODEL...'+str(len(device_model))
    # for dmod in device_model:
    #     print dmod
    #print '\n\n'

    print 'DEVICE TYPE...'+str(len(device_type))
    # for dtype in device_type:
    #     print dtype
    #print '\n\n'

    print 'DEVICE CONNECTION TYPE...'+str(len(device_conn_type))
    # for dcon in device_conn_type:
    #     print dcon
    #print '\n\n'

    print 'C14...'+str(len(c14))
    # for c4 in c14:
    #     print c4
    #print '\n\n'

    print 'C15...'+str(len(c15))
    # for c5 in c14:
    #     print c5
    #print '\n\n'

    print 'C16..'+str(len(c16))
    # for c6 in c16:
    #     print c6
    #print '\n\n'

    print 'C17...'+str(len(c17))
    # for c7 in c17:
    #     print c7
    #print '\n\n'

    print 'C18...'+str(len(c18))
    # for c8 in c18:
    #     print c8
    #print '\n\n'

    print 'C19...'+str(len(c19))
    # for c9 in c19:
    #     print c9
    #print '\n\n'

    print 'C20...'+str(len(c20))
    # for c2 in c20:
    #     print c2
    #print '\n\n'

    print 'C21...'+str(len(c21))
    # for q in c21:
    #     print q
    #print '\n\n'
    print 'STATS...'
    print 'NUMBER CLICKED...'+str(count_click)

    # #ad id
    # ad_id_rates=[]
    # for key, value in ad_id_clicked.iteritems():
    #     hits=float(value)
    #     miss=float(0.0)
    #     if key in ad_id_not_clicked:
    #          miss=ad_id_not_clicked[key]
    #     rate=float(hits/(hits+miss))
    #     ad=(key,rate,hits,miss,hits+miss)
    #     if hits>1 and miss>0:
    #         ad_id_rates.append(ad)
    # print 'NUMBER OF AD ID...'+str(len(ad_id_rates))
    #
    # device_id_rates=[]
    # for key, value in device_id_clicked.iteritems():
    #     hits=float(value)
    #     miss=float(0.0)
    #     if key in device_id_not_clicked:
    #         miss=device_id_not_clicked[key]
    #     rate=float(hits/(hits+miss))
    #     ban=(key,rate,hits,miss,hits+miss)
    #     if hits>2 and miss>0:
    #         device_id_rates.append(ban)
    # print 'NUMBER OF DEVICE ID...'+str(len(device_id_rates))
    #
    # #banner
    # banner_rates=[]
    # for key,value in banner_position_clicked.iteritems():
    #     hits=float(value)
    #     miss=float(0.0)
    #     if key in banner_position_not_clicked:
    #         miss=banner_position_not_clicked[key]
    #     rate=float(hits/(hits+miss))
    #     ban=(key,rate,hits,miss,hits+miss)
    #     banner_rates.append(ban)
    #
    # c1_rates=[]
    # for key, value in c1_clicked.iteritems():
    #     hits=float(value)
    #     miss=float(0.0)
    #     if key in c1_not_clicked:
    #         miss=c1_not_clicked[key]
    #     rate=float(hits/(hits+miss))
    #     instance=(key,rate,hits,miss,hits+miss)
    #     c1_rates.append(instance)
    #
    # c15_rates=[]
    # for key,value in c15_clicked.iteritems():
    #     hits=float(value)
    #     miss=float(0.0)
    #     if key in c15_not_clicked:
    #         miss=c15_not_clicked[key]
    #     rate=float(hits/(hits+miss))
    #     instance=(key,rate,hits,miss,hits+miss)
    #     c15_rates.append(instance)
    #
    # c16_rates=[]
    # for key, value in c16_clicked.iteritems():
    #     hits=float(value)
    #     miss=float(0.0)
    #     if key in c16_not_clicked:
    #         miss=c16_not_clicked[key]
    #     rate=float(hits/(hits+miss))
    #     instance=(key,rate,hits,miss,hits+miss)
    #     c16_rates.append(instance)
    #
    # c18_rates=[]
    # for key,value in c18_clicked.iteritems():
    #     hits=float(value)
    #     miss=float(0.0)
    #     if key in c18_not_clicked:
    #         miss=c18_not_clicked[key]
    #     rate=float(hits/(hits+miss))
    #     instance=(key,rate,hits,miss,hits+miss)
    #     c18_rates.append(instance)
    #
    # c19_rates=[]
    # for key,value in c19_clicked.iteritems():
    #     hits=float(value)
    #     miss=float(0.0)
    #     if key in c19_not_clicked:
    #         miss=c19_not_clicked[key]
    #     rate=float(hits/(hits+miss))
    #     instance=(key,rate,hits,miss,hits+miss)
    #     c19_rates.append(instance)

    # ad_id_rates=sorted(ad_id_rates,key=lambda x:x[4], reverse=True)
    # device_id_rates=sorted(device_id_rates,key=lambda x:x[4],reverse=True)
    # banner_rates=sorted(banner_rates,key=lambda x:x[1], reverse=True)
    # c1_rates=sorted(c1_rates,key=lambda x:x[1], reverse=True)
    # c15_rates=sorted(c15_rates,key=lambda x:x[1], reverse=True)
    # c16_rates=sorted(c16_rates,key=lambda x:x[1], reverse=True)
    # c18_rates=sorted(c18_rates,key=lambda x:x[1], reverse=True)
    # c19_rates=sorted(c19_rates,key=lambda x:x[1], reverse=True)
    #
    # print 'BANNER RATES...'
    # for rate in banner_rates:
    #     print rate
    #
    # print 'C1 RATES...'
    # for rate in c1_rates:
    #     print rate
    #
    # print 'C15 RATES...'
    # for rate in c15_rates:
    #     print rate
    #
    # print 'C16 RATES...'
    # for rate in c16_rates:
    #     print rate
    #
    # print 'C18 RATES...'
    # for rate in c18_rates:
    #     print rate
    #
    # print 'C19 RATES...'
    # for rate in c19_rates:
    #     print rate
    #
    # print 'DEVICE ID RATES...(TOP)'
    # for t in range(250):
    #     print device_id_rates[t]
    #
    # print 'AD ID RATES...(TOP)'
    # for t in range(len(ad_id_rates)):
    #     print ad_id_rates[t]

    print 'DONE....'

get_features_from_set()