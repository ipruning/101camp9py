# ch1: CLI 是元袓 MVP
> 101camp9py 第一任务


## summary
> 提要

嗯哼，经过各种折腾，完成 ch0 任务的同学们，讲真哪：

- 本质上已经证明自己拥有编程能力了
- 因为，编程就是这样一种行为模式：
    + 明确问题/目标
    + 分析/分解为一系列阶段子任务
    + 每个任务都有明确的达成指标
    + 逐一完成并检验
    + 齐了...
- 这其中最困难的，就是每个子任务的 `达成指标`:
    + 需要自己独立设定
    + 并设计对应实验来检验
    + 什么是实验？
        * 就是实际检验
        * 输入给定数据
        * 获得期待数据
        * 比如：这坨代码
            - 给 `1+1` 进去
            - 出来的一定是 `2`
            - 否则，就是代码有问题


## story
> 场景/背景/情景/...

上节说过笔者在毕业多年后，通过 Python 完成一个软件，
才算体验了一次完整的开发实践，
从而破除迷妄，自此有自信自学到任何所需技术。

> 那么，猜？是什么软件？

->以俺曾经怼过的`天气预报网络自动抓取工具`来说：

- 因为之前自学过 asp/ActionScript/PHP/.. 等等开发技术
- 但是，都没有形成一个实用功能的独立构造，都是在原有系统基础上的功能增补
- 所以，在发现 Python 是种跨平台的通用脚本语言后：
    + 决定续上大学时一直未了的心愿
    + 独立完成一个软件的开发：
        * 有实用功能
        * 有用户交互
        * 可以运行在各种系统中
        * ...
- 前后用了两周的业余时间;
    + 最终才形成那个不到 100 行的脚本
    + 但是，包含预期的所有功能
    + 特别是过程中不得不学习并就地运用了几十个，在开始前自己绝对预想不到的知识点：
        * 网络请求
        * 页面解析
        * CLI 交互
        * 排版
        * 用户文档
        * ...
- 再回头和以往各种语言的开发体验一对比：
    + 彻底对 Python 有了认同感
    + 内置的模块太多了，几乎支持支撑日常绝大多数情景中的开发
    + 社区生态也非常强大，而且有 Zope 这种怪兽级别的大型应用体系
    + ...
- 一切，都是从完成一个今天看起来功能微小到可以忽略不计的工具软件而触发

所以：

    学习编程
        就得从编程
    直接开干


### 增补背景说明：

- 课程所有内容是在 macOS 系统环境中完成的
- 如果学员日常环境不是 macOS 就没有针对性说明了
    + 好在 Python 本身是跨平台的
    + 只要有了运行环境，其它所有调试/自学过程整体上并无差异
    + 即便有不同，通过日常的搜索也足以自行解决
- 只是，这一课程特殊在：
    + 对于大家如何自行解决问题的过程异常关注
    + 并要求大家尽可能通过合适的渠道 (Issue) 反馈给课程全体
    + 以便进行针对性分析/辅导
    + 并想证明，在自学过程中，失败经验远比成功体验要有用
        * 因为每一次失败都是自身进步的契机，将获得全新知识点/技能树
        * 而每一次成功，只是已往旧经验有效的简单证明

> 简单的说：

- 在任何一个系统环境中学习/实践 Python 都没有问题
- 问题只是在不同的初始化过程，以及编辑器环境：
    + 好在 VSCode 等等一批跨平台编辑器也早已发布
    + 大家可以在任何一种桌面环境中，使用相同的编辑器来嗯哼了。


## problems
> 现实问题，知识阐述

预习任务是：

- 完成基本环境安装：
    + Python 3.7.3 (当然，只要是 Python 3 系列的其实都可以)
- 并运行指定代码
- 尝试理解其中涉及的编程常识：
    + 并形成分析/说明
    + 发布到课程仓库 Issue 中

得承认，开篇任务其实故意埋了很多坑：

- Python 是种软件嘛？从哪儿下载？不同版本可以共存嘛？
    + 如何安装？如何知道安装好了？
    + 如何交互/调试？如何运行自己的脚本？...
- `尝试理解...编程常识` 这好象不是行为，只是结果：
    + 如何理解，怎么尝试？
    + 什么是常识？
    + 分析/说明应该如何写？
    + Issue 是什么？怎么发布文字到 Issue 中？
    + 用什么格式发布？
    + ...
