# My Railways

A unified operational layer for mobile-device orchestration, MCP server integration, and enterprise automation workflows.

## Goals
- Manage real devices, simulators, and emulators through a single API
- Run Python orchestration for business workflows
- Expose device automation through MCP-compatible interfaces
- Provide testable, auditable logging and configuration patterns
- Support CI automation with quality gates

## Quick start

### Python environment
```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

# Node tooling
```bash
npm install
```
# Run device orchestrator
```bash
python main-devices.py
```

# Run tests
```bash
pytest -q
```

# Environment
Copy `.env.example` to `.env` and configure local values.
```Code

pyproject.toml

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my-railways"
version = "0.1.0"
description = "Unified railways orchestration platform for mobile device automation"
readme = "README.md"
requires-python = ">=3.11"
authors = [{ name = "AnticipatedD" }]
license = { text = "MIT" }

dependencies = [
  "pydantic>=2.7.0",
  "python-dotenv>=1.0.1",
  "requests>=2.31.0",
]

[project.optional-dependencies]
dev = [
  "pytest>=8.0.0",
  "pytest-cov>=5.0.0",
  "ruff>=0.5.0",
  "mypy>=1.10.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]

[tool.ruff]
line-length = 100
target-version = "py311"
```
---
# my-railways
A complete railways automation and mobile orchestration repository for device control, logging, testing, and CI/CD.

---
