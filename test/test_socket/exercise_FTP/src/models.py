#coding=utf-8
# @Author: wjn
import pickle
from test.test_socket.exercise_FTP.config import settings
import os

class BaseModel:
    file_path = settings.db_path
    @staticmethod
    def save_user(username,pwd):
        # 使用pickle将内容保存到文件中
        # data = '{0},{1}'.format(username,pwd)
        try:
            pickle.dump(pwd,open(BaseModel.file_path+'/'+username,'wb'))
            os.mkdir(os.path.join(settings.file_path,username))
        except BaseException as e:
            print(e)


if __name__ == '__main__':
    username = 'wjn'
    print(BaseModel.file_path+'/'+username)