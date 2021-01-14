# TJUThesisLatexTemplate

Latex template for TJU thesis. Modified from [here](https://code.google.com/p/tjuthesis)

# 说明

天津大学本科生毕业论文 LaTeX 模版。

# 为何使用 LaTeX

在刚刚结束的毕业设计撰写中，很多使用 Word 的同学在写作过程中出现大量难以解决的格式问题，非常蛋疼。LaTeX 虽然学习曲线较为陡峭，但花费一个小时左右时间熟悉后即可完全专注于内容撰写而无需操心任何格式问题。本模版即旨在你只需复制粘贴修改具体内容即可作出 __完全__ 符合天大现行规范的毕业设计。

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

首先请阅读文档《[一份不太简短的 LaTeX 介绍](http://www.ctan.org/tex-archive/info/lshort/chinese/)》，了解 LaTeX 的基础语法。

打开 `Thesis/preface/cover.tex`，修改封面内容。

打开 `Thesis/body.tex`，开始根据示例书写你的毕业设计。绝大部分需求（标引、插图、表格、数学公式、代码环境）等均在示例中有所体现，可直接复制粘贴修改内容。

## 数学公式

数学公式的具体书写方式参考文档《[一份不太简短的 LaTeX 介绍](http://www.ctan.org/tex-archive/info/lshort/chinese/)》，注意：需要标号的公式请在`equation`环境下配合`\label{}`标签使用，在需要引用的地方使用`\eqref{}`命令引用相应公式。示例如下：

```latex
销售商决策如式~\eqref{rcond}~所示：
\begin{equation}
    \label{rcond}
    \left\{\begin{array}{l}
        p_{1s}=v_h-(v_h-p_2)\mathbb{E}(\varphi)                            \\
        p_{2s}=v_l                                                         \\
        q_s \in \underset{q \geq 0}{\mathrm{argmax}} \beta_R (q, p_1, p_2) \\
    \end{array}\right.
\end{equation}
```

## 插图与表格

参考文档与模板示例。建议图像使用`.eps`矢量格式，放入 `figures` 目录下。

插图示例：

```latex
图像如图~\ref{fig:simuP1P2Result}~所示。
\begin{figure}[htbp!]
    \centering
    \includegraphics[width=0.75\textwidth]{figures/p1p2figure.eps}
    \caption{最优$p_1, p_2$仿真结果}\label{fig:simuP1P2Result}
    \vspace{-1em}
\end{figure}
```

表格示例：

```latex
\begin{table}[htbp]
    \caption{符合本科生毕业论文绘图规范的表格}\label{tab:table1}
    \vspace{0.5em}\centering\wuhao
    \begin{tabular}{ccccc}
        \toprule[1.5pt]
        $D$(in) & $P_u$(lbs) & $u_u$(in) & $\beta$ & $G_f$(psi.in) \\
        \midrule[1pt]
        5       & 269.8      & 0.000674  & 1.79    & 0.04089       \\
        10      & 421.0      & 0.001035  & 3.59    & 0.04089       \\
        20      & 640.2      & 0.001565  & 7.18    & 0.04089       \\
        5       & 269.8      & 0.000674  & 1.79    & 0.04089       \\
        10      & 421.0      & 0.001035  & 3.59    & 0.04089       \\
        20      & 640.2      & 0.001565  & 7.18    & 0.04089       \\
        5       & 269.8      & 0.000674  & 1.79    & 0.04089       \\
        10      & 421.0      & 0.001035  & 3.59    & 0.04089       \\
        20      & 640.2      & 0.001565  & 7.18    & 0.04089       \\
        5       & 269.8      & 0.000674  & 1.79    & 0.04089       \\
        10      & 421.0      & 0.001035  & 3.59    & 0.04089       \\
        20      & 640.2      & 0.001565  & 7.18    & 0.04089       \\
        \bottomrule[1.5pt]
    \end{tabular}
    \vspace{\baselineskip}
\end{table}
```

## 参考文献

所有参考文献在 `Thesis/references/reference.bib` 中。BibTex 格式的参考文献可通过以下步骤获得：

* 打开浏览器，访问 [Google Scholar](http://scholar.google.com)
* 查找你所需的文献
* 点击文献下方 引用/cite 按钮
* 在弹出框内点击 BibTex
* 复制新窗口里的文本粘贴到 reference.bib 中
* 在 body.tex 中需要引用的地方使用`\cite{}`命令进行引用，括号里填参考文献第一行左花括号后面的 identifier。如使用下面推荐的工具链可以实现参考文献自动补全

## 目录，字体，字号，编号，序号，页码，页眉，排版...

全都是自动的。

# 关于本魔改

本魔改适用于 texlive 2020，使用 `xelatex->bibtex->xelatex->xelatex` 编译链。在 macOS, Windows 10 下进行修改与测试，无法完全保证其它平台的正常使用。希望 Linux 用户踊跃反馈。

## 魔改内容

* 天大 logo 更新及矢量校名
* 移除 CJK，使用 ctex
* 根据现行本科生毕业论文规范修改格式
* 适应 macOS, Windows 与 xelatex
* 为适应我推荐的工具链做了一些优化

## 编译

> - 以下编译操作都**需要用户进入 `tjumain.tex` 所在目录下**
> - 有多种编译形式，本质都一样，选择某种自己喜欢的即可，欢迎补充。

### 使用`Latexmk`编译

#### 首先检查是否安装了`Latexmk`

```bash
latexmk -help
```

如果没有报错，正确打印了类似如下所示的帮助信息即说明`Latexmk`已在机器上安装。

```
Latexmk 4.67: Automatic LaTeX document generation routine

Usage: latexmk [latexmk_options] [filename ...]

  Latexmk_options:
   -aux-directory=dir or -auxdir=dir
                 - set name of directory for auxiliary files (aux, log)
                 - Currently this only works with MiKTeX
   -bibtex       - use bibtex when needed (default)
   -bibtex-      - never use bibtex
   -bibtex-cond  - use bibtex when needed, but only if the bib file exists
   -bibtex-cond1 - use bibtex when needed, but only if the bib file exists;
                   on cleanup delete bbl file only if bib file exists
   -bm <message> - Print message across the page when converting to postscript
   -bi <intensity> - Set contrast or intensity of banner
   -bs <scale> - Set scale for banner
   -commands  - list commands used by latexmk for processing files
   -c     - clean up (remove) all nonessential files, except
            dvi, ps and pdf files.
            This and the other clean-ups are instead of a regular make.
   -C     - clean up (remove) all nonessential files
            including aux, dep, dvi, postscript and pdf files
            and file of database of file information
...
```

#### 使用`Latexmk`编译

```bash
latexmk -pvc -xelatex -file-line-error -interaction=nonstopmode -synctex=1 tjumain.tex
```

运行命令，`Latexmk`会使用 xelatex 引擎编译 `tjumain.tex` 文件，并在 PDF 阅读器中打开预览，并持续更新文件。当然，它也会监测文件保存动作，并自动重新编译。

使用`Latexmk`应该可以做到只需运行一次，然后每次文件保存动作后，自动重新编译。

#### 清理临时文件

运行LaTeX之后，当前目录被大量临时文件污染；可以使用这个命令清理

```bash
latexmk -c
```

这不会删除`.pdf /.ps /.dvi`如果你想删除这些文件，使用

```bash
latexmk -C
```

_更多`Latexmk`命令参数及其含义可以查询help手册或者通过文档等其他方式了解。_

### 手动编译

**依次运行**以下四条命令：

```bash
xelatex tjumain.tex
bibtex tjumain.aux
xelatex tjumain.tex
xelatex tjumain.tex
```

注意：由于存在目录、参考文献和图表编号等，需要多次编译以保证顺序正确。

### 其他编译方式

相信大家一定可以自己解决😉，非常欢迎在此分享。


## 清理缓存及日志

### Atom

安装插件`language-latex`和`latex`，提供 Build 和 Clean 的功能。

### Visual Studio Code

安装插件 `LaTeX Workshop`，提供 clean up

### 其他

也可使用 [@Halcao](https://github.com/Halcao) 提供的小脚本：

* 打开终端
* 拖入 `clean.sh` 执行

如提示 Permission Denied，请使用 `chmod +x空格`，然后拖入 `clean.sh`，再次拖入 `clean.sh` 执行即可。

# 推荐工具链

* 发行版
    * macOS: MacTex
    * Windows: TeX Live
* Visual Studio Code
	* LaTeX Workshop
* Atom
	* language-latex
	* latexer
    * latextools
* Sublime Text 3
	* LatexTools
	* Latex-cwl
	* LatexWordCount

注意：使用 VS Code 配合 LaTeX Workshop 插件，可能需要在 VS Code 设置中加入

```js
"latex-workshop.latex.tools": [
    {
        "name": "xelatex",
        "command": "xelatex",
        "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "%DOCFILE%" // 将%DOC%替换成%DOCFILE%可以支持编译中文路径下的文件
        ]
    },
    {
        "name": "bibtex",
        "command": "bibtex",
        "args": [
            "%DOCFILE%"
        ]
    }
],
"latex-workshop.latex.recipes": [
    {
        "name": "xelatex",
        "tools": [
            "xelatex"
        ],
    },
    {
        "name": "xe->bib->xe->xe", // 使用本模板推荐的编译链
        "tools": [
            "xelatex",
            "bibtex",
            "xelatex",
            "xelatex"
        ]
    },
],
"latex-workshop.latex.clean.fileTypes": [ // 清除编译生成的中间文件
    "*.aux",
    "*.bbl",
    "*.blg",
    "*.idx",
    "*.ind",
    "*.lof",
    "*.lot",
    "*.out",
    "*.toc",
    "*.acn",
    "*.acr",
    "*.alg",
    "*.glg",
    "*.glo",
    "*.gls",
    "*.ist",
    "*.fls",
    "*.log",
    "*.fdb_latexmk",
    "*.bcf",
    "*.run.xml",
    "*.synctex.gz"
]
```

# 致谢

tjuthesis 的原作者们作出了前人栽树的不可磨灭的贡献：

* 张井 天津大学2010级管理与经济学部信息管理与信息系统专业硕士生
* 余蓝涛 天津大学2008级精密仪器与光电子工程学院测控技术与仪器专业本科生

以及北京大学孟祥溪院士，膜。

# License

由于原项目使用 GNU GPL v3 协议，本项目作为基于 tjuthesis 的衍生项目，仍保持 GNU GPL v3 协议。
