# Git 学习

### [Git 初始化](init.md)

### [Git 拉代码](pull.md)

### [Git 提交修改](commit.md)

### [Git 推送代码](push.md)

### [Git 撤销修改](reset.md)

### [Git 同步代码](sync.md)

### [Git 回退代码](back.md)

## git checkout 切换分支或恢复工作树文件

git checkout <branch>  切换到分支 ，切换分支会清除修改，所以要先提交在切换分支      
git checkout -b branchname 创建并切换到新的分支.    
git checkout -f branchname 强制切换到分支.原分支的修改会被清除，可以先提交规避

```shell
git checkout .  # 放弃工作区中全部的修改

git checkout -- filename  # 放弃工作区中某个文件的修改：

git checkout -f  # 强制放弃 index 和 工作区 的改动,这是不可逆的操作，会直接覆盖
```

## git commit 记录对存储库的更改

git commit -m "message"：提交暂存区到本地仓库中，[message] 可以是一些备注信息。   
git commit -a： -a参数设置修改文件后不需要执行 git add 命令，直接来提交，文件添加还是需要先git add 再commit   
git commit --amend：出现编辑界面（vim），按i键进入编辑模式，编辑完后按ESC键退出编辑，然后输入:wq回车退出并保存修改，完成提交

## git stash

git stash 暂存工作目录   
git stash list 查看暂存工作目录文件/提交    
git stash push 追加暂存工作目录     
git stash pop 恢复暂存工作目录     
git stash pop {index} 恢复第几个暂存提交
`git stash pop stash@{id} # example`

git stash drop <stash@{id}>  删除stash。
> 如果不加stash编号，默认的就是删除最新的，也就是编号为0的那个， 加编号就是删除指定编号的stash。    
git stash clear 是清除所有stash,整个世界一下子清净了！

git stash push -a "messeag"，添加改动到stash。 -a选项才会将新加入的代码文件同时放入暂存区。

## git fetch - 从另一个存储库下载对象和引用

git fetch --append 将提取的引用的引用名称和对象名称追加到现有内容中。如果没有此选项，中的旧数据将被覆盖   
git fetch --depth=<depth> 限制提取的提交数

## git pull - 从另一个存储库或本地分支获取并与之集成

将远程存储库中的更改合并到当前分支中。如果当前分支位于远程分支后面，则默认情况下，它将快进当前分支以匹配远程分支。如果当前分支和远程分支已发散，则用户需要指定如何将发散分支与 或（或 中的相应配置选项）进行协调。

`git pull <远程主机名> <远程分支名>:<本地分支名>  # 格式，如果远程分支是与当前分支合并，则冒号后面的部分可以省略。 `
git pull --rebase

## git push - 更新远程引用以及关联的对象

`git push <远程主机名> <本地分支名>:<远程分支名>  # 格式，如果本地分支名与远程分支名相同，则可以省略冒号：及后面`    
git push -d 删除远程分支

## git remote - 管理一组跟踪的存储库/远程仓库

git remote -v 查看远程仓库  
git remote add <url>  添加远程仓库  
git remote rename <old> <new>  将名为 <old> 的远程重命名为 <new>。将更新远程跟踪的所有分支和配置设置。    
git remote rm name 删除远程<name>仓库.

` git remote add -f -t master -m master origin git://example.com/git.git/`

```shell
git remote add [name] [url]  # 作用是添加远程版本库

name 是自己取的仓库的名字 url 是地址

这个也是经常用到的, 添加了之后 一般都是使用 git fetch --all 拉去下代码 , 然后在 

git push name HEAD:refs/for/分支名   提交代码.

# 这里name就是刚才自己取的名字.
```

## git am - 将修补程序应用于文件和/或索引

