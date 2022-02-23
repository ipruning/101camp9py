# Ch1: CLI 是元袓 MVP

## Python 项目结构

``` markdown
ProjectName/
|-- bin/
|   |-- ProjectName
|
|-- docs/
|   |-- conf.py
|   |-- XXXX.md
|
|-- ProjectName/
|   |-- __init__.py
|   |-- main.py

|-- tests/
|   |-- __init__.py
|   |-- test_main.py
|
|-- setup.py
|-- requirements.txt
|-- README.md
```

- bin：存放可执行文件
- docs：存放文档
    - conf.py：配置文件
- ProjectName：存放所有源代码、包
- tests：存放单元测试源代码
- setup.py: 安装、部署、打包脚本，可用 setuptools 管理
- requirements.txt: 存放依赖的外部 Python 包
- README.md：Github 创始人 Tom Preston-Werner 发明的 README 文件驱动协同方法论，更详细的描述参见 [Readme Driven Development](http://tom.preston-werner.com/2010/08/23/readme-driven-development.html)。

```bash
# 生成 requirements.txt 文件
pip freeze > requirements.txt

# 安装 requirements.txt 依赖
pip install -r requirements.txt
```

## Argparese

不要用 `argparese.py` 作为文件名

## Reference

- [结构化您的工程](https://pythonguidecn.readthedocs.io/zh/latest/writing/structure.html)

## ChangeLog

- 200705 fix 补充 Python 项目笔记
- 200604 init
