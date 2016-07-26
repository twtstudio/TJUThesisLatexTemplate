# TJUThesisLatexTemplate

Latex template for TJU thesis. Modified from code.google.com/p/tjuthesis

# 说明

天津大学本科生毕业论文 LaTeX 模版。

# 为何使用 LaTeX

在刚刚结束的毕业设计撰写中，很多使用 Word 的同学在写作过程中出现大量难以解决的格式问题，非常蛋疼。LaTeX 虽然学习曲线较为陡峭，但花费一个小时左右时间熟悉后即可完全专注于内容撰写而无需操心任何格式问题。本模版即旨在你只需复制粘贴修改具体内容即可作出__完全__符合天大现行规范的毕业设计。

LaTeX 加本模板可以实现：

* 无比优雅的数学公式
* 章节的自动标号
* 公式的自动标号
* 插图的自动标号
* 表格的自动标号
* 目录的自动生成
* 参考文献和标引的自动标号
* __所有格式的自动正确__

# 如何使用本模板

## 基本使用

首先请阅读文档《[一份不太简短的 LaTeX 介绍]((http://www.ctan.org/tex-archive/info/lshort/chinese/))》，了解 LaTeX 的基础语法。

然后打开 Thesis/preface/cover.tex，修改封面内容。

然后打开 Thesis/body.tex，开始根据示例书写你的毕业设计。绝大部分需求（标引、插图、表格、数学公式、代码环境）等均在示例中有所体现，可直接复制粘贴修改内容。

## 数学公式

数学公式的具体书写方式参考文档《一份不太简短的 LaTeX 介绍》，注意：需要标号的公式请在`equation`环境下配合`\label{}`标签使用，在需要引用的地方使用`\eqref{}`命令引用相应公式。

## 插图与表格

参考文档与模板示例。建议图像使用`.eps`矢量格式，放入 figures 目录下。

## 参考文献

所有参考文献在 Thesis/references/reference.bib 中。BibTex 格式的参考文献可通过以下步骤获得：

* 打开浏览器，访问 [Google Scholar](http://scholar.google.com)
* 查找你所需的文献
* 点击文献下方 引用/cite 按钮
* 在弹出框内点击 BibTex
* 复制新窗口里的文本粘贴到 reference.bib 中
* 在 body.tex 中需要引用的地方使用`\cite{}`命令进行引用，括号里填参考文献第一行左花括号后面的 identifier。如使用下面推荐的工具链可以实现参考文献自动补全

## 目录，字体，字号，编号，序号，页码，页眉，排版...

全都是自动的。

# 关于本魔改

本魔改适用于 texlive 2015，使用 xelatex 进行编译。在 OS X（macOS）下进行修改与测试，无法完全保证其它平台的正常使用。希望 Windows/Linux 用户踊跃反馈。

## 魔改内容

* 天大 logo 更新及矢量校名
* 移除 CJK，使用 ctex
* 根据现行本科生毕业论文规范修改格式
* 适应 OS X 与 xelatex
* 为适应我推荐的工具链做了一些优化

## 编译

之前的编译脚本（调用命令行 `xelatex tjumain.tex`）会导致参考文献无法编译，正在努力解决问题，请以正常编译 LaTeX 文档的方式编译 tjumain.tex 或 body.tex。

注意：由于存在目录、参考文献和图表编号等，需要多次编译以保证顺序正确（推荐4次为佳）。

## 清理缓存及日志

如使用 Atom 编辑器，可安装插件`language-latex`和`latex`，提供 Build 和 Clean 的功能。

也可使用我提供的小脚本：

* 打开终端
* 拖入 clean.py 执行

如提示 Permission Denied，请使用 `sudo chmod 777`。

# 推荐工具链

* OS X: MacTex, Windows: ctex
* Editor: Sublime Text 3
	* LatexTools
	* Latex-cwl
	* LatexWordCount
* 可选：Atom
	* language-latex
	* latex

# 致谢

tjuthesis 的原作者们作出了前人栽树的不可磨灭的贡献：

* 张井 天津大学2010级管理与经济学部信息管理与信息系统专业硕士生
* 余蓝涛 天津大学2008级精密仪器与光电子工程学院测控技术与仪器专业本科生

以及北京大学孟祥溪院士，膜。

# License

WTFPL – Do What the Fuck You Want to Public License.
