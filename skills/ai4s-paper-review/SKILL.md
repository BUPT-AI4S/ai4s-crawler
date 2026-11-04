---
name: ai4s-paper-review
description: Review AI4S paper candidates and assigned venues, assign evidence-backed labels, verify paper metadata, and deliver mergeable JSON.
---

# AI4S 初筛候选清洗

以负责人提供的代码初筛结果（通常是 `ai4s.json`）为唯一候选范围。每次由负责人指定年份或年份范围、来源分工和数据快照。每人独立处理自己的部分并签收，最后交一个 JSON。

1. **锁定输入。** 按本次分工读取候选文件，保留来源代码、年份和论文标识。优先使用指定快照的来源文件。用 (venue, year, id) 识别同一条来源记录。相同记录只处理一次，字段冲突先交负责人确认。
2. **逐篇精筛。** 先用已有标题和摘要判断科学任务、AI 的实际作用及两者关系。证据足够就直接判定，只有会影响结论或标签的疑点才打开论文页，按需读方法、实验或结果。证据仍不足时记为「待定」并说明缺什么。具体口径见 [精筛与标签规则](references/review-rules.md)。
3. **打标签。** 每篇「纳入」论文由模型按维度选择简洁、可复用的标签。拆开训练阶段、方法与科学对象，优先复用同义规范名，再按证据补充新概念。可查阅随技能附带的 [AI4S 分类表](references/ai4s_taxonomy.json)。每项记录维度、名称和证据。其他状态的标签数组留空。
4. **核对来源与论文元数据。** 按 [刊会核验规则](references/venue-review.md) 核对本人负责的期刊和会议。对纳入论文核对 DOI、论文页、公开 PDF 和其他交付字段，将已查证的补充值放入 ai4s_review.verified_metadata。
5. **交付。** 按 [JSON 交付说明](references/team-handoff.md) 输出一份与采集文件同为论文对象数组的 JSON，保留原字段，仅添加 ai4s_review。预算用完时为未审记录保留 unreviewed 状态，便于续做。

无需核对全量论文目录、读取 `papers.json`、抽查未命中论文或提交补采工单。用智能体逐篇判断，保留原始数据。


