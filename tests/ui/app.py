import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC  #判断此元素是否存在的，返回的bool值。
import inspect

from src.file import File

'''
https://appium.io/docs/en/commands/mobile-command/#android-uiautomator2-only
'''

class App:
    def __init__(self, driver):
        self.driver = driver

    '''判断标题'''
    def is_title(self,title,timeout=5):
        WebDriverWait(self.driver,timeout).until(EC.title_is(title))

    '''预期内容是否包含在标题内'''
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
    def swipe_el(self,el1,el2,duration=1000):
        self.driver.scroll(el1, el2,duration)  # 它可以从一个元素，滑动到另一个元素。

    '''从一个坐标，滑动到另一个坐标'''
    def swipe_pos(self, start_x, start_y, end_x, end_y, duration=1000):
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    '''点击某一坐标'''
    def click_pos(self,x,y):
        self.driver.tap([(x, y)])

    '''找到元素并获取元素的中心点'''
    def get_el_center(self,*loc,timeout=10):
        ele =WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(loc)) #可见

        # 计算元素中心点坐标公式：
        # 元素中心点x  =（右下角 x - 左上角x）/2 + 左上角x
        # # 元素中心点y  =（元素的高）/2 + 左上角y
        # '''
        # see_Center_X = int((s1.rect['width'] - s1.rect['x']) /2  +s1.rect['x'])
        # see_Center_Y = int(s1.rect['height']/2 +s1.rect['y'])

        #获取元素的尺寸和坐标 rect [x,y] 左上角坐标，location 只能获取左上角坐标
        Center_X = int((ele.rect['width'] - ele.rect['x']) /2  +ele.rect['x'])
        Center_Y = int(ele.rect['height']/2 +ele.rect['y'])

        return Center_X,Center_Y


    '''获取屏幕的中心坐标'''
    def get_pos_center(self):
        size = self.driver.get_window_size()
        width = size['width'] / 2
        height = size['height'] / 2
        return width,height

    '''获取屏幕的分辨率'''
    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    '''切进webview'''
    def switch_webview(self,target_webview):
        webviews = self.driver.contexts
        for viw in webviews:
            if target_webview in viw:
                self.driver.switch_to.context(viw)
                break

    '''返回native'''
    def switch_native(self):
        self.driver.switch_to.context("NATIVE_APP")  # 这个NATIVE_APP是固定的参数
        # self.driver.switch_to.context(contexts[0])  # 从contexts里取第一个参数

    '''获取当前的环境'''
    def get_context(self):
        return  self.driver.current_context

    # 屏幕向上滑动
    def swipeUp(self):
        px = self.get_size()
        x1 = int(px[0] * 0.5)  # x坐标
        y1 = int(px[1] * 0.75)  # 起始y坐标
        y2 = int(px[1] * 0.25)  # 终点y坐标
        self.swipe_pos(x1,y1,x1,y2)  # x轴不变，y轴变小

    # 屏幕向下滑动
    def swipeDown(self):
        px = self.get_size()
        x1 = int(px[0] * 0.5)  # x坐标
        y1 = int(px[1] * 0.25)  # 起始y坐标
        y2 = int(px[1] * 0.75)  # 终点y坐标
        self.swipe_pos(x1,y1,x1,y2)  # x轴不变，y轴变大

    # 屏幕向左滑动
    def swipLeft(self):
        px = self.get_size()
        x1 = int(px[0] * 0.75)
        y1 = int(px[1] * 0.5)
        x2 = int(px[0] * 0.05)
        self.swipe_pos(x1, y1, x2, y1) # y轴不变，X轴减小

    # 屏幕向右滑动
    def swipRight(self):
        px = self.get_size()
        x1 = int(px[0] * 0.05)
        y1 = int(px[1] * 0.5)
        x2 = int(px[0] * 0.75)
        self.swipe_pos(x1, y1, x2, y1) #y轴不变，X轴变大

    # 滑动总方法
    def swipe(self,direct,count=1):
        for i in range(count):
            if direct =='up':
                self.swipeUp()
            elif direct =='down':
                self.swipeDown()
            elif direct == 'left':
                self.swipLeft()
            elif direct == 'right':
                self.swipRight()

    #操作按键仅Android
    '''
    电话键
    
    KEYCODE_CALL 拨号键 5
    
    KEYCODE_ENDCALL 挂机键 6
    
    KEYCODE_HOME 按键Home 3
    
    KEYCODE_MENU 菜单键 82
    
    KEYCODE_BACK 返回键 4
    
    KEYCODE_SEARCH 搜索键 84
    
    KEYCODE_CAMERA 拍照键 27
    
    KEYCODE_FOCUS 拍照对焦键 80
    
    KEYCODE_POWER 电源键 26
    
    KEYCODE_NOTIFICATION 通知键 83
    
    KEYCODE_MUTE 话筒静音键 91
    
    KEYCODE_VOLUME_MUTE 扬声器静音键 164
    
    KEYCODE_VOLUME_UP 音量增加键 24
    
    KEYCODE_VOLUME_DOWN 音量减小键 25
    
    控制键
    
    KEYCODE_ENTER 回车键 66
    
    KEYCODE_ESCAPE ESC键 111
    
    KEYCODE_DPAD_CENTER 导航键 确定键 23
    
    KEYCODE_DPAD_UP 导航键 向上 19
    
    KEYCODE_DPAD_DOWN 导航键 向下 20
    
    KEYCODE_DPAD_LEFT 导航键 向左 21
    
    KEYCODE_DPAD_RIGHT 导航键 向右 22
    
    KEYCODE_MOVE_HOME 光标移动到开始键 122
    
    KEYCODE_MOVE_END 光标移动到末尾键 123
    
    KEYCODE_PAGE_UP 向上翻页键 92
    
    KEYCODE_PAGE_DOWN 向下翻页键 93
    
    KEYCODE_DEL 退格键 67
    
    KEYCODE_FORWARD_DEL 删除键 112
    
    KEYCODE_INSERT 插入键 124
    
    KEYCODE_TAB Tab键 61
    
    KEYCODE_NUM_LOCK 小键盘锁 143
    
    KEYCODE_CAPS_LOCK 大写锁定键 115
    
    KEYCODE_BREAK Break/Pause键 121
    
    KEYCODE_SCROLL_LOCK 滚动锁定键 116
    
    KEYCODE_ZOOM_IN 放大键 168
    
    KEYCODE_ZOOM_OUT 缩小键 169
    
    
    组合按键
    KEYCODE_ALT_LEFT Alt+Left
    
    KEYCODE_ALT_RIGHT Alt+Right
    
    KEYCODE_CTRL_LEFT Control+Left
    
    KEYCODE_CTRL_RIGHT Control+Right
    
    KEYCODE_SHIFT_LEFT Shift+Left
    
    KEYCODE_SHIFT_RIGHT Shift+Right
    
    '''
    def key_code(self,number):
        self.driver.press_keycode(number)

    # 长按3秒然后抬起
    def long_press(self,*loc,timeout=3):
        action = TouchAction(self.driver)
        el = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(loc))  # 可见
        action.long_press(el,timeout).release().perform()

    # 获取截图，保存到report的img 目录中
    def get_img(self):
        path = File.get_root_path("Pytest_Auto")
        img_path = path + '\\report\\img'
        # 正在运行模块的名称
        m_name = File.get_file_name(inspect.stack()[1][1])
        # 正在运行的
        f_name = inspect.stack()[1][3]
        current_time = time.strftime('_%H:%M:%S_', time.localtime(time.time()))
        img_path = img_path+'\\'+m_name+'_'+f_name+current_time+'.png'
        self.driver.get_screenshot_as_file(img_path)

    # 连续滑动，手机解锁，press 和move_to 也可以是元素
    def hold_swipe(self):
        TouchAction(self.driver).press(x=243, y=381).wait(2000)\
            .move_to(x=455, y=390).wait(1000) \
            .move_to(x=643, y=584).wait(1000) \
            .move_to(x=647, y=784).wait(1000) \
            .release().perform()


    '''
    层级定位
    https://www.cnblogs.com/Chilam007/p/12728316.html
    '''

    def find_child(self,*parent,*child,timeout=5):

        parent_el =WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(parent)) #可见

        WebDriverWait(self.driver, timeout).until(
            lambda driver: parent_el.find_element(child[0], child[1]))



    '''
    
    https://github.com/rushtang/myappauto/blob/master/base/action.py
    
    '''











