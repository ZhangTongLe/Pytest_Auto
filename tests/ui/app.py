from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC  #判断此元素是否存在的，返回的bool值。



class App:
    def __init__(self, driver):
        self.driver = driver

    def click_EL(self, *loc):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(loc)).click()


    def tap_EL(self,*loc):
        action = TouchAction(self.driver)
        el =WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
        action.tap(el,count=1).perform()


    '''返回元素列表'''
    def finds_EL(self,*loc):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located(loc))


    '''判断目标元素是否包含此字符串'''
    def is_EL_str(self,text,*loc):
        return  WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element(loc,text))



