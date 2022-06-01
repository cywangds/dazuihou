import  pymysql
# 注意 args 参数可以传空值[]
class Mysqls(object):
    def __init__(self):
         # 读取配置文件
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host='39.97.246.118', user='saas_test', password='SaaS2019#Sql', db='saas_db_test', port=3306, charset='utf8')    #  可以把主机连接等写入配置文件 等
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

#
# if __name__ == '__main__':
#     sqll="INSERT INTO `saas_db_test`.`t_saas_make_scene_base_project_answer`(`scene_base_id`, `user_id`, `user_enterprise_id`, `audit_status`, `audit_dt`, `audit_opinion`, `is_out`, `luodi_id`, `project_id`, `project_structure_type`, `customer_id`, `customer_name`, `start_dt`, `visit_minute`, `visit_longitude`, `visit_latitude`, `visit_address`, `address_pic_url`, `address_watermark_pic_url`, `create_dt`, `status`, `finish_dt`, `task_code`, `end_dt`, `is_revoke`, `revoke_dt`, `is_pic_repeat`, `audit_oss_status`, `audit_gongye_status`, `audit_oss_dt`, `audit_gongye_dt`, `is_overdue`, `project_industry_fenpei_id`, `cso_order_people_id`, `supplier_order_people_id`, `bi_pdf_url_pc`, `bi_pdf_url_pc_gongye`, `user_enterprise_helper_id`, `user_enterprise_helper_task_status`, `sign_in_dt`, `repair_flag`, `cso_audit_user`, `bi_pdf_url_mobile`, `save_dt`, `insert_pic_list`, `rebuild_task_list`, `is_pic_check`, `pic_repeat_status`, `audit_flag`, `is_pic_task`) VALUES (2220, 97529, NULL, 1, NULL, NULL, 0, NULL, 23537, 1, 36438, '蝴蝶背', '2022-02-21 10:13:00', '10', '116.49211', '39.97742', '-', 'https://cdn.yxvzb.com/sunflower/receipt/SZKQ6C_1645410313846.jpg', 'https://cdn.yxvzb.com/sunflower/receipt/SZKQ6C_1645410313846.jpg', '2022-02-21 10:40:37', 2, '2022-02-21 10:40:37', 'PZ_1645411236580', '2022-02-21 10:23:00', 0, NULL, 0, 0, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2022-02-21 10:23:00', 0, NULL, NULL, '2022-02-21 10:40:37', 'https://cdn.yxvzb.com/sunflower/xcx/Z6E8LT_1645410370192.jpg?x-oss-process=style/set-jpg&auto-orient&aHash=30083668312837C833E83BC817C807A4279807F810400C300FF40FF00C300FF0&pHash=85D87A6242892D24,https://cdn.yxvzb.com/sunflower/xcx/63JT1P_1645410382523.jpg?x-oss-process=style/set-jpg&auto-orient&aHash=0078007C017E03F80FF06FFFBFF8E218E40FC1CF0804000000001004C73FFE7F&pHash=C20419F901802610', NULL, 1, 1, 0, 1);"
#     id=Mysqls().get_create(sqll)