CREATE DATABASE  IF NOT EXISTS `myownapi` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `myownapi`;
-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: localhost    Database: myownapi
-- ------------------------------------------------------
-- Server version	5.5.41-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `quotes`
--

DROP TABLE IF EXISTS `quotes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quotes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quote` text,
  `author` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quotes`
--

LOCK TABLES `quotes` WRITE;
/*!40000 ALTER TABLE `quotes` DISABLE KEYS */;
INSERT INTO `quotes` VALUES (1,'Learn the rules like a pro, so you can break them like an artist.','Pablo Picasso'),(2,'Java is to JavaScript what Car is to Carpet. ','Chris Heilmann'),(3,'If debugging is the process of removing software bugs, then programming must be the process of putting them in.','Edsger Dijkstra'),(4,'Any fool can write code that a computer can understand. Good programmers write code that humans can understand. ','Martin Fowler'),(5,'Computers are good at following instructions, but not at reading your mind.','Donald Knuth'),(6,'Measuring programming progress by lines of code is like measuring aircraft building progress by weight.','Bill Gates'),(7,'There are only two kinds of languages: the ones people complain about and the ones nobody uses','Bjarne Stroustrup'),(8,'It\'s all talk until the code runs.','Ward Cunningham'),(9,'A clever person solves a problem. A wise person avoids it.','Albert Einstein'),(10,'Being a good software engineer is 3% talent, 97% not being distracted by the internet.','Unknown'),(11,'You silly bear','Christopher Robin'),(12,'Resistance is futile.','Anonymous'),(13,'Imagine a world without hypothetical situations.','Steven Wright'),(14,'I\'m a kangaroo!','roo'),(15,'I\'m a kangaroo!','roo'),(16,'I\'m a kangaroo!','roo'),(17,'I\'m a kangaroo!','roo'),(18,'I\'m a kangaroo!','roo'),(19,'I\'m a small animal indeed!','piglet'),(20,'I cannot tell a lie. My sister cut down the tree.','George Washington'),(21,'I cannot tell a lie. My sister and dog cut down the tree and buried the body.','George Washington'),(22,'Peanuts. I am so tired of peanuts.','George Washington Carver'),(23,'Peanuts, morning, noon, and night.','George Washington Carver'),(24,'I\'d love to have you over for dinner.','Hanibal Lector'),(25,'I\'d love to have you over for dinner, along with your friend.','Hanibal Lector'),(26,'Do it.','Bill'),(27,'I bring you glad tidings.','Michael');
/*!40000 ALTER TABLE `quotes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-01 20:50:15
