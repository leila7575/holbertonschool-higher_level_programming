-- lists the number of records with the same score in the table second_table
-- displays score and numbr of records for this score 
SELECT score AS score,
	COUNT(*) AS number
FROM second_table 
GROUP BY score
ORDER BY score DESC;
