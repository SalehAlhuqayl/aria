## 使用方式

`@preprocess.md`

## 上下文

- 项目基础信息：`docs/01-basic-information.md`
- 原始数据存放于 `data/raw/`
- 原始数据分析：`docs/02-raw-data-analysis.md`

## 可用工具

- 使用 `cat`、`head`、`tail`、`grep`、`pandas`、`json` 等工具读取数据

## 流程

1. 阅读项目基础信息：`docs/01-basic-information.md`
2. 阅读原始数据分析：`docs/02-raw-data-analysis.md`
3. 结合基础信息与原始数据分析，设计数据预处理方案，使数据更适合后续分析，并将方案写入 `docs/03-preprocess-plan.md`
4. 按预处理方案在 `scripts/` 目录编写必要脚本，处理后的数据存放于 `data/processed/`
5. 运行脚本执行数据预处理
6. 阅读并分析处理后的数据，将结果写入 `docs/04-processed-data-analysis.md`，内容需简明清晰，包含数据类型、字段类型、数量、存储位置、数据特征等信息
7. 更新项目基础信息：在 `docs/01-basic-information.md` 中补充预处理方案与处理后数据分析的要点
