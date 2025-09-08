-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: produtobd
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `NOME` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=501 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,'Peixaria'),(2,'Categoria 2'),(3,'Categoria 3'),(4,'Categoria 4'),(5,'Categoria 5'),(6,'alimentos'),(7,'grãos'),(8,'eletrônicos'),(9,'jogos'),(10,'celulares'),(11,'guloseimas'),(35,'Automobilisticos'),(36,'Mercearia'),(37,'Frios'),(40,'utilidades'),(43,'hortifruti'),(55,'Badulaques'),(66,'Açougue'),(77,'Abobrinha');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produto`
--

DROP TABLE IF EXISTS `produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produto` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `NOME` varchar(100) NOT NULL,
  `DESCRICAO` varchar(1000) DEFAULT NULL,
  `PRECO_COMPRA` decimal(9,2) NOT NULL,
  `PRECO_VENDA` decimal(9,2) NOT NULL,
  `QUANTIDADE` int NOT NULL DEFAULT '0',
  `DISPONIVEL` tinyint(1) NOT NULL DEFAULT '1',
  `DT_CADASTRO` timestamp NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produto`
--

LOCK TABLES `produto` WRITE;
/*!40000 ALTER TABLE `produto` DISABLE KEYS */;
INSERT INTO `produto` VALUES (1,'Arroz','Tipo 1',20.00,28.00,100,1,'2024-09-02 03:00:00'),(2,'Iphone','Celular Apple',20000.00,25000.00,100,1,'2024-09-02 03:00:00'),(3,'IOS','Celular Apple',320.00,400.00,30,1,'2024-09-02 03:00:00'),(4,'Sorvete','Sorvete tipo napolitano',10.00,30.00,40,1,'2024-09-02 03:00:00'),(5,'Video game','Nintendo Switch',150.00,300.00,100,1,'2024-09-02 03:00:00'),(6,'Rebimboca da parafuseta','xxx',2.00,2.50,100,1,'2024-09-10 03:00:00'),(7,'secador de gelo elétrico','xxx',50.00,75.50,100,1,'2024-09-10 03:00:00'),(8,'Tang sabor Pixirica','xxx',1.00,1.50,100,1,'2024-09-10 03:00:00'),(9,'jiló em calda com coco ralado','xxx',10.00,12.00,100,1,'2024-09-10 03:00:00');
/*!40000 ALTER TABLE `produto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produto_categoria`
--

DROP TABLE IF EXISTS `produto_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produto_categoria` (
  `ID_PRODUTO` bigint NOT NULL,
  `ID_CATEGORIA` int NOT NULL,
  KEY `FK_PRODUTO` (`ID_PRODUTO`),
  KEY `FK_CATEGORIA` (`ID_CATEGORIA`),
  CONSTRAINT `FK_CATEGORIA` FOREIGN KEY (`ID_CATEGORIA`) REFERENCES `categoria` (`ID`),
  CONSTRAINT `FK_PRODUTO` FOREIGN KEY (`ID_PRODUTO`) REFERENCES `produto` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produto_categoria`
--

LOCK TABLES `produto_categoria` WRITE;
/*!40000 ALTER TABLE `produto_categoria` DISABLE KEYS */;
INSERT INTO `produto_categoria` VALUES (1,6),(1,6),(1,7),(4,6),(4,11),(5,9),(5,8),(3,8),(3,10),(2,10),(2,8);
/*!40000 ALTER TABLE `produto_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venda`
--

DROP TABLE IF EXISTS `venda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venda` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data` datetime NOT NULL,
  `quantidade` int NOT NULL,
  `id_produto` bigint NOT NULL,
  `dinheiro` char(1) NOT NULL,
  `cartao` char(1) NOT NULL,
  `parcelas` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_produto` (`id_produto`),
  CONSTRAINT `venda_ibfk_1` FOREIGN KEY (`id_produto`) REFERENCES `produto` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venda`
--

LOCK TABLES `venda` WRITE;
/*!40000 ALTER TABLE `venda` DISABLE KEYS */;
INSERT INTO `venda` VALUES (1,'2024-07-10 00:00:00',10,1,'S','N',1),(2,'2024-07-10 00:00:00',25,2,'N','S',10),(3,'2024-07-10 00:00:00',50,3,'S','N',1),(4,'2024-07-10 00:00:00',35,4,'N','S',1),(5,'2024-07-10 00:00:00',27,5,'N','S',1),(6,'2024-07-10 00:00:00',5,6,'N','S',1),(7,'2024-07-10 00:00:00',9,7,'N','S',1);
/*!40000 ALTER TABLE `venda` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-28 17:11:55
