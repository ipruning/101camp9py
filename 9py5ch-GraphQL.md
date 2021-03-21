---
marp: true
---

# 背景

https://gitlab.com/101camp/9py/tasks/-/commit/f20f0af915bf4525a0ed1c70ee1c08048f9dfc71#note_389408987

@ZoomQuiet 高兴你追查到 GraphQL 接口，这和 RESTful 的区别是什么？使用起来有什么差别？你的体验和建议？

---

# 为什么想要探索 GraphQL？

最近尝试 Headless CMS 可以更轻松的组织内容，跨渠道重用，它严格的将内容和格式分离，使我们回归到内容管理的本源。

一种为你的 API 查询语言，之后用于配置内容模型。例如，10 个同学发来的头像，运营同学可以直接更新官网，而不是重新部署。

---

# REST 是什么

- 看 URL 就知道要什么。即，一个 URL Endpoint 代表一个资源 https://gitlab.com/api/v4/projects/18907382/issues"
- 看 HTTP Method 就知道干什么。通过 HTTP 动词操作资源 POST、GET、PUT、DELETE。
- 看 HTTP Status Code 就知道结果如何。

---

# GraphQL 是什么

- 一种 API 查询语言，之后用于配置内容模型。
- 只有一个 Endpoint https://gitlab.com/api/graphql
- 只有 Query、Mutation 两种操作资源方式
- 基于图数据库 https://dgraph.io/graphql

---

# GraphQL 的优势

- GraphQL 会提示 field argument 的错误，搭配合适的开发工具能有良好的开发体验。鼠标放上去还能看到返回的类型。
- GraphQL 让你可以取你需要的数据，不多也不少，节省空间。
- GraphQL 回避了 REST 需要请求 summary representation 再查询 detailed representation 的问题。（取回所有 Pull Request 但是没有是否 mergeable 的属性，所有需要再查一次）
- GraphQL 支持嵌套查询。

---

# GraphQL 的劣势 #Todo

- 推测和图数据库有关，还没深入信分。
- 增加后端复杂度，99.99% 的需求都可以用简单的方法解决根本不需要上 GraphQL 带来不必要的麻烦与坑。

---

# 使用 GraphQL Voyager 可视化数据库结构最佳实践

在 https://gitlab.com/-/graphql-explorer 中根据 https://apis.guru/graphql-voyager/ 查询，并把返回结果倒入即可。

---

# GraphQL GitLab 实操

这里我选择阅读 GitLab 官方文档，并尝试利用 Python/Postman 调用 GitLab GraphQL & REST API 调用。

- [GitLab GraphQL API Playground](https://gitlab.com/-/graphql-explorer)
- [GitLab GraphQL API Doc](https://docs.gitlab.com/ee/api/graphql/getting_started.html)

---

GraphQL API：

- Method 选 POST
- URL 选 https://gitlab.com/api/graphql
- Authorization 选 Bearer Token 并填写私有 Token。
- Body 选 Query

REST API

- Method 为 GET
- URL 选 https://gitlab.com/api/v4/projects/这里填写RepoID/issues
- Authorization 选 Bearer Token
- Body 无

---

# 坑

GraphQL 无法查询 GitLab Branch。
