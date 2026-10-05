from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main() -> None:
    manifest = {
        "project": "my-railways",
        "status": "ready",
        "python_modules": ["src"],
        "node_modules": ["mcp_server.ts"]
    }
    print(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    main()
