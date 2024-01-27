-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 05, 2023 at 09:43 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hr`
--

-- --------------------------------------------------------

--
-- Table structure for table `personel`
--

CREATE TABLE `personel` (
  `id_emp` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` varchar(80) NOT NULL,
  `salary` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `personel`
--

INSERT INTO `personel` (`id_emp`, `name`, `email`, `phone`, `address`, `salary`) VALUES
(1, 'vasilis', 'mylonastest@gmail.com', '6983654637', 'ifigenias 31, Kallithea', 1500),
(2, 'giorgos', 'giorgos@hotmail.gr', '6978061689', 'olympoy 47, larissa', 1101),
(3, 'mpampis', 'mpampis@gmail.com', '6975748873', 'sinopis 9, kavala', 800),
(4, 'takis', 'takis@yahoo.gr', '6810220345', 'edmondoy rostan 46, 8essaloniki', 600),
(5, 'antonis', 'antonis@gmail.com', '5879461237', 'antonis 4, mytilini', 799),
(6, 'zioyzios', 'zioyzios@hotmail.gr', '5794684592', 'perikleoys 14, patra', 1450);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `personel`
--
ALTER TABLE `personel`
  ADD PRIMARY KEY (`id_emp`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
