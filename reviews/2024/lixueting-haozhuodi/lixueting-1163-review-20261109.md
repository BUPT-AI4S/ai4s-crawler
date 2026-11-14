# 李雪婷 2024 年 1163 条待定记录复核（2026-11-09）

本轮纳入 200 条、排除 690 条、仍待定 273 条；没有新增原始作者摘要。范围是此前全量台账中的全部 1,163 条 pending，包含原个人文件中的 318 条及尚未进入个人交付的 845 条。

| 本轮输入 | 纳入 | 排除 | 待定 | 合计 |
|---|---:|---:|---:|---:|
| 已有摘要 | 200 | 663 | 6 | 869 |
| 缺摘要 | 0 | 27 | 267 | 294 |
| 合计 | 200 | 690 | 273 | 1,163 |

294 条缺摘要记录均检索了 Europe PMC、OpenAlex、出版方及可定位的公开版本。22 条读到正文后排除，5 条依据机构存档明确文献类型排除；267 条仍缺足够正文证据。访问失败、摘要预览、元数据页面不计作已阅读全文，也不把模型生成的概述填成作者摘要。

已有摘要的 869 条均逐篇复核。70 条边界记录进一步查找方法或实验，解决 64 条，仍有 6 条待定。证据详情分别标注输入摘要、正文、出版方节选、相关作者版本或仅检索；两条参考相关作者版本，未将后来文章当作已读会议原文。

## 最新李雪婷个人统计

| 范围 | 纳入 | 排除 | 待定 | 合计 |
|---|---:|---:|---:|---:|
| 个人交付 JSON | 2,309 | 1,976 | 273 | 4,558 |
| 2024 全量审核台账 | 2,309 | 26,707 | 273 | 29,289 |

845 条此前仅在全量台账中的记录本轮补入个人交付；两份记录的 273 条待定标识完全一致。上述是李雪婷文件与全量台账统计，网站若因其他交付存在冲突而暂不计数，应以逐篇证据核对；本轮未修改其他负责人文件。

## 仍需原文的 6 条已有摘要记录

- **Brain Cortical Surface Can Predict Fiber Trajectories.**（本轮编号 1131）：读取纤维坐标预测方法与训练过程。 [论文页面](https://ieeexplore.ieee.org/document/10635365/)
- **A Pipeline for Histopathology Analysis of Prostate Cancer Guided by Mass Spectrometry Imaging.**（本轮编号 1137）：核实肿瘤/非肿瘤区域识别采用何种学习方法及验证。 [论文页面](https://ieeexplore.ieee.org/document/10635223/)
- **A Joint Training and Confidence Calibration Procedure That is Robust to Label Noise.**（本轮编号 1143）：读取医学影像数据和诊断终点，确认非一般噪声基准。 [论文页面](https://ieeexplore.ieee.org/document/10635160/)
- **Double Functionally Independent Primitives Provide Disorder Specific Fingerprints of Mental Illnesses.**（本轮编号 1153）：读取层级分解方法、学习模型与疾病关联分析。 [论文页面](https://ieeexplore.ieee.org/document/10635116/)
- **DNA-DIR: 2D-3D Geometry Embedding for Intraoperative Partial-to-Full Registration.**（本轮编号 1155）：读取DNA-DIR几何嵌入、训练及配准模块，核实AI作用。 [论文页面](https://ieeexplore.ieee.org/document/10635158/)
- **Saccadic Detection in Virtual Gaming for Dyslexia Classification.**（本轮编号 1161）：读取当前分割及分类实现，确认新扫视特征是否进入学习模型并评价。 [论文页面](https://doi.org/10.1109/ISBI56570.2024.10635745)

其余 267 条缺摘要待定条目的标识、题名、检索结果和所缺证据在[待定清单](lixueting-1163-review-20261109-pending.json)逐条列出。DOI `10.1016/j.jacc.2024.08.084` 还存在工作簿与仓库题名不一致的问题，未覆盖原始信息。

## 数据与核验

- [逐篇审计记录（JSONL gzip）](lixueting-1163-review-20261109.jsonl.gz)：1,163 条，含结论、理由、证据位置和链接、摘要哈希、访问结果、旧判断和本轮双语标签。
- [本轮汇总及一致性核验](lixueting-1163-review-20261109-summary.json)。全量台账、个人交付、缺摘要清单、162 条已有补录记录的判定和 29 个来源的阶段反馈同步更新。
- 原始论文字段、此前审核历史、其他论文和其他负责人数据保持不变；本轮没有补写摘要，也没有改动采集快照。
- 新增 8 个中英文规范任务标签，均有实际纳入论文证据；其余标签复用共享词表。
- 最新个人行动清单和词表读取自提交 `99b38afb5ee60f85689e7f84f2216393dd565212`；论文输入快照 `2026-11-05T10:31:19.144426+08:00`。

全年官网总量、非本批记录及 2025/2026 年审核不在本轮范围，保留既有状态。