git am llvm.patch 将名字为llvm.patch的patch打上    
git am --signoff llvm.patch 添加-s或者--signoff，还可以把自己的名字添加为signed off by信息，作用是注明打patch的人是谁，因为有时打patch的人并不是patch的作者 git am ~
/patch-set/*.patch 将路径~/patch-set/*.patch按先后顺序打上    
git am --abort 当git am失败时，用以将已经在am过程中打上的patch废弃掉（比如有三个patch，打到第三个patch时有冲突，那么这条命令就把打上的前面两条patch丢弃掉，返回没有打patch的状态） git am
--resolved 当git am失败，解决完冲突之后，这条命令会接着打patch 合入一个patch包
> git apply是另外一种打patch的命令，其与git am的区别是，
> git apply并不会将commit message等打上去，打完patch后需要重新git add和git commit，
> 而git am会直接将patch的所有信息打上去，而且不用重新git add和git commit,author也是patch的author而不是打patch的人

## git apply - 将修补程序应用于文件和/或索引

git apply --check 不要应用修补程序，而是查看修补程序是否适用于当前工作树和/或索引文件并检测错误。   
git apply --index 将修补程序同时应用于索引和工作树。   
git apply --cached 仅将修补程序应用于索引，而不触及工作树。  
git apply --reverse 反向应用修补程序。    
git apply --reject git 应用默认会使整个补丁失败，并且当某些大块不应用时，它不会触及工作树。

## git cherry-pick - 应用一些现有提交引入的更改

git cherry-pick --edit 允许您在提交之前编辑提交消息。 git cherry-pick --abort 取消这次更新

```shell
git cherry-pick master
应用提交在主分支的顶端引入的更改，并使用此更改创建一个新提交。

git cherry-pick ..master
git cherry-pick ^HEAD master
应用所有提交引入的更改，这些提交是 master 的祖先，但不是 HEAD 的祖先，以生成新的提交。

git cherry-pick maint next ^master
git cherry-pick maint master..next
应用所有提交引入的更改，这些提交是维护或下一个的祖先，但不是 master 或其任何祖先。请注意，后者并不意味着 和 之间的一切;具体来说，如果它包含在 中，则不会使用。maintmasternextmaintmaster

git cherry-pick master~4 master~2
应用 master 指向的第五次和第三次最后提交引入的更改，并使用这些更改创建 2 个新提交。

git cherry-pick -n master~1 next
将 master 指向的倒数第二个提交和下一个指向的最后一个提交引入的更改应用于工作树和索引，但不要使用这些更改创建任何提交。

git cherry-pick --ff ..next
如果历史记录是线性的，并且 HEAD 是 next 的祖先，请更新工作树并推进 HEAD 指针以匹配 next。否则，将 next 中但不是 HEAD 中的那些提交引入的更改应用于当前分支，为每个新更改创建一个新提交。

git rev-list --reverse master -- README | git cherry-pick -n --stdin
将接触自述文件的主分支上所有提交引入的更改应用到工作树和索引中，以便可以检查结果并在合适的情况下将其转换为单个新提交。
```

## git diff - 显示提交、提交和工作树等之间的更改

git diff [<options>] [--merge-base] <commit> <commit> [--] [<path>...]  这是为了查看两个任意<提交>之间的更改。

## git rebase - 在另一个基本提示之上重新应用提交

```shell
# now in topic
git rebase master
git rebase master topic
```

## git reset Git回退命令

git reset --hard 版本序列号 回退到指定版本    
git reset --soft HEAD~1 撤回上一次的提交，保留提交前的代码	   
git reset HEAD . 撤回上一次文件添加，保留原来修改

## git revert - 还原一些现有的提交

git revert --no-edit 使用此选项，git 还原将不会启动提交消息编辑器。

```shell
git revert HEAD~3  # 在 HEAD 中还原最后一个提交指定的更改，并使用还原的更改创建一个新提交。
```

```shell
git revert -n master~5..master~2
# 将提交所做的更改从 master（包含）中的第五个最后一个提交还原到 master（包含）中的第三个最后提交，但不要使用还原的更改创建任何提交。还原仅修改工作树和索引。
```

## git format-patch 生成patch

git format-patch HEAD^ 生成最近一次commit的patch	  
git format-patch HEAD^^ 生成最近两次commit的patch   
git format-patch <r1>..<r2/>  生成两个commit间的修改的patch,（包含两个commit. <r1>和<r2>都是具体的commit号)   
git format-patch -1 <r1>   生成单个commit的patch	  
git format-patch <r1>    生成某commit以来的修改patch（不包含该commit） git format-patch --root <r1>   生成从根到r1提交的所有patch






<br />
<br />
<br />
<br />
<br />

......    
[回到主目录](../README.md)   
......    


