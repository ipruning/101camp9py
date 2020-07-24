# Web 是高速 MVP
> 101camp9py 第3周任务



## summary
> 提要


互联网已经发展为移动互联网, 
可以说互联网早已每天/无时不刻弥漫在周遭, 
必须有能力自主加入其中, 而不是永远作为被广播的被动方.



## story
> 场景/背景/情景/...


Web 1.0 时代, 所在计算机系刚好是学校首届, 
所以, 建设校园网, 包含学校官网的构建都是我们这届上;
那时, 真就是一边看着技术手册, 一边用 Notepad (在 win3.2 系统中) 手工编写每个 html 的;

工作前, 自学了一系列网页编辑工具, 
其中 [macromedia dreamweaver](https://en.wikipedia.org/wiki/Adobe_Dreamweaver)
(macromedia 公司97年成立, 2005被 Adobe 收购, 所以, 现在只有 Adobe Dreamweaver) 工具因为包含了可定制模板功能,
在供职的首家公司中, 还成功安利给同事们一套件内部元模块来快速复用到不同网站中;

但是, 在没有 asp 加持时, 网页都是静态的呢,

虽然, 没有 flash (macromedia 当年还有个 FireWork 专门用来设计/管理/生成 Flash 交互动画)
那么好看又好玩, 而且也不用依赖复杂的后台系统,
单纯一个工具, 发布为一个文件就可以完成一个网站方案呢...

当年是那么喜欢 flash , 甚至于后来真的在上海交通局一个项目中过了把瘾:

- 将后台 asp 给出的动态 XML 数据包
- 解析为一个可以智能转换为指定街道地图以及其中 出租车 行驶状态
- 是的: 就是现在 `的的打车` 类似的功能, 不过是使用 flash 4.0 的 actionscript 来完成
- 而调试方式和 PHP 完全相同:
    + 只是 PHP 通过将后台终端中打印调试信息
    + flash 则是通过在界面中插入一个调试信息输出区域对象
    + 在开发阶段可以打印出运行时数据对象的真实数据而已

要知道, 那时平均每秒 flash 动画市值是1000元起的;

谁想的到, 不过几年, flash 就变成了没有浏览器支持的废品?

其实, 万维网发明的目标就是为了数据互联, 以便打破 `专用硬件+专用软件+专用数据` 僵死格局;
所以, 在 Ajax 组合技术提出之前,
可想人们为了让 web 页面能有交互, 是多么努力折腾啊...

不过,其中 [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) 的概念被更加简单的 URL 无形中替代了,
直到 RESTful 的重新提出, 大家才发现, [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)  才是 web 的本质.


## problems
> 现实问题,知识阐述

数据是弥漫在消息中的,而消息充斥在我们周围, 随着移动互联网的发展, 
更加肆无忌惮的弥漫了...

可是只有数据是难以形成理解和概念的:

- 比如, 我们通过各种手段长期坚持, 记录了一条河流每天最高/低水位
    + 连续记录了10年
    + 那么, 如何通过历史记录预测下周水位
    + 以便决定是灌溉呢还是等等?
- 换个角度, 再比如, 我们真实记录了课程学习过程中
    + 每天每个任务花费的时间长度
    + 坚持了几周, 遇到新任务时
    + 我们如何预测这一新任务可能需要多久才能完成?
- 这就需要将数据进一步整理/统计/可视化
    + 以便帮助我们发现规律, 或是印证规律
- 进一步的, 数据以及统计结果的交流也非常重要
    + 毕竟无论数据采集/清理/整理/统计/...都需要时间
    + 而数据是永远在变动的
    + 也就是说通过通过代码自动完成的阶段统计也只能代表统计出结果那一瞬间世界的状态
    + 如何高速将状态数据发布出来?
    + 甚至于能将多个业务/统计系统串/并联起来, 获得更大范畴, 更深入的结论?
- 也就是说, 如何令程序之间高速交流?
    + 是的, 就是大家已经接触到的 API 
    + Application Programming Interface
    + 应用程序编程接口 -> 简称接口


以往网络协议还处于探索阶段时, 根据硬件条件出现过非常多种

(开始报个菜名哪)

- 数据链路层:Wi-Fi(IEEE 802.11) · WiMAX(IEEE 802.16) ·ATM · DTM · 令牌环 · 以太网 ·FDDI · 帧中继 · GPRS · EVDO ·HSPA · HDLC · PPP · L2TP ·PPTP · ISDN·STP · CSMA/CD 等
- 网络层协议:IP (IPv4 · IPv6) · ICMP· ICMPv6·IGMP ·IS-IS · IPsec · ARP · RARP · RIP 等
- 传输层协议:TCP · UDP · TLS · DCCP · SCTP · RSVP · OSPF 等
- 应用层协议:DHCP ·DNS · FTP · Gopher · HTTP· IMAP4 · IRC · NNTP · XMPP ·POP3 · SIP · SMTP ·SNMP · SSH ·TELNET · RPC · RTCP · RTP ·RTSP· SDP · SOAP · GTP · STUN · NTP· SSDP · BGP 等


... 别怕, 之所以, 列这么多, 并不是要求大家都去理解...

- 而是给大家展示一下人类是多数努力来打破计算间的隔离
- 好消息是, 发展到今天, Internet ~ 互联网已经足够智能
- 而且, 最通用的协议也已经稳定在了两个:
    + e-mail
    + web(TCP/IP)
- 前者只能单向/异步, 虽然可以通过其它手段完成伪实时双向交流, 但是, 过于情怀了
- 所以, 大家一开始能发布 web 应用/接口/数据就足以融入互联网了


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
- 英文名: Proof of Learning
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
    + 本周进一步:
        * 探索获得课程以来所有分支学员的所有 commit 数据:
            - 何时
            - 由谁
            - 可选:
                + 删除了几行
                + 变更了几行
                + 修改了几个文件
        * 以及相互讨论的 Commit-Comments 数据:
            - 何时
            - 由谁
            - 可选:
                + 针对哪行代码/文字
                + 写了多少字 Comments?


#### action
> 具体行动

- 以团队为基础, 统一实践 IDD (Issue Driver Developing)
- d1 创建任务周报 Issue:
    + 使用 `Report` 模板
    + 标题: `[ch3] <团队@队长ID> (对当前任务推进状态感想/情绪)`
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


![IDD demo](https://ipic.zoomquiet.top/2019-08-08-190504IDD.jpg)


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
    + `logging/` 目录中
    + 创建团队手册
    + 文件名模式: `Team[团队缩写].md`
        * 比如: TeamFoo.md
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


### option:
> 额外任务, 若有余力, 也请完成

- 现在每周统计出来的课程活跃度数据越来越详细
- 详细数据已经无法直觉的观察到课程活跃情况了
- 请尝试:
    + 选择一种 web 网站发布引擎
    + 在本地发布统计出来的数据:
        * 当前整体数据,一共多少:
            - is ~ Issue?
            - ic ~ Issue-Comments?
            - ci ~ Commit?
            - cc ~ Commit-Comments?
        * 指定成员数据: 同上四项
- 进一步的, 尝试用最简单的方式, 将本地 web 网站可以发布到公共网络中:
    + 以便其它成果可以通过我们发布的网站接口访问到统计数据?
    + 比如:
        * `http://[ip地址][:拟定端口|默认 80]/api/v0/9py/commits`
        * `http://[ip地址][:拟定端口|默认 80]/api/v0/9py/ccomments`
        * ...

提示:

- 不必永久稳定发布
- 可以在团队内部完成远程协同测试就好
- 记得截屏/录像 => gif 分享出来就好.


![ch3](https://ipic.zoomquiet.top/2019-08-11-101camp2py-ch3.gif)





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



- [Client-Server Overview - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview)
- [WebApplications - Python Wiki](https://wiki.python.org/moin/WebApplications)
    + [Web Applications & Frameworks — The Hitchhiker's Guide to Python](https://docs.python-guide.org/scenarios/web/)
    + [ObpLovelyPython/PCS304 Python Web应用框架纵论](https://wiki.woodpecker.org.cn/moin/ObpLovelyPython/PCS304)
        * [Bottle: Python Web Framework — Bottle 0.13-dev documentation](https://bottlepy.org/docs/dev/)
- [curl/curl: A command line tool and library for transferring data with URL syntax, supporting HTTP, HTTPS, FTP, FTPS, GOPHER, TFTP, SCP, SFTP, SMB, TELNET, DICT, LDAP, LDAPS, FILE, IMAP, SMTP, POP3, RTSP and RTMP. libcurl offers a myriad of powerful features](https://github.com/curl/curl)
    + [jakubroztocil/httpie: As easy as httpie /aitch-tee-tee-pie/ 🥧 Modern command line HTTP client – user-friendly curl alternative with intuitive UI, JSON support, syntax highlighting, wget-like downloads, extensions, etc. https://twitter.com/clihttp](https://github.com/jakubroztocil/httpie)
    + [Chapter 11 – Web Scraping](https://automatetheboringstuff.com/chapter11/)
    + ...
- [ngrok - secure introspectable tunnels to localhost](https://ngrok.com/)
- [Readme · Api · Help · GitLab](https://gitlab.com/help/api/README.md)
    + [Events · Api · Help · GitLab](https://gitlab.com/help/api/events.md)
    + ...
- [invoke · PyPI](https://pypi.org/project/invoke/)
- [pickle --- Python 对象序列化 — Python 3.7.4 文档](https://docs.python.org/zh-cn/3/library/pickle.html)
    + [marshal --- Internal Python object serialization — Python 3.7.4 文档](https://docs.python.org/zh-cn/3/library/marshal.html)
    + ...


> Pythonic 

- 本身是即有单词
- 意为: 神谕的,预言的,大蟒蛇的
- 但是, 在 Python 技术社区, 则指代了一种实效精神:
    + 以够用为第一目标, 先快速解决问题, 再逐步优化
    + 不仅仅能在 Python 编程中实践, 在其它任何工程场景中都可适行

## logging
> 版本/追踪/修改...

- 200712 re-pub 9py
- 200614 re-pub 8py
- 200510 re-pub 7py
- 200412 re-pub 6py
- 200315 re-pub 5py
- 191215 re-pub 4py
- 191006 re-pub 3py
- 190929 review
- 190811 2242 发布
- 190810 增补参考
- 190809 re-重构
- 190729 重构
- 190414 发布
- 190409 统一节奏
- 190401 优化结构
- 180111 章结构明确
- 180101 init.
