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
    path =File.get_root_path("Auto_Test")
    '''按指定目录运行case,用例执行是按目录顺序执行'''
    pytest.main([path+'\\tests\\ui']) #运行指定目录的case

