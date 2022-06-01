#encoding=utf-8
import pymysql
from concurrent.futures import ThreadPoolExecutor

class Mysqlcy(object):

    def __init__(self):
        self.db=None

    def star(self,sql_select,sql_type):
        # 打开数据库连接
        self.db=pymysql.connect(host='39.97.246.118',user='saas_test',password='SaaS2019#Sql',db='saas_db_test',port=3306,charset='utf8')
        cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

        # 使用 cursor() 方法创建一个游标对象 cursor
        if(sql_type=="c"):

            # 使用 execute()  方法执行 SQL 查询
            cursor.execute(sql_select)
            # 使用 fetchone() 方法获取单条数据.
            data = cursor.fetchone()
            return data
        elif(sql_type=="r"):

            cursor.execute(sql_select)
            self.db.commit()
            return True

        elif (sql_type == "i"):

            cursor.execute(sql_select)
            last_id = cursor.lastrowid
            self.db.commit()
            return last_id
            # 关闭数据库连接
            self.db.close()


    def bx(self):

        try:
            sqll="INSERT INTO `saas_db_test`.`t_saas_make_scene_base_project_answer`(`scene_base_id`, `user_id`, `user_enterprise_id`, `audit_status`, `audit_dt`, `audit_opinion`, `is_out`, `luodi_id`, `project_id`, `project_structure_type`, `customer_id`, `customer_name`, `start_dt`, `visit_minute`, `visit_longitude`, `visit_latitude`, `visit_address`, `address_pic_url`, `address_watermark_pic_url`, `create_dt`, `status`, `finish_dt`, `task_code`, `end_dt`, `is_revoke`, `revoke_dt`, `is_pic_repeat`, `audit_oss_status`, `audit_gongye_status`, `audit_oss_dt`, `audit_gongye_dt`, `is_overdue`, `project_industry_fenpei_id`, `cso_order_people_id`, `supplier_order_people_id`, `bi_pdf_url_pc`, `bi_pdf_url_pc_gongye`, `user_enterprise_helper_id`, `user_enterprise_helper_task_status`, `sign_in_dt`, `repair_flag`, `cso_audit_user`, `bi_pdf_url_mobile`, `save_dt`, `insert_pic_list`, `rebuild_task_list`, `is_pic_check`, `pic_repeat_status`, `audit_flag`, `is_pic_task`) VALUES (2220, 97529, NULL, 1, NULL, NULL, 0, NULL, 23537, 1, 36438, '蝴蝶背', '2022-02-21 10:13:00', '10', '116.49211', '39.97742', '-', 'https://cdn.yxvzb.com/sunflower/receipt/SZKQ6C_1645410313846.jpg', 'https://cdn.yxvzb.com/sunflower/receipt/SZKQ6C_1645410313846.jpg', '2022-02-21 10:40:37', 2, '2022-02-21 10:40:37', 'PZ_1645411236580', '2022-02-21 10:23:00', 0, NULL, 0, 0, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2022-02-21 10:23:00', 0, NULL, NULL, '2022-02-21 10:40:37', 'https://cdn.yxvzb.com/sunflower/xcx/Z6E8LT_1645410370192.jpg?x-oss-process=style/set-jpg&auto-orient&aHash=30083668312837C833E83BC817C807A4279807F810400C300FF40FF00C300FF0&pHash=85D87A6242892D24,https://cdn.yxvzb.com/sunflower/xcx/63JT1P_1645410382523.jpg?x-oss-process=style/set-jpg&auto-orient&aHash=0078007C017E03F80FF06FFFBFF8E218E40FC1CF0804000000001004C73FFE7F&pHash=C20419F901802610', NULL, 1, 1, 0, 1);"
            id=Mysqlcy.star(self,sqll,"i")
            id=str(id)
            print(id)
            sq1="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20864, '选项1', '选项1', '2022-02-21 10:40:37');"
            sq2="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20865, '[\"选项2\",\"选项3\"]', '[\"选项2\",\"选项3\"]', '2022-02-21 10:40:37');"
            sq3="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20866, '选项4', '选项4', '2022-02-21 10:40:37');"
            sq4="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20867, '5', '5', '2022-02-21 10:40:37');"
            sq5="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20868, '[\"1\",\"2\",\"3\"]', '[\"1\",\"2\",\"3\"]', '2022-02-21 10:40:37');"
            sq6="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20869, '4', '4', '2022-02-21 10:40:37');"
            sq7="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20870, '5', '5', '2022-02-21 10:40:37');"
            sq8="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20871, '挖潜增', '挖潜增', '2022-02-21 10:40:37');"
            sq9="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20872, '13121634145', '13121634145', '2022-02-21 10:40:37');"
            sq10="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20873, '1422667330@qq.com', '1422667330@qq.com', '2022-02-21 10:40:37');"
            sq11="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20874, 'https://cdn.yxvzb.com/sunflower/xcx/RD7JU3_1645410356042.jpg', 'https://cdn.yxvzb.com/sunflower/xcx/RD7JU3_1645410356042.jpg', '2022-02-21 10:40:37');"
            sq12="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ( "+id+", 20875, '[{\"file\":{},\"fileType\":\"application/pdf\",\"isPdf\":true,\"message\":\"上传完成\",\"name\":\"平台.pdf\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/RC8K4N_1645410359024.pdf\"}]', '[{\"file\":{},\"fileType\":\"application/pdf\",\"isPdf\":true,\"message\":\"上传完成\",\"name\":\"平台.pdf\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/RC8K4N_1645410359024.pdf\"}]', '2022-02-21 10:40:37');"
            sq13="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20876, '[{\"file\":{},\"fileType\":\"application/msword\",\"message\":\"上传完成\",\"name\":\"123.doc\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/DA2WM5_1645410361082.doc\"}]', '[{\"file\":{},\"fileType\":\"application/msword\",\"message\":\"上传完成\",\"name\":\"123.doc\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/DA2WM5_1645410361082.doc\"}]', '2022-02-21 10:40:37');"
            sq14="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20877, '[{\"file\":{},\"fileType\":\"application/vnd.ms-powerpoint\",\"message\":\"上传完成\",\"name\":\"1.ppt\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/CFOV71_1645410364349.ppt\"}]', '[{\"file\":{},\"fileType\":\"application/vnd.ms-powerpoint\",\"message\":\"上传完成\",\"name\":\"1.ppt\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/CFOV71_1645410364349.ppt\"}]', '2022-02-21 10:40:37');"
            sq15="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20878, '[{\"file\":{},\"fileType\":\"application/vnd.ms-excel\",\"message\":\"上传完成\",\"name\":\"工作簿1.xls\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/YBLM8N_1645410366558.xls\"}]', '[{\"file\":{},\"fileType\":\"application/vnd.ms-excel\",\"message\":\"上传完成\",\"name\":\"工作簿1.xls\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/YBLM8N_1645410366558.xls\"}]', '2022-02-21 10:40:37');"
            sq16="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20879, '[{\"fileType\":\"image/jpg\",\"message\":\"上传完成\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/Z6E8LT_1645410370192.jpg?x-oss-process=style/set-jpg&auto-orient&aHash=30083668312837C833E83BC817C807A4279807F810400C300FF40FF00C300FF0&pHash=85D87A6242892D24\"},{\"fileType\":\"image/jpg\",\"message\":\"上传完成\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/63JT1P_1645410382523.jpg?x-oss-process=style/set-jpg&auto-orient&aHash=0078007C017E03F80FF06FFFBFF8E218E40FC1CF0804000000001004C73FFE7F&pHash=C20419F901802610\"}]', '[{\"fileType\":\"image/jpg\",\"message\":\"上传完成\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/Z6E8LT_1645410370192.jpg?x-oss-process=style/set-jpg&auto-orient&aHash=30083668312837C833E83BC817C807A4279807F810400C300FF40FF00C300FF0&pHash=85D87A6242892D24\"},{\"fileType\":\"image/jpg\",\"message\":\"上传完成\",\"status\":1,\"url\":\"https://cdn.yxvzb.com/sunflower/xcx/63JT1P_1645410382523.jpg?x-oss-process=style/set-jpg&auto-orient&aHash=0078007C017E03F80FF06FFFBFF8E218E40FC1CF0804000000001004C73FFE7F&pHash=C20419F901802610\"}]', '2022-02-21 10:40:37');"
            sq17="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20880, '2022年02月21日 10时25分', '2022年02月21日 10时25分', '2022-02-21 10:40:37');"
            sq18="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20881, '2022年02月', '2022年02月', '2022-02-21 10:40:37');"
            sq19="INSERT INTO `saas_db_test`.`t_saas_make_scene_project_topic_answer`(`project_topic_answer_id`, `topic_id`, `answer`, `init_pic_answer`, `create_dt`) VALUES ("+id+", 20882, '', '', '2022-02-21 10:40:37');"
            Mysqlcy.star(self,sq1,"r")
            Mysqlcy.star(self,sq2,"r")
            Mysqlcy.star(self,sq3,"r")
            Mysqlcy.star(self,sq4,"r")
            Mysqlcy.star(self,sq5,"r")
            Mysqlcy.star(self,sq6,"r")
            Mysqlcy.star(self,sq7,"r")
            Mysqlcy.star(self,sq8,"r")
            Mysqlcy.star(self,sq9,"r")
            Mysqlcy.star(self,sq10,"r")
            Mysqlcy.star(self,sq11,"r")
            Mysqlcy.star(self,sq12,"r")
            Mysqlcy.star(self,sq13,"r")
            Mysqlcy.star(self,sq14,"r")
            Mysqlcy.star(self,sq15,"r")
            Mysqlcy.star(self,sq16,"r")
            Mysqlcy.star(self,sq17,"r")
            Mysqlcy.star(self,sq18,"r")
            Mysqlcy.star(self,sq19,"r")
        except Exception as e:
            self.db.rollback;
            print("有数据插入失败")
            print(e)
        else:
            self.db.commit;

    def main(self):
        print('线程开始')

        for i in range(1,2):
            Mysqlcy.bx(self)
            #print(i)
        print('线程结束')


if __name__ == '__main__':
    thread_name = ['1']
    with ThreadPoolExecutor(max_workers=10) as executor:
        result=executor.map(Mysqlcy().main(),thread_name)
        # for res in result:
        #     print(res)
