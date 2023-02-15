-- List the score which is equal as a number.
SELECT `score`, count(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
