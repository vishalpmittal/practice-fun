/*
Utilizing the Bay Area Bike Share database (both Year 1 & 2, Aug. 2013- Aug. 2015)- what is the most popular start station based on trip data?
*/

SELECT Z.ss, COUNT(Z.ss) as ss_count
FROM (
SELECT 14td_2.startstation as ss FROM 201402_trip_data 14td_2
UNION ALL
SELECT 14td_8.startstation as ss FROM 201408_trip_data 14td_8
UNION ALL
SELECT 15td.startstation as ss FROM 201508_trip_data 15td
) AS Z
GROUP BY Z.ss
ORDER BY ss_count DESC

-- san francisco caltrain
-- -------------------------------------------------
-- -------------------------------------------------
/*
Utilizing the Bay Area Bike Share database (Year 1 only, Aug. 2013- Feb 2014) - Which is the least popular(least used) start station in the Bike share trips data?

(Hint: Use the count of start station, group and order in ascending order)
*/

SELECT 14td.startstation, COUNT(14td.startstation) as ss_count
FROM 201402_trip_data 14td
GROUP BY 14td.startstation
ORDER BY ss_count ASC

-- Mezes Park
-- -------------------------------------------------
-- -------------------------------------------------
/*
Utilizing the Bay Area Bike Share database (for Year 1 only, Aug. 2013 - Aug. 2014 only) - what is the SECOND MOST popular end station based on trip data?

(Hint: Use the count of end station, group and order in descending order)
*/

SELECT Z.es, COUNT(Z.es) as es_count
FROM (
SELECT 14td_2.endstation as es FROM 201402_trip_data 14td_2
UNION ALL
SELECT 14td_8.endstation as es FROM 201408_trip_data 14td_8
) AS Z
GROUP BY Z.es
ORDER BY es_count DESC

-- Embarcadero at Sansome
-- -------------------------------------------------
-- -------------------------------------------------