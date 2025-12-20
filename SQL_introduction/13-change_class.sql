-- Drop rows that have bad scores
DELETE *
FROM second_table
WHERE score<=5;

