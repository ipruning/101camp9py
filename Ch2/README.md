# Ch2: API 是 MVP 资源

## 明确任务

- 获得所有课程 Issue 数据, 包含:
    - 有多少 Issue
    - 各 Issue 有几个回复
    - 每个 Issue / 回复, 分别是谁创建/回复的?
- 这种数据比较重要, 需要保存到本地,进一步分析:
    - 所以, 请同时合理保存到本地
    - 以合适的格式, 以便能随时从本地加载展开统计/分析

## 分析探索

- 用 GraphQL 实现 GitLab Issue 查询 e1ef3b5b74d520ca6a983b753b7cb70f31f68d63
- 查询常见数据结构，最后采用 JSON 作为本地保存
- 试写一个 JSON 文件读取程序 dc9996b8752e84f05ae40cc470ce6e2ee9c5c83e
- 利用 JSON 改造 PoL 增加从 configs/default.json 中读取 API 配置的功能 912e19cc083fb6981f0e982ec23f8ef119b15442
- 将 GraphQl API 查询封装为一个 Class d837c5a9e8c6414f148850f12a044f2aeddc5f49
- 创建 Class 时，检索 Class 命名的最佳实践 f20f0af915bf4525a0ed1c70ee1c08048f9dfc71
- 将 REST API 查询封装为一个 Class f20f0af915bf4525a0ed1c70ee1c08048f9dfc71
- 将两个 Class 存入 ./pol/api.py 导入 ./pol/main.py。遇到模块无法导入，最后通过重制路径解决 `export PYTHONPATH=.` f20f0af915bf4525a0ed1c70ee1c08048f9dfc71
- 跟着 LPTHW 中单元测试案例 f57ee2ec2179970fbe6d5c9c2d1978e364f03159 试写 ./tests/test_main.py f78d1967b9ed301c7dc937a8b1f929587638de6f

## ChangeLog

- 200731 fix 补充章节 2 任务探索
- 200706 init
