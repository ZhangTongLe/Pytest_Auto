import pytest
from src.file import File
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)



class run:

    def hell(self):
        print('我是run hell')


if __name__ == '__main__':
    path =File.get_root_path("Pytest_Auto")
    '''按指定目录运行case,用例执行是按目录顺序执行'''
    pytest.main([path+'\\tests\\ui','--alluredir=./report/']) #

    # generate 生成静态报告，serve 打开服务器
    os.popen('allure generate ./report/ -o ./report/allure-report/ --clean')


    