
# 1.导入appium的webdriver
from appium import webdriver
from appium.webdriver.webdriver import By

import time


class Myphone(object):

    def __init__(self):
        self.driver=Myphone.get_driver(self)


    def get_driver(self):
        """
            获取设备driver
        """
        desired_caps = {}
        desired_caps['deviceName'] = 'V2055A'  # 手机/模拟器的型号：adb shell getprop ro.product.model
        desired_caps['udid'] = '39R0221514001411'
        desired_caps['platformVersion'] = '11'                  # 安卓系统的版本号：adb shell getprop ro.build.version.release
        desired_caps['appPackage'] = 'com.e_young.host.doctor_assistant'               # app的名字：
        desired_caps['appActivity'] ='com.e_young.host.doctor_assistant.splash.SplashActivity'         # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
                                                                # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
        desired_caps['platformName'] = 'Android'  # 打开什么平台的app，固定的 > 启动安卓平台
        desired_caps['unicodeKeyboard'] = True                  # 为了支持中文
        desired_caps['resetKeyboard'] = True                    # 设置成appium自带的键盘
        desired_caps['noReset'] =True
        # 去打开app，并且返回当前app的操作对象
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        return self.driver

    def test(self):
        """
            查找单个元素
        """
        # 获取driver
        driver = Myphone.get_driver()

        # 返回键
        driver.back()

        # 通过text获取元素
        Animation = driver.find_element_by_android_uiautomator('new UiSelector().text("Animation")')
        Animation.click()

        # 返回键
        driver.back()

        # 通过content-desc来获取元素
        app = driver.find_element_by_accessibility_id("App")
        app.click()

        # 返回键
        driver.back()
        # 通过xpath获取:使用最多
        media = driver.find_element_by_xpath("//android.widget.TextView[@text='Media' and @content-desc='Media']")
        media.click()

    def test1(self):

        #driver = Myphone.get_driver()
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[2]').click()
            self.driver.find_element(By.ID, 'com.e_young.host.doctor_assistant:id/psw_plan_tv').click()
            time.sleep(2)
            self.driver.find_element(By.ID,'com.e_young.host.doctor_assistant:id/login_phone').send_keys('13000000001')
            self.driver.find_element(By.ID, 'com.e_young.host.doctor_assistant:id/login_code').send_keys('111111')
            self.driver.find_element(By.ID, 'com.e_young.host.doctor_assistant:id/cb_agree').click()
            self.driver.find_element(By.ID, 'com.e_young.host.doctor_assistant:id/login_btn').click()
        except:
            print('登录用户无需登录')

        def kepeizhi():
            print('敬请期待')








if __name__ == "__main__":
    Myphone().test1()


