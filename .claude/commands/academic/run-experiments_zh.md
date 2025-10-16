## 使用方式

`@run-experiments.md`

## 上下文

- 执行指南：`docs/07-execution-instructions.md`
- 实验主脚本：`scripts/run_experiment.py`
- 处理后数据位于 `data/processed/`
- 输出目录：`data/output/`

## 流程

1. 阅读执行指南：`docs/07-execution-instructions.md`
2. 确认环境配置与依赖项已就绪
3. 创建输出目录结构：
   - `data/output/models/` 保存训练模型
   - `data/output/results/` 保存数值结果
   - `data/output/figures/` 保存可视化图表
   - `data/output/logs/` 保存运行日志
4. 执行实验流水线：
   ```bash
   uv run python scripts/run_experiment.py
   ```
5. 监控运行进度并记录所有错误
6. 核对生成的输出是否齐全：
   - 模型文件
   - 结果指标（CSV/JSON）
   - 可视化图形
   - 运行日志
7. 在 `data/output/execution_summary.txt` 中撰写执行摘要，包含：
   - 起止时间
   - 使用的参数
   - 生成的文件
   - 警告或错误
8. 验证输出的完整性与可靠性
