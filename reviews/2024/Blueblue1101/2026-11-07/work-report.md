# 王婉婷｜AI4S 论文复核与漏筛补录工作汇报

2026 年 11 月 8 日 · GitHub：Blueblue1101 · 论文年份：2024

**初筛候选已全部复核；本次继续完成 2,276 条，新增确认纳入 87 篇。成果已保存本地，尚未上传 GitHub。**

## 已有进度与本次增量

此前已完成 1,574 条初筛候选复核，其中包含原有 1,383 条个人记录；加上漏筛检查和文献类型排除，共形成 8,451 条审核记录。这些成果全部保留，本次只接着未审清单处理。

| 指标 | 本次新增 | 当前累计 |
|---|---:|---:|
| 完成审核记录 | 2,276 | 10,727 |
| 确认漏筛并纳入 | 87 | 1,198 |
| 补齐并核验完整摘要 | 330 | 1,175 |



当前个人文件：**纳入 2,349 篇、排除 7,824 条、待定 554 条**。全量数据还有 **19,741 条未审**，这些是刊会全部文章，不等于还剩同样数量的 AI4S 候选。

## 各来源本次处理量

本次主要从已有全量数据中查找关键词漏筛。下表“漏筛补入”不是重新爬取的论文；本次没有新增经官网确认的漏采论文。摘要补齐与论文采集分开统计。

| 期刊 / 会议 | 本次续审 | 漏筛补入 | 排除 | 待定 |
|---|---:|---:|---:|---:|
| CVPR | 590 | 65 | 506 | 19 |
| Nature Communications | 575 | 4 | 542 | 29 |
| Science Translational Medicine | 247 | 1 | 231 | 15 |
| Renewable and Sustainable Energy Reviews | 174 | 8 | 148 | 18 |
| Science Immunology | 160 | 0 | 132 | 28 |
| Trends in Ecology & Evolution | 133 | 1 | 130 | 2 |
| Applied Catalysis B Environment and Energy | 123 | 0 | 119 | 4 |
| Trends in Molecular Medicine | 105 | 0 | 103 | 2 |
| Matter | 49 | 0 | 47 | 2 |
| Pharmacological Reviews | 36 | 0 | 35 | 1 |
| Neuron | 22 | 1 | 20 | 1 |
| Artificial Intelligence Review | 21 | 3 | 18 | 0 |
| eTransportation | 8 | 2 | 5 | 1 |
| Information Fusion | 7 | 1 | 6 | 0 |
| Advances in Applied Energy | 6 | 1 | 4 | 1 |
| International Journal of Mining Science and Technology | 4 | 0 | 4 | 0 |
| Nature Physics | 4 | 0 | 3 | 1 |
| Journal of Energy Chemistry | 3 | 0 | 1 | 2 |
| Chem | 2 | 0 | 1 | 1 |
| Molecular Cell | 2 | 0 | 2 | 0 |
| Journal of Materials Science & Technology | 2 | 0 | 2 | 0 |
| Nano Energy | 2 | 0 | 2 | 0 |
| Energy Storage Materials | 1 | 0 | 1 | 0 |
| **合计** | **2,276** | **87** | **2,062** | **127** |

## 规则与标签

沿用 main 当前规则，仅根据摘要判断科学任务、AI 的作用及两者关系，排除评论、宣传与其他不合要求类型。遇到致谢、正文片段或残缺摘要，单独标记；证据不足的条目列为待定，没有把它们计为完整摘要补齐。

词表已同步至 main `285a238`（748 项）。此前提出的“支持向量机”已在共享词表中，直接复用；“梯度提升树”统一到现有“梯度提升”。累计保留 6 项本地新增词项（含此前的食品来源鉴别）。本次新提 5 项；如有新增，具体规范名与定义见交付包中的标签记录。以下列出本次最常用的标签，同一篇论文可有多个标签，完整列表另存《本次续审标签明细.md》。

| 常用标签 | 英文规范名 | 本次使用篇数 |
|---|---|---:|
| AI 用于工程科学 | AI for engineering sciences | 65 |
| 反问题 | Inverse problem | 19 |
| AI 用于生命科学 | AI for life sciences | 14 |
| Transformer 架构 | Transformer | 13 |
| 物理与数据融合建模 | Hybrid physics-data modeling | 12 |
| 交通场景建模 | Traffic scenario modeling | 8 |
| 隐式神经表示 | Implicit neural representation | 8 |
| 大语言模型 | Large language model | 8 |
| 人体姿态识别 | Human posture recognition | 6 |
| 扩散模型 | Diffusion model | 6 |
| 自动驾驶感知 | Autonomous driving perception | 6 |
| 机器人航迹规划 | Robot trajectory planning | 6 |

## 覆盖范围与剩余工作

新清单 49 个来源中，38 个与此前实际审核的 41 个来源重合，约占新清单的 78%；11 个来源此前没有个人审核记录，但不代表仓库未采集。保留另外 3 个历史来源后，本地工作范围共 52 个来源、30,468 条记录。

官网目录核验沿用已保存证据：12 个 Nature 系列来源及 CVPR、ECAI 已完成相应目录比对；Nature Communications 仅完成年总量及部分成员核验。已核验范围未确认具体漏采，不能据此宣称所有刊会补漏完成。访问失败的来源按效率优先要求暂缓。

接下来继续未审记录、待定摘要与未核实链接。GitHub 因 2FA 无法登录，**本轮没有创建远程提交或 PR**；恢复登录后需再同步词表，再提交个人 JSON 与审计文件。

三个子代理仍受额度限制；2026年11月8日主模型已从断点继续并保存新增156条。全量审核仍未完成。

另外，历史成果与他人文件有 890 条同键记录，其中 46 条判定不同，已单列审计；本次新增记录中有 0 条同键重合。上传前需核对历史差异，未覆盖他人的文件。
