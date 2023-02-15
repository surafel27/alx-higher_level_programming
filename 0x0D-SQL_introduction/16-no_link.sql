-- List the score and the name if only name exist.
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC;
