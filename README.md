# CheckManagement

Desktop cheque and customer management application built with Python, PyQt5 and MySQL. The application UI is currently Persian.

## Supported platform

- **Recommended:** Windows 10 (64-bit), Python 3.12, MySQL Server 8.0.
- Ubuntu/Linux with Python 3.12 and MySQL Server 8.0.
- **Windows 7 is not a supported target for this setup.** Current Python and MySQL releases no longer provide a reliable supported installation path for Windows 7. Use Windows 10 or newer.

## Windows 10 installation

1. Install 64-bit Python 3.12 from [python.org](https://www.python.org/downloads/windows/). Enable the Python launcher during installation.
2. Install MySQL Server 8.0 using the [official MySQL Installer](https://dev.mysql.com/downloads/installer/). Remember the MySQL administrator password.
3. Open Command Prompt or PowerShell and clone the repository:

```powershell
git clone https://github.com/sepideh54/CheckManagement.git
cd CheckManagement
```

4. Run the setup script:

```bat
setup_windows.bat
```

5. Create the database schema from Command Prompt (enter the MySQL root password when prompted):

```bat
mysql -u root -p < schema.sql
```

6. Create a dedicated application account. Open the MySQL command line as administrator:

```bat
mysql -u root -p
```

Then run the following SQL, replacing the example password with a strong unique password:

```sql
CREATE USER 'check_manager'@'127.0.0.1' IDENTIFIED BY 'REPLACE_WITH_A_STRONG_PASSWORD';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, INDEX, REFERENCES
ON check_management.* TO 'check_manager'@'127.0.0.1';
FLUSH PRIVILEGES;
EXIT;
```

7. Open the generated `.env` file in a text editor and set `MYSQL_HOST=127.0.0.1`, `MYSQL_PORT=3306`, `MYSQL_DATABASE=check_management`, `MYSQL_USER=check_manager`, and the password you chose.
8. Double-click `run_windows.bat` to launch the application.

## Ubuntu/Linux installation

Install Python 3.12, MySQL Server 8.0 and Git, then run:

```bash
git clone https://github.com/sepideh54/CheckManagement.git
cd CheckManagement
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
sudo systemctl enable --now mysql
sudo mysql < schema.sql
cp .env.example .env
```

Create the same dedicated MySQL account shown in the Windows section, then edit `.env` and run:

```bash
python main.py
```

## Database and existing records

- `schema.sql` creates the initial empty database and four tables used by the current CRUD code: `customer_table`, `bank_table`, `check_table`, and `operation`.
- The schema was inferred from the SQL statements in the repository. It has not been compared with the original live database or validated against a complete application test suite.
- **Do not import this schema over an existing database containing important records.** Back up existing data first. This file creates the initial schema; it does not transfer existing records.
- Image files are stored under `images/checks/`. Keep this folder with the project. Images selected later are copied there by the application.

## Configuration and security

- `.env.example` is a template. The local `.env` file contains credentials and is excluded from Git.
- Never commit database passwords or local configuration.
- A database password was present in an earlier Git commit. The current source no longer contains it, but the old credential remains in Git history. Rotate it and do not reuse it.

## Development

- Use `requirements.txt` to recreate the Python environment on each computer.
- Do not copy `.venv/` between computers.
- Start the app from the project directory so relative image paths resolve correctly.
- The repository contains the Python source, Qt UI files, generated Qt resources, and image assets required by the current application.
- A successful installation setup is not the same as a verified end-to-end test. Database compatibility and all GUI workflows still need regression testing before relying on this application for important financial records.


## Database inspection and backup

For an existing database, do not run `schema.sql` as an upgrade script. First create a verified backup, then inspect the live schema:

```bash
python scripts/backup_mysql.sh
mysql --host=127.0.0.1 --user=check_manager --password check_management < scripts/audit_schema.sql
```

The audit script is read-only and reports tables, columns, constraints and indexes. Compare its output with `schema.sql` before planning any migration. No automatic migration is performed by this repository.

The backup script reads credentials from `.env`, writes compressed dumps under `backups/`, and restricts local file permissions. Store an additional copy of backups on a separate encrypted device or trusted backup location. Periodically test restoration into a separate database; a backup that has never been restored is not verified.

## Automated tests

Run the fast, database-independent validation tests with:

```bash
python -m unittest discover -s tests -v
python -m compileall -q .
python -m pip check
```

These tests verify input contracts only. They do not prove live MySQL CRUD, schema compatibility, GUI behavior, concurrency safety, or successful backup restoration. Those checks must be completed against a disposable test database before production use.

## Current development hardening

The `hardening/crud-and-data-integrity` branch consolidates CRUD connection cleanup, removes the duplicate customer listing implementation, adds input guards, connects the bank lookup table to the cheque form, and adds a read-only schema audit and backup utility. Review and test this branch before merging it into `master`.
