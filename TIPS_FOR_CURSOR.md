# CURSOR 使用技巧

## 安装指南与基础用法

- 参考 [Cursor 文档](https://cursor.com/cn/docs)

## 使用建议

### 在 Cursor 中使用 Claude 命令

- Cursor 的最新版已支持 Claude Code 命令工具（commands）和声明文件（CLAUDE.md）。
- 配置方式：进入 `Cursor Settings` -> `Rule & Memories`，勾选 `Include CLAUDE.md in context` 与 `Import Claude Commands`。
- 使用方式：在 Cursor 的 AI 聊天框中输入斜杠 `/`，即可选择相应的命令。

### 自动运行模式

- 为实现流程自动化，建议在 `Cursor Settings` -> `Chat` -> `Auto-Run` 中将 `Auto-Run Mode` 设为 `Run Everything`，同时勾选 `External-File Protection` 以防止工作区外的文件被修改。