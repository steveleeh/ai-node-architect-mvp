# Skill: Session Reset (时空重置)

## Description
当用户感到对话被“污染”、历史过于冗长或需要切换截然不同的新任务时，使用此技能进行“清零”操作。

## Triggers
- "/reset"
- "开启新对话"
- "清除历史"
- "重启对话"

## Behavior (Agent Instructions)
当你检测到上述触发词时，请执行以下操作：
1. **回复确认**：发送一个极简且带有仪式感的确认，例如："✨ 时空重置完成。新 Session 已开启。"
2. **逻辑重置**：
   - 立即放弃（Drop）当前所有活跃的未完成任务目标。
   - 忽略（Ignore）本 Session 中此前所有的业务定义（例如：如果你之前是 Coder，现在重置为通用助手）。
   - 按照 SOUL.md 和 IDENTITY.md 的初始值重新初始化对话。
3. **静默操作 (Silent Action)**：如果环境支持，向 Gateway 发出一个重启 Session 的内部信号（通过 NO_REPLY 标签与新 ID 回复相结合）。

## Impact
这不会删除物理存储的日志，但会强制 AI 本次的“注意力 (Attention)”和“上下文窗口 (Context window)”进行逻辑剥离。
