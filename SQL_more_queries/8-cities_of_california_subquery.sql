-- list all cities in California
SELECT id, name
FROM states
WHERE name='California'
ORDER BY cities.id;
