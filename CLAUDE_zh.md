# CLAUDE.md

本文件用于指导 AI 助手在本仓库中协作编写代码。

## 项目简介

ARIA（Automated Research Intelligence Assistant）是一个用于科学数据分析、可视化与报告生成的快速搭建框架，遵循从原始数据分析到学术论文撰写的结构化工作流。

## 项目结构

```
aria/
├── .claude/commands/academic/  # 各工作阶段的 AI 命令文件
├── data/
│   ├── raw/                   # 原始数据文件
│   └── processed/              # 预处理后可直接分析的数据
│   └── output/                 # 实验输出
│       ├── models/             # 训练好的模型
│       ├── results/            # 实验结果
│       ├── figures/            # 可视化图表
│       └── logs/               # 运行日志
├── docs/                       # 所有项目文档（按序编号）
│   ├── 01-basic-information.md        # 项目基础（手动创建）
│   ├── 02-raw-data-analysis.md        # 原始数据探索
│   ├── 03-preprocess-plan.md          # 预处理策略
│   ├── 04-processed-data-analysis.md  # 预处理后数据特征
│   ├── 05-research-plan.md            # 研究方案设计
│   ├── 06-implementation-docs.md      # 代码实现文档
│   ├── 07-execution-instructions.md   # 执行指南
│   ├── 08-experiment-results/         # 单项结果分析
│   ├── 09-experiment-report.md        # 综合分析报告
│   ├── 10-manuscript.md                # 学术论文
│   ├── 10-manuscript-supplement.md    # 论文补充材料
│   ├── 10-cover-letter.md             # 投稿附信
│   └── 11-model-deployment-guide.md   # Gradio 部署指南
├── src/                        # 源码模块
│   ├── feature_engineering.py
│   ├── models.py
│   ├── evaluation.py
│   ├── visualization.py
│   ├── pipeline.py
│   ├── utils.py
│   └── gradio_app.py          # （存在模型时）
├── scripts/                    # 运行脚本
│   ├── run_experiment.py
│   └── launch_app.py          # （存在模型时）
```

## 工作流命令

按顺序执行以下命令以完成研究工作流：

1. `@raw-data-analysis.md` - 分析 `data/raw/` 中的原始数据
2. `@preprocess.md` - 设计并执行数据预处理
3. `@research-plan.md` - 制定完整研究方案
4. `@code-implementation.md` - 实现分析代码并进行质量检查
5. `@run-experiments.md` - 运行实验流水线
6. `@experiment-analysis.md` - 分析实验结果并撰写文档
7. `@research-report.md` - 生成 Nature/Science 风格论文
8. `@gradio-app.md` - 构建模型部署界面（如适用）

## 代码质量标准

- **类型注解**：所有函数必须包含类型标注
- **文档字符串**：模块、类与函数均需提供完整 docstring
- **测试**：运行 `mypy src/` 进行类型检查
- **代码规范**：运行 `ruff check src/` 与 `ruff format src/`
- **错误处理**：实现完善的异常处理与日志记录

## 依赖管理

项目使用 UV 管理依赖：
- 添加依赖：`uv add <package-name>`
- 同步环境：`uv sync`
- 锁定文件：`uv.lock`

常用依赖：
- 数据处理：pandas、numpy
- 机器学习：scikit-learn、xgboost、lightgbm
- 深度学习：torch、tensorflow（按需）
- 可视化：matplotlib、seaborn、plotly
- Web 交互：gradio
- 质量工具：mypy、ruff

## 运行脚本

- 运行 Python 脚本时务必使用 uv。

## 重要指南

### 文件创建
- 非必要不要新增文件
- 优先编辑已有文件，而非新建
- 文档文件仅按工作流要求创建

### 文档编写
- 遵循 `docs/` 下的编号结构
- 保持内容简洁、清晰、数据驱动
- 聚焦可复现性与方法论

### 学术写作
- 论文须符合 Nature/Science 格式
- 强调方法学严谨性和统计显著性
- 提供必要的补充材料
- 产出可发表的图表

### 模型部署
- 仅在存在训练模型时创建 Gradio 应用
- 注重推理接口的可用性
- 加入完善的输入校验与错误处理

## Git 工作流

- 未经用户明确要求，不要提交任何变更
- 提交时需撰写清晰、描述性的提交信息
- 遵循仓库的提交信息规范
