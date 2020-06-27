# Ch0 笔记

## Git

- `git clone https://gitlab.com/101camp/9py/tasks.git --branch your_branch --single-branch` # Clone single branch
- `git checkout old_branch` # Rename branch locally
- `git branch -m new_branch` # Rename branch locally
- `git push origin :old_branch` # Delete the old branch
- `git push --set-upstream origin new_branch` # Push the new branch, set local branch to track the new remote

## guessno 任务

- 修正 Print 格式后试运行，报错 `NameError: name 'raw_input' is not defined`
- 推测可能函数用错，构造检索式 `Python input`
- 搜到 https://www.runoob.com/python/python-func-input.html，了解 input () 和 raw_input ()
- 构造检索式 `input () raw_input ()` 检索一年内信息，阅读后得知在 python3.x 中，已经删除 raw_input ()，取而代之的是 input ()
- 把最后一个颜文字前的反斜杠 `\` 修改为 `\\`
- 修改后程序能正常运行 ![guessno 运行截图](https://i.loli.net/2019/07/18/5d3049e8702fa86761.png)

所以，在 Python3.x 中 input () 函数接受一个标准输入数据，返回为 string 类型。

``` python
from random import uniform # 用于从 random 中导入 uniform 到目前命名空间

myNumber = int(uniform(2,99)) # uniform(x,y) 返回一个 x、y 之间的浮点数，int() 将其转化为整形，并存入 myNumber
noGuess = 1

while noGuess: # 因为 noGuess 为一，表达式为真，所以不断循环
    urNumber = int(input('guess 1~99 number? --> ')) # 在 Python 中四个空格作为缩进显示嵌套关系
    if urNumber < myNumber: print ("...(~_~) small") # 判断表达式的真值
    elif urNumber > myNumber: print ("......big (^_-")
    else:
        print ("u got it \\(^o^)/ play again")
        break # 跳出循环
```

通过这个任务，我学到：

- Pythonx.x 大版本号没有向下兼容，应该首先考虑版本问题
- 检索式构建错误，应该从官方文档出发检索，即使用 `raw_input site:docs.python.org` 在第三条就能看到答案 ![检索式](https://i.loli.net/2019/07/18/5d3043f5b09e244249.png)
- 正确的资料搜索路径，先官网 -> 再英文 -> 最后中文 -> 实在没法儿了, 用 baidu 娱乐一下, 再回到官网。

## ChangeLog

- 200625 init
