-- upgrade --
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(20) NOT NULL,
    `content` TEXT NOT NULL
) CHARACTER SET utf8;
CREATE TABLE IF NOT EXISTS `client_users` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6)   DEFAULT CURRENT_TIMESTAMP(6),
    `modified_at` DATETIME(6)   DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_del` INT NOT NULL  DEFAULT 0,
    `auth_user_id` VARCHAR(250) NOT NULL UNIQUE,
    `username` VARCHAR(100),
    `mobile` VARCHAR(100),
    `real_name` VARCHAR(100),
    `email` VARCHAR(100),
    `avatar` VARCHAR(100)   DEFAULT '98d2d0f6-6851-49a8-8d31-8603204cc7311591066453.png',
    `status` INT,
    `tencent_user_id` VARCHAR(100)  UNIQUE,
    `tencent_auth_status` INT
) CHARACTER SET utf8 COMMENT='save ik user info';
