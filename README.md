# Chinese Social Intelligence Skill（中国社会语境智能）

让 Agent / LLM 不只是“会说中文”，而是在现代中国社会语境里更懂 **关系、分寸、面子、礼数、边界、时机、潜台词与行动后果**。

> 核心目标：先像一个熟悉中国社会交往的人那样判断局面，再决定怎么说、怎么做；不是把回复套成“高情商话术”。

## 特点

- **即插即用**：符合 Agent Skills 的 `SKILL.md` 目录规范；支持 Skills 的 Agent 可直接加载。
- **普通 LLM 也能用**：`dist/chinese-social-intelligence.system.md` 可直接放进 system/developer prompt 或知识库。
- **不是模板库**：先判断关系、场合、公开/私下、长期关系、责任与风险，再生成语言或动作。
- **古典材料经过现代化编译**：从《论语》《孟子》《礼记》《菜根谭》《增广贤文》《朱子家训》《弟子规》等提炼“可执行规则”，不是让模型机械复古。
- **现代边界优先**：平等、尊重、隐私、同意、法治、职业伦理、安全与事实准确性，高于传统礼俗。
- **覆盖操作而非只覆盖说话**：适用于发消息、回复、催办、拒绝、送礼、请客、群聊、公开/私下处理、冲突降级、慰问、求人办事等。

## 30 秒接入

### A. Agent Skills

把整个仓库（或至少 `SKILL.md + references/`）放入你的 Agent Skills 目录，让 Agent 在涉及中文社会互动、措辞、关系处理、礼仪与沟通时加载本 Skill。

### B. 任意 LLM

将：

```
dist/chinese-social-intelligence.system.md
```

作为 system/developer prompt。若模型支持 RAG，再把 `references/` 建索引。

### C. 应用级集成

推荐两阶段：

1. **Social reasoning**：判断关系、风险、面子、边界、时机、渠道。
2. **Surface realization**：生成符合具体关系与媒介的自然中文。

不要先生成一句“礼貌中文”再润色；先做社会判断。

## 目录

```text
.
├── SKILL.md
├── dist/
│   └── chinese-social-intelligence.system.md
├── references/
│   ├── social-model.md
│   ├── classics-to-rules.md
│   ├── modern-principles.md
│   ├── language-pragmatics.md
│   ├── scenario-playbook.md
│   └── action-policy.md
├── examples/
│   └── quick-examples.md
├── evals/
│   └── cases.jsonl
├── scripts/
│   └── validate.py
├── SOURCES.md
├── NOTICE.md
└── LICENSE
```

## 默认文化范围

默认是 **现代中国大陆普通社会交往语境**，但绝不假定存在唯一的“中国人说话方式”。模型必须继续根据：

- 年龄与代际
- 亲疏
- 家庭 / 学校 / 职场 / 商务
- 正式 / 非正式
- 微信 / 电话 / 邮件 / 当面
- 一对一 / 群聊 / 公开场合
- 地区与组织文化（若已知）
- 用户本人明确偏好

动态调整。

## 设计原则

### 1. 先读局，再说话

不是“这句话怎么说更高情商”，而是先问：

- 对方是谁？
- 关系远近与角色是什么？
- 谁在求人，谁承担责任？
- 有没有第三人在场？
- 需要保全谁的体面？
- 是一次性交互还是长期关系？
- 当前真正目标是什么？
- 现在最不该做什么？

### 2. “懂人情”不等于“迎合”

本 Skill 不把阿谀、强迫喝酒、送礼换利益、隐瞒严重错误、无底线服从等行为包装成“中国文化”。

### 3. 高风险场景直接性高于含蓄

涉及安全、法律、医疗、金钱、学术诚信、合同、明确责任时：可以保留体面，但不能牺牲事实、证据或必要的明确表达。

## 项目来源

本项目受到 [SocialAI-tianji/Tianji](https://github.com/SocialAI-tianji/Tianji) “按社交场景组织人情世故能力”的工程思路启发。Tianji 使用 Apache-2.0 License。本仓库的规则正文为重新整理、提炼和编写的独立内容，并在 `NOTICE.md` 中记录参考来源。

Agent Skills 结构遵循开放的 [Agent Skills Specification](https://agentskills.io/specification)。

## 状态

当前为 **v0.1 foundation**：先建立可运行的文化推理骨架、核心准则、场景与评测。后续重点是继续从公开/可合法使用的经典、教材标准、语言学与真实匿名场景中扩充高质量规则与 eval，而不是堆砌话术。

## License

Apache-2.0.
