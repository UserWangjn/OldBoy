#coding=utf-8
# @Author: wjn

import importlib

module_name = 'src.a_common'
func_name = 'add'

module = importlib.import_module(module_name)


func = getattr(module,func_name)
func()