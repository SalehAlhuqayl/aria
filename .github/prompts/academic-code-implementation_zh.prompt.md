## 使用方式

`@code-implementation.md`

## 上下文

- 研究方案：`docs/05-research-plan.md`
- 处理后数据存放于 `data/processed/`
- 源代码目录：`src/`

## 可用工具

- Python 及科学计算库（pandas、numpy、scikit-learn 等）
- 代码质量工具：mypy、ruff

## 流程

1. 阅读研究方案：`docs/05-research-plan.md`
2. 基于研究方案实现代码模块：
   - 创建 `src/feature_engineering.py`：特征工程
   - 创建 `src/models.py`：分析方法/模型
   - 创建 `src/evaluation.py`：评估指标
   - 创建 `src/visualization.py`：数据可视化
   - 创建 `src/pipeline.py`：实验流水线
   - 创建 `src/utils.py`：通用工具函数
3. 确保代码结构完善，包括：
   - 所有函数具备类型注解
   - 模块、类与函数具备 docstring
   - 完善的错误处理与日志记录
   - 配置管理到位
4. 运行代码质量检查：
   - `mypy src/` 进行类型检查
   - `ruff check src/` 检查代码风格
   - `ruff format src/` 格式化代码
5. 创建 `scripts/run_experiment.py` 主执行脚本（涵盖训练、评估、可视化等流程）
6. 将实现文档写入 `docs/06-implementation-docs.md`，包含：
   - 模块说明与依赖关系
   - 核心算法与方法
   - 关键配置参数
   - 代码结构概览
7. 将执行指南写入 `docs/07-execution-instructions.md`，涵盖：
   - 环境准备
   - 脚本使用方法
   - 参数配置说明
   - 预期输出

## 说明

- 如需额外依赖，必须使用 UV 添加
- 使用 UV 运行所有 Python 脚本
- 在输出目录中，除最终结果外，还需保存基线结果、训练日志、可视化图等关键中间产物
- 深度学习框架优先选择 PyTorch，不要使用 TensorFlow
