# SSG 是耐用 MVP
> 101camp9py 第4周任务



## summary
> 提要




![MVP](https://blog.jjonline.cn/Upload/image/201901/20190122170723.png)

其实, 就是得将思考/编程之外的一切, 尽可能自动化.



## story
> 场景/背景/情景/...


"最勤劳的GitHub员工" -- Hubot

最初只是运维团队想偷懒:

- Ryan Tomayko 是 Hubot 的创始人
- 在他之前的 DevOps(持续开发及部署, 一种全新的软件工程态度)公司中, 有类似工具
- 所以到了 GitHub 后, 自然利用全新资源快速构建出一个习惯的工具:
    + 甚至于偷懒用了 CoffeeScript(长的象 Python 的 node.js 方言)
    + 提供一个聊天室一般的界面
    + 然后用 `/` 开头的命令, 来通过 Hubot 进行各种系统管理:
        * 安装/升级系统/软件/配置/模块/...
        * 重启系统
        * 进行测试
        * 通知成员
        * ... 几乎是一切
- 当然, 开始并不是一切, 只是系统管理员们日常的嗯哼
- 但是, Hubot 从一开始就开源了 
    + 而且基于 GitHub 完美的 API 设计经验
    + 本身接口也非常简洁和科学
    + 于是, 全球想偷懒的程序猿都来贡献 Hubot 扩展
    + 现在, Hubot 适配了所有主流操作系统/开发语言/聊天协议/云平台/项目托管空间/...
        * 并促生了第三方生态
        * 类似 IFTTT 的中间件服务厂商
        * 通过联级不同服务间的接口, 为用户提供更加简单/直觉的软件驱动界面
        * 并友好接入 Hubot
- 进而形成了 `ChatOps` 工作方式:
    + 通过编写合适的插件
    + 从而将所有工作都转化为 `Chat`
    + 是的, Slack 不甘心总是被 Hubot 调用
    + 现在也发布了 `SlackBot`
- 以及其它同等兴盛的 `ChatOps` 平台:
    + Ruby 的 Lita
    + Python 的 Errbot


![chatbots](https://ipic.zoomquiet.top/2019-08-19-chatbots.png)



所以, 程序猿最合理的偷懒方式, 就是创造出能为自己干活的 bot ;-)



## problems
> 现实问题,知识阐述

上周任务坑在于...

- 网络是什么?
- 内外网有什么差别?
- 为什么不能将内网应用直接发布到外网?
- 如何从外网调试?
- ...

以及, 为了减少体积, 加速截屏演示 gif 动画后,

- 很多学员肉眼无法 got 到足够细节时,就先放弃了
- 导致, 无法 got 到 `暗示`
- 虽然有小队第一时间, 通过合适的工具, 完成了关键 got
- 但是, 这一经验并没及时扩散到整个儿课程
    + 甚至于, 在 ch3d3 定长直播答疑中, 大妈再次明确提醒
    + 依然没有扩散到位
- 这其实, 才是蟒营学习, 或是说任何学习场景中最大的问题:
    + 如果看过相关技术史就知道
    + 无论中外, 类似曼哈顿项目/apollo工程/两弹一星/...世纪级别成功项目中
    + 无论涉及多少种技术/部门/工厂/...以及多少位技师/科学家/...
    + 任何一个场景中获得的任何一个新经验都通过标准化流程, 尽可能快的传播给全体
    + 而 google 为什么能保持每年非常高的工程师增长速度, 同时工程质量得以保持?
    + 就是通过将上亿行代码保管在唯一一个大版本仓库中
    + 任何一个产品/岗位上, 产生任何新技巧/思想/概念/模块/....
    + 都可以通过内部知识渠道, 立即为全球几万工程师获知, 并能方便的第一时间尝试
- 而在传统文化中, 独门技艺是必须传子不传女的...
- 不过, 在传统师徒制中从来不直接传授, 而是以偷学形式来传承
- 这倒是蟒营发现和自由/开源软件社区中自主学习模式相当的:
    + 从小托入师门
    + 从杂务作起, 一点点儿靠零星说明, 以及自己观察, 私下练习
    + 慢慢成长为可以代师傅作事儿的大徒弟
    + 但是, 核心技术绝对不教
    + 直到积累的经验发现技术关键因素时, 在那一瞬间加以强化:
        * 以往铁匠的焠火都是不传之密
        * 徒弟发现, 无论模仿用料/用火/煅打手法/...所有细节都作到位
        * 但是, 随手住水里最后那一焠出来的效果完全不同
        * 自己怎么折腾, 不是过于韧就是过于刚
        * 终于有一天排除所有可能性, 明确只可能是师傅那水的温度有问题
        * 在师傅准备焠火时, 伸手试那水温
        * 师傅这才用烤红的铁件印到徒弟胳膊上:
            - 说:"记住这个温度吧"
            - 伸出自己的胳膊 --> 相同的烙印
    + 嗯哼, 这不就是BC(血案, Blood Case)嘛?


所以,享受 BC 吧:

- 谁激发的多, 说明谁探索的多
- 在 BC 发生时, 其它环境一般选择无视的
- 而蟒营, 才愿意将 BC 视作进步的契机, 尽力制造并接引为作者成长
- 虽然, 这一过程对心灵冲击是痛苦的, 但是, 也正是成长最快的节点
- 对比其它课程都是竭力避免这种冲突, 事先将对应知识点配套陈列出:
    + 将创造性练习过程
    + 变成枯燥的固定答案记忆列表
- 那么, 无论记忆多少所谓知识, 真正独立写代码时
    + 心理依然条件反射式的想找对应配套知识点说明
    + 那么, 是难以完成任务的
    + 卡到崩溃是可预期的...

以上, 共勉:

    编程知识, 只能通过编程来获得


### Q & A
> 收集并集中回答学员曾反复撞出的问题, 

9py-ch3d3 大妈录制 链接:https://pan.baidu.com/s/1scUy3B92jr1AtKDqJ54NcA  密码:zhy2

## task
> 周任务

每周唯一任务, 全员尽力完成:

- 鼓励相互协助
- 鼓励相互参考
- 鼓励相互优化
- 鼓励相互进行一切有助进步的交互


### develop:
> 进一步挖掘课程真实数据...

- 工程名: 学习通证
- 英文名: Proo of Learnning
- 缩写名: PoL
- 目标:
    + 对课程涉及的各种资源进行一系列自动化监察/统计
    + 最终形成关键活跃度统计图表/排名/...
- 要求:
    + 可运行
    + 输入指令,可以获得:
        * 当前 task 仓库有多少学员 orphan 分支
        * 以便作为进一步客观行为基础数据来自动化监察
    + 获得所有课程 Issue 数据, 包含:
        * 有多少 Issue
        * 各 Issue 有几个 Comment
        * 每个 Issue / Comment , 分别是谁创建/回复的?
    + 这种数据比较重要, 需要保存到本地,进一步分析:
        * 所以, 请同时合理保存到本地
        * 以合适的格式, 以便能随时从本地加载展开统计/分析
    + 探索获得课程以来所有分支学员的所有 commit 数据:
        * 何时
        * 由谁
        * 可选:
            - 删除了几行
            - 变更了几行
            - 修改了几个文件
    + 以及相互讨论的 Commit-Comments 数据:
        * 何时
        * 由谁
        * 可选:
            - 针对哪行代码/文字
            - 写了多少字 Comments?
            - 变更了几行
    + 本周最后一嗯哼:
        * 综合以往挖掘到的数据:
            - ci ~ 每个分支所有 commit
            - cc ~ 每个 commit 可能的 comments
            - is ~ 每个 Issue
            - ic ~ 每个 Issue 可能的 comments
            - 每则数据都有:
                + 触发时间
                + 内容
                + 作者
        * 那么尝试:
            - 给出开课以来总排名吧:
                + top5 ci 
                + top5 cc
                + top5 is
                + top5 ic
                + 每个排都包含 学员id 对应行为数量
            - 可选 -> 给出近7天相同行为的 top5 排名
        * 可选任务:
            - 将以上成果发布为 gitlab-pages 网站吧
            - 类似: [Plain SSG demo (base GitLab Pages)by DAMA](https://101camp.gitlab.io/9py/students/demo/)


#### action
> 具体行动

- 以团队为基础, 统一实践 IDD (Issue Driver Developing)
- d1 创建任务周报 Issue:
    + 使用 `Report` 模板
    + 标题: `[ch4] <团队@队长ID> (对当前任务推进状态感想/情绪)`
    + 基于 IDD (Issue Driver Developing , 提案驱动式开发)
    + 用 Issue 进行规划/追踪/讨论/分派/...
        * 每天更新
        * 每个对应子任务, 完成后, 缀上对应的 commit-log 链接
        * 成员讨论就通过 Issue 的回复
        * 回复也可以对应 replay
        * ...
- 最终, 可以在下次例行直播中, 可以:
    + 流畅的汇报团队当周进展
    + 展示成果
    + 分享经验
    + 赞扬进步
    + ...
    + 并每一点都有对应证据<--这是重点:
        * 什么是行为证据?
        * 在 gitlab 中关键行为有什么?
            - 分别对应什么链接证据?

>> 提醒:

其实, 从第1周开始的周报, 就是当前任务最终参考形式了 ;-)

[weekly · master · 101Camp / 9py / tasks · GitLab](https://gitlab.com/101camp/9py/tasks/blob/master/weekly)




### prepare:
> 团队任务

参考:
[初心:是什么打动了我 / Zoe的Python星际之旅](https://zoejane.gitbooks.io/omooc2py/content/0MOOC/like-it.html)

- 团队笔记应该开始周报的发布:
    + 在队长笔记网站中
    + 每周一 2042 前, 发布周报, 包含:
        * 上周任务完成情况
        * 关键链接和演示说明
        * 回复团队协同状态:
            - 好的
            - 不好的
            - 改进点
- 并在 tasks 维基仓库中
    + Logging 目录中
    + 创建团队手册
    + 文件名模式: `Team[团队缩写].md`
        * 比如: TeamGASC.md
        * 注意, 不要包含:
            - 中文
            - 空格
            - 符号
    + 每周独立章节,共同追踪团队变化,记录, 索引:
        * 团队所有正式会议录音下载链接, 文字记要
        * 所有 Issue
        * 所有成员/成员仓库
        * 所有笔记网站外部访问链接
        * 如果有成员原有外部文章发布渠道, 也应该给出
            - 比如私人 blog
            - 公众号
            - weibo
            - 知乎
            - ...


### prompting:
> 提示:

既然是团队任务:

- 就应该开始考虑如何协同
- 是按功能垂直切分, 还是按数据水平划分?
- 总之要想办法, 形成团队内部节奏:
    + 每个成员, 都有充分的自行探索空间
    + 又同时, 科学的和其它成员形成上下文关系
    + 整体上齐头并进的状态
- 进一步的:
    + 和任务类似, 团队里成员以往(以及当周)
    + 关键行为的统计和对比图表化, 都可以尝试了


### option:
> 额外任务, 若有余力, 也请完成

已经有这么丰富的数据以及统计排名了:

- 基于 markdown 以及 gitlab-pages 内置服务
- 请尝试:
    + 如何通过 CI/CD (持续集成/部署) 功能
    + 令 gitlab 可以感知到小队分支变化
    + 并自动化完成:
        * 统计数据
        * 数据可视化
        * 团队笔记网站更新发布
- 简单说, 是否可以将以往人工指令方式完成的一系列行为
    + 变成可以通过某种仓库行为触发自动化过程?
    + 类似:
        * 在指定目录中新增一个 `__deploy.md` 空白文件
        * push 到 gitlab 后
        * 自动完成后续以往必须人工完成的动作?


提示:

- CI/CD 的工具/服务很多, 各有特色大胆选择
- 但是, 不依赖任何服务,只通过一个长期运行的主机也一样可以完成低配版 CI/CD 响应
    + 甚至于, 什么是触发?
    + 触发只能是被动的嘛?
    + ...
- 记得截屏/录像 => gif 向半年前的自己炫耀吧.







### social coding 
> 光说不练徦把式, 这门课配套有代码仓库, 并强烈建议通过真实的编程实践掌握知识点.

- 仓库: 
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
    + #9py 自动提醒,日常实时讨论
    + #general 通告频道, 课程方重要通知
    + #random 随机主题和蟒营过往所有学员交流
- 笔记: 基于模板 `NoteCamp` 每周发布 Issue
- 时间帐单: [\[LOG\] 每日课程用时日报 (#2)](https://gitlab.com/101camp/9py/tasks/issues/2) 持续回复
- 列表: 101camp9py@googlegroups.com
    + 发言: 直接邮件-> 101camp9py@googlegroups.com
        * 用邮件和所有同学/助教们讨论一切嗯哼...
        * 以及课程自动提醒所有同学的嗯哼...
    + 订阅: 发空白邮件-> 101camp9py+subscribe@googlegroups.com
    + 退订: 发空白邮件-> 101camp9py+unsubscribe@googlegroups.com


101camp9py 是课程编号, 其中:

- 101camp ~ 蟒营, 是课程设计框架和工具箱, 官网 -> 101.camp
- 2py 是课程代号:
    + 0py 是原型班
    + 1py 是正式班一期
    + ...
    + 所以, 9py 就是是正式班四期
- 代表: 蟒营 Pythonic 入门正式班第三期
- 所以, 进入编程世界, 第一个应该形成的习惯就是:
    + 要开始有意识为一切事物/对象设立一个有规律的唯一的名字



## refer
> 参考资料,扩展阅读...

- 永远的: [提问的智慧 ~ How To Ask Questions The Smart Way](https://github.com/DebugUself/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md)
    + [留住你所达到的文明高度. · Yixuan](https://yixuan.li/geek/2016/03/06/mailinglist/)


- [The 52 Best — And Weirdest — Charts We Made In 2016 | FiveThirtyEight](https://fivethirtyeight.com/features/the-52-best-and-weirdest-charts-we-made-in-2016/)
    + [10 Useful Python Data Visualization Libraries for Any Discipline](https://mode.com/blog/python-data-visualization-libraries)
    + [Welcome to Bokeh — Bokeh 1.3.4 documentation](https://bokeh.pydata.org/en/latest/)
    + ...
- [xkcd-style charts in R, JavaScript, and Python | FlowingData](https://flowingdata.com/2012/10/19/xkcd-style-charts-in-r-javascript-and-python)
    + [XKCD-style plots in Matplotlib | Pythonic Perambulations](http://jakevdp.github.io/blog/2012/10/07/xkcd-style-plots-in-matplotlib/)
    + [showcase example code: xkcd.py — Matplotlib 2.0.2 documentation](https://matplotlib.org/examples/showcase/xkcd.html)
    + ...
- [Termgraph](https://github.com/mkaz/termgraph)
    + [maxhumber/chart: 📊 Python charts with 0 dependencies](https://github.com/maxhumber/chart)
    + [tehmaze/diagram: Text mode diagrams using UTF-8 characters and fancy colors](https://github.com/tehmaze/diagram)
    + ...


- CI (Continuous Integration) ~ 持续集成
- CD (Continuous Delivery/Deployment) ~ 持续交付/部署
- [GitLab CI/CD](https://gitlab.com/help/ci/README.md)
    + [Readme · Examples · Ci · Help · GitLab](https://gitlab.com/help/ci/examples/README.md)
    + [Pipelines · Ci · Help · GitLab](https://gitlab.com/help/ci/pipelines.md#visualizing-pipelines)
    + [aitemr/awesome-git-hooks: 😎 A collection of awesome Git Hooks](https://github.com/aitemr/awesome-git-hooks)
        * [Git Hooks | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/git-hooks)
        * [利用 GitHook 构建持续交付和部署 - CODING 博客](https://blog.coding.net/blog/GitHook-for-delivery-and-deployment)
        * ...
- [Index · Pages · Project · User · Help · GitLab](https://gitlab.com/help/user/project/pages/index.md)
    + [SSGs Part 1: Static vs Dynamic Websites | GitLab](https://about.gitlab.com/blog/2016/06/03/ssg-overview-gitlab-pages-part-1-dynamic-x-static/)
    + ...
- [cron \- Wikipedia](https://en.wikipedia.org/wiki/Cron)
    + [Crontab – Quick Reference](https://www.adminschoice.com/crontab-quick-reference)
    + [Crontab Syntax Tutorial With Examples \- LinuxMoz](https://linuxmoz.com/crontab-syntax-tutorial/)
    + [Mcron \- GNU Project \- Free Software Foundation](https://www.gnu.org/software/mcron/)
    + ...


> Pythonic 

- 本身是即有单词
- 意为: 神谕的,预言的,大蟒蛇的
- 但是, 在 Python 技术社区, 则指代了一种实效精神:
    + 以够用为第一目标, 先快速解决问题, 再逐步优化
    + 不仅仅能在 Python 编程中实践, 在其它任何工程场景中都可适行

## logging
> 版本/追踪/修改...

- 200621 2242 发布9py
- 200517 1242 发布7py
- 200418 2242 发布6py
- 200322 2242 发布5py
- 191013 2242 发布
- 190930 re-3py
- 190818 2242 发布
- 190816 增补参考
- 190814 re-重构
- 190729 重构
- 190414 发布
- 190409 统一节奏
- 190401 优化结构
- 180111 章结构明确
- 180101 init.
