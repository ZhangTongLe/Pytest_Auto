import filecmp
import os
import difflib

import sys

'''
 do_path功能：处理递归文件夹、找出指定文件返回文件列表

 path ：基本目录
 start :要匹配的文件开头的字符串
 end: 匹配文件结尾的字符串
 file_list； 递归遍历的文件的绝对路径装在到空列表里
 start :要处理的文件名称的开头叫什么
 end: 要处理的文件后缀名是什么
 '''

class File:

    def do_path(self, path, start=(), end=()):
        file_list = []
        for root, dirs, files in os.walk(path):
            for name in files:
                # 如果只处理某文件格式，可以把and  替换成or，或者自己继续添加if
                if name.startswith(start) and name.endswith(end):
                    file_list.append(os.path.join(root, name))

        return file_list

    '''do_path的like版本'''
    def do_path_like(self, path, type):
        file_list = []
        for root, dirs, files in os.walk(path):
            for name in files:
                # 通过增加if 模式，增加like匹配
                if type in name:
                    file_list.append(os.path.join(root, name))
        print(file_list)
        return file_list

    @staticmethod
    # 1、比较两个文件是否相等
    def diff_file(file1, file2):
       return filecmp.cmp(file1,file2)

    # 2、比较两目录下文件是否一致,闭包的设计模式
    def diff_files(self,dir1,dir2):
        dcmp = filecmp.dircmp(dir1, dir2)

        def print_diff_files(dcmp):
            for name in dcmp.diff_files:
                print("diff_file %s found in %s and %s" % (name, dcmp.left, dcmp.right))
            for sub_dcmp in dcmp.subdirs.values():
                print_diff_files(sub_dcmp)

        return print_diff_files(dcmp)

    # 3、 比较两个文件夹内指定文件是否相等。
    @staticmethod
    def diff_zd(dir1, dir2, common=['a.txt', 'b.txt']):
        match, mismatch, errors = filecmp.cmpfiles(dir1, dir2, common)
        return match,mismatch,errors

   # 4、打印出两个字符串列表的差异

    def diff_str(self,s1,s2):
        sys.stdout.writelines(difflib.context_diff(s1, s2, fromfile='before.py', tofile='after.py'))


    # 5、返回列表中模糊匹配的字符串
    def like_list(self,like,dir_list):
        difflib.get_close_matches(like, dir_list)


    # 6、创建多级目录文件夹
    def file_make(self,path):
        os.makedirs(path)

    '''
    7、修改部分文件名称
    '''
    def rename_some(self, path, name='_result'):
        # 在原有名字上做补充
        # 不带后缀名的绝对路径+补充名字+后缀名
        new_name = os.path.splitext(path)[0] + name + os.path.splitext(path)[1]
        return new_name

    '''
    8、根据原有类型文件的后缀名，在当前目录拼接新名字同类型的文件
    '''
    def rename_full(self, path, name='result'):
        # 文件的目录地址+完整文件名字+原有的文件后缀名
        new_name = os.path.dirname(path) + name + os.path.splitext(path)[1]
        return new_name


    '''
    9、重命名文件
    '''
    def rename(self,old_file_path,new_file_path):
        os.renames(old_file_path,new_file_path)



    '''
    10、自定义停用词
    '''
    def stop_words(self):

        FILE = os.path.dirname(__file__)
        STOPWORDS = set(map(str.strip, open(os.path.join(FILE, 'stopwords')).readlines()))

        print(STOPWORDS)

    '''
    11、获取项目根路径
    
    '''
    @staticmethod
    def get_root_path(project_name):
        curPath = os.path.abspath(os.path.dirname(__file__))

        # windows写法
        rootPath = curPath[:curPath.find(project_name) + len(project_name)]  # 获取myProject，也就是项目的根路径
        # Mac
        # rootPath = curPath[:curPath.find("myProject/") + len("myProject/")]  # 获取myProject，也就是项目的根路径
        return rootPath




'''
__file__参数获取当前文件 如os.path.basename(__file__)获取当前文件名
os.sep:取代操作系统特定的路径分隔符 windows为\ Linux为/
os.name:指示你正在使用的工作平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
os.getcwd():得到当前工作目录。
os.getenv()和os.putenv:分别用来读取和设置环境变量
  一、设置系统环境变量
    1、os.environ['环境变量名称']='环境变量值' #其中key和value均为string类型
    2、os.putenv('环境变量名称', '环境变量值')
  二、获取系统环境变量
    1、os.environ['环境变量名称']
    2、os.getenv('环境变量名称')
os.listdir():返回指定目录下的所有文件和目录名
os.remove(file):删除一个文件(文件夹不可删除)
os.stat（file）:获得文件属性
os.chmod(file):修改文件权限和时间戳
os.mkdir(name):创建目录
os.rmdir(name):删除目录
os.removedirs（r“c：\python”）:删除多个空目录
os.system():运行shell命令
os.exit():终止当前进程
os.linesep:给出当前平台的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
os.path.split():返回一个路径的目录名和文件名
os.path.isfile()和os.path.isdir()分别检验给出的路径是一个目录还是文件
os.path.existe():检验给出的路径是否真的存在
os.listdir(dirname):列出dirname下的目录和文件
os.curdir:返回当前目录（'.'）
os.chdir(dirname):改变工作目录到dirname
os.path.isdir(name):判断name是不是目录，不是目录就返回false
os.path.isfile(name):判断name这个文件是否存在，不存在返回false
os.path.exists(name):判断是否存在文件或目录name
os.path.getsize(name):或得文件大小，如果name是目录则返回0
os.path.abspath(name):获得绝对路径
os.path.isabs():判断是否为绝对路径
os.path.normpath(path):规范path字符串形式
os.path.split(name):分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
os.path.splitext():分离文件名和扩展名
os.path.join(path,name):连接目录与文件名或目录
os.path.basename(path):返回文件名
os.path.dirname(path):返回文件路径


'''

    





if __name__ == '__main__':
    f = File()

    root_path = f.get_root_path("ZhangTongle")
    print(root_path)
 # dir1 = 'E:\ZhangTongle'
 # dir2 = 'D:\ZhangTongle'



 # f.diff_files(dir1,dir2)


