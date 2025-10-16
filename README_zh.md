# ARIA - 自动化研究智能助手

**🚀 Transform months of research into minutes of insight**

[English](./README.md) | 中文

ARIA 是一个用于科学数据分析、可视化和报告生成的自动化研究助手框架。

## 项目结构

```
aria/
├── .claude/commands/           # Claude AI 命令文件
│   ├── academic/               # 学术研究工作流命令
│   ├── git/                    # Git 操作命令
│   └── python/                 # Python 环境命令
├── data/
│   ├── raw/                   # 原始数据
│   ├── processed/              # 预处理后的数据
│   └── output/                 # 实验输出
│       ├── models/             # 训练的模型
│       ├── results/            # 实验结果
│       ├── figures/            # 可视化图表
│       └── logs/               # 执行日志
├── docs/                       # 项目文档
├── src/                        # 源代码
├── scripts/                    # 执行脚本
├── GETTING_STARTED.md          # 快速上手指南（英文）
├── GETTING_STARTED_zh.md       # 快速上手指南（中文）
├── INSTALL.md                  # 安装指南（英文）
├── INSTALL_zh.md               # 安装指南（中文）
└── README.md                   # 本文件
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

### Python 环境命令

Python 命令文件位于 `.claude/commands/python/` 目录：

- `@setup-environment.md` - 自动化环境配置
  - 检查并安装 Git、Python 3.12+ 和 UV 包管理器
  - 使用 `uv sync` 配置项目依赖
  - 包含网络问题时使用清华源的回退方案
  - 提供完整的环境验证

### Git 操作命令

Git 命令文件位于 `.claude/commands/git/` 目录：

- `@git-commit.md` - 智能 Git 提交
  - 自动创建结构化的提交信息
  - 当文件修改较多时，自动分批提交（每批不超过10个文件）
  - 根据代码变更自动生成有意义的提交描述

## 示例项目

展示 ARIA 完整工作流的示例项目：

- 🏠 [**aria-example-buston**](https://github.com/Biaoo/aria-example-buston) - 波士顿房价预测（回归）| [OpenML数据集](https://www.openml.org/d/531)
- 💎 [**aria-example-diamonds**](https://github.com/Biaoo/aria-example-diamonds) - 钻石价格预测（回归）| [OpenML数据集](https://www.openml.org/d/42225)
- 🐛 [**aria-example-kc1**](https://github.com/Biaoo/aria-example-kc1) - 软件缺陷预测（分类）| [OpenML数据集](https://www.openml.org/d/1067)
- 🧩 [**aria-example-sat11**](https://github.com/Biaoo/aria-example-sat11) - SAT求解器性能预测（回归）| [OpenML数据集](https://www.openml.org/d/41980)

所有数据集均来自 [OpenML](https://www.openml.org/)，一个开放的机器学习平台。每个项目都包含完整的文档、生产级代码、训练好的模型和学术论文。

## 快速开始

**新手入门？从这里开始：[快速上手指南](./GETTING_STARTED_zh.md)** 📖

完整指南涵盖：

- 安装 Git 和 AI 代码编辑器（Cursor/VSCode/通义灵码）
- 使用 `@setup-environment.md` 自动配置环境
- 从数据到论文的逐步工作流程
- 故障排查和最佳实践

### 有经验的用户

1. **配置环境**：使用 `@setup-environment.md` 配置 Python 和依赖
2. **准备数据**：将原始数据放入 `data/raw/`
3. **创建项目描述**：编写 `docs/01-basic-information.md`
4. **执行工作流**：使用 Claude AI 依次执行学术命令
5. **版本控制**：使用 `@git-commit.md` 进行智能提交

📚 **完整文档**：参见 [GETTING_STARTED_zh.md](./GETTING_STARTED_zh.md) 和 [INSTALL_zh.md](./INSTALL_zh.md)

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

## 许可证

本项目采用双重许可：

- **GNU AGPL-3.0** - 开源使用（个人、研究、教育、开源项目）
- **商业许可** - 专有/商业使用（联系获取许可）

详见 [LICENSE](LICENSE) 文件。

## 贡献

欢迎提交 Issue 和 Pull Request！

## 联系方式

如有问题、建议或合作机会，请通过以下方式联系：

- **GitHub Issues**: [创建 issue](https://github.com/Biaoo/aria/issues)
- **邮箱**: [biao00luo@gmail.com](mailto:biao00luo@gmail.com)
- **项目主页**: [ARIA on GitHub](https://github.com/Biaoo/aria)

### 加入社区

<div align="center">
  <img src="assets/wechat-qr.png" alt="微信群二维码" width="200"/>
  <p>扫码加入微信交流群</p>
</div>
