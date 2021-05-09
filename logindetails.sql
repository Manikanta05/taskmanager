-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 09, 2021 at 04:10 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `task_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `logindetails`
--

CREATE TABLE `logindetails` (
  `id` int(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `designation` varchar(50) NOT NULL,
  `emailid` varchar(100) NOT NULL,
  `passwd` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `logindetails`
--

INSERT INTO `logindetails` (`id`, `name`, `department`, `designation`, `emailid`, `passwd`) VALUES
(2, 'Prabhudev Jagadeesh. M.P', 'cse', 'Associate Professor', 'prabhu.jagadeesh@gmail.com', '25556589252'),
(3, 'Naveen.N.C', 'cse', 'Head', 'naveennc@jssateb.ac.in', '12366461341'),
(4, 'Sneha .Y.S.', 'cse', 'Associate Professor', 'sneha.girisha@gmail.com', '31042687552'),
(5, 'P.B. Mallikarjuna', 'cse', 'Associate Professor', 'mallikarjunapb@jssateb.ac.in', '28896622752'),
(6, 'Nagasundara K B', 'cse', 'Associate Professor', 'nagasundarakb@gmail.com', '95780434620'),
(7, 'Naidila Sadashiv', 'cse', 'Associate Professor', 'naidilasg@gmail.com', '32835054298'),
(8, 'Snehalatha .N', 'cse', 'Asst. Prof.', 'snehim@rediffmail.com', '60612768493'),
(9, 'Bhavani .B.H.', 'cse', 'Asst. Prof.', 'bhavaninageshms@gmail.com', '52313062779'),
(10, 'K.S. Rajeshwari.', 'cse', 'Asst. Prof.', 'ksrajeshwari@jssateb.ac.in', '42955626340'),
(11, 'K.V. Shanthala.', 'cse', 'Asst. Prof.', 'kv.shan76@gmail.com', '57289808208'),
(12, 'Sharana Basavana Gowda', 'cse', 'Asst. Prof.', 'sharanbg2011@gmail.com', '40088325696'),
(13, 'Pooja.H.', 'cse', 'Asst. Prof.', 'pooja.h.28@gmail.com', '81404471637'),
(14, 'Manjunath. B.Talawar', 'cse', 'Asst. Prof.', 'mbtalawar@gmail.com', '40645887264'),
(15, 'Niranjan Chanabasappa Kundur', 'cse', 'Asst. Prof.', 'niranjanckt@gmail.com', '29187883316'),
(16, 'Savita. S', 'cse', 'Asst. Prof.', 'savita.s.cs@gmail.com', '36830940799'),
(17, 'Shweta S. kaddi', 'cse', 'Asst. Prof.', 'swethaskaddi@jssateb.ac.in', '54265147975'),
(18, 'H.K. Pradeep', 'cse', 'Asst. Prof.', 'phk.contact@gmail.com', '85634975936'),
(19, 'Sreenatha.M.', 'cse', 'Asst. Prof.', 'sreenath.jssate@gmail.com', '29794239979'),
(20, 'Abhilash. C.B', 'cse', 'Asst. Prof.', 'abhilash@gmail.com', '89305422885'),
(21, 'Renuka Rajendra. B', 'cse', 'Asst. Prof.', 'renukarajendrab@gmail.com', '14616911277'),
(22, 'Rohitaksha. K.', 'cse', 'Asst. Prof.', 'rohithaksha.k@gmail.com', '77358962610'),
(23, 'Rashmi . B.N', 'cse', 'Asst. Prof.', 'rashmi.1011bn@gmail.com', '5440556692'),
(24, 'Prasad. M.R', 'cse', 'Asst. Prof.', 'mrp.prasad@gmail.com', '1689722997'),
(25, 'Vikhyath K B', 'cse', 'Asst. Prof.', 'vikhyath059@gmail.com', '57602615737'),
(26, 'Ranjitha S R', 'cse', 'Asst. Prof.', 'ranjithasr12@gmail.com', '4129782280');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `logindetails`
--
ALTER TABLE `logindetails`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `logindetails`
--
ALTER TABLE `logindetails`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
