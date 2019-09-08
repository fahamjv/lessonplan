-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Sep 08, 2019 at 09:14 AM
-- Server version: 5.7.27
-- PHP Version: 7.2.19-0ubuntu0.19.04.2

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
  `teacher` varchar(20) COLLATE utf8_persian_ci DEFAULT NULL,
  `grade` varchar(15) COLLATE utf8_persian_ci DEFAULT NULL,
  `major` varchar(20) COLLATE utf8_persian_ci DEFAULT NULL,
  `lesson_code` varchar(10) COLLATE utf8_persian_ci DEFAULT NULL,
  `day` varchar(10) COLLATE utf8_persian_ci DEFAULT NULL,
  `start_time` varchar(15) COLLATE utf8_persian_ci DEFAULT NULL,
  `end_time` varchar(15) COLLATE utf8_persian_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

--
-- Dumping data for table `classes`
--

INSERT INTO `classes` (`id`, `lesson_name`, `teacher`, `grade`, `major`, `lesson_code`, `day`, `start_time`, `end_time`) VALUES
(28, 'برنامه نویسی ۱', 'پیمان صفری', 'دهم', 'کامپیوتر', '۱۲۳۴', 'شنبه', '08:00:01', '12:30:01'),
(29, 'فتوشاپ', 'باقری', 'دهم', 'کامپیوتر', '۴۳۵۶', 'یکشنبه', '08:00:01', '09:30:01'),
(30, 'ساختمان داده', 'مریدانی', 'دهم', 'کامپیوتر', '۳۴۲۴', 'سه شنبه', '09:00:01', '13:00:01'),
(31, 'معماری مدرن', 'رحمانی', 'یازدهم', 'ساختمان', '۳۴۳۵', 'شنبه', '09:00:01', '11:30:01'),
(32, 'اصول بتون ریزی', 'قاسمی', 'یازدهم', 'ساختمان', '۶۴۳۵', 'شنبه', '08:00:01', '10:00:01'),
(33, 'الگوریتم', 'مفره زاده', 'دوازدهم', 'کامپیوتر', '۲۳۴۵', 'دوشنبه', '09:00:01', '11:30:01'),
(34, 'حسابان', 'رمضانی', 'یازدهم', 'حسابداری', '۲۱۳۴۵', 'دوشنبه', '10:00:01', '14:00:01'),
(36, 'شبکه', 'پویایی', 'دهم', 'کامپیوتر', '۱۲۴۵', 'شنبه', '09:00:01', '10:00:01'),
(37, 'ریاضی ۲', 'رضایی', 'دهم', 'کامپیوتر', '۳۴۵۴', 'سه شنبه', '08:00:01', '10:00:01'),
(38, 'مدار ۱', 'عمرازی', 'دهم', 'الکترونیک', '۱۲۳۴۵', 'دوشنبه', '08:00:01', '13:00:01'),
(40, '', '', 'دهم', 'کامپیوتر', '', 'شنبه', '10:00:01', '12:30:01');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
