-- MariaDB dump 10.17  Distrib 10.4.14-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: AGP
-- ------------------------------------------------------
-- Server version	10.4.14-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `arrivals`
--

DROP TABLE IF EXISTS `arrivals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `arrivals` (
  `year` year(4) NOT NULL,
  `greece` float NOT NULL,
  `spain` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arrivals`
--

LOCK TABLES `arrivals` WRITE;
/*!40000 ALTER TABLE `arrivals` DISABLE KEYS */;
INSERT INTO `arrivals` VALUES (2016,24996000,123541778),(2017,27211300,129392382),(2018,33585600,130803657),(2019,34202100,135008823);
/*!40000 ALTER TABLE `arrivals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arrivals_non`
--

DROP TABLE IF EXISTS `arrivals_non`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `arrivals_non` (
  `year` year(4) NOT NULL,
  `greece` float NOT NULL,
  `spain` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arrivals_non`
--

LOCK TABLES `arrivals_non` WRITE;
/*!40000 ALTER TABLE `arrivals_non` DISABLE KEYS */;
INSERT INTO `arrivals_non` VALUES (2016,16916000,61341839),(2017,19068700,65233045),(2018,24320900,65771059),(2019,25038500,67728098);
/*!40000 ALTER TABLE `arrivals_non` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `night`
--

DROP TABLE IF EXISTS `night`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `night` (
  `year` year(4) NOT NULL,
  `greece` float NOT NULL,
  `spain` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `night`
--

LOCK TABLES `night` WRITE;
/*!40000 ALTER TABLE `night` DISABLE KEYS */;
INSERT INTO `night` VALUES (2016,110020000,454957250),(2017,119009000,471199729),(2018,142940000,466940717),(2019,143594000,469813551);
/*!40000 ALTER TABLE `night` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `night_non`
--

DROP TABLE IF EXISTS `night_non`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `night_non` (
  `year` year(4) NOT NULL,
  `greece` float NOT NULL,
  `spain` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `night_non`
--

LOCK TABLES `night_non` WRITE;
/*!40000 ALTER TABLE `night_non` DISABLE KEYS */;
INSERT INTO `night_non` VALUES (2016,87912800,294556428),(2017,97034400,305907462),(2018,118876000,301022634),(2019,119971000,299091409);
/*!40000 ALTER TABLE `night_non` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-12 19:52:39
