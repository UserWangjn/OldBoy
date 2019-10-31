#coding=utf-8
# @Author: wjn
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_path = os.path.join(BASEDIR,'db','user').strip()
file_target_path = os.path.join(BASEDIR,'db','files').strip()
file_source_path = os.path.join(BASEDIR,'file_source').strip()