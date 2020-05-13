###1. 新建分支
```javascript
git branch zbmenu
```

###2. 切换到新建的分支
```javascript
git checkout zbmenu
```
git如何新建分支
1) 切换到基础分支，如主干

git checkout master

2）创建并切换到新分支

git checkout -b panda

git branch可以看到已经在panda分支上

3)更新分支代码并提交

git add *

git commit -m "init panda"

git push origin panda