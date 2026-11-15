#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [[ ! -f .env ]]; then
  echo "Missing .env file." >&2
  exit 1
fi

set -a
source .env
set +a

: "${MYSQL_DATABASE:?MYSQL_DATABASE is required}"
: "${MYSQL_USER:?MYSQL_USER is required}"
: "${MYSQL_PASSWORD:?MYSQL_PASSWORD is required}"

BACKUP_DIR="${BACKUP_DIR:-$ROOT_DIR/backups}"
mkdir -p "$BACKUP_DIR"
chmod 700 "$BACKUP_DIR"
STAMP="$(date +%Y%m%d_%H%M%S)"
OUTPUT="$BACKUP_DIR/${MYSQL_DATABASE}_$STAMP.sql.gz"

MYSQL_PWD="$MYSQL_PASSWORD" mysqldump \
  --host="${MYSQL_HOST:-127.0.0.1}" \
  --port="${MYSQL_PORT:-3306}" \
  --user="$MYSQL_USER" \
  --single-transaction --routines --triggers --events \
  "$MYSQL_DATABASE" | gzip > "$OUTPUT"

chmod 600 "$OUTPUT"
echo "Backup created: $OUTPUT"
