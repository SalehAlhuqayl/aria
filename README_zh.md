# ARIA - 自动化研究智能助手

**🚀 Transform months of research into minutes of insight**

[English](./README.md) | 中文

ARIA 是一个用于科学数据分析、可视化和报告生成的自动化研究助手框架。

## 项目结构

```
aria/
├── .claude/commands/           # Claude AI 命令文件
│   ├── academic/               # 学术研究工作流命令
│   └── git/                    # Git 操作命令
├── data/
│   ├── raw/                   # 原始数据
│   └── processed/              # 预处理后的数据
│   └── output/                 # 实验输出
│       ├── models/             # 训练的模型
│       ├── results/            # 实验结果
│       ├── figures/            # 可视化图表
│       └── logs/               # 执行日志
├── docs/                       # 项目文档
├── src/                        # 源代码
├── scripts/                    # 执行脚本
```

## 工作流程

### 1. 数据准备阶段
- 将原始数据放入 `data/raw/` 文件夹
- 手动创建 `docs/01-basic-information.md` 描述项目背景、目标和数据概况

### 2. 数据分析阶段
- **原始数据分析**: 使用 `@raw-data-analysis.md` 命令分析原始数据，生成 `docs/02-raw-data-analysis.md`
- **数据预处理**: 使用 `@preprocess.md` 命令设计预处理方案（`docs/03-preprocess-plan.md`），执行预处理，分析处理后数据（`docs/04-processed-data-analysis.md`）

### 3. 研究设计阶段
- **研究方案**: 使用 `@research-plan.md` 命令制定研究计划，包括特征工程、模型选择、评估指标等，生成 `docs/05-research-plan.md`

### 4. 代码实现阶段
- **代码开发**: 使用 `@code-implementation.md` 命令实现研究方案，创建必要的Python模块
- 生成 `docs/06-implementation-docs.md`（实现文档）和 `docs/07-execution-instructions.md`（执行指南）
- 代码质量检查：使用 mypy 和 ruff 确保代码质量

### 5. 实验执行阶段
- **运行实验**: 使用 `@run-experiments.md` 命令执行实验脚本
- 输出保存到 `output/` 目录下的相应子文件夹

### 6. 结果分析阶段
- **结果分析**: 使用 `@experiment-analysis.md` 命令分析实验输出
- 生成 `docs/08-experiment-results/` 目录下的单项分析
- 生成 `docs/09-experiment-report.md` 综合实验报告

### 7. 论文撰写阶段
- **学术论文**: 使用 `@research-report.md` 命令生成高水平期刊格式的论文
- 生成 `docs/10-manuscript.md`（主文）、`docs/10-manuscript-supplement.md`（补充材料）、`docs/10-cover-letter.md`（投稿信）

### 8. 模型部署（可选）
- **Gradio界面**: 如有训练模型，使用 `@gradio-app.md` 命令创建模型调用界面
- 生成 `docs/11-model-deployment-guide.md` 部署指南

## Claude AI 命令

### 学术研究命令

所有学术命令文件位于 `.claude/commands/academic/` 目录：

- `@raw-data-analysis.md` - 原始数据分析
- `@preprocess.md` - 数据预处理
- `@research-plan.md` - 研究方案设计
- `@code-implementation.md` - 代码实现
- `@run-experiments.md` - 实验执行
- `@experiment-analysis.md` - 结果分析
- `@research-report.md` - 学术论文生成
- `@gradio-app.md` - 模型部署界面

### Git 操作命令

Git 命令文件位于 `.claude/commands/git/` 目录：

- `@git-commit.md` - 智能 Git 提交
  - 自动创建结构化的提交信息
  - 当文件修改较多时，自动分批提交（每批不超过10个文件）
  - 根据代码变更自动生成有意义的提交描述

## 快速开始

1. **准备数据**：将原始数据放入 `data/raw/`
2. **创建项目描述**：编写 `docs/01-basic-information.md`
3. **执行工作流**：使用 Claude AI 依次执行上述命令
4. **版本控制**：使用 `@git-commit.md` 进行智能提交

## 依赖管理

使用 UV 进行Python依赖管理：

```bash
uv add <package-name>  # 添加新依赖
uv sync                # 同步依赖
```

## 代码质量

- 类型检查：`mypy src/`
- 代码风格：`ruff check src/`
- 代码格式化：`ruff format src/`

## 特性

- 📊 **数据驱动**: 从原始数据到学术论文的完整工作流
- 🤖 **AI 辅助**: Claude AI 命令自动化各个研究阶段
- 📝 **学术标准**: 生成符合 Nature/Science 标准的论文
- 🎯 **质量保证**: 集成代码质量检查工具
- 🚀 **模型部署**: 支持 Gradio 界面快速部署
- 📦 **版本控制**: 智能 Git 提交管理

## TODO / 开发计划

### 近期目标
- [ ] **AI 客户端兼容性测试**
  - Claude Code（当前支持）
  - Cursor AI 适配
  - GitHub Copilot 集成
  - OpenAI CodeX 兼容
  - 其他 AI 编码助手

- [ ] **全流程自动化**
  - 设计自主研究 Agent
  - 实现端到端流水线自动化
  - 添加检查点和恢复机制
  - 并行实验执行支持

- [ ] **功能增强**
  - 多模态数据支持（图像、音频、视频）
  - 分布式计算集成
  - 实时协作功能
  - 云部署选项（AWS、GCP、Azure）

### 长期愿景
- [ ] **框架扩展**
  - 自定义工作流插件系统
  - 常见研究类型模板库
  - 主流 ML 框架集成（PyTorch、TensorFlow、JAX）
  - 支持更多学术期刊格式

- [ ] **质量改进**
  - 自动化测试框架
  - 性能基准测试
  - 文档自动生成
  - 交互式教程

- [ ] **社区功能**
  - 研究模板市场
  - 工作流共享平台
  - 协作研究工具
  - 预构建分析模块

## 许可证

本项目基于 MIT 许可证开源 - 详见 [LICENSE](LICENSE) 文件。

## 贡献

欢迎提交 Issue 和 Pull Request！

## 联系方式

如有问题、建议或合作机会，请通过以下方式联系：

- **GitHub Issues**: [创建 issue](https://github.com/Biaoo/aria/issues)
- **邮箱**: `biao00luo@gmail.com`
- **项目主页**: [ARIA on GitHub](https://github.com/Biaoo/aria)