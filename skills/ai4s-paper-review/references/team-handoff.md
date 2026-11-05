# 分工与 JSON 交付

每批按当期负责人表指定年份、来源和输入快照，以初筛候选篇数估算工作量。每人交一个 UTF-8 JSON 文件，例如 `ai4s-cleaned-批次-负责人.json`。

## 与采集格式对齐

交付文件顶层为论文对象数组，与原 `ai4s.json` 一致。每条复制输入对象的全部原字段和原值，仅新增 `ai4s_review`。原有 `ai4s_tags`、`ai4s_tagging`、`ai4s_hits` 等字段存在时原样保留，精筛标签统一放到 `ai4s_review.tags`。以下只展示部分原字段和新增对象，实际提交须保留输入中的全部字段。

```json
[
  {
    "id": "<原论文标识>",
    "venue": "<原来源代码>",
    "year": 2025,
    "title": "<原标题>",
    "url": "<原链接>",
    "ai4s_review": {
      "schema_version": 2,
      "batch_id": "<批次>",
      "owner": "<负责人>",
      "snapshot_at": null,
      "decision": "include",
      "rationale": "模型参与蛋白质序列建模，研究明确报告预训练目标。",
      "verified_metadata": {
        "url": "https://example.org/paper",
        "pdf_url": null,
        "evidence_urls": ["https://example.org/paper"]
      },
      "tags": [
        {"axis": "training_stage", "label": "预训练", "evidence_location": "方法 §2", "rationale": "训练目标为预测被掩码的氨基酸。"},
        {"axis": "method", "label": "掩码建模", "evidence_location": "方法 §2", "rationale": "训练时对输入序列随机掩码。"}
      ]
    }
  }
]
```

`decision` 使用 `include`（纳入）、`exclude`（排除）、`pending`（已审但待定）或 `unreviewed`（未审）。四类都保留记录，汇总后按 `ai4s_review.decision == "include"` 导出最终纳入集。纳入至少带一个有证据的标签，其他状态的 `tags` 为空。待定原因写入 `rationale`，未审可用 `null`。来源文件缺失时在交付说明里列出，不构造占位论文。

合并前核对批次和快照，按 `(venue, year, id)` 查重后合并数组。同一键若出现字段或判定冲突，交原负责人确认。跨来源相同 DOI 可关联，保留各来源出处。若现有读取器只读原字段，仍能读取这批记录。筛出最终纳入集、展示精筛标签时使用新增字段。

> 使用 `$ai4s-paper-review`。我是【负责人】，处理【年份和来源】，初筛文件为【路径】。清洗候选，按维度打可复用的标签。交一个保留原字段、仅追加 `ai4s_review` 的论文数组 JSON。


## 官网总量与补录记录

按来源和年份记录采集快照、全量采集数、官网同口径总数、差额、官网目录链接及差额的核实结果。官网总数未知时说明原因。列出已补录条目及证据；大批漏采时写明需补采的卷期或分轨。

补录后通过初筛的论文沿用同样的论文对象格式和 `ai4s_review` 字段。用 DOI 或来源的稳定官方标识作为 `id`，在 `ai4s_review.rationale` 注明「官网漏采补录」及核实理由，并把官方证据链接放入 `ai4s_review.verified_metadata.evidence_urls`。与已有记录按 `(venue, year, id)`、DOI 和题名作者去重后再合并。

## 摘要覆盖核验记录

在交付说明中按来源和年份记录快照、全量和候选各自的摘要缺失数与总数、缺失是否集中、对初筛漏检或精筛证据的影响，以及自己的处理决定和依据。只有候选数据时明确写「全量覆盖未知」。如抽查发现疑似漏筛，列出 DOI 或论文页和发现依据，便于负责人补摘要、重跑初筛后重新分配。

## 纳入论文的交付字段

保留爬取记录的 `id`、`venue`、`year`、`title`、`authors`、`abstract` 和其他原字段。核对已知信息是否对应同一论文和正式版本。把新增或需纠正的值放入 `ai4s_review.verified_metadata`，用 `evidence_urls` 数组注明出处。

| 字段 | 内容 |
|---|---|
| `title`、`authors` | 正式题名、按原顺序排列的作者数组 |
| `abstract` | 来源可查的原摘要 |
| `doi` | DOI 标识，保留 10. 开头的形式 |
| `url` | 出版方、会议论文集或正式记录的页面 |
| `pdf_url` | 已核实的公开直达 PDF 链接，与正式版或其公开版本对应 |
| `code_url`、`project_url`、`dataset_url` | 作者提供或论文引用的代码、项目及数据链接 |
| `evidence_urls` | 支撑核对结果的公开页面数组 |

没查到的补充字段可省略或填 `null`。论文页面填 `url`，实际公开 PDF 才填 `pdf_url`。汇总时用非空的已验证值补充展示字段，合并键始终取原记录的 `(venue, year, id)`。旧版交付没有 verified_metadata 时按原字段读取。
