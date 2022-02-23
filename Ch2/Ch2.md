# ch2: API 是 MVP 资源
> 101camp9py 第 2 周任务

## summary
> 提要

- Application Programming Interface
    + 应用程序编程接口
- 是一些预先定义的函数，目的是提供应用程序与开发人员基于某软件或硬件得以访问一组例程的能力，而又无需访问源码，或理解内部工作机制的细节;

## story
> 场景/背景/情景/...


06 年前，AWS(亚马逊网络服务) -> 亚马逊网站 (Amazon.com) 旗下 SaaS (云基础设施即服务) 部门创办之初默默无闻，只是亚马逊网站的一个副业。
而今天，AWS 本身就是一家非常成功的公司，年收入高达 100 亿美元，已经是 Amazon 帝国最核心的利益增长点，
更加可贵的是其本身所有服务接口文档以及形式，
已经是整个儿 SaaS 产业标准，其它所有后来者，包括 Google 的 GCP 业务集群，
都不得不先兼容 AWS 接口，才可能扩展自己的。

AWS 历史一切可以追溯到 2000 年前后，
当时这家公司想要推出一项名为 Merchant.com 的电子商务服务，
旨在帮助像 Target 或 玛莎百货 (Marks & Spencer) 这样的第三方商家，
在亚马逊的电子商务平台基础上搭建在线购物网站。

后来发现，构建一个外部开发平台比当初想象的要难多了，
因为与许多初创公司一样，
亚马逊网站在 1994 年创办时，
其实没有针对未来需求做好充分的规划。

亚马逊不知不觉中构建了一堆凌乱的系统，而不是一个井然有序的开发环境。这样一来，区分各项服务，构建一个对第三方来说大有用处的集中式开发平台是个巨大挑战。

正是那一年，Jeff Bezos 强行要求从现在起就内部的所有团队提供的所有服务/功能，
必须以 API 访问的方式来发布以及使用，
以此为根本原则，实质上已经无形中将整个儿 Amazone 变成了一个 100% 云端化企业，
一切业务都可以无缝自动化迁移/备份/扩容/升级/...

但是，当时并没有人意识到这种形态的服务以及开发方式就是一门全新的业务，
直到 AWS 内部建设到一定程度，有足够多的冗余计算能力后，
才提出低价发售一部分内部 API 式服务能力;

没想到，一经发布，就受到创业团队认可，并立即有一大批成功案例涌现;
AWS 一时间几乎变成硅谷创业基础标准配置。

到今天海外几乎所有流行服务都有 RESTful 风格的 API 公开，
并因此形成了二级服务，即组合各种稳定的主服务，变成全新的更加方便的产品/服务。




## problems
> 现实问题，知识阐述



Python 作为跨平台通用动态脚本语言，是注定会流行的：

