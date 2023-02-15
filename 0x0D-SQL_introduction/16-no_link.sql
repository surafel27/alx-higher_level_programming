-- List the score and the name if only name exist.
SELECT `score`, `name` FROM `second_table` WHERE EXISTS (SELECT `name` FROM `second_table`) ORDER BY `score` DESC;
