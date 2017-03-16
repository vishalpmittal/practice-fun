-- *******   PIG LATIN SCRIPT for Yelp Assignmet ******************

-- 0. get function defined for CSV loader
-- linux > sudo yum install -y datafu

register /usr/lib/pig/piggybank.jar;
register /usr/lib/pig/datafu.jar;
register /usr/lib/pig/piggybank.jar;
define CSVLoader org.apache.pig.piggybank.storage.CSVLoader();

-- 1 load data

Y = LOAD '/user/cloudera/pig_input2/yelp_data.csv' USING CSVLoader() AS(business_id:chararray,cool,date,funny,id,stars:int,text:chararray,type,useful:int,user_id,name,full_address,latitude,longitude,neighborhoods,open,review_count,state);
Y_good = FILTER Y BY (useful is not null and stars is not null);

--2 Find max useful
Y_all = GROUP Y_good ALL;
Umax  = FOREACH Y_all GENERATE MAX(Y_good.useful);
DUMP Umax

-- this shows max useful rating of 28! ...

-- 3 Now limit useful field to be <=5 and then get wtd average

Y_rate  = FOREACH Y_good GENERATE business_id,stars,(useful>5 ? 5:useful) as useful_clipped;
Y_rate2 = FOREACH Y_rate GENERATE $0..,(double) stars*(useful_clipped/5) as wtd_stars;

-- 4 Rank businesses

Y_g = GROUP Y_rate2 BY business_id;
Y_m = FOREACH Y_g
      GENERATE group as business_idgroup,COUNT(Y_rate2.stars) as num_ratings ,
          AVG(Y_rate2.stars) as avg_stars,
          AVG(Y_rate2.useful_clipped) as avg_useful,
          AVG(Y_rate2.wtd_stars) as avg_wtdstars;
         
Y_rnk = RANK Y_m BY avg_wtdstars;

-- Question 1
--  ----------------------------------
Y_srtd = ORDER Y_m BY avg_wtdstars DESC;
DUMP Y_srtd;

-- Answer
-- -----------
-- 5.0

-- Question 2
--  ----------------------------------
-- The overall task in this question is the following:
-- For businesses that have more than 1 rating, find the average of weighted stars across businesses.
-- 
-- Here is one way to solve it that gets the average of the average:
--
-- A. start with Y_m from the Yelp script in the readings.
-- B. try >DESCRIBE Y_m to see whats in there
DESCRIBE Y_m
-- Y_m: {business_idgroup: chararray,num_ratings: long,avg_stars: double,avg_useful: double,avg_wtdstars: double}

-- C. Enter commands, here is some pseudo code:
--  1. Filter Y_m to choose those business with num_ratings > 1, call the relation Y_m2
Y_m2 = FILTER Y_m BY (num_ratings > 1);

--  2. Use a GROUP ALL to create a bag of avg_wtdstars
Y_m2_all = GROUP Y_m2 ALL;
DESCRIBE Y_m2_all

--  3. Use the AVG function in a FOREACH statment to find AVG(Y_m2.avg_wtdstars),
StarAvg  = FOREACH Y_m2_all GENERATE AVG(Y_m2.avg_wtdstars);

--  4. DUMP the relation and answer the question
DUMP StarAvg;

-- Answer
-- -----------
-- (0.4011627906976744)


-- Question 3
--  ----------------------------------
-- Here is another way to get the average of weighted stars across businesses.
-- 
-- Get the average of all wtd_stars from all businsss with number of ratings > 1, grouped together.
-- Strategy: First, we have to group the businesses to get a count of the number of ratings. Then we filter that set - we actually already have that in Y_m2 from Question 2 above.
-- 
-- Then we have to use that result to select only businesses that are in that set.
-- Here is Pseudo-code for one way to solve it:
-- Start with Y_rate2, which has wtd_stars, and Y_m2 which has the businesses with number of ratings > 1 
-- 1. Join Y_rate2 with Y_m2 using business id as the key. Do you want an inner or outer join?
Y_joined = JOIN Y_rate2 BY business_id, Y_m2 By business_idgroup;
DESCRIBE Y_joined;

-- 2. Make a GROUP ALL so the wtd_stars is in a bag
Y_joined_all = GROUP Y_joined ALL;
DESCRIBE Y_joined_all;

-- 3. Use FOREACH to generate the average wtd_stars,
StarAvg2 = FOREACH Y_joined_all GENERATE AVG(Y_joined.wtd_stars);

-- DUMP the relation and answer the question
DUMP StarAvg2

-- Answer
-- -----------
-- (0.40390879478827363)




