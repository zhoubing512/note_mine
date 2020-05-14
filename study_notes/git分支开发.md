###git 分支开发

* **新建分支**
```javascript
git branch zbmenu
```

* **切换到新建的分支**
```javascript
git checkout zbmenu
```
git branch可以看到已经在zbmenu分支上

* **更新分支代码并提交**
```javascript
git add *

git commit -m "init zbmenu"

git push --set-upstream origin zbmenu
```
* **合并分支代码**
```javascript
如：将zbmenu分支代码合并到master分支

先切换到master分支

git checkout master

merge代码，保证主分支代码最新

git merge zbmenu

push到远端仓库

git push
```
