# Chinese Social Intelligence Skill（中国社会语境智能）

让 Agent / LLM 不只是“会说中文”，而是在现代中国社会语境里更懂 **关系、分寸、面子、礼数、边界、时机、潜台词与行动后果**。

> 核心目标：先像一个熟悉中国社会交往的人那样判断局面，再决定怎么说、怎么做；不是把回复套成“高情商话术”。

## v0.2：460 条可执行 Guide

当前版本已经从 foundation 扩展为：

- **460 条**原子化、可执行 social guides
- **23 个**现实场景模块
- **6 组** book/research digests
- 一套关系/面子/人情/公开-私下的社会判断模型
- 现代边界：平等、同意、隐私、法治、职业伦理、安全、反腐与反胁迫
- Agent 外部行动策略
- 现有 JSONL rules + eval cases + CI validation

这些 guide 不是“中国人都这样”的刻板模板，而是 **默认启发 + 适用条件 + 应做 + 避免 + 现代边界 + 来源层**。

## 30 秒接入

### A. Agent Skills

把整个仓库放入 Agent Skills 目录。入口是 `SKILL.md`。

Agent 不应一次加载全部规则；`references/guides/INDEX.md` 会告诉它按场景选择 1–3 个模块。

### B. 任意 LLM

直接使用：

```
dist/chinese-social-intelligence.system.md
```

作为 system/developer prompt；再把 `references/` 建 RAG 索引。

### C. 推荐运行顺序

1. **读局**：目标、关系、亲疏、角色、公开/私下、情绪、风险、时机。
2. **载入规则**：从 23 个 guide 模块选 1–3 个。
3. **现代过滤**：安全、法律、同意、隐私、专业规则优先。
4. **行动选择**：说 / 不说 / 私聊 / 公开 / 延后 / 留证 / 拒绝 / 补救。
5. **自然措辞**：最后才生成微信、邮件、口语或正式文本。

## 核心内容

```text
.
├── SKILL.md
├── SOURCE_CORPUS.md
├── dist/
│   └── chinese-social-intelligence.system.md
├── references/
│   ├── social-model.md
│   ├── modern-principles.md
│   ├── language-pragmatics.md
│   ├── action-policy.md
│   ├── book-digests/
│   │   ├── 01-confucian-classics.md
│   │   ├── 02-self-cultivation-household.md
│   │   ├── 03-chinese-sociology.md
│   │   ├── 04-guanxi-face-anthropology.md
│   │   ├── 05-communication-conflict.md
│   │   └── 06-modern-civic-ethics.md
│   └── guides/
│       ├── INDEX.md
│       ├── 01-relationship-distance.md
│       ├── ...
│       └── 23-agent-action.md
├── data/
│   └── rules.jsonl
├── evals/
│   └── cases.jsonl
├── scripts/
│   └── validate.py
├── SOURCES.md
├── NOTICE.md
└── LICENSE
```

## 23 个 Guide 模块

1. 关系距离与定位
2. 长辈与家庭
3. 朋友与同辈
4. 职场协作
5. 上下级与权力差
6. 学校师生与同学
7. 求人、帮忙与人情往来
8. 送礼、请客与宴席
9. 微信、短信与线上表达
10. 群聊、公开场合与面子
11. 请求、拒绝与边界表达
12. 催办、deadline、金钱与记录
13. 道歉、感谢与关系修复
14. 冲突、纠错与难谈话
15. 丧事、疾病、失败与脆弱情境
16. 隐私、闲话与第三方信息
17. 信任、承诺与可靠性
18. 新人进入环境与礼俗适配
19. 面子、身份与体面
20. 自然中文与措辞
21. 喜事、节日与社交仪式
22. 服务、陌生人与公共空间
23. 社交判断与 Agent 行动

## 来源层

### 公版/古典
《论语》《孟子》《礼记》《大学》《中庸》《荀子》《道德经》《庄子》《菜根谭》《增广贤文》《朱子家训》《弟子规》《颜氏家训》《围炉夜话》《小窗幽记》《了凡四训》《曾国藩家书》等。

### 现代中国社会学 / 人类学
包括费孝通《乡土中国》、翟学伟关于关系/脸面/人情/社会信任的研究，以及 Hu、Hwang、Mayfair Yang、Kipnis、Yunxiang Yan 等关于 face / guanxi / gift exchange 的经典研究。

### 沟通理论
Goffman、Brown & Levinson、Face-Negotiation、Difficult Conversations、Getting to Yes、NVC 等只作为辅助机制，不取代中国本土语境。

现代版权著作只做**概念级原创提炼**，不复制章节或长段落。完整来源策略见 `SOURCE_CORPUS.md` 与 `SOURCES.md`。

## 设计原则

- 先读局，再说话。
- “懂人情”不等于迎合。
- “给面子”不等于隐瞒。
- “礼尚往来”不等于行贿或强制债务。
- “尊长”不等于无条件服从。
- 低风险社交可含蓄；高风险事实必须明确。
- 用户真实上下文永远优先于“中国人通常怎样”的先验。
- 最终输出要像真实的人，而不是 AI 在表演礼貌。

## Inspiration

本项目受 [SocialAI-tianji/Tianji](https://github.com/SocialAI-tianji/Tianji) 按真实社交场景组织能力的工程方向启发。Tianji 使用 Apache-2.0 License；本仓库规则正文、guide、digests、examples 与 eval 均为独立整理与原创转译，详见 `NOTICE.md`。

## License

Apache-2.0.
