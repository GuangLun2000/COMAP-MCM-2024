### 模板演示------2020美赛D题

-   文档类型、应用的样式sty文件
-   本sty文件识别不了中文，故不要输入中文、中文标点
-   题号、队伍号、标题的输入
-   **`\begin{document}……\end{document}`是必不可少的。**
-   Notations表格的改进(使用`\hline`而非`\midrule`)
-   三线表的综合应用（在博客的[第二篇LaTeX札记](https://levitate-qian.github.io/2020/07/06/latex-note-02/)有一定的说明）
-   列表环境中的换行（就是列表环境里面怎么不出现编号，当然就是不写没有`\item`）
-   在LaTeX中插入PDF，用于插入信件（见附录前被注释的那一段）
-   相对位置的引用（指的是图片和代码位置的引用）
-   **建议使用XeLaTeX进行编译，而非其他编译方法。在生成目录的过程中，做好要编译两次。**

（上述有的没来得及讲，有什么看不懂的问我吧。）

*（最近有点忙，beamer做的比较仓促，今天讲的不太行，大家见谅/(ㄒoㄒ)/~~）*



## 网址归纳

+ 编程队友知乎：[阿尔法杨XDU - 知乎 (zhihu.com)](https://www.zhihu.com/people/mu-yi-yang-42-66/columns)

+ 论文队友Blog：https://levitate-qian.github.io/

  + 【配置环境】[如何优雅的书写LaTeX论文 | Levitate_ (levitate-qian.github.io)](https://levitate-qian.github.io/2020/07/21/latex-vscode/)
  + 【常用代码】[【持续更新】论文常用LaTeX代码 | Levitate_ (levitate-qian.github.io)](https://levitate-qian.github.io/2020/08/30/latex-code/)
  + 【表格相关】[LaTeX札记（二）：表格 | Levitate_ (levitate-qian.github.io)](https://levitate-qian.github.io/2020/07/06/latex-note-02/)
  + 【公式相关】[LaTeX札记（三）：公式 | Levitate_ (levitate-qian.github.io)](https://levitate-qian.github.io/2020/07/12/latex-note-03/)
  + 【作图相关】[10类案例带你了解论文插图制作 | Levitate_ (levitate-qian.github.io)](https://levitate-qian.github.io/2020/05/04/10类案例带你了解论文插图制作/)（配着下面视频看更佳）
  + 【总经验-转杨神】[【转】数学建模竞赛经验分享 | Levitate_ (levitate-qian.github.io)](https://levitate-qian.github.io/2020/06/18/MCM-experience-sharing/)
  + 【数模历程-一丢丢心路历程吧】[听说西电有一支有丶东西的数模队 | Levitate_ (levitate-qian.github.io)](https://levitate-qian.github.io/2020/04/29/数学建模-听说西电有一支有丶东西的数模队/)
  + 【用处不大的一些句子】[数模论文替换词、短语 | Levitate_ (levitate-qian.github.io)](https://levitate-qian.github.io/2020/03/09/数模论文替换词、短语/)

+ 插图制作视频：[【西电MSC】数模美赛冠名O奖学长教你论文插图制作_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili](https://www.bilibili.com/video/BV1c5411W7U9) （标题有点离谱，为了吸引眼球）

+ tex模板来源：https://github.com/qyxf/easymcm/releases （不知道会不会更新新的，如果今年Summary Sheet 不改的话问题不大；同时模板顶端的2020MCM/ICM到2021年是会更新成2021的不用手动改）

+ 《数学建模竞赛入门& 美赛经验分享》beamer中出现的网址

  + 学校选修PPT：https://alpha-yang.lanzous.com/b01tqvl8h 提取码：ge1o
  + 阿尔法杨XDU. 数模竞赛备赛常用模型与算法：https://zhuanlan.zhihu.com/p/147853046
  + 【MATLAB】强推b 站教程，台大郭彦甫.MATLAB 教程：https://www.bilibili.com/video/BV1GJ41137UH?from=search&seid=10111640569179808375
  + 【ML】[可选]吴恩达教授的《Machine Learning》课程：https://www.bilibili.com/video/BV164411b7dx?from=search&seid=92807526979575575
  + 阿尔法杨XDU. 如何写出一篇高质量的数模竞赛答卷：https://zhuanlan.zhihu.com/p/145434397
  + 2017-2020 年数模美赛O 奖论文合集 https://zhuanlan.zhihu.com/p/314325181

+ 《$\LaTeX$入门》beamer中出现的网址

  + 一份（不太）简短的$\LaTeX2\varepsilon$ 介绍[Index of /CTAN/info/lshort/chinese/ | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/CTAN/info/lshort/chinese/)
  + $\LaTeX$ 科技排版：华师大老师的网站，主要是讲座的beamer [LaTeX科技排版 (ecnu.edu.cn)](http://www.math.ecnu.edu.cn/~jypan/Teaching/Latex/)
  + MathF(图片转公式)：[MathF (mathcode.herokuapp.com)](https://mathcode.herokuapp.com/)
  + 在线LaTeX公式编辑器：[在线LaTeX公式编辑器-妈叔出品 (latexlive.com)](https://www.latexlive.com/)
  + 表格转$\LaTeX$：[Create LaTeX tables online – TablesGenerator.com](https://www.tablesgenerator.com/latex_tables)

  