- 可以说，每个具体行动都可能迎头撞到无数问题：
    + 这是进入任何一种陌生知识领域应该的状态
    + 当然，这种状态的体验是极端的，令人反感的
        * 要是过程中，没有起过几次白毛汗，内心，甚至于真的开口骂这坑爹的课程
        * 说明，你并没有开始尝试完成任务...
    + 那么，就象私人健身教练服务：
        * 想减的体脂长在自己身上
        * 教练提供锻炼方案，给出计划，行动要求
        * 如果不真的来撸铁/跑步/控制/饮食/...
        * 那么，无论去充多少钱到卡上
        * 肥肉那真是一毫克也不可能自行消失的哪。
- 所以，先撸起来：
    + 过程中，有任何具体问题，都可以去仓库 Issue 中提出问题
        * 为了引导大家如何思考问题本身
        * 课程已经预先设计好了对应 `Ask` 模板
        * ![](http://ydlj.zoomquiet.top/ipic/2020-04-26-usage-tpl4issue.jpg)
        * 自动为一则新 Issue 填写问题结构
        * 请结合 [提问的智慧 ~ How To Ask Questions The Smart Way](https://github.com/DebugUself/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md) 来服用
    + 这样，讲师/助教/同学/路人/扫地僧/... 无数好心人才能例证回答，提供帮助
    + 但是，如果不问，就憋在心里扎小人，对课程学习是一丝帮助也冇咯


### Q & A
> 收集并集中回答学员曾反复撞出的问题，


当然，期待所有具体问题，都能自行解决并->记要下来发布到课程 wiki 合适目录，

这样，任何同学，再次遇见时，简单丢链接过来就好 ;-)

- Python 的娘家：[About Python™ | Python.org](https://www.python.org/about/)
    + 模块大本营：[PyPI – the Python Package Index · PyPI](https://pypi.org/)
- 以及课程公众号也将跟随报道：

![蟒营](http://ydlj.zoomquiet.top/ipic/2020-02-15-mainium-qr-barnner.jpg)


## task
> 周任务

每周唯一任务，全员尽力完成：

- 鼓励相互协助
- 鼓励相互参考
- 鼓励相互优化
- 鼓励相互进行一切有助进步的交互


### develop:
> PoL -> 学习通证

任何软件都可以抽象为三部分：

- 输入
- 处理
- 输出

所以，实用问题，主要类型也都是：

- 自动化获得目标数据
- 自动化根据设想处置
- 自动化输出指定形式

那么，作为网络课程无论指定外部哪种目标数据都可能引发纠纷，
所以，共同来关注课程本身：

- 工程名：学习通证
- 英文名: Proof of Learning
- 缩写名: PoL
- 整体目标：
    + 对课程涉及的各种资源进行一系列自动化监察/统计
    + 最终形成关键活跃度统计图表/排名/...
- 当周要求：
    + 可运行
    + 输入指令，可以获得当前 tasks 仓库有多少分支
        * 以便作为进一步行为监察的基础数据


> 最终效果参考

![ch1-0-brs](https://ipic.zoomquiet.top/2019-07-28-ch1-0-brs.gif)


#### action
> 具体行动

- 立即创建任务周报 Issue:
    + 使用 `Report` 模板
    + 标题：`[ch1] @自己 ID (对课程当下感想/情绪)`
    + 基于 IDD (Issue Driver Develop , 提案驱动式开发)
    + 用 Issue 进行规划/追踪/讨论/分派/...
        * 每天更新
        * 每个对应子任务，完成后，缀上对应的 commit-log 链接
        * 成员讨论就通过 Issue 的回复
        * 回复也可以对应 replay
        * ...
- 最终，可以在下次例行直播中，可以：
    + 流畅的汇报当周进展
    + 展示成果
    + 分享经验
    + 赞扬进步
    + ...
    + 并每一点都有对应证据。


### prompting:
> 提示：

- DS(Data Science 数据科学) 兴趣相关学员
    + 可以网络爬虫角度来考虑这个任务的实现
    + (注意，但是，并不意味上爬虫.)
- 其它学员，应该优先从数据获取方便性着手

### option:
> 额外任务，若有余力，也请完成

    参考：
[初心：是什么打动了我 / Zoe 的 Python 星际之旅](https://zoejane.gitbooks.io/omooc2py/content/0MOOC/like-it.html)

- 从第一天开始就记录学习过程中的成功和失败故事吧
    + 先形成笔记习惯，并理想笔记网站应该需要什么功能
        * 然后，才能科学高效的选择对应方案来增补
    + 当前也可以直接在各自课程笔记中追加对应学习感想
- 当前可以参考 [\[inti\] yixin 的起点](../../wikis/Usage/yixin-baseline)
    + 倡议：直接使用 Isuue 公开分析笔记，以便每周对比发现自己的进步
- 也可以在 tasks 课程主仓库的私人 orphan 分支中
    + 专门建立 `logging/` 目录
    + 来容纳每天/周笔记
- 推荐文件命名格式为：
    + `yymmdd-101camp9py-你的帐号名-ch?[d?].md`
    + 比如：
        * 200228-101camp9py-zoomquiet-ch0.md ~ 报名阶段的探索笔记
        * 200301-101camp9py-zoomquiet-ch1d0.md  ~ 第 1 周第 0 天的笔记
- 并探索是否能进一步识别出 task 仓库有多少 orphan 分支
    + 关键是，哪些不是？如何能从数据中识别出来？


### social coding 
> 光说不练徦把式，这门课配套有代码仓库，并强烈建议通过真实的编程实践掌握知识点。

- 仓库：
    + https://gitlab.com/101camp/9py/playground
        * 游乐场
        * 实验所有 gitlab 功能
        * 以及尝试 git 的各种操作 -> 才好去正式课程仓库嗯哼
    + https://gitlab.com/101camp/9py/tasks
        * 课程主仓库
        * 每周发布任务/周刊
        * 在各自 私人 分支中持续嗯哼
- 提案: https://gitlab.com/101camp/9py/tasks/issues
    + 日常提问/讨论/建议/...
- 维基: https://gitlab.com/101camp/9py/tasks/wikis
    + 汇集各种资料/FAQ/知识点资料/...
- 直播: Zoom 会议
    + 会议 ID:420 101 4200
    + 密码:101camp
    + 平时大家也可以随时利用 zoom 发起自己交流
- 交流: 101camp.slack.com
    + #9py 自动提醒，日常实时讨论
    + #general 通告频道，课程方重要通知
    + #random 随机主题和蟒营过往所有学员交流
- 笔记：基于模板 `NoteCamp` 每周至少发布一则 Issue
    + 也可以使用 IDD 模式来连续追踪自己当周的探索记要
- 时间帐单: [ch1\[LOG\] 每日课程用时日报 (#37)](https://gitlab.com/101camp/9py/tasks/issues/25) 持续回复
- 列表: 101camp9py@googlegroups.com
    + 发言：直接邮件-> 101camp9py@googlegroups.com
        * 用邮件和所有同学/助教们讨论一切嗯哼...
        * 以及课程自动提醒所有同学的嗯哼...
    + 订阅：发空白邮件-> 101camp9py+subscribe@googlegroups.com
    + 退订：发空白邮件-> 101camp9py+unsubscribe@googlegroups.com


101camp9py 是课程编号，其中：

- 101camp ~ 蟒营，是课程设计框架和工具箱，官网 -> 101.camp
- 2py 是课程代号：
    + 0py 是原型班
    + 1py 是正式班一期
    + ...
    + 所以，9py 就是是正式班四期
- 代表：蟒营 Pythonic 入门正式班第三期
- 所以，进入编程世界，第一个应该形成的习惯就是：
    + 要开始有意识为一切事物/对象设立一个有规律的唯一的名字


## refer
> 参考资料，扩展阅读...

- 永远的：[提问的智慧 ~ How To Ask Questions The Smart Way](https://github.com/DebugUself/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md)
    + [留住你所达到的文明高度. · Yixuan](https://yixuan.li/geek/2016/03/06/mailinglist/)


[What Is Pip? A Guide for New Pythonistas – Real Python](https://realpython.com/what-is-pip/) 

![python_environment](https://imgs.xkcd.com/comics/python_environment.png)

- 以及当前可用的 Python 环境到底是如何的？
- [pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv)
    + [pyenv/pyenv-installer: This tool is used to install `pyenv` and friends.](https://github.com/pyenv/pyenv-installer)
        * [Home · pyenv/pyenv Wiki](https://github.com/pyenv/pyenv/wiki)
        * [Common build problems · pyenv/pyenv Wiki](https://github.com/pyenv/pyenv/wiki/Common-build-problems)
    + [自分の為の python 環境設定まとめ\[mac\]\[ubuntu\] - Qiita](https://qiita.com/miyamotok0105/items/55a828070b6d6abc1a7c)
    + [pyenv と pyenv-virtualenv で環境構築 - Qiita](https://qiita.com/Kodaira_/items/feadfef9add468e3a85b)
    + [Plugins · pyenv/pyenv Wiki](https://github.com/pyenv/pyenv/wiki/Plugins)
        * [pyenv/pyenv-virtualenvwrapper: an alternative approach to manage virtualenvs from pyenv.](https://github.com/pyenv/pyenv-virtualenvwrapper)
    + [An Effective Python Environment: Making Yourself at Home – Real Python](https://realpython.com/effective-python-environment/)
- [python - What is the difference between venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, etc? - Stack Overflow](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe/41573588#41573588)
- [Pocket: Simplify Your Python Developer Environment](http://scm.zoomquiet.top/data/20190323095254/index.html)
    + [My Python Development Environment, 2018 Edition | Jacob Kaplan-Moss](https://jacobian.org/2018/feb/21/python-environment-2018/)
    + [Pyenv+Virtualenv+Virtualenvwrapper 轻量级 python 环境管理 - S.Mona](https://silbertmonaphia.github.io/pyenv+virtualenv+virtualenvwrapper%E8%BD%BB%E9%87%8F%E7%BA%A9python%E7%8E%AF%E5%A2%83%E7%AE%A1%E7%90%86.html)



- [Command-line Applications](https://docs.python-guide.org/scenarios/cli/)
    + [Running Python on your OS](https://www.cs.bu.edu/courses/cs108/guides/runpython.html)
- [如何向完全没有任何编程知识的人介绍编程 - ghosTB10G](http://devrel.zoomquiet.top/data/20140121194425/index.html)
    + [一个神奇的故事 --- 为什么程序能够工作](http://blog.shell909090.org/blog/archives/2530/)
    + [极简 Python 上手导念 - Zoom.Quiet Personal Static Wiki](http://wiki.zoomquiet.io/pythonic/MinimalistPyStart)
    + ...
- [无需翻墙的 python 基本语法练习网站](https://www.learnpython.org/)
- [彩云小译 --- 英文网页内逐行对照翻译的工具](https://fanyi.caiyunapp.com/#/web)
- [刻意练习 ( [美] 安德斯·艾利克森 (Anders Ericsson) / 罗伯特·普尔 (Robert Pool))](https://book.douban.com/subject/26895993/)
    + [天才源自刻意练习 ([美] 杰夫·科尔文)](https://book.douban.com/subject/27088714/)
    + [刻意练习：如何成为一个高手 ((美) 道格•莱莫夫 / 艾丽卡•伍尔韦 / 凯蒂•叶兹)](https://book.douban.com/subject/27054052/)
    + ...
- [ConEmu - Handy Windows Terminal](https://conemu.github.io/)
    + windows 用户的福音...

[SSG](https://about.gitlab.com/2016/06/03/ssg-overview-gitlab-pages-part-1-dynamic-x-static/)

- [SSGs Part 2: Modern Static Site Generators | GitLab](https://about.gitlab.com/2016/06/10/ssg-overview-gitlab-pages-part-2/)
    + [SSGs Part 3: Build any SSG site with GitLab Pages | GitLab](https://about.gitlab.com/2016/06/17/ssg-overview-gitlab-pages-part-3-examples-ci/)
- [Pages · Help · GitLab](https://gitlab.com/help/user/project/pages/index.md)
    + [GitLab Pages examples · GitLab](https://gitlab.com/pages)
- [Plain HTML site using GitLab Pages](https://101camp.gitlab.io/1py/students/demo/)
    + [GitLab Pages · Help · GitLab](https://gitlab.com/help/user/project/pages/index.md)
    + 以及：
        * [几分钟学会 html](https://learnxinyminutes.com/docs/html/)
        * [几分钟学会 css](https://learnxinyminutes.com/docs/css/)

![Markdown](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg/96px-Markdown-mark.svg.png) [Markdown - Wikipedia](https://en.wikipedia.org/wiki/Markdown)

- [Markdown Cheatsheet · adam-p/markdown-here Wiki](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Daring Fireball: Markdown Syntax Documentation](https://daringfireball.net/projects/markdown/syntax)
- [Markdown Guide](https://www.markdownguide.org/)
- ...


> Pythonic 

- 本身是即有单词
- 意为：神谕的，预言的，大蟒蛇的
- 但是，在 Python 技术社区，则指代了一种实效精神：
    + 以够用为第一目标，先快速解决问题，再逐步优化
    + 不仅仅能在 Python 编程中实践，在其它任何工程场景中都可适行

## logging
> 版本/追踪/修改...

- 200628 为 9py 发布
- 200531 为 8py 发布
- 200426 为 7py 发布
- 200328 为 6py 发布
- 200228 调整团队要求到 ch2
- 191229 增补 4py 场景
- 190922 增补发布 3py
- 190919 为 3py 修改
- 190728 2242 发布
- 190725 增补 任务提示
- 190704 发布 2py
- 190630 重构
- 190414 发布
- 190409 统一节奏
- 190401 优化结构
- 180111 章结构明确
- 180101 init.




