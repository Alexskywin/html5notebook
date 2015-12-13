#!/usr/bin/env python
# coding=utf-8

"""
结构中通常都会存在根目录
root
    1
        1.xxxxxxxxxxxxx.md
        1.1xxxxxxxxxxxxx.md
        1.2xxxxxxxxxxxxx.md
        1.3xxxxxxxxxxxxx.md
"""

import sys
import os
import os.path

# print sys.argv
rootname = ''

if len(sys.argv) > 1:
    rootname = sys.argv[1]
else:
    rootname = 'default'


# 检测用户文件夹是否存在
if not os.path.exists(rootname):
    os.makedirs(rootname)

print '[根目录] 已创建.....√'

menutree = [
    [
        {'title': '1.HTML5与HTML4的区别'},
        {'title': '1.1推出的理由及目标和语法的改变'},
        {'title': '1.2新增的元素和废除的元素以及新增的属性和废除的属性'},
        {'title': '1.3全局属性'},
    ]
]

for key, item in enumerate(menutree):
    level = key + 1
    # 创建目录
    tmpath = os.path.join(rootname, str(level))
    if not os.path.exists(tmpath):
        os.makedirs(tmpath)
    print '[%s] %s' % (tmpath, '已创建.....√')
    # 创建目录下的文件
    for i in item:
        tmpfilepath = os.path.join(tmpath, i['title'] + '.md')
        if not os.path.exists(tmpfilepath):
            resource = open(tmpfilepath, 'w')
            resource.close()
        print '[%s] %s' % (tmpfilepath, '已创建.....√')
