-- List cities of ALL CITIES in database.
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON cities.id = states.id ORDER BY cities.id ASC;
