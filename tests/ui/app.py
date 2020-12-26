from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC  #判断此元素是否存在的，返回的bool值。

class App:
    def __init__(self, driver):
        self.driver = driver

    '''判断标题'''
    def is_title(self,title,timeout=5):
        WebDriverWait(self.driver,timeout).until(EC.title_is(title))

    def is_title_con(self, title, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.title_contains(title))


    '''判断元素是否存在(隐藏的也算)'''
    def is_Ele(self, *loc, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(loc))
            return  True
        except NoSuchElementException as e:
            return False
        
    
    '''发送文本'''
    def send(self, Ele, keys):
        Ele.clear()
        Ele.send_keys(keys)
    

    '''正常元素点击'''
    def click_EL(self, *loc,timeout=5):
        WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(loc)).click()

    '''点击不带点击事件的元素'''
    def tap_EL(self,*loc,timeout=5,count=1):
        action = TouchAction(self.driver)
        el =WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(loc)) #可见
        action.tap(el,count).perform()

    '''返回元素列表'''
    def finds_EL(self,*loc,timeout=5):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_any_elements_located(loc))

    '''判断目标元素中是否包含此字符串'''
    def is_EL_str(self,text,*loc,timeout=5):
        return  WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element(loc,text))

    '''判断目标元素的属性值是否包含预期的字符串'''
    def is_El_value(self,text,*loc,timeout=5):
        return  WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element_value(loc,text))


    '''判断当前页面是否有alert,有返回alert'''
    def is_Elert(self,timeout=5):
        return  WebDriverWait(self.driver,timeout).until(EC.alert_is_present())


    '''判断元素是否被选中'''
    def is_Sel(self, *loc, timeout=5, boll_ele=True):
        return  WebDriverWait(self.driver,timeout).until(EC.element_located_selection_state_to_be(loc, boll_ele))


    '''获取屏幕的宽高'''
    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height


    '''从一个元素滚动到另一个元素'''
    def swipe_el(self,el1,el2):
        self.driver.scroll(el1, el2)  # 它可以从一个元素，滑动到另一个元素。



    '''点击某一坐标'''
    def click_pos(self,x,y):
        self.driver.tap([(x, y)])





