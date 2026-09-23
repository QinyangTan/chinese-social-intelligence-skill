# Rule schema

`data/rules.jsonl` 每行一个 JSON object：

```json
{
  "id": "CSI-C01",
  "source": "论语",
  "cue": "己所不欲，勿施于人",
  "principle": "换位且不强迫",
  "when": ["请求帮忙"],
  "do": ["给拒绝出口"],
  "avoid": ["利用羞耻感逼答应"],
  "guardrail": "必要职责仍可明确要求履行"
}
```

## 设计理由

LLM 直接读自然语言规则很方便；JSONL 则方便：

- RAG 索引
- 规则过滤
- eval 对照
- 未来做 fine-tuning / preference data
- 按 source / scenario / risk 检索

规则不是事实数据库。模型仍要做情境判断，并优先遵守 `SKILL.md` 中的现代优先级。
