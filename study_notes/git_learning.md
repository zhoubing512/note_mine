###问题1：git commit
git: git commit 提交时，提示Please enter the commit message for your changes......如何解决？

![git_problem](./images/git_commit_problem.png)

```bash
 Please enter the commit message for your changes. Lines starting

 with '#' will be ignored, and an empty message aborts the commit.



 On branch master

 Your branch is up to date with 'origin/master'.
```
提交git commit 时，没有输入说明导致

当前页面输入 :wq ，回车即可退出该页面
**注意：** 冒号+wq（wq要小写）

退出后重新提交，git commit -m 后面添加上代码提交说明即可

git commit -m "代码提交说明"---代码提交说明可以任意写(最好代码说明有意义，方便日后查询)
