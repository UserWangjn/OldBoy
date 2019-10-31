# @Author: wjn
# @Time: 2019-08-12 20:47

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import sys
sys.path.append(BASE_DIR)
# print(BASE_DIR)

from module import main
main.test_main()