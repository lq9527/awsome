import os
import subprocess
from git import Repo
import sys, getopt


# TODO 目录自动获取


def checkout_func(lib, dir, branchName):
    os.chdir(dir)
    repo = Repo()
    currentBranch = repo.active_branch
    print(">" + lib + "切换前分支，", currentBranch)
    # 返回是否有改动（包括未add和未commit的）
    if repo.is_dirty() is True:
        print(">" + lib + "❎本地有未提交的更改")
        return 1

    remote = repo.remote()
    remote.fetch()

    repo.git.checkout(branchName)
    print(">" + lib + "切换后分支，", repo.active_branch)

    print(">" + lib + "✅checkout SUCCESS，", repo.active_branch)
    return 0


def checkout(branchName):
    root = os.getcwd()  # 当前的目录
    # branchName = input("请输入目标分支名:\n")
    code1 = checkout_func("58ClientProject", root, branchName)
    code2 = checkout_func("58JobLib", root + "/58JobLib", branchName)


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

    if branch.strip() == '':
        print('>❎输入的分支为 empty')
    else:
        checkout(branch)


if __name__ == "__main__":
    main(sys.argv[1:])
