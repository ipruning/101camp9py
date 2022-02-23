# Ch3: Web 是高速 MVP

## GraphQL

- [GitLab GraphQL API Playground](https://gitlab.com/-/graphql-explorer)
- [GitLab GraphQL API Doc](https://docs.gitlab.com/ee/api/graphql/getting_started.html)
- [为什么 GraphQL 比 REST 好用？](https://www.bilibili.com/video/BV1f4411A7qA)
- [GraphQL 查询语言入门：官方例子](https://www.bilibili.com/video/BV1hJ41157sz)

## 明确任务

- 探索获得课程以来所有分支学员的所有 commit 数据：
    - 何时
    - 由谁
    - 可选：
        - 删除了几行
        - 变更了几行
        - 修改了几个文件
- 以及相互讨论的 Commit-Comments 数据：
    - 何时
    - 由谁
    - 可选：
        - 针对哪行代码/文字
        - 写了多少字 Comments?
- 选择一种 web 网站发布引擎
- 在本地发布统计出来的数据：
    - 当前整体数据，一共多少：
        - is ~ Issue?
        - ic ~ Issue-Comments?
        - ci ~ Commit?
        - cc ~ Commit-Comments?
    - 指定成员数据：同上四项
- 进一步的，尝试用最简单的方式，将本地 web 网站可以发布到公共网络中：
    - 以便其它成果可以通过我们发布的网站接口访问到统计数据？
    - 比如：
        - `http://[ip 地址][:拟定端口 | 默认 80]/api/v0/9py/commits`
        - `http://[ip 地址][:拟定端口 | 默认 80]/api/v0/9py/ccomments`
        - ...

## 分析探索

## 当前成果

## ChangeLog

- 200715 init
