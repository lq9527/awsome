import os
import subprocess
from git import Repo
import sys, getopt


# TODO 目录自动获取


def merge_func(lib, dir, branchName):
    os.chdir(dir)
    repo = Repo()
    currentBranch = repo.active_branch
    print(">" + lib + "切换前分支，", currentBranch)
    # 返回是否有改动（包括未add和未commit的）
    if repo.is_dirty() is True:
        print(">" + lib + "❎本地有未提交的更改")
        return 1

    remote = repo.remote()
    # repo.git.fetch()
    # subprocess.call(['git','pull','origin',str(currentBranch)])
    # repo.git.checkout(branchName)
    subprocess.call(['git','fetch'])
    subprocess.call(['git','pull'])
    code = subprocess.call(['git','merge','--no-commit','origin',str(currentBranch)])

    if(code == 0):
        print(">" + lib + "✅merge SUCCESS")
    else:
        print(">" + lib + "❎merge ERROR")

    return 0


def merge(branchName):
    root = os.getcwd()  # 当前的目录
    # branchName = input("请输入目标分支名:\n")
    code1 = merge_func("58ClientProject", root, branchName)
    code2 = merge_func("58JobLib", root + "/58JobLib", branchName)


def main(argv):
    branch = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["obranch="])
    except getopt.GetoptError:
        print('batch_merge.py -o <branch>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('batch_merge.py -o <branch>')
            sys.exit()
        elif opt in ("-o", "--obranch"):
            branch = arg

    if branch.strip() == '':
        print('>❎输入的分支为 empty')
    else:
        merge(branch)


if __name__ == "__main__":
    main(sys.argv[1:])
