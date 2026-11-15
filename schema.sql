-- Initial schema for a NEW CheckManagement installation.
-- Do not run this over an existing production database without a backup.
CREATE DATABASE IF NOT EXISTS check_management
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE check_management;

CREATE TABLE IF NOT EXISTS customer_table (
    customer_id INT NOT NULL AUTO_INCREMENT,
    customer_code VARCHAR(20) NOT NULL,
    customer_name VARCHAR(150) NOT NULL,
    organization_name VARCHAR(200) NULL,
    customer_phone VARCHAR(30) NULL,
    customer_mobile VARCHAR(30) NULL,
    customer_address TEXT NULL,
    PRIMARY KEY (customer_id),
    UNIQUE KEY uq_customer_code (customer_code),
    KEY idx_customer_name (customer_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS bank_table (
    bank_id INT NOT NULL AUTO_INCREMENT,
    bank_name VARCHAR(120) NOT NULL,
    PRIMARY KEY (bank_id),
    UNIQUE KEY uq_bank_name (bank_name)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO bank_table (bank_name) VALUES
    ('بانک ملی'),
    ('بانک مهر ایران'),
    ('بانک صادرات'),
    ('بانک کشاورزی'),
    ('بانک ملت'),
    ('بانک مسکن'),
    ('بانک تجارت')
ON DUPLICATE KEY UPDATE bank_name = VALUES(bank_name);

CREATE TABLE IF NOT EXISTS check_table (
    check_id INT NOT NULL AUTO_INCREMENT,
    check_code VARCHAR(30) NOT NULL,
    sayadi_number VARCHAR(50) NOT NULL,
    customer_id INT NOT NULL,
    amount DECIMAL(18,2) NOT NULL DEFAULT 0,
    due_date DATE NOT NULL,
    bank_id INT NULL,
    front_image VARCHAR(500) NULL,
    back_image VARCHAR(500) NULL,
    description TEXT NULL,
    created_at DATE NOT NULL,
    is_deleted TINYINT(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (check_id),
    UNIQUE KEY uq_check_code (check_code),
    KEY idx_check_sayadi (sayadi_number),
    KEY idx_check_customer (customer_id),
    KEY idx_check_bank (bank_id),
    CONSTRAINT fk_check_customer FOREIGN KEY (customer_id)
      REFERENCES customer_table(customer_id)
      ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_check_bank FOREIGN KEY (bank_id)
      REFERENCES bank_table(bank_id)
      ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS operation (
    operation_id INT NOT NULL AUTO_INCREMENT,
    check_id INT NOT NULL,
    operation_code VARCHAR(40) NOT NULL,
    operation_type VARCHAR(100) NOT NULL,
    operation_date DATE NOT NULL,
    related_person VARCHAR(150) NULL,
    description TEXT NULL,
    sayad_system_status VARCHAR(100) NULL,
    PRIMARY KEY (operation_id),
    UNIQUE KEY uq_operation_code (operation_code),
    KEY idx_operation_check (check_id),
    CONSTRAINT fk_operation_check FOREIGN KEY (check_id)
      REFERENCES check_table(check_id)
      ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
