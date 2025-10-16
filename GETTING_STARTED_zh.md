# ARIA 快速上手指南

本指南将带你完成从环境搭建到生成首份研究报告的完整 ARIA（Automated Research Intelligence Assistant）使用流程。

## 前置条件

- Python 3.12 或更高版本
- Git
- [Claude Code](https://claude.com/product/claude-code) 或 [Cursor](https://www.cursor.com/)
- UV 包管理器（推荐）或 pip

## 步骤 1：Fork 并克隆仓库

### 方案 A：在 GitHub 上 Fork（推荐）

1. 访问 [ARIA on GitHub](https://github.com/Biaoo/aria)
2. 点击右上角的 "Fork" 按钮
3. 克隆你 Fork 后的仓库：

```bash
git clone https://github.com/YOUR_USERNAME/aria.git
cd aria
```

### 方案 B：在 Gitee 上 Fork（国内用户推荐）

1. 访问 [ARIA on Gitee](https://gitee.com/BiaooGitee/aria)
2. 点击右上角的 "Fork" 按钮
3. 克隆你 Fork 后的仓库：

```bash
git clone https://gitee.com/YOUR_USERNAME/aria.git
cd aria
```

### 方案 C：直接克隆

如果不需要 Fork，可以直接从 GitHub 或 Gitee 克隆：

**从 GitHub 克隆：**

```bash
git clone https://github.com/Biaoo/aria.git
cd aria
```

**从 Gitee 克隆：**

```bash
git clone https://gitee.com/BiaooGitee/aria.git
cd aria
```

## 步骤 2：配置 Python 环境

详细说明参见 [INSTALL.md](./INSTALL.md)。

## 步骤 3：初始化项目结构

如目录不存在，可运行以下命令创建：

```bash
mkdir -p data/raw data/processed
mkdir -p docs
mkdir -p data/output/{models,results,figures,logs}
```

## 步骤 4：准备数据

1. 将原始数据文件放入 `data/raw/` 目录：

   ```bash
   cp /path/to/your/data/* data/raw/
   ```

2. 创建初始项目文档：

   ```bash
   touch docs/01-basic-information.md
   ```

3. 编辑 `docs/01-basic-information.md`，涵盖以下内容：
   - 项目标题与目标
   - 数据说明与来源
   - 研究问题
   - 预期成果

示例结构：

```markdown
# 项目：[你的项目名称]

## 研究背景

### 领域介绍（可选）

[说明研究所属领域以及该问题的重要性]

### 研究动机（可选）

[阐述研究必要性与拟填补的空白]

## 研究目标（可选）

### 总体目标（可选）

[写出研究的核心目标]

### 具体目标（可选）

1. [第一个具体目标]
2. [第二个具体目标]
3. [第三个具体目标]

## 原始数据说明

### 数据来源

- 来源：[数据来源 - 数据库、实验、调查等]
- 采集方式：[数据采集方法]
- 时间范围：[数据采集时间]
- 地理范围：[如适用]

### 数据特征

- 文件格式：[CSV、JSON、Excel、图像等]
- 文件数量：[数据文件数量]
- 总体积：[文件大小]
- 样本量：[记录/样本数量]
- 特征数：[变量/列数]

### 数据结构

- 主键字段：[唯一标识字段]
- 特征类型：[数值、类别、文本等]
- 目标变量：[若为监督学习]
- 缺失情况：[初步的完整性评估]
```

## 步骤 5：使用 Claude AI 命令

ARIA 通过 Claude AI 命令自动化研究工作流，命令位于 `.claude/commands/`。

### 执行工作流

在 Claude Code 中依次运行以下命令：

1. **分析原始数据**

   ```
   @raw-data-analysis.md
   ```

   分析原始数据并生成 `docs/02-raw-data-analysis.md`

2. **数据预处理**

   ```
   @preprocess.md
   ```

   制定预处理方案并完成数据处理

3. **设计研究方案**

   ```
   @research-plan.md
   ```

   输出完整的研究方法设计

4. **实现代码**

   ```
   @code-implementation.md
   ```

   在 `src/` 中生成所需 Python 模块

5. **运行实验**

   ```
   @run-experiments.md
   ```

   执行实验流水线

6. **结果分析**

   ```
   @experiment-analysis.md
   ```

   解析实验输出并生成报告

7. **撰写学术论文**

   ```
   @research-report.md
   ```

   生成可投稿的学术论文

8. **部署模型（可选）**

   ```
   @gradio-app.md
   ```

   构建模型的交互式 Web 界面

## 步骤 6：代码质量检查

实现代码后，请运行以下命令确保质量：

```bash
# 类型检查
mypy src/

# 代码规范检查
ruff check src/

# 代码格式化
ruff format src/
```

## 步骤 7：版本控制

使用智能 Git 提交命令：

```
@git-commit.md
```

该命令会自动生成结构化提交，可在文件较多时批量处理。

## 快速示例：鸢尾花（Iris）分类

以下示例展示如何使用经典的鸢尾花数据集完成完整流程：

1. **准备数据**：

   ```bash
   # 下载鸢尾花数据集到 data/raw/
   python -c "
   from sklearn.datasets import load_iris
   import pandas as pd
   iris = load_iris()
   df = pd.DataFrame(iris.data, columns=iris.feature_names)
   df['target'] = iris.target
   df.to_csv('data/raw/iris.csv', index=False)
   "
   ```

2. **撰写项目描述**：

   ```bash
   cat > docs/01-basic-information.md << 'EOF'
   # 项目：鸢尾花物种分类

   ## 研究目标
   - 构建识别鸢尾花物种的分类器
   - 对比多种机器学习算法

   ## 数据概览
   - 经典鸢尾花数据集
   - 150 条样本，4 个特征
   - 3 个类别标签

   ## 研究问题
   1. 哪些特征对分类最重要？
   2. 哪个算法表现最佳？

   ## 预期成果
   - 训练准确率超过 95% 的分类器
   - 特征重要性分析
   EOF
   ```

3. **执行 Claude AI 工作流**：
   打开 Claude Code，依次运行以下命令：

   ```
   @raw-data-analysis.md
   @preprocess.md
   @research-plan.md
   @code-implementation.md
   @run-experiments.md
   @experiment-analysis.md
   @research-report.md
   ```

## 故障排查

### 常见问题

1. **导入错误**：确认所有依赖均已安装

   ```bash
   uv sync  # 或 pip install -e .
   ```

2. **找不到 Claude AI 命令**：确保在使用 Claude Code 且命令位于 `.claude/commands/`

3. **找不到数据**：检查数据是否位于 `data/raw/` 目录

4. **内存不足**：针对大规模数据，可考虑：
   - 先使用数据子集
   - 分块处理
   - 增加系统内存

### 寻求帮助

- 查看已有问题： [GitHub Issues](https://github.com/Biaoo/aria/issues)
- 新建 Issue 时请提供：
  - 错误信息
  - 复现步骤
  - 环境详情

## 后续步骤

在完成首次分析后，可以：

1. **自定义工作流**：根据需求修改 `.claude/commands/` 下的命令
2. **扩展自定义模块**：在 `src/` 目录编写专用函数
3. **丰富可视化**：于 `src/visualization.py` 中新增自定义图表
4. **分享成果**：使用 Gradio 部署模型或构建仪表盘

## 成功秘诀

1. **从小规模开始**：先用小数据集验证流程
2. **做好记录**：持续更新 `docs/01-basic-information.md`
3. **善用版本控制**：频繁使用 `@git-commit.md` 提交
4. **检查输出**：每个阶段都审阅生成的文档
5. **持续迭代**：按需重复任意步骤

## 额外资源

- [ARIA 文档](./README.md)
- [Claude AI 文档](https://docs.anthropic.com)
- [UV 包管理器](https://github.com/astral-sh/uv)
- [Python 类型提示](https://docs.python.org/3/library/typing.html)

---

准备好了吗？把数据放入 `data/raw/`，然后从 `@raw-data-analysis.md` 开始！
