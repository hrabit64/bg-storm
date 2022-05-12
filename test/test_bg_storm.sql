-- --------------------------------------------------------
-- 호스트:                          ubuntu.hrabit64.xyz
-- 서버 버전:                        10.5.15-MariaDB-1:10.5.15+maria~focal - mariadb.org binary distribution
-- 서버 OS:                        debian-linux-gnu
-- HeidiSQL 버전:                  11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- bg-storm-test 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `bg-storm-test` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `bg-storm-test`;

-- 테이블 bg-storm-test.actions 구조 내보내기
CREATE TABLE IF NOT EXISTS `actions` (
  `ACTION_PK` int(11) NOT NULL,
  `ACTION_STATUS` enum('Error','Pulling','Success','Change','Execute') COLLATE armscii8_bin DEFAULT NULL,
  `ACTION_START_TIME` datetime DEFAULT NULL,
  `ACTION_END_TIME` datetime DEFAULT NULL,
  `API_API_NAME` varchar(50) COLLATE armscii8_bin NOT NULL,
  PRIMARY KEY (`ACTION_PK`),
  KEY `API_API_NAME` (`API_API_NAME`),
  CONSTRAINT `API_API_NAME` FOREIGN KEY (`API_API_NAME`) REFERENCES `api` (`API_NAME`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;

-- 테이블 데이터 bg-storm-test.actions:~0 rows (대략적) 내보내기
DELETE FROM `actions`;
/*!40000 ALTER TABLE `actions` DISABLE KEYS */;
/*!40000 ALTER TABLE `actions` ENABLE KEYS */;

-- 테이블 bg-storm-test.alembic_version 구조 내보내기
CREATE TABLE IF NOT EXISTS `alembic_version` (
  `version_num` varchar(32) COLLATE armscii8_bin NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;

-- 테이블 데이터 bg-storm-test.alembic_version:~0 rows (대략적) 내보내기
DELETE FROM `alembic_version`;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;

-- 테이블 bg-storm-test.api 구조 내보내기
CREATE TABLE IF NOT EXISTS `api` (
  `API_NAME` varchar(50) COLLATE armscii8_bin NOT NULL DEFAULT '',
  `API_INDEX` text COLLATE armscii8_bin DEFAULT NULL,
  `API_NGINX_DOMAIN` varchar(50) COLLATE armscii8_bin NOT NULL,
  `API_BLUE_PORT` int(11) NOT NULL DEFAULT 0,
  `API_GREEN_PORT` int(11) NOT NULL DEFAULT 0,
  `API_RUNNING_STATUS` enum('Green','Blue') COLLATE armscii8_bin DEFAULT 'Blue',
  PRIMARY KEY (`API_NAME`),
  UNIQUE KEY `BLUE_PORT` (`API_BLUE_PORT`,`API_NGINX_DOMAIN`,`API_GREEN_PORT`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;

-- 테이블 데이터 bg-storm-test.api:~0 rows (대략적) 내보내기
DELETE FROM `api`;
/*!40000 ALTER TABLE `api` DISABLE KEYS */;
/*!40000 ALTER TABLE `api` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
