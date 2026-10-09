# Token权限矩阵与撤销回归自动化测试系统

## 📖 项目简介
基于 Python + Pytest 搭建的接口自动化测试框架，模拟真实企业级系统的 Token 权限控制与撤销机制，覆盖权限矩阵、越权拦截、Token失效等核心安全场景。

## 🛠️ 技术栈
- 测试框架：Python、Pytest、Requests
- 数据驱动：YAML
- 持续集成：GitHub Actions
- 环境模拟：Flask
- 数据库校验：SQLite

## 📂 项目结构
- `mock_server/`：本地 Mock 服务（4个接口 + 重置接口）
- `data/`：YAML 测试数据（10条权限矩阵用例）
- `tests/`：测试脚本（权限矩阵、撤销回归、数据库校验）

## 🚀 如何运行
1. 安装依赖：`pip install -r requirements.txt`
2. 启动 Mock 服务：`python mock_server/app.py`
3. 执行测试：`pytest tests/ -s`

## 💡 项目亮点
- 数据驱动：YAML 管理 10 条权限用例，代码与数据分离
- 安全回归：验证 Token 撤销后接口不可用、非法 Token 拦截
- CI 自动化：代码提交自动触发 GitHub Actions 流水线