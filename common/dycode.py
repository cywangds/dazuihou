# -*- coding:utf-8 -*-
import requests
import json
from common import basejm
import time
import sys



class Mydy(object):

    def __init__(self):
        self.urlhj='https://saas-crm-wx-1.jimijiayuan.cn'
        self.phone='13000003396'
        self.password ='111111'
        self.header={}


    def dl(self):

        url ='/rest/saas/crm/xcx/user/login'
        data = {
            'phone': self.phone,
            'password': self.password}

        self.header = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        }
        searchList = requests.post(url=self.urlhj+url, data=data, headers=self.header, verify=False)
        searchList = searchList.json()
        #print(searchList['data']['token'])

        self.header = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'SaasCrmXcxToken':searchList['data']['token']
        }
        return self.header

    def dykey(self):

        self.header=Mydy().dl()
        url = '/rest/saas/crm/xcx/questionnaire/questionnaireDetail'
        data = {
            'projectId':'24327',
            'projectType':5,
            'userId':97555,
            'platformType':'crm_xcx',
            'answerId':'NaN',
            #'openid':97555
            'openid':'okjbX5Qn0YhmZzh6Qn6OxXSpALRs'
        }

        searchList = requests.post(url=self.urlhj + url, data=data, headers=self.header, verify=False)
        try:
            searchList = searchList.json()
            print(searchList)
            searchList1=searchList['data']['key']
        except:
            return searchList
            sys.exit()
        # print(self.header)
        return searchList1

    def dy(self):

        self.header=Mydy().dl()
        dy_key=Mydy().dykey()
        #print(dy_key)

        #c={"answerStartDt":1656062993308,"questionnaireId":3756,"projectId":"24327","projectType":"5","userId":97555,"answerEndDt":1656557550000,"answers":[{"topicId":223965,"answer":"选项2"},{"topicId":223966,"answer":"[\"选项1\",\"选项3\"]"},{"topicId":223967,"answer":"选项1"},{"topicId":223968,"answer":"123"},{"topicId":223969,"answer":"[\"11\",\"22\"]"},{"topicId":223970,"answer":"44"},{"topicId":223971,"answer":"小明2"},{"topicId":223972,"answer":"4"},{"topicId":223973,"answer":"7"},{"topicId":223974,"answer":"13121634145"},{"topicId":223975,"answer":"1422667330@qq.com"},{"topicId":223976,"answer":"2022年06月24日17时31分"},{"topicId":223977,"answer":"2022年06月"},{"topicId":223978,"answer":""}],"openid":"97555","idType":"userId","key":"PmWQ68EvJz7TJO_lh939klFXWrKT85MLRGx4SuWbPjUhVCjsdLz-VZA2xp5XfiW-yHxnyULJJCUMjzTOIJShTFgf4G0jk6iHozAdPYLEewSLnUomU8S6jJxuAms72JJRFjP5ljOWZXIOcGhJJFS-My3K0sKTTEsRTOvJFbAjFSI"}
        c={"answerStartDt":1656062993308,"questionnaireId":3756,"projectId":"24327","projectType":"5","userId":97555,"answerEndDt":1656557550000,"answers":[{"topicId":223965,"answer":"选项2"},{"topicId":223966,"answer":"[\"选项1\",\"选项3\"]"},{"topicId":223967,"answer":"选项1"},{"topicId":223968,"answer":"123"},{"topicId":223969,"answer":"[\"11\",\"22\"]"},{"topicId":223970,"answer":"44"},{"topicId":223971,"answer":"小明13"},{"topicId":223972,"answer":"4"},{"topicId":223973,"answer":"7"},{"topicId":223974,"answer":"13121634145"},{"topicId":223975,"answer":"1422667330@qq.com"},{"topicId":223976,"answer":"2022年06月24日17时31分"},{"topicId":223977,"answer":"2022年06月"},{"topicId":223978,"answer":""}],"openid":"okjbX5Qn0YhmZzh6Qn6OxXSpALRs","idType":"openId","key":"PmWQ68EvJz7TJO_lh939klFXWrKT85MLRGx4SuWbPjUhVCjsdLz-VZA2xp5XfiW-yHxnyULJJCUMjzTOIJShTFgf4G0jk6iHozAdPYLEewSLnUomU8S6jJxuAms72JJRFjP5ljOWZXIOcGhJJFS-My3K0sKTTEsRTOvJFbAjFSI"}

        c['key']=dy_key
        c=basejm.AesCrypt().encrypt(str(c))
        # print('加密')
        # print(c)
        # print(self.header)
        url = '/rest/saas/crm/xcx/questionnaire/answerQuestionnaireEncryption'
        data = {
            'c': c,
        }
        time.sleep(14)
        searchList = requests.post(url=self.urlhj + url, data=data, headers=self.header, verify=False)
        searchList = searchList.json()
        print(searchList)
        return searchList
    def szwjkey(self):

        self.header=Mydy().dl()
        url = '/rest/saas/crm/xcx/digitalQuestionnaire/informationDetail'
        data = {
            'projectId':'24328',
            'channelId':195,
            'informationId':18,
            'questionnaireId':56,
            'distinctId':'',
            'userId':97555,
            '_t':'1656397600580'
        }

        searchList = requests.post(url=self.urlhj + url, data=data, headers=self.header, verify=False)
        try:
            searchList = searchList.json()
            searchList1=searchList['data']['key']
            print(searchList1)
        except:
            print(searchList)
            return searchList
            sys.exit()
        # print(self.header)
        return searchList1

    def szwj(self):

        self.header=Mydy().dl()
        dy_key=Mydy().szwjkey()
        #print(dy_key)
        #c={"answerStartDt":1656062993308,"questionnaireId":3756,"projectId":"24327","projectType":"5","userId":97555,"answerEndDt":1656557550000,"answers":[{"topicId":223965,"answer":"选项2"},{"topicId":223966,"answer":"[\"选项1\",\"选项3\"]"},{"topicId":223967,"answer":"选项1"},{"topicId":223968,"answer":"123"},{"topicId":223969,"answer":"[\"11\",\"22\"]"},{"topicId":223970,"answer":"44"},{"topicId":223971,"answer":"小明2"},{"topicId":223972,"answer":"4"},{"topicId":223973,"answer":"7"},{"topicId":223974,"answer":"13121634145"},{"topicId":223975,"answer":"1422667330@qq.com"},{"topicId":223976,"answer":"2022年06月24日17时31分"},{"topicId":223977,"answer":"2022年06月"},{"topicId":223978,"answer":""}],"openid":"97555","idType":"userId","key":"PmWQ68EvJz7TJO_lh939klFXWrKT85MLRGx4SuWbPjUhVCjsdLz-VZA2xp5XfiW-yHxnyULJJCUMjzTOIJShTFgf4G0jk6iHozAdPYLEewSLnUomU8S6jJxuAms72JJRFjP5ljOWZXIOcGhJJFS-My3K0sKTTEsRTOvJFbAjFSI"}
        c={"projectId":"24328","channelId":"195","informationId":"18","questionnaireId":"56","openid":"","userId":"97555","idType":"userId","key":"480:1&481:2&482:1&483:2&480:1&481:2&482:1&483:2&","answers":[{"topicId":484,"answer":"选项2"},{"topicId":485,"answer":"[\"选项1\",\"选项2\"]"},{"topicId":486,"answer":"选项1"},{"topicId":487,"answer":"[\"选项2\",\"选项1\"]"},{"topicId":488,"answer":"选项2"},{"topicId":489,"answer":"[\"选项2\",\"选项3\"]"}]}
        c['key']=dy_key
        #print(c)
        c=basejm.AesCrypt().encrypt(str(c))
        url = '/rest/saas/crm/xcx/digitalQuestionnaire/submitDigitalQuestionnaire'
        data = {
            'c': c,
            'userId':97555

        }
        time.sleep(6)
        print(c)
        searchList = requests.post(url=self.urlhj + url, data=data, headers=self.header, verify=False)
        searchList = searchList.json()
        print(searchList)
        return searchList

# if __name__ == '__main__':
#     Mydy().szwj()
    # a='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'
    # c = basejm.AesCrypt().decrypt(str(a))
    # print(c)