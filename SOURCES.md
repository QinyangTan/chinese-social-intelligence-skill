# Sources and methodology

This project separates **source material** from **executable rules**.

A source may describe a value, custom, social expectation, or educational goal. We do not ask the model to imitate source language. We convert it into a modern behavioral rule with scope, exceptions, and guardrails.

## Engineering references

### Tianji

- Repository: https://github.com/SocialAI-tianji/Tianji
- License: Apache-2.0
- Useful idea: organizing social-intelligence capabilities by real-life interaction scenarios and supporting prompt/RAG/agent/fine-tuning routes.

### Agent Skills

- Specification: https://agentskills.io/specification
- Reference repository: https://github.com/agentskills/agentskills
- Anthropic examples: https://github.com/anthropics/skills

## Classical Chinese sources

Public-domain texts can be checked through Chinese Text Project:

- 《论语》: https://ctext.org/analects
- 《孟子》: https://ctext.org/mengzi
- 《礼记》: https://ctext.org/liji
- 《道德经》: https://ctext.org/dao-de-jing
- Chinese Text Project home: https://ctext.org/

Additional public-domain works used as cultural reference:

- 《菜根谭》
- 《增广贤文》
- 《朱子家训》
- 《弟子规》

For these works, the repository stores short source cues and **newly written modern rules**, not long reproduced editions or modern annotations.

## Modern civic / educational references

### 教育部：义务教育课程方案和课程标准（2022年版）

Official notice:
https://www.moe.gov.cn/srcsite/A26/s8001/202204/t20220420_619921.html

《义务教育道德与法治课程标准（2022年版）》 emphasizes dimensions including moral cultivation, rule-of-law awareness, sound personality, responsibility, and assessment through behavior in real-life contexts. We use those dimensions as a modern filter for actionable social behavior.

### 《新时代公民道德建设实施纲要》

Official public text:
https://www.gov.cn/gongbao/content/2019/content_5449646.htm

Used only as public context for civic themes such as civility, honesty, responsibility, family/community conduct, and rule observance.

## Method

For each source idea:

1. Identify the underlying social function.
2. Separate descriptive tradition from normative instruction.
3. Rewrite as a concrete Agent rule.
4. Define where the rule applies.
5. Add exceptions for equality, consent, privacy, law, safety, professional ethics, and factual accuracy.
6. Add positive/negative examples.
7. Test against modern scenarios.

## What is deliberately excluded

- Long copyrighted textbook passages.
- Unverified “Chinese people always…” stereotypes.
- Manipulation tactics disguised as social intelligence.
- Bribery, coercive drinking, forced deference, or concealment of serious wrongdoing.
