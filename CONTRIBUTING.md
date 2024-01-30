# 贡献者指南

首先，感谢为本项目付出宝贵时间！

以下是些指导性建议，并非强制要求。一般您阅读 [README](./README.md) 即可，此处只针对复杂修改。

## 🔄实时预览

如果您有一定计算机基础（例如能运行 Python 程序），可在本地实时预览修改效果。

1. [克隆][git-book]本仓库。

2. 安装依赖。

   ```shell
   $ just bootstrap
   ```

   这会使用`python -m pip`安装一些包。

   > [!NOTE]
   >
   > [`just`](https://just.systems/man/en/chapter_1.html)是个命令运行器；您也可手动运行[`justfile`](./justfile)中的命令。

   > [!TIP]
   >
   > 若想指定用哪一`python`，请创建[`.env`文件](https://just.systems/man/en/chapter_26.html)，写入`PYTHON = "/path/to/python"`，例如`PYTHON = "py -3.12"`（使用 Python 3.12）或`PYTHON = "./.venv/Scripts/python.exe"`（使用[虚拟环境][python-venv]）。

3. 编辑。

4. 本地预览。

   ```shell
   $ just serve
   ```

   若使用 VS Code，还可以按<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd>调用任务。

[git-book]: https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E8%8E%B7%E5%8F%96-Git-%E4%BB%93%E5%BA%93 "2.1 Git 基础 - 获取 Git 仓库 | Pro Git"
[python-venv]: https://docs.python.org/zh-cn/3/tutorial/venv.html "12. 虚拟环境和包 | Python 3 文档"
