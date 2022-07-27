# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2019/11/12 21:27
# @author  : Mo
# @function: post service of fastapi

from pydantic import BaseModel
from fastapi import FastAPI,Form
#from MysqlObject import *
import random
from time import strftime,localtime
import time
import pymysql
from typing import Optional,Set

class Item(BaseModel):
    name: str
    tags: Set[str]=[]


app = FastAPI()
class Mysqlcy(object):

    def __init__(self):
        self.connect()

    def connect(self):
        #self.db=pymysql.connect(host='39.97.246.118',user='saas_test',password='SaaS2019#Sql',db='saas_db_test',port=3306,charset='utf8')
        self.conn = pymysql.connect(host='10.0.30.82',user='wangchaoyue',password='qwer1234',db='dabai',port=3306,charset='utf8')    #  可以把主机连接等写入配置文件 等
        #self.conn = pymysql.connect(host='hw-db.jimijiayuan.cn',user='saas_test_hw',password='SaaS2022#Sql',db='saas_db_test_hw',port=15307,charset='utf8')
        self.cursor=self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 获取所以数据
    def get_all(self,sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return  res

    # 获取一行数据
    def get_one(self,sql,args):
        self.cursor.execute(sql, args)
        res = self.cursor.fetchone()
        return res

    # 添加  就是添加一次提交多次
    def get_mode (self,sql,args):
        self.cursor.execute(sql, args)
        self.conn.commit()

    # 添加并且带返回值
    def get_create(self,sql):
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.lastrowid
    # python插入记录后取得主键id的方法(cursor.lastrowid和conn.insert_id())

    # 批量加入 以元祖的形式传参数   就是添加一次提交一次
    def mul_mode(self, sql, args):
        # self.cursor.executemany("insert into user (id,name) values (%s,%s)",[(1,"aaa"),(2,"bbb"),(3,"ccc")])  传参方式
        self.cursor.executemany(sql, args)
        self.conn.commit()

        # 添加  就是添加一次提交多次
    def get_up(self,sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def get_close(self):
        self.cursor.close()
        self.conn.close()

    def d_time(self):
        d_time=(strftime("%Y-%m-%d %H:%M:%S",localtime()))
        return d_time

    def bx(self):

        try:
            sqll="INSERT INTO `dabai`.`B`(`name`, `class`) VALUES ('刷刷', '一班');"
            id=Mysqlcy.get_create(self,sqll)
            id=str(id)
            sq1="INSERT INTO `dabai`.`A`(`course`, `score`, `user_id`,`creat_time`) VALUES (%s,%s,%s,%s);"
            args=[('数学',random.randint(1,100),id,Mysqlcy.d_time(self)),
                  ('语文', random.randint(1,100), id,Mysqlcy.d_time(self)),
                  ('历史', random.randint(1,100), id,Mysqlcy.d_time(self)),
                  ('政治', random.randint(1,100), id,Mysqlcy.d_time(self)),
                  ('化学', random.randint(1,100), id,Mysqlcy.d_time(self)),
                  ('物理', random.randint(1,100), id,Mysqlcy.d_time(self)),
                  ('英语', random.randint(1,100), id,Mysqlcy.d_time(self)),
                  ('地理', random.randint(1,100), id,Mysqlcy.d_time(self)),
                  ('生物', random.randint(1,100), id,Mysqlcy.d_time(self))]
            Mysqlcy.mul_mode(self,sq1,args)

        except Exception as e:
            self.conn.rollback;
            print("有数据插入失败")
            print(e)
        else:
            self.conn.commit;

    def ccc(self):

        sqll = "SELECT * FROM B LEFT JOIN A ON B.id=A.user_id"
        Mysqlcy.get_all(self, sqll)


    def kepz(self):

        try:
            sqll="INSERT INTO `saas_db_test_hw`.`t_saas_make_scene_base_project_answer`(`scene_base_id`, `user_id`, `user_enterprise_id`, `audit_status`, `audit_dt`, `audit_opinion`, `is_out`, `luodi_id`, `project_id`, `project_structure_type`, `customer_id`, `customer_name`, `start_dt`, `visit_minute`, `visit_longitude`, `visit_latitude`, `visit_address`, `address_pic_url`, `address_watermark_pic_url`, `create_dt`, `status`, `finish_dt`, `task_code`, `end_dt`, `is_revoke`, `revoke_dt`, `is_pic_repeat`, `audit_oss_status`, `audit_gongye_status`, `audit_oss_dt`, `audit_gongye_dt`, `is_overdue`, `project_industry_fenpei_id`, `cso_order_people_id`, `supplier_order_people_id`, `bi_pdf_url_pc`, `bi_pdf_url_pc_gongye`, `user_enterprise_helper_id`, `user_enterprise_helper_task_status`, `sign_in_dt`, `repair_flag`, `cso_audit_user`, `bi_pdf_url_mobile`, `save_dt`, `insert_pic_list`, `rebuild_task_list`, `is_pic_check`, `pic_repeat_status`, `audit_flag`, `is_pic_task`) VALUES (2220, 97529, NULL, 1, NULL, NULL, 0, NULL, 23537, 1, 36438, '蝴蝶背', '2022-02-21 10:13:00', '10', '116.49211', '39.97742', '-', 'https://cdn.yxvzb.com/sunflower/receipt/SZKQ6C_1645410313846.jpg', 'https://cdn.yxvzb.com/sunflower/receipt/SZKQ6C_1645410313846.jpg', '2022-02-21 10:40:37', 2, '2022-02-21 10:40:37', 'PZ_1645411236580', '2022-02-21 10:23:00', 0, NULL, 0, 0, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2022-02-21 10:23:00', 0, NULL, NULL, '2022-02-21 10:40:37', 'https://cdn.yxvzb.com/sunflower/xcx/Z6E8LT_1645410370192.jpg?x-oss-process=style/set-jpg&auto-orient&aHash=30083668312837C833E83BC817C807A4279807F810400C300FF40FF00C300FF0&pHash=85D87A6242892D24,https://cdn.yxvzb.com/sunflower/xcx/63JT1P_1645410382523.jpg?x-oss-process=style/set-jpg&auto-orient&aHash=0078007C017E03F80FF06FFFBFF8E218E40FC1CF0804000000001004C73FFE7F&pHash=C20419F901802610', NULL, 1, 1, 0, 1)"
            id=Mysqlcy.get_create(self,sqll)
            id=str(id)
            sq1="INSERT INTO `saas_db_test_hw`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES (%s, %s, %s, %s,%s);"
            args=[(id,20864, '选项1', '选项1', '2022-02-21 10:40:37'),
                  (id,20865, '[\"选项2\",\"选项3\"]', '[\"选项2\",\"选项3\"]', '2022-02-21 10:40:37'),
                  (id,20866, '选项4', '选项4', '2022-02-21 10:40:37'),
                  (id,20867, '5', '5', '2022-02-21 10:40:37'),
                  (id,20868, '[\"1\",\"2\",\"3\"]', '[\"1\",\"2\",\"3\"]', '2022-02-21 10:40:37'),
                  (id,20869, '4', '4', '2022-02-21 10:40:37'),
                  (id,20870, '5', '5', '2022-02-21 10:40:37'),
                  (id,20871, '挖潜增', '挖潜增', '2022-02-21 10:40:37'),
                  (id,20872, '13121634145', '13121634145', '2022-02-21 10:40:37'),
                  (id,20873, '1422667330@qq.com', '1422667330@qq.com', '2022-02-21 10:40:37'),
                  (id,20874, 'https://cdn.yxvzb.com/sunflower/xcx/RD7JU3_1645410356042.jpg', 'https://cdn.yxvzb.com/sunflower/xcx/RD7JU3_1645410356042.jpg', '2022-02-21 10:40:37'),
                  (id,20875, '[{\"file\":{},\"fileType\":\"application/pdf\",\"isPdf\":true,\"message\":\"上传完成\",\"name\":\"平台.pdf\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/RC8K4N_1645410359024.pdf\"}]', '[{\"file\":{},\"fileType\":\"application/pdf\",\"isPdf\":true,\"message\":\"上传完成\",\"name\":\"平台.pdf\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/RC8K4N_1645410359024.pdf\"}]', '2022-02-21 10:40:37'),
                  (id,20876, '[{\"file\":{},\"fileType\":\"application/msword\",\"message\":\"上传完成\",\"name\":\"123.doc\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/DA2WM5_1645410361082.doc\"}]', '[{\"file\":{},\"fileType\":\"application/msword\",\"message\":\"上传完成\",\"name\":\"123.doc\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/DA2WM5_1645410361082.doc\"}]', '2022-02-21 10:40:37'),
                  (id,20877, '[{\"file\":{},\"fileType\":\"application/vnd.ms-powerpoint\",\"message\":\"上传完成\",\"name\":\"1.ppt\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/CFOV71_1645410364349.ppt\"}]', '[{\"file\":{},\"fileType\":\"application/vnd.ms-powerpoint\",\"message\":\"上传完成\",\"name\":\"1.ppt\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/CFOV71_1645410364349.ppt\"}]', '2022-02-21 10:40:37'),
                  (id,20878, '[{\"file\":{},\"fileType\":\"application/vnd.ms-excel\",\"message\":\"上传完成\",\"name\":\"工作簿1.xls\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/YBLM8N_1645410366558.xls\"}]', '[{\"file\":{},\"fileType\":\"application/vnd.ms-excel\",\"message\":\"上传完成\",\"name\":\"工作簿1.xls\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/YBLM8N_1645410366558.xls\"}]', '2022-02-21 10:40:37'),
                  (id,20879, '[{\"fileType\":\"image/jpg\",\"message\":\"上传完成\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/Z6E8LT_1645410370192.jpg?x-oss-process=style/set-jpg&auto-orient&aHash=30083668312837C833E83BC817C807A4279807F810400C300FF40FF00C300FF0&pHash=85D87A6242892D24\"},{\"fileType\":\"image/jpg\",\"message\":\"上传完成\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/63JT1P_1645410382523.jpg?x-oss-process=style/set-jpg&auto-orient&aHash=0078007C017E03F80FF06FFFBFF8E218E40FC1CF0804000000001004C73FFE7F&pHash=C20419F901802610\"}]', '[{\"fileType\":\"image/jpg\",\"message\":\"上传完成\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/Z6E8LT_1645410370192.jpg?x-oss-process=style/set-jpg&auto-orient&aHash=30083668312837C833E83BC817C807A4279807F810400C300FF40FF00C300FF0&pHash=85D87A6242892D24\"},{\"fileType\":\"image/jpg\",\"message\":\"上传完成\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/63JT1P_1645410382523.jpg?x-oss-process=style/set-jpg&auto-orient&aHash=0078007C017E03F80FF06FFFBFF8E218E40FC1CF0804000000001004C73FFE7F&pHash=C20419F901802610\"}]', '2022-02-21 10:40:37'),
                  (id,20880, '2022年02月21日 10时25分', '2022年02月21日 10时25分', '2022-02-21 10:40:37'),
                  (id,20881, '2022年02月', '2022年02月', '2022-02-21 10:40:37'),
                  (id,20882, '', '', '2022-02-21 10:40:37')]
            Mysqlcy.mul_mode(self,sq1,args)
            Mysqlcy.get_close()

        except Exception as e:
            self.conn.rollback;
            print("有数据插入失败")
            print(e)
        else:
            self.conn.commit;
    def szwz(self):

        try:
            sqll="INSERT INTO `saas_db_test_hw`.`t_saas_number_questionnaire_answer`(`task_code`, `user_id`, `user_enterprise_id`, `information_id`, `questionnaire_id`, `questionnaire_channel_id`, `project_id`, `audit_status`, `audit_oss_status`, `audit_gongye_status`, `audit_dt`, `audit_oss_dt`, `audit_gongye_dt`, `audit_opinion`, `is_out`, `luodi_id`, `project_structure_type`, `is_revoke`, `revoke_dt`, `is_overdue`, `project_industry_fenpei_id`, `cso_order_people_id`, `supplier_order_people_id`, `finish_dt`, `bi_pdf_url_pc`, `bi_pdf_url_pc_gongye`, `cso_audit_user`, `create_dt`, `source_ip`, `source_province`, `source_city`) VALUES ('DQ141565673744869883969', 3, NULL, 215, 82, 196, 679, 2, 2, 0, '2022-04-28 15:57:23', '2022-04-28 15:57:23', NULL, NULL, 0, 1, 1, 0, NULL, 0, NULL, NULL, NULL, '2022-04-28 15:57:23', NULL, NULL, NULL, '2022-04-28 15:57:23', '123.125.216.90', NULL, NULL);"
            id=Mysqlcy.get_create(self,sqll)
            id=str(id)
            sq1="INSERT INTO `saas_db_test_hw`.`t_saas_number_questionnaire_topic_answer`(`questionnaire_answer_id`, `questionnaire_channel_id`, `information_id`, `questionnaire_id`, `project_id`, `answer`, `create_dt`, `topic_id`) VALUES (%s, %s, %s, %s,%s,%s,%s,%s);"
            args=[(id, 196, 215, 82, 679, '雨天', '2022-04-28 15:57:23', 1653),
                  (id, 196, 215, 82, 679, '[\"多选\",\"填空\"]', '2022-04-28 15:57:23', 1654),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1655),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1656),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1657),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1658),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1659),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1660),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1661),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1662),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1663),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1664),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1665),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1666),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1667),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1668),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1669),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1670),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1671),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1672),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1673),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1674),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1675),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1676),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1677),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1678),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1679),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1680),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1681),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1682),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1683),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1684),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1685),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1686),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1687),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1688),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1689),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1690),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1691),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1692),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1693),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1694),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1695),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1696),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1697),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1698),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1699),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1700),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1701),
                  (id, 196, 215, 82, 679, '', '2022-04-28 15:57:23', 1702)]
            Mysqlcy.mul_mode(self,sq1,args)

        except Exception as e:
            self.conn.rollback;
            print("有数据插入失败")
            print(e)
        else:
            self.conn.commit;




@app.post('/test/',response_model=Item)
async def test2(item: Item):
    res = {"res":item}
    print(item)
    return res

@app.get('/shua')
def shua():

    Mysqlcy().ccc()
    #Mysqlcy().bx()
    # a=random.randint(1,5)
    # time.sleep(a)
    return {"status":'200'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app,
                host="10.0.20.114",
                port=8089,
                workers=1)
