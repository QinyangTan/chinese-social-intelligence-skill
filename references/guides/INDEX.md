# Guide Index — 460 executable guides

The 460 guides are split into 23 modules so an Agent can load only the relevant context.

| Range | Module | File |
|---|---|---|
| G001–G020 | 关系距离与定位 | 01-relationship-distance.md |
| G021–G040 | 长辈与家庭 | 02-family-elders.md |
| G041–G060 | 朋友与同辈 | 03-friends-peers.md |
| G061–G080 | 职场协作 | 04-workplace.md |
| G081–G100 | 上下级与权力差 | 05-power-distance.md |
| G101–G120 | 学校师生与同学 | 06-school.md |
| G121–G140 | 求人、帮忙与人情往来 | 07-favors.md |
| G141–G160 | 送礼、请客与宴席 | 08-gifts-hospitality.md |
| G161–G180 | 微信、短信与线上表达 | 09-wechat.md |
| G181–G200 | 群聊、公开场合与面子 | 10-public-group.md |
| G201–G220 | 请求、拒绝与边界表达 | 11-requests-boundaries.md |
| G221–G240 | 催办、deadline、金钱与记录 | 12-deadlines-money.md |
| G241–G260 | 道歉、感谢与关系修复 | 13-apology-repair.md |
| G261–G280 | 冲突、纠错与难谈话 | 14-conflict.md |
| G281–G300 | 丧事、疾病、失败与脆弱情境 | 15-vulnerable-situations.md |
| G301–G320 | 隐私、闲话与第三方信息 | 16-privacy-gossip.md |
| G321–G340 | 信任、承诺与可靠性 | 17-trust-promises.md |
| G341–G360 | 新人进入环境与礼俗适配 | 18-new-environment.md |
| G361–G380 | 面子、身份与体面 | 19-face-status.md |
| G381–G400 | 自然中文与措辞 | 20-natural-chinese.md |
| G401–G420 | 喜事、节日与社交仪式 | 21-rituals-celebrations.md |
| G421–G440 | 服务、陌生人与公共空间 | 22-public-service.md |
| G441–G460 | 社交判断与 Agent 行动 | 23-agent-action.md |

## Loading rule

Do **not** load all 460 guides by default.

1. Read `SKILL.md`.
2. Read `references/social-model.md` and `references/modern-principles.md` when the task is socially sensitive.
3. Load 1–3 guide modules matching the actual situation.
4. Load a `references/book-digests/` file only when cultural explanation, provenance, or ambiguous principles need deeper context.
5. For direct “怎么回” requests, generate the usable response after applying the guides; do not dump the guide analysis unless asked.

## Cross-module examples

- 给叔叔回丧事消息 → family-elders + vulnerable-situations + natural-chinese
- 催同学交作业 → school + deadlines-money + wechat
- 向领导表达不同意见 → power-distance + conflict + natural-chinese
- 请学长内推 → relationship-distance + favors + requests-boundaries
- 饭局拒绝喝酒 → gifts-hospitality + requests-boundaries + power-distance if relevant
- 在群里纠正老师/同事时间 → public-group + school/workplace + face-status
- Agent 要替用户发送敏感消息 → agent-action + the relevant domain module
