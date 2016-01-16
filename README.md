# TJUThesisLatexTemplate

Latex template for TJU thesis. Forked from code.google.com/p/tjuthesis

# 说明

本魔改适用于 texlive 2015，使用 xelatex 进行编译。在 OS X 下进行修改与测试，不保证其它平台的正常使用。

# 魔改内容

* 天大 logo 更新及矢量校名
* 移除 CJK，使用 ctex
* 根据现行本科生毕业论文规范修改格式
* 适应 OS X 与 xelatex

# 编译

* 打开终端
* `cd`到模板目录下
* `python compile.py`，脚本会自动执行多次编译（以保证目录、图、表等编号正确）并清理各种 log, synctex, aux 文件

# License

名义上 MIT，实际上 WTFPL – Do What the Fuck You Want to Public License.