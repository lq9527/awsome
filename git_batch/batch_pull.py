import os
import subprocess
from git import Repo

# TODO 目录自动获取


def pull_func(lib,dir):
    os.chdir(dir)
    repo = Repo()
    currentBranch = repo.active_branch
    print(">"+lib+"当前的分支，",currentBranch)
    # 返回是否有改动（包括未add和未commit的）
    if repo.is_dirty() is True:
        print(">"+lib+"❎本地有未提交的更改")
        return 1
    # 获取默认版本库 origin
    remote = repo.remote()
    # 从远程版本库拉取分支
    code = remote.pull()

    print(">"+lib+"✅pull SUCCESS，",repo.active_branch)
    return 0

def pull():
    root = os.getcwd()# 当前的目录
    code1 = pull_func("58ClientProject",root)
    if code1 != 0:
        return
    code2 = pull_func("58JobLib",root+"/58JobLib")
    if code2 != 0:
        return
    code3 = pull_func("58WuxianClient",root+"/58WuxianClient")
    if code3 != 0:
        return        

pull()
