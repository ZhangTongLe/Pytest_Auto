import pytest
from src.file import File


class run:


    def hell(self):
        print('我是run hell')


if __name__ == '__main__':
    path =File.get_root_path("Auto_Test")

    pytest.main([path+'\\tests\\ui']) #
