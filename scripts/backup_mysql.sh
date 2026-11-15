#!/usr/bin/env python3
"""Create a compressed, permission-restricted MySQL logical backup."""
import gzip
import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

from dotenv import dotenv_values

ROOT = Path(__file__).resolve().parents[1]
CONFIG = dotenv_values(ROOT / ".env")
required = ("MYSQL_DATABASE", "MYSQL_USER", "MYSQL_PASSWORD")
missing = [key for key in required if not CONFIG.get(key)]
if missing:
    raise SystemExit("Missing required .env settings: " + ", ".join(missing))

backup_dir = Path(os.environ.get("BACKUP_DIR", ROOT / "backups"))
backup_dir.mkdir(parents=True, exist_ok=True)
os.chmod(backup_dir, 0o700)

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output = backup_dir / f"{CONFIG['MYSQL_DATABASE']}_{stamp}.sql.gz"
env = os.environ.copy()
env["MYSQL_PWD"] = CONFIG["MYSQL_PASSWORD"]

command = [
    "mysqldump",
    "--host=" + (CONFIG.get("MYSQL_HOST") or "127.0.0.1"),
    "--port=" + (CONFIG.get("MYSQL_PORT") or "3306"),
    "--user=" + CONFIG["MYSQL_USER"],
    "--single-transaction",
    "--routines",
    "--triggers",
    "--events",
    CONFIG["MYSQL_DATABASE"],
]

try:
    with output.open("wb") as raw_file:
        with gzip.GzipFile(fileobj=raw_file, mode="wb") as compressed:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, env=env)
            assert process.stdout is not None
            shutil.copyfileobj(process.stdout, compressed)
            process.stdout.close()
            return_code = process.wait()
            if return_code != 0:
                raise subprocess.CalledProcessError(return_code, command)
    os.chmod(output, 0o600)
except Exception:
    output.unlink(missing_ok=True)
    raise

print(f"Backup created: {output}")
