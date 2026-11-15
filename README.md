# CheckManagement

Desktop cheque and customer management application built with Python, PyQt5 and MySQL.

## Requirements

- Python 3.10 or newer
- MySQL Server 8.0 or newer
- A graphical Linux desktop (for the PyQt5 interface)

## 1. Clone the project

```bash
git clone https://github.com/sepideh54/CheckManagement.git
cd CheckManagement
```

## 2. Create a virtual environment and install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3. Prepare MySQL

Start MySQL and import the initial schema into a NEW installation:

```bash
sudo systemctl enable --now mysql
sudo mysql < schema.sql
```

Create a dedicated application user for the default TCP host `127.0.0.1` (replace the sample password with a strong, unique one):

```bash
sudo mysql
```

Then, at the MySQL prompt:

```sql
CREATE USER 'check_manager'@'127.0.0.1' IDENTIFIED BY 'REPLACE_WITH_A_STRONG_PASSWORD';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, INDEX, REFERENCES
ON check_management.* TO 'check_manager'@'127.0.0.1';
FLUSH PRIVILEGES;
EXIT;
```

If you set `MYSQL_HOST=localhost` in `.env`, create the corresponding MySQL account as `'check_manager'@'localhost'` too.

**Security:** A database password was previously committed in the repository's Git history. The current code no longer contains it, but removing it from the latest version does not erase historical commits. Rotate that old database password immediately and do not reuse it.

**Existing data:** `schema.sql` creates the initial empty schema; it does not migrate or restore data from another computer. Back up and transfer the existing database separately before using this setup on a machine that already contains important records.

## 4. Configure the application

```bash
cp .env.example .env
```

Edit `.env` and set `MYSQL_HOST`, `MYSQL_PORT`, `MYSQL_DATABASE`, `MYSQL_USER` and `MYSQL_PASSWORD` to match your MySQL setup. Never commit `.env` or real passwords to Git.

## 5. Run

From the project directory, with the virtual environment activated:

```bash
python main.py
```

Keep `images/` in the project directory. The application stores cheque image paths relative to the working directory.

## Development notes

- Do not copy `.venv/` between computers; recreate it using `requirements.txt`.
- `schema.sql` is the initial schema inferred from the application's current SQL queries. Validate it against a backup of the original working database before migrating real records.
- This repository setup documents installation; it is not a guarantee that every existing application workflow has been fully regression-tested on a clean machine.
