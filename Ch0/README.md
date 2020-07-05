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

## Python 的字符串

- 单引号（`'`）双引号（`"`）

    你可以用单引号、ㅔ指示字符串，就如同 `'Quote me on this'` 这样。所有的空白，即空格和制表符都照原样保留。

    在双引号中的字符串与单引号中的字符串的使用完全相同，例如 `"What's your name?"`。

- 三引号（`'''` 或 `"""`）

    利用三引号，你可以指示一个多行的字符串。你可以在三引号中自由的使用单引号和双引号。

## Python 的转义符

`\`

## Python 与 Unicode

Python 允许你处理 Unicode 文本——只需要在字符串前加上前缀 `u` 或 `U`。例如 `u"This is a Unicode string."`。

## Python if while 案例

``` python
#!/usr/bin/python
# Filename: while.py

number = 23
running = True

while running:
    guess = int(raw_input('Enter an integer : '))

    if guess == number:
        print 'Congratulations, you guessed it.' 
        running = False # this causes the while loop to stop
    elif guess < number:
        print 'No, it is a little higher than that' 
    else:
        print 'No, it is a little lower than that' 
else:
    print 'The while loop is over.' 
    # Do anything else you want to do here

print 'Done'
```

## Python for 案例

``` python
#!/usr/bin/python
# Filename: for.py

for i in range(1, 5):
    print i
else:
    print 'The for loop is over'
```

## Python break

`break` 语句是用来终止循环语句的。

## Python continue

用于忽略组块中剩余的语句。

## Python 函数

函数通过 `def` 关键字定义。`def` 关键字后跟一个函数的标识符名称，然后跟一对圆括号。圆括号之中可以包括一些变量名，该行以冒号结尾。

## ChangeLog

- 200625 init
