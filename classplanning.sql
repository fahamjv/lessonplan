-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Aug 04, 2019 at 05:29 AM
-- Server version: 5.7.26
-- PHP Version: 7.2.19-0ubuntu0.19.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `classplanning`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `id` int(11) NOT NULL,
  `username` varchar(100) COLLATE utf8_persian_ci DEFAULT NULL,
  `password` varchar(100) COLLATE utf8_persian_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

-- --------------------------------------------------------

--
-- Table structure for table `classes`
--

CREATE TABLE `classes` (
  `id` int(11) NOT NULL,
  `lesson_name` varchar(100) COLLATE utf8_persian_ci DEFAULT NULL,
  `lesson_code` varchar(10) COLLATE utf8_persian_ci DEFAULT NULL,
  `day` varchar(10) COLLATE utf8_persian_ci DEFAULT NULL,
  `start_time` varchar(10) COLLATE utf8_persian_ci DEFAULT NULL,
  `end_time` varchar(10) COLLATE utf8_persian_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

--
-- Dumping data for table `classes`
--

INSERT INTO `classes` (`id`, `lesson_name`, `lesson_code`, `day`, `start_time`, `end_time`) VALUES
(3, NULL, '3456', 'یکشنبه', '13:40:01', '15:00:01'),
(4, NULL, '2134', 'شنبه', '12:00:01', '15:00:01'),
(5, NULL, '4325', 'شنبه', '13:00:01', '14:30:01'),
(7, NULL, '3456', 'سه شنبه', '12:30:01', '15:00:01'),
(8, NULL, '6789', 'چهارشنبه', '10:00:01', '13:00:01'),
(9, NULL, '4556', 'چهارشنبه', '11:30:01', '13:00:01'),
(14, '234324', '1', 'سه شنبه', '15:24:01', '21:00:01'),
(15, 'تست', '۷۴۳۵', 'دوشنبه', '09:00:01', '11:30:01'),
(16, 'برنامه نویسی - کارگاه', '8976', 'سه شنبه', '08:00:01', '14:00:01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `classes`
--
ALTER TABLE `classes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admins`
--
ALTER TABLE `admins`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `classes`
--
ALTER TABLE `classes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
