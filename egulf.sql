-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 01, 2022 at 03:50 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `egulf`
--

-- --------------------------------------------------------

--
-- Table structure for table `CARTS`
--

CREATE TABLE `CARTS` (
  `cartId` int(11) NOT NULL,
  `uname` varchar(25) NOT NULL,
  `itemId` int(11) NOT NULL,
  `itemName` varchar(25) NOT NULL,
  `itemQuantity` int(11) NOT NULL,
  `itemPrice` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `INVENTORY`
--

CREATE TABLE `INVENTORY` (
  `itemId` int(11) NOT NULL,
  `itemPrice` float NOT NULL,
  `itemName` varchar(25) NOT NULL,
  `itemQuantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `INVENTORY`
--

INSERT INTO `INVENTORY` (`itemId`, `itemPrice`, `itemName`, `itemQuantity`) VALUES
(1, 10000, 'speedboat', 5),
(2, 20000, 'Pontoon', 19),
(3, 30000, 'Tritoon', 33),
(4, 60000, 'Bay boats', 20),
(5, 100000, 'Cuddy Cabin', 10);

-- --------------------------------------------------------

--
-- Table structure for table `ORDERS`
--

CREATE TABLE `ORDERS` (
  `orderId` int(11) NOT NULL,
  `uname` varchar(25) NOT NULL,
  `numItems` int(11) NOT NULL,
  `subtotal` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ORDERS`
--

INSERT INTO `ORDERS` (`orderId`, `uname`, `numItems`, `subtotal`) VALUES
(1, 'rs1234', 3, 30000),
(2, 'rs1234', 3, 30000),
(3, 'rs1234', 9, 100000),
(4, 'rs1234', 1, 10000);

-- --------------------------------------------------------

--
-- Table structure for table `USERS`
--

CREATE TABLE `USERS` (
  `fname` varchar(25) NOT NULL,
  `lname` varchar(25) NOT NULL,
  `uname` varchar(25) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(15) NOT NULL,
  `addr1` varchar(10) DEFAULT NULL,
  `addr2` varchar(10) DEFAULT NULL,
  `city` varchar(25) DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  `zip` varchar(5) DEFAULT NULL,
  `cardNum` varchar(16) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `USERS`
--

INSERT INTO `USERS` (`fname`, `lname`, `uname`, `email`, `password`, `addr1`, `addr2`, `city`, `state`, `zip`, `cardNum`) VALUES
('rs', 'rs', 'rs1234', 'rs1234@gmail.com', 'rs@1234', '', '', '', '', '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `CARTS`
--
ALTER TABLE `CARTS`
  ADD PRIMARY KEY (`cartId`,`uname`),
  ADD KEY `uname` (`uname`);

--
-- Indexes for table `INVENTORY`
--
ALTER TABLE `INVENTORY`
  ADD PRIMARY KEY (`itemId`),
  ADD KEY `itemName` (`itemName`);

--
-- Indexes for table `ORDERS`
--
ALTER TABLE `ORDERS`
  ADD PRIMARY KEY (`orderId`),
  ADD KEY `uname` (`uname`);

--
-- Indexes for table `USERS`
--
ALTER TABLE `USERS`
  ADD PRIMARY KEY (`uname`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `realName` (`fname`,`lname`) USING BTREE;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `CARTS`
--
ALTER TABLE `CARTS`
  MODIFY `cartId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `INVENTORY`
--
ALTER TABLE `INVENTORY`
  MODIFY `itemId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `ORDERS`
--
ALTER TABLE `ORDERS`
  MODIFY `orderId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
