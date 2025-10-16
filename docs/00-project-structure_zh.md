# 项目文档结构

本文档说明 ARIA 研究项目的标准化文档命名与结构。

## 文档流程

1. **01-basic-information.md** - 项目基础信息（手动创建）
2. **02-raw-data-analysis.md** - 原始数据探索
3. **03-preprocess-plan.md** - 数据预处理策略
4. **04-processed-data-analysis.md** - 预处理后数据特征
5. **05-research-plan.md** - 综合研究设计
6. **06-implementation-docs.md** - 代码实现文档
7. **07-execution-instructions.md** - 实验执行指南
8. **08-experiment-results/** - 单项结果分析目录
9. **09-experiment-report.md** - 综合实验分析
10. **10-manuscript.md** - 学术论文（Nature/Science 格式）
11. **10-manuscript-supplement.md** - 补充材料
12. **10-cover-letter.md** - 投稿附信
13. **11-model-deployment-guide.md** - Gradio 应用部署指南

## 目录结构

```
docs/
├── 00-project-structure.md          # 本文件
├── 01-basic-information.md          # 手动创建
├── 02-raw-data-analysis.md
├── 03-preprocess-plan.md
├── 04-processed-data-analysis.md
├── 05-research-plan.md
├── 06-implementation-docs.md
├── 07-execution-instructions.md
├── 08-experiment-results/           # 单项分析目录
│   ├── model-performance.md
│   ├── feature-importance.md
│   └── ...
├── 09-experiment-report.md
├── 10-manuscript.md
├── 10-manuscript-supplement.md
├── 10-cover-letter.md
└── 11-model-deployment-guide.md
```
