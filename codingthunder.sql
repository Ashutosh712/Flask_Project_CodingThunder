-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 23, 2023 at 04:27 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunder`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `Contact_Id` int(10) NOT NULL,
  `Name` varchar(25) NOT NULL,
  `Phone_Number` varchar(12) NOT NULL,
  `Email_Address` varchar(20) NOT NULL,
  `Message` varchar(100) NOT NULL,
  `Date_Time` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`Contact_Id`, `Name`, `Phone_Number`, `Email_Address`, `Message`, `Date_Time`) VALUES
(1, 'Ashutosh Malik', '01234567890', 'abc@gmail.com', 'Hello, This is the first message from my blog to sql database.', '2023-06-21'),
(2, 'Ashutosh Malik', '01234567890', 'abc@gmail.com', 'Hello, This is the first message from my blog to sql database.', '2023-06-21'),
(3, 'Harry', '9876543210', 'Harry@gmail.com', 'Code explained by code with Harry for the flask python', '2023-06-21'),
(4, 'ashu', '9878675609', 'abcde@gmail.com', 'Hi, this is the sample email ', '2023-06-21'),
(5, 'ashu', '9878675609', 'abcde@gmail.com', 'Hi, this is the sample email ', '2023-06-21'),
(6, 'malik', '8796590120', 'ab12@gmail.com', 'Hello, message from blog to database ', '2023-06-21');

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `Post_Id` int(10) NOT NULL,
  `Title` varchar(100) NOT NULL,
  `Sub_Title` varchar(100) NOT NULL,
  `Slug` varchar(20) NOT NULL,
  `Content` varchar(500) NOT NULL,
  `Date` date NOT NULL DEFAULT current_timestamp(),
  `img_file` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`Post_Id`, `Title`, `Sub_Title`, `Slug`, `Content`, `Date`, `img_file`) VALUES
(1, 'Variables, Constants and Literals', 'Learn Python Variables, Constants and Literals with', 'first-post', 'Python Variables\r\nIn programming, a variable is a container (storage area) to hold data.\r\nPython Constant - constant is a special type of variable whose value cannot be changed.\r\nPython Literals - Literals are representations of fixed values in a program.\r\n', '2023-06-21', 'post-sample-image.jpg'),
(2, 'Data Types in python', 'Python Data Types with examples', 'second-post', 'Python Data Types\r\nNumeric	int, float, complex holds numeric values String str holds sequence of characters Sequence list, tuple, range holds collection of items Mapping dict holds data in key-value pair form Boolean	bool holds either True or False Set set, frozen set hold collection of unique items', '2023-06-21', 'post-sample-image2.jpg'),
(3, 'Python operators ', 'Python Operators with examples', 'third-post', 'Types of Python Operators\r\nHere\'s a list of different types of Python operators.\r\n\r\nArithmetic operators\r\nAssignment Operators\r\nComparison Operators\r\nLogical Operators\r\nBitwise Operators\r\nSpecial Operators\r\n', '2023-06-21', 'post-sample-image3.jpg'),
(6, 'Python Content', 'Programming of Python', 'four-post', 'Hello, this is the python content blog.', '2023-06-22', 'sample-image1.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`Contact_Id`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`Post_Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `Contact_Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `Post_Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
