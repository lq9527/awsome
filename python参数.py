# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import subprocess
import sys, getopt


# 实例
# 假定我们创建这样一个脚本，可以通过命令行向脚本文件传递两个文件名，同时我们通过另外一个选项查看脚本的使用。脚本使用方法如下：
#
# usage: test.py -i <inputfile> -o <outputfile>
#
# 执行以下代码
# $ python test.py -h
# usage: test.py -i <inputfile> -o <outputfile>
#
# $ python test.py -i inputfile -o outputfile
# 输入的文件为： inputfile
# 输出的文件为： outputfile

def main(argv):
    branch = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["obranch="])
    except getopt.GetoptError:
        print('batch_checkout.py -o <branch>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('batch_checkout.py -o <branch>')
            sys.exit()
        elif opt in ("-o", "--obranch"):
            branch = arg
    print('输入的分支为：', branch)


if __name__ == "__main__":
    main(sys.argv[1:])
