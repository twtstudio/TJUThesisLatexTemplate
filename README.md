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

之前的编译脚本（调用命令行 `xelatex tjumain.tex`）会导致参考文献无法编译，正在努力解决问题，请以正常编译 latex 文档的方式编译 tjumain.tex。注意：由于存在目录及参考文献等，需要多次编译以保证顺序正确。

# 清理缓存及日志

* 打开终端
* 拖入 clean.py 执行

如提示 Permission Denied，请使用 `sudo chmod 777`

# License

名义上 MIT，实际上 WTFPL – Do What the Fuck You Want to Public License.