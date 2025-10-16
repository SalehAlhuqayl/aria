# ARIA 快速上手指南

本指南将带你完成从环境搭建到生成首份研究报告的完整 ARIA（Automated Research Intelligence Assistant）使用流程。

## 前置条件

开始之前，你需要安装以下工具：

- **Python 3.12 或更高版本** - [下载 Python](https://www.python.org/downloads/)
- **Git** - 版本控制系统 [下载 Git](https://git-scm.com/downloads)
- **AI 代码编辑器** - 选择其一：
  - [Cursor](https://www.cursor.com/)（推荐，内置 AI）
  - [Claude Code](https://claude.com/product/claude-code)（AI 开发工具）
  - [Visual Studio Code](https://code.visualstudio.com/) + AI 插件
  - [通义灵码 Lingma IDE](https://lingma.aliyun.com/download)（国内用户推荐，当 Claude Code/Cursor 部分模型无法访问时的替代方案）
- **UV 包管理器** - 快速的 Python 包安装工具 [UV 文档](https://docs.astral.sh/uv/)
  - 推荐使用，性能优于 pip
  - 安装说明见下文

### 工具安装指南

#### 1. 安装 Git

**Windows：**

- 从 [git-scm.com](https://git-scm.com/download/win) 下载安装包
- 使用默认设置运行安装程序

**macOS：**

```bash
# 使用 Homebrew（推荐）
brew install git

# 或从 https://git-scm.com/download/mac 下载
```

**Linux (Ubuntu/Debian)：**

```bash
sudo apt-get update
sudo apt-get install git
```

验证安装：

```bash
git --version
```

#### 2. 安装 Python

**Windows：**

- 从 [python.org](https://www.python.org/downloads/) 下载安装包
- ⚠️ 重要：安装时勾选 "Add Python to PATH"

**macOS：**

```bash
# 使用 Homebrew（推荐）
brew install python@3.12

# 或从 https://www.python.org/downloads/ 下载
```

**Linux (Ubuntu/Debian)：**

```bash
sudo apt-get update
sudo apt-get install python3.12 python3.12-venv
```

验证安装：

```bash
python3 --version  # 应显示 3.12 或更高版本
```

#### 3. 安装 UV 包管理器

**所有平台：**

```bash
# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

验证安装：

```bash
uv --version
```

更多详情请参阅 [UV 安装指南](https://docs.astral.sh/uv/getting-started/installation/)

#### 4. 安装 AI 代码编辑器

选择以下**其中一个**选项：

---

**方案 A：Cursor**

Cursor 是一款内置 AI 功能的代码编辑器。

**特点：**

- 内置 AI 功能（无需安装扩展插件）
- 斜杠命令系统，便于执行工作流
- 支持 Claude、GPT-4 等多种 AI 模型
- 基于 VSCode

**安装步骤：**

1. 访问 [cursor.com](https://www.cursor.com/)
2. 下载适合你操作系统的版本
3. 安装应用程序
4. 打开 Cursor 并登录（或跳过直接使用）
5. 在设置中配置你偏好的 AI 模型
6. 在对话框中输入 `/` 可查看可用命令，选择 ARIA 工作流命令

---

**方案 B：Visual Studio Code + AI 插件**

如果你已经在使用 VSCode 或更偏好它，可以通过插件添加 AI 功能。

**步骤 1：安装 Visual Studio Code**

- 访问 [code.visualstudio.com](https://code.visualstudio.com/)
- 下载并安装适合你操作系统的版本

**步骤 2：安装 AI 插件**（选择**其中一个**）：

**GitHub Copilot**（支持斜杠命令）

- 打开 VSCode
- 进入扩展市场（`Ctrl+Shift+X` 或 `Cmd+Shift+X`）
- 搜索并安装 "GitHub Copilot" 和 "GitHub Copilot Chat"
- 两个扩展都需要安装
- 使用 GitHub 账号登录
- 在 Copilot Chat 中输入 `/` 即可使用 ARIA 工作流命令
- 了解更多：[GitHub Copilot](https://github.com/features/copilot)

**OpenAI Codex**（支持斜杠命令）

- 打开 VSCode
- 进入扩展市场（`Ctrl+Shift+X` 或 `Cmd+Shift+X`）
- 搜索 "OpenAI" 或 "ChatGPT" 相关扩展
- 点击安装并使用你的 OpenAI API 密钥进行配置
- 在对话框中输入 `/` 即可使用 ARIA 工作流命令
- 了解更多：[OpenAI Platform](https://platform.openai.com/)

**步骤 3：安装 Python 扩展**（推荐）

- 在扩展市场搜索 "Python" by Microsoft
- 点击安装，获得更好的 Python 开发支持

---

**方案 C：通义灵码 Lingma IDE**（国内用户推荐）

通义灵码 Lingma IDE 是阿里云通义团队开发的 AI 驱动开发工具，专为中国用户设计，当国际 AI 模型（Claude Code/Cursor）无法访问时的理想选择。

**特点：**

- 全面集成 AI 编码助手（内置功能，无需插件）
- 工程级代码理解和生成
- 行间对话和代码建议
- 终端命令执行
- 记忆感知和上下文理解
- 编程智能体能力
- 国内访问流畅，无需VPN

**安装步骤：**

1. 访问 [通义灵码 IDE 下载页面](https://lingma.aliyun.com/download)
2. 下载适合你系统的版本：
   - **macOS**：macOS 10.15+（支持 Intel 和 Apple Silicon）
   - **Windows**：Windows 10/11（x86、arm64）
3. 安装应用程序
4. 打开 Lingma IDE，使用阿里云账号登录
5. 即可开始使用 AI 编码功能

**在 Lingma IDE 中使用 ARIA 命令：**

Lingma IDE 支持类似 Cursor 的工作流命令：

1. 在 Lingma IDE 中打开 ARIA 项目文件夹
2. 使用对话功能引用 ARIA 命令文件
3. 输入 `@` 后跟命令文件名（例如：`@raw-data-analysis.md`）
4. 按照 AI 引导的工作流程进行操作

了解更多：[通义灵码官方网站](https://lingma.aliyun.com/download)

---

**对比：**

| 功能     | Cursor       | VSCode + 插件                      | 通义灵码 Lingma IDE |
| -------- | ------------ | ---------------------------------- | ------------------- |
| 内置 AI  | 是           | 否（需要安装插件）                 | 是                  |
| 命令支持 | 斜杠命令     | 是（GitHub Copilot、OpenAI Codex） | @ 命令              |
| 安装步骤 | 仅安装编辑器 | 安装编辑器 + 插件                  | 仅安装编辑器        |
| 国内访问 | 可能需要VPN  | 取决于插件                         | 专为国内优化        |
| 可定制性 | 标准选项     | 广泛的插件生态系统                 | 标准选项            |

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

安装完所有工具后，让我们为 ARIA 配置 Python 环境：

### 创建虚拟环境

```bash
# 进入 ARIA 项目目录
cd aria

# 使用 Python 3.12 创建虚拟环境
uv venv --python 3.12
```

### 激活虚拟环境

**Windows：**

```bash
.venv\Scripts\activate
```

**macOS/Linux：**

```bash
source .venv/bin/activate
```

### 安装依赖包

```bash
uv sync
```

**国内用户**（可选，加速下载）：

```bash
UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple uv sync
```

### 验证安装

```bash
# 检查包是否正确安装
python -c "import pandas; import numpy; import sklearn; print('✓ 所有包已成功安装！')"
```

> **提示：** 更多高级配置选项请参阅 [INSTALL.md](./INSTALL.md)。

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

## 步骤 5：使用 AI 工作流命令

ARIA 通过 AI 工作流命令自动化研究过程，命令位于 `.claude/commands/academic/`。

### 执行工作流

依次执行以下步骤：

> **通义灵码 Lingma IDE 用户注意：**  
> 如果使用 Lingma IDE，请使用 `@文件名` 方式代替 `/` 命令。  
> 例如：输入 `@raw-data-analysis.md` 而不是从 `/` 菜单中选择。

**Cursor/VSCode + AI 插件用户：**

1. **分析原始数据**

   在对话框中输入 `/` 并选择 `raw-data-analysis.md`

   分析原始数据并生成 `docs/02-raw-data-analysis.md`

2. **数据预处理**

   输入 `/` 并选择 `preprocess.md`

   制定预处理方案并完成数据处理

3. **设计研究方案**

   输入 `/` 并选择 `research-plan.md`

   输出完整的研究方法设计

4. **实现代码**

   输入 `/` 并选择 `code-implementation.md`

   在 `src/` 中生成所需 Python 模块

5. **运行实验**

   输入 `/` 并选择 `run-experiments.md`

   执行实验流水线

6. **结果分析**

   输入 `/` 并选择 `experiment-analysis.md`

   解析实验输出并生成报告

7. **撰写学术论文**

   输入 `/` 并选择 `research-report.md`

   生成可投稿的学术论文

8. **部署模型（可选）**

   输入 `/` 并选择 `gradio-app.md`

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

- **Cursor/VSCode + AI 插件：** 输入 `/` 并选择 `git-commit.md`
- **通义灵码 Lingma IDE：** 输入 `@git-commit.md`

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

3. **执行 AI 工作流**：

   **使用 Cursor/VSCode + AI 插件：**

   打开编辑器，在对话框中输入 `/` 并依次选择：
   - 选择 `raw-data-analysis.md`
   - 选择 `preprocess.md`
   - 选择 `research-plan.md`
   - 选择 `code-implementation.md`
   - 选择 `run-experiments.md`
   - 选择 `experiment-analysis.md`
   - 选择 `research-report.md`

   **使用通义灵码 Lingma IDE：**

   依次输入 `@` 后跟命令文件名：
   - `@raw-data-analysis.md`
   - `@preprocess.md`
   - `@research-plan.md`
   - `@code-implementation.md`
   - `@run-experiments.md`
   - `@experiment-analysis.md`
   - `@research-report.md`

## 故障排查

### 工具安装问题

1. **Git 命令无法识别**：
   - Windows：安装后重启终端，或手动将 Git 添加到 PATH
   - 验证：`git --version`

2. **找不到 Python**：
   - Windows：重新安装 Python 并勾选 "Add Python to PATH"
   - macOS/Linux：尝试使用 `python3` 而非 `python`
   - 验证：`python --version` 或 `python3 --version`

3. **找不到 UV**：
   - 安装后关闭并重新打开终端
   - 检查 UV 是否在 PATH 中：`echo $PATH` (macOS/Linux) 或 `echo %PATH%` (Windows)
   - 尝试重新安装：[UV 安装指南](https://docs.astral.sh/uv/getting-started/installation/)

4. **权限被拒绝错误**：
   - macOS/Linux：系统级安装可能需要使用 `sudo`
   - Windows：以管理员身份运行 PowerShell 或命令提示符

### 常见运行时问题

1. **导入错误**：确认所有依赖已安装且虚拟环境已激活

   ```bash
   # 首先激活虚拟环境
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows

   # 然后同步依赖
   uv sync
   ```

2. **找不到 AI 命令**：
   - 确保使用的是 Cursor
   - 验证命令文件位于 `.claude/commands/academic/`
   - 在 Cursor 对话框中，输入 `/` 查看可用命令

3. **找不到数据**：检查数据是否位于 `data/raw/` 目录

   ```bash
   ls data/raw/  # macOS/Linux
   dir data\raw  # Windows
   ```

4. **内存不足**：针对大规模数据，可考虑：
   - 先使用数据子集
   - 分块处理
   - 增加系统内存
   - 使用内存更大的机器

5. **虚拟环境无法激活**：
   - 确保位于项目根目录
   - 尝试重新创建虚拟环境：`uv venv --python 3.12`
   - Windows 上可能需要启用脚本执行：
     ```powershell
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
     ```

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
3. **善用版本控制**：频繁使用 `/` 命令选择 `git-commit.md` 提交
4. **检查输出**：每个阶段都审阅生成的文档
5. **持续迭代**：按需重复任意步骤

## 额外资源

- [ARIA 文档](./README.md)
- [Claude AI 文档](https://docs.anthropic.com)
- [UV 包管理器](https://github.com/astral-sh/uv)
- [Python 类型提示](https://docs.python.org/3/library/typing.html)

---

准备好了吗？把数据放入 `data/raw/`，打开 Cursor，在对话框中输入 `/` 并选择 `raw-data-analysis.md` 开始吧！
