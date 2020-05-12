# git 多仓库，批量操作脚本
[TOC]

### 功能
多仓库，多分支开发，往往需要频繁的切分支，git操作。这里通过python 脚本，简化操作；

###### 批量更新
- 命令：python batch_pull.py      
- 场景：一键更新多个仓库

###### 批量创建分支
- 命令：python batch_create.py -o <branchName>
- 场景：在当前工作分支的基础上，拉取新的分支

###### 批量切换分支
- 命令：python batch_checkout.py -o <branchName>
- 场景：一键切换多仓库分支

### 运行环境

- 需要安装 GitPython库

```
sudo pip install gitpython
```
- python 3.x：

```
Python 3.7.0  & mac os catalina 10.15.4 亲测可行;
window 没有测试
```

- 脚本放在58ClientProject 目录下即可


```

特殊情况，可以修改源码，有注释，很简单

```

