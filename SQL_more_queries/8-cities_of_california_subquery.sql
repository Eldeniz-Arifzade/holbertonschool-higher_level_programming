-- list all cities in California
USE hbtn_0d_usa;
SELECT id, name
FROM states
WHERE name='California'
ORDER BY cities.id;
