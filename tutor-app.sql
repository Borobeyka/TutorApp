-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Май 27 2022 г., 23:25
-- Версия сервера: 10.3.16-MariaDB
-- Версия PHP: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `tutor-app`
--

-- --------------------------------------------------------

--
-- Структура таблицы `lessons`
--

CREATE TABLE `lessons` (
  `id` int(11) NOT NULL,
  `tutor_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `student_id` int(11) NOT NULL,
  `lesson_type_id` int(11) NOT NULL,
  `payment_type_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `lessons`
--

INSERT INTO `lessons` (`id`, `tutor_id`, `date`, `time`, `student_id`, `lesson_type_id`, `payment_type_id`) VALUES
(1, 1, '2022-05-28', '09:00:00', 1, 2, 1),
(2, 1, '2022-05-27', '14:30:00', 1, 2, 2),
(3, 1, '2022-05-28', '10:20:00', 3, 1, 2),
(4, 1, '2022-05-28', '17:00:00', 2, 3, 2),
(5, 2, '2022-05-28', '13:20:00', 4, 1, 1),
(6, 2, '2022-05-28', '21:00:00', 5, 1, 2),
(9, 2, '2022-05-29', '21:00:00', 5, 3, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `lesson_type`
--

CREATE TABLE `lesson_type` (
  `id` int(11) NOT NULL,
  `lesson_type` varchar(32) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `lesson_type`
--

INSERT INTO `lesson_type` (`id`, `lesson_type`) VALUES
(3, 'Онлайн'),
(2, 'Очно у преподавателя'),
(1, 'Очно у ученика');

-- --------------------------------------------------------

--
-- Структура таблицы `payment_type`
--

CREATE TABLE `payment_type` (
  `id` int(11) NOT NULL,
  `payment_type` varchar(32) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `payment_type`
--

INSERT INTO `payment_type` (`id`, `payment_type`) VALUES
(1, 'Наличные'),
(2, 'Перевод');

-- --------------------------------------------------------

--
-- Структура таблицы `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `name` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(11) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'Не указан',
  `address` varchar(128) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'Не указан',
  `tutor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `students`
--

INSERT INTO `students` (`id`, `name`, `phone`, `address`, `tutor_id`) VALUES
(1, 'Вова', '89998887766', 'Не указан', 1),
(2, 'Илия', '89876543210', 'Не указан', 1),
(3, 'Настя ОГЭ', '81112223344', 'Перовская, 3', 1),
(4, 'Вера', 'Не указан', 'шоссе Энтузиастов, 86Ак1', 2),
(5, 'Настя ЕГЭ', '81118882266', 'Напротив карибии', 2);

-- --------------------------------------------------------

--
-- Структура таблицы `tutors`
--

CREATE TABLE `tutors` (
  `id` int(11) NOT NULL,
  `login` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `tutors`
--

INSERT INTO `tutors` (`id`, `login`, `password`) VALUES
(1, 'borobeyka', '1234'),
(2, 'aakul', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `lessons`
--
ALTER TABLE `lessons`
  ADD PRIMARY KEY (`id`),
  ADD KEY `student_id` (`student_id`),
  ADD KEY `lesson_type_id` (`lesson_type_id`),
  ADD KEY `payment_type_id` (`payment_type_id`),
  ADD KEY `tutor_id` (`tutor_id`);

--
-- Индексы таблицы `lesson_type`
--
ALTER TABLE `lesson_type`
  ADD PRIMARY KEY (`id`),
  ADD KEY `name` (`lesson_type`),
  ADD KEY `name_2` (`lesson_type`);

--
-- Индексы таблицы `payment_type`
--
ALTER TABLE `payment_type`
  ADD PRIMARY KEY (`id`),
  ADD KEY `name` (`payment_type`);

--
-- Индексы таблицы `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tutor_id` (`tutor_id`);

--
-- Индексы таблицы `tutors`
--
ALTER TABLE `tutors`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `lessons`
--
ALTER TABLE `lessons`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT для таблицы `lesson_type`
--
ALTER TABLE `lesson_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `payment_type`
--
ALTER TABLE `payment_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `tutors`
--
ALTER TABLE `tutors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `lessons`
--
ALTER TABLE `lessons`
  ADD CONSTRAINT `lessons_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`),
  ADD CONSTRAINT `lessons_ibfk_3` FOREIGN KEY (`lesson_type_id`) REFERENCES `lesson_type` (`id`),
  ADD CONSTRAINT `lessons_ibfk_4` FOREIGN KEY (`payment_type_id`) REFERENCES `payment_type` (`id`),
  ADD CONSTRAINT `lessons_ibfk_5` FOREIGN KEY (`tutor_id`) REFERENCES `tutors` (`id`);

--
-- Ограничения внешнего ключа таблицы `students`
--
ALTER TABLE `students`
  ADD CONSTRAINT `students_ibfk_1` FOREIGN KEY (`tutor_id`) REFERENCES `tutors` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