![python_environment](https://imgs.xkcd.com/comics/python_environment.png)

即便有上图所示的复杂运行时环境加载问题，
但是，语言生态带来巨大便利，
总是能快速协助用户完成构想，实现 MVP(最小可用产品),

而用户越来越活跃，应用领域越来越广，问题也越来越明显：

- 随着用户增长，Python 直面的实际问题也在增长
    + 当用户解决了新问题，并将其封装为标准模块时
    + 通过什么渠道来标准化的广播给全球所有 Python 用户？
    + 这将是 Python 得以腾飞的核心动力
- 可是，1991 Python 发布以来，优秀模块的涌现并不汹涌
- 直到 2000 [distutils](https://packaging.python.org/key_projects/#distutils) 才作为一个模块的打包工具发布
- 2001 [PEP 241](https://www.python.org/dev/peps/pep-0241) 预言并规划了 Python 模块生态的运营图景
- 用了两年，在 2003 年，伟大的 [PyPI](https://packaging.python.org/glossary/#term-python-package-index-pypi) 才上线，模块开始澎湃
- 2004 年，[setuptools](https://packaging.python.org/key_projects/#setuptools) 发布，并以 `.eeg` 为目标对象完成模块编译/发行 (毕竟，Python 的模块当然是个`蛋`)
- 2008 **[pip](https://packaging.python.org/key_projects/#pip) ** 替代前者成为官方推荐模块管理工具，加入 Python 发行版本
    + 同时将模块编译目标升级为：`wheel`
    + (反正一定得是圆东西)
- 从那时起，Python 用户再也不用：
    + 先必须安装 `easy_install` 
    + 然后，再用 `easy_install` 安装 `setuptools` 
    + 最后，才能用 `setuptools` 来安装上 `pip` 
    + 最终，进入无尽的 `PyPi` 世界了...
- 当然，另外为了解决开发/测试/发行/生产环境中 Python 模块依赖问题
    + 人们还尝试有其它模块依赖管理工具
    + 比如：`pipenv`, peep, buildout, zc.buildout, ...
    + 但是，pip 至今还是最稳定的模块管理工具
- 你值得拥有 ;-)




### 剪枝效应
> 为什么直接开发项目，比学知识要有效？

这儿有一个可怕的秘密：

    没有学校/教程是教授编程的
    以往所有课程都是讲述编程语言而已

然而，知识来源自实践，
特别是软件开发，一向比理论发展的要快，在科学家们研究出全新算法/语言/...之前，
工程师们早已组合/开发出全新的工具链来完成任务了。

所以，在直接面对经过实践/总结/术语化/撰写/印刷 后原先鲜活的工程经验，就变成了枯燥的知识点。

> 怎么破？

回到编程原本的行为序列中来：

- 2/8 原理揭示了世界一种自然法则：
    + 核心问题/资源/效率/... 总是只有 20%
    + 大多数被关注到的，不过是 80% 的噪音/低效/重复性嗯哼
- 也就是说，被抽象总结成型的知识，虽然占 20%
- 但是，要想理解，真正将其化为自身能力，则需要用 80% 的时间/精力来亲自嗯哼
- 即：知识发源自经验，但是，知识的习得不可能直接从知识的载体中 got 到
    + 也必须从自身对应经验中重新抽象出来
    + 各种媒介中记录的知识点阐述，也只能算是个路标
    + 以免后进再走弯路
- 综上，`蠎营` 课程，就是利用这一原理：
    + 通过精心设计的任务序列
    + 引导大家通过真实的编程实践
    + 并随时针对具体问题提供有限帮助
    + 对各自编程实践进行 `镇流` 以便高效完成经验->技能的转换以及积累



![chaos comm](https://ipic.zoomquiet.top/2019-08-04-us-chaos-comm.PNG)

如果没有一个坚固的线索来约束实践过程中的尝试/念头，
那么，就如图所示：

    将是一种无法控制的纷乱对撞
    双方都无法对结果有任何控制

不过，由任务组成的线索，不同其它线索：

- 每个任务的成果除了自身依然晦涩难明的新知识体系外
- 还有通过编译器检验的明确/清晰的可运行代码
- 代码是比文本更加可信的经验载体：
    + 因为在运行时环境夯定情况下
    + 无论运行多少次，其结果都是可预期的
    + 而且，代码随着继续封装/隔离/抽象/...
    + 可以变成自己的模块/库/服务/...
    + 继续组合/叠加/嵌入/...嗯哼到其它代码/工程/软件/系统中
    + 即，在可执行层面上完成经验/知识的直接注入
- 而在这个过程中：
    + 一切纷繁的念头都得以是否能通过编译器检验
    + 是否当前代码可正确运行
    + 是否能完成当前设想的功能
    + ...
    + 等等，绝对又简洁的唯一指标来检验
    + 从而将那些控制不了，又不断喷射出的各种有谱没谱想法们
    + `cut` 掉，从而有效专注在当前任务关联的知识点
- 好玩的是，这种有效的象吃豆人一般，一粒粒吃到的经验/知识点
    + 反而能在内部形成知识结构后
    + 可以加速对新问题的决策/实验/完成
    + 那些从一开始先对领域知识进行整体了解后，就能高效解决领域问题的课程
    + 都是妄图...



## task
> 周任务

每周唯一任务，全员尽力完成：

- 鼓励相互协助
- 鼓励相互参考
- 鼓励相互优化
- 鼓励相互进行一切有助进步的交互


### prepare:
> 立即分组

- 因为，课程最后有毕业大作业，要求团队协同，
- 所以，提前划分好团队，加速相互熟悉;
- 同时，每位学员对目标作品期待各不相同，按照口味聚合最能形成默契 ;-)


要求：

- 期限: 42 小时以内
    + 逾期未成组成团队的学员
    + 将随机组合为团队
- 人数: 2~4 人
- 行动：
    + ch2d1 先发布自我推荐 Issue
    + 标题：`[info] <gitlabID> 特长 0| 特长 1| 方向 0| 方向 1|...`
    + 使用 HandBook 模板为参考，修改综合陈述自己：
        * 最擅长的技能以及证明
        * 最想学习的编程领域是什么？
        * 最想实现的软件/系统/工具/...是什么？
    + 不用象招聘简历那么完备，快速展示自己的决心就好
    + 给其它所有同学一个第一印象 (是的，这是一个明显的暗示...应该有照片)
    + 充分利用大家各自社交能力
    + 高速交流/宣告/说明/...自己想开发的作品/兴趣方向
        * 提醒：如果可能一定要有录音，而且应该通过云盘分享/记录下来
- 发布：
    + 在决定团队成员后
    + 创建 Issue，使用 `Report` 模板
    + 标题：
        * [team] <团队名 @队长 ID> (缩写，英文名) 作品方向
    + 合理修改/排版发布团队基本信息：
        * 中文名
        * 英文名
        * 缩写
        * 成员，队长
        * 协力分支 (建议直接使用队长的私人分支)
            - 所以，在标题中也要表现出来
        * 作品方向：
            - 概述
            - 当前目测主要技术难点是什么
            - 已经开始看的资料链接


建议：

> 根据大家报名时提交的作品设想

可以大致分为以下几个大方向：


- web:
    + 从搭建 blog 开始
    + 微信小程序
    + 一个可视化网页 demo，根据听能数据制作，用来科普听觉障碍群体的听能差异。
    + 能够制作一个较为精美的 web 网页运用一些简单算法并实现前后端的的连接
    + 能够运用算法独立完成一个完整的网页或系统
- 专门系统：
    + 能够查看到各个版本的法规条款
    + 办公自动化
    + 类似公司简单项目
- 具体工具：
    + 利用中文分词，计算本地 Markdown 卡片相似度最后可视化的软件。
    + 游戏
- 数据科学：
    + 一个能自主学习的软件
    + 人物表情识别系统
    + 主要目标是转型到数据科学岗位，但学了很多发现最终还是绕不开扎实的编程基础
    + 爬取网上数据，自动化办公，开发软件。
    + 一套完整的爬虫系统
    + 一个带有展示页面的神经网络训练模型
- ...
    + 希望了解它怎么让普通的人工作更容易
    + 学习编程思维吧
    + 暂时没有具体作品的想法，希望通过课程学习一点新的技能，提升学习和思维方式
    + ...实际有用的

大家根据自己学习目标相近原则组队

- 但是，毎队不要超过 5 人
- 因为，三人为众，对于协同已经包含很重的沟通成本了


### develop:
> 进一步挖掘课程真实数据...

- 工程名：学习通证
- 英文名: Proof of Learning
- 缩写名: PoL
- 目标：
    + 对课程涉及的各种资源进行一系列自动化监察/统计
    + 最终形成关键活跃度统计图表/排名/...
- 要求：
    + 可运行
    + 输入指令，可以获得：
        * 当前 task 仓库有多少学员 orphan 分支
        * 以便作为进一步客观行为基础数据来自动化监察
    + 本周进一步：
        * 获得所有课程 Issue 数据，包含：
            - 有多少 Issue
            - 各 Issue 有几个回复
            - 每个 Issue / 回复，分别是谁创建/回复的？
        * 这种数据比较重要，需要保存到本地，进一步分析：
            - 所以，请同时合理保存到本地
            - 以合适的格式，以便能随时从本地加载展开统计/分析


![iss](https://ipic.zoomquiet.top/2019-08-04-190804ch2.gif)


#### action
> 具体行动

- ch2d3 之前结成团队，并发布通告 Issue
- 以团队为基础，统一 IDD (Issue Driver Developing)
- d1 创建任务周报 Issue:
    + 使用 `Report` 模板
    + 标题：`[ch2] <团队 @队长 ID> (对当前任务推进状态感想/情绪)`
    + 基于 IDD (Issue Driver Developing , 提案驱动式开发)
    + 用 Issue 进行规划/追踪/讨论/分派/...
        * 每天更新
        * 每个对应子任务，完成后，缀上对应的 commit-log 链接
        * 成员讨论就通过 Issue 的回复
        * 回复也可以对应 replay
        * ...
- 最终，可以在下次例行直播中，可以：
    + 流畅的汇报团队当周进展
    + 展示成果
    + 分享经验
    + 赞扬进步
    + ...
    + 并每一点都有对应证据<--这是重点：
        * 什么是行为证据？
        * 在 gitlab 中关键行为有什么？
            - 分别对应什么链接证据？

### prepare:
> 团队任务

参考：
[初心：是什么打动了我 / Zoe 的 Python 星际之旅](https://zoejane.gitbooks.io/omooc2py/content/0MOOC/like-it.html)

- 团队笔记应该开始周报的发布：
    + 在队长笔记网站中
    + 每周一 2042 前，发布周报，包含：
        * 上周任务完成情况
        * 关键链接和演示说明
        * 回复团队协同状态：
            - 好的
            - 不好的
            - 改进点
- 并在 tasks 仓库团队分支中：
    + Logging 目录下
    + 创建团队手册
    + 文件名模式：`Team[团队缩写].md`
        * 比如: TeamGASC.md
        * 注意，不要包含：
            - 中文
            - 空格
            - 符号
    + 共同追踪团队变化，记录，索引：
        * 团队所有正式会议录音下载链接，文字记要
        * 所有 Issue
        * 所有成员/成员仓库
        * 所有笔记网站外部访问链接
        * 如果有成员原有外部文章发布渠道，也应该给出
            - 比如私人 blog
            - 公众号
            - weibo
            - 知乎
            - ...


### prompting:
> 提示：

- DS: 数据科学相关团队
    + 应该从网络爬虫角度来考虑这个任务的实现
- 其它团队，应该优先从数据获取方便性着手



### option:
> 额外任务，若有余力，也请完成

- 当前笔记网站，使用 原始 html 来组织发布的
- 尝试美化：
    + 使用好看点儿的 CSS 模板？
    + 换用其它简洁的 md -> html 工具？
    + ...

当然，额外任务，不应该占用周任务时间，
可以指定成员轮值/兼职完成探索，
再统一相互协助升级。

参考：
[初心：是什么打动了我 / Zoe 的 Python 星际之旅](https://zoejane.gitbooks.io/omooc2py/content/0MOOC/like-it.html)

- 从第一天开始就记录学习过程中的成功和失败故事吧
    + 先形成笔记习惯，并理想笔记网站应该需要什么功能
        * 然后，才能科学高效的选择对应方案来增补
    + 当前也可以直接在各自课程笔记中追加对应学习感想
- 当前可以参考 [\[inti\] yixin 的起点](https://gitlab.com/101camp/9py/tasks/issues/11)
    + 直接使用 Isuue 公开笔记
- 也可以在 tasks 课程主仓库的私人 orphan 分支中
    + 专门建立 `logging/` 目录
    + 来容纳每天/周笔记
- 推荐文件命名格式为：
    + `yymmdd-101camp9py-你的帐号名-ch?[d?].md`
    + 比如：
        * 200228-101camp9py-zoomquiet-ch0.md ~ 报名阶段的探索笔记
        * 200301-101camp9py-zoomquiet-ch1d0.md  ~ 第 1 周第 0 天的笔记
- 是的，这也意味着：
    + 团队宣告以及每周的周报 Issue 中
    + 每位成员都应该给出自己笔记网站链接
    + 以及，更新对应内容，证明开始笔记


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
- 笔记：基于模板 `NoteCamp` 每周发布 Issue
- 时间帐单: [ch2 \[LOG\] 每日课程用时日报 (#43)](https://gitlab.com/101camp/9py/tasks/-/issues/43) 持续回复
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
    + 所以，4py 就是是正式班四期
- 代表：蟒营 Pythonic 入门正式班第三期
- 所以，进入编程世界，第一个应该形成的习惯就是：
    + 要开始有意识为一切事物/对象设立一个有规律的唯一的名字




## refer
> 参考资料，扩展阅读...

- 永远的：[提问的智慧 ~ How To Ask Questions The Smart Way](https://github.com/DebugUself/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md)
    + [留住你所达到的文明高度. · Yixuan](https://yixuan.li/geek/2016/03/06/mailinglist/)


- [CommandlineTools - Python Wiki](https://wiki.python.org/moin/CommandlineTools?highlight=%28CLI%29)
    + [awesome-python#command-line-tools](https://github.com/vinta/awesome-python#command-line-tools)
    + [Command-line Applications — The Hitchhiker's Guide to Python](https://docs.python-guide.org/scenarios/cli/)
    + [docopt](http://docopt.org/)


- [Architectural Styles and the Design of Network-based Software Architectures](https://www.ics.uci.edu/%7Efielding/pubs/dissertation/top.htm)
    + [RESTful Web - Geek Starter](http://pythonic.zoomquiet.top/data/20141202091001/index.html)
    + [理解 RESTful 架构 - 阮一峰的网络日志](http://pythonic.zoomquiet.top/data/20110912210739/index.html)
    + [RESTful 架构详解 | 菜鸟教程](http://www.runoob.com/w3cnote/restful-architecture.html)
- [HTTP 幂等性概念和应用 | | 酷 壳 - CoolShell](https://coolshell.cn/articles/4787.html)
- [Best Practices for Designing a Pragmatic RESTful API | Vinay Sahni](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)
    + [RESTful Web Services (豆瓣)](https://book.douban.com/subject/2054201/)
    + [GitHub API v3 \| GitHub Developer Guide](https://developer.github.com/v3/)
- [Learn html in Y Minutes](https://learnxinyminutes.com/docs/html/)
- [Learn css in Y Minutes](https://learnxinyminutes.com/docs/css/)
- [Bottle: Python Web Framework — Bottle 0.12.16 documentation](https://bottlepy.org/docs/0.12/)


![requests](https://ipic.zoomquiet.top/2019-08-04-requests-sidebar.jpg)


- [快速上手 — Requests 2.18.1 文档](http://cn.python-requests.org/en/latest/user/quickstart.html)
- [Chapter 14 – Working with CSV Files and JSON Data](https://automatetheboringstuff.com/chapter14/)
- ...

- [Index · Git · Topics · Help · GitLab](https://gitlab.com/help/topics/git/index.md)
    + [Index · Branches · Repository · Project · User · Help · GitLab](https://gitlab.com/help/user/project/repository/branches/index.md)
    + [Command-line-commands · Gitlab-basics · Help · GitLab](https://gitlab.com/help/gitlab-basics/command-line-commands.md)
    + [Start-using-git · Gitlab-basics · Help · GitLab](https://gitlab.com/help/gitlab-basics/start-using-git.md)
    + [Create-your-ssh-keys · Gitlab-basics · Help · GitLab](https://gitlab.com/help/gitlab-basics/create-your-ssh-keys.md)
    + [Add-image · Gitlab-basics · Help · GitLab](https://gitlab.com/help/gitlab-basics/add-image.md)
    + [Gitlab flow · Workflow · Help · GitLab](https://gitlab.com/help/workflow/gitlab_flow.md)
    + ...
- [git-cheat-sheet.pdf](https://about.gitlab.com/images/press/git-cheat-sheet.pdf)
- [A Visual Guide to Version Control – BetterExplained](https://betterexplained.com/articles/a-visual-guide-to-version-control/)
    + [GitHub 协作五大业余姿势 - ishanshan's blog](https://ishanshan.im/community/HbGitHubCooperate.html)



- 有关调试和开发过程细节演示：
    + 视频链接:https://pan.baidu.com/s/1j6wqz_HyOKEHbDj6PC_0DQ  密码:gikj
    + 内容: 93 分钟现场编程
    + 代码：处理时间帐单历史非规格数据清洗


> Pythonic 

- 本身是即有单词
- 意为：神谕的，预言的，大蟒蛇的
- 但是，在 Python 技术社区，则指代了一种实效精神：
    + 以够用为第一目标，先快速解决问题，再逐步优化
    + 不仅仅能在 Python 编程中实践，在其它任何工程场景中都可适行



## logging
> 版本/追踪/修改...

- 200705 1742 9py 发布
- 200607 1242 8py 发布
- 200503 1242 7py 发布
- 200405 2242 6py 发布
- 200308 2242 5py 发布
- 200208 2242 4py 发布
    + 增补 4py 中 SSG 场景
- 190929 2242 发布
- 190927 3py 调节
- 190804 2242 发布
- 190729 重构
- 190414 发布
- 190409 统一节奏
- 190401 优化结构
- 180111 章结构明确
- 180101 init.
