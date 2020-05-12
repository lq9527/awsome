import os
import subprocess
from git import Repo

# TODO 目录自动获取


def checkout_func(lib,dir,branchName):
    os.chdir(dir)
    repo = Repo()
    currentBranch = repo.active_branch
    print(">"+lib+"当前分支，",currentBranch)
    # 返回是否有改动（包括未add和未commit的）
    if repo.is_dirty() is True:
        print(">"+lib+"❎本地有未提交的更改")
        return 1

    repo.git.branch(branchName)
    
    repo.git.checkout(branchName)

    print(">"+lib+"新分支，",repo.active_branch)

    print(">"+lib+"✅create SUCCESS，",repo.active_branch)
    return 0

def checkout():
    root = os.getcwd()# 当前的目录
    branchName = input("请输入要创建的分支名:\n")
    code1 = checkout_func("58ClientProject",root,branchName)
    code2 = checkout_func("58JobLib",root+"/58JobLib",branchName)

checkout()
