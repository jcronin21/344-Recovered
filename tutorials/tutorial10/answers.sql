-- Exercise 1 (done for you): Selecting all columns
SELECT * FROM users;



-- Exercise 2 (done for you): Selecting some columns
SELECT id, first_name, last_name 
FROM users;



-- Exercise 3: Sorting
SELECT * FROM users ORDER BY first_name, last_name



-- Exercise 4: Filtering
SELECT * FROM id,users, image_url
WHERE users =26;



-- Exercise 5: Filtering with logical operators
SELECT id, user_id, image_url
FROM posts
WHERE user_id IN(12,26)



-- Exercise 6: Using functions in a select statement

SELECT COUNT(*) AS post_count
FROM posts;


-- Exercise 7: Aggregating data
SELECT user_id, COUNT (*) AS comment_count
FROM comments
GROUP BY user_id
ORDER BY comment_count DESC;



-- Exercise 8: Joining: two tables
SELECT p.id, p.image_url, p.user_id, u.username, u.first_name, u.last_name
FROM posts post_count
JOIN users u ON p.user_id = u.id
WHERE p.user_id IN (12,26);



-- Exercise 9: More joining practice: two tables
SELECT p.id, p.pub_date, f.following_id
FROM posts p
JOIN following f ON p.user_id = f.following_id
WHERE f.user_id =26;



-- Exercise 10: More joining practice: three tables (Optional)
SELECT p.id, p.pub_date, f.following_id, u.username
FROM posts p
JOIN following f ON p.user_id = f.following_id
JOIN users u ON p.user_id = u.id
WHERE f.user_id =26
ORDER BY p.pub_date DESC;



-- Exercise 11: Inserting records
INSERT INTO bookmarks (user_id, post_id)
VALUES (26,219);
INSERT INTO bookmarks(user_id, post_id)
VALUES (26, 220);
INSERT INTO bookmarks (user_id, post_id)
 VALUES (26,221);


-- Exercise 12: Deleting records
DELETE FROM bookmarks 
WHERE user_id = 26 AND post_id = 219;
DELETE FROM bookmarks
WHERE user_id =26 AND post_id =220;
DELETE FROM bookmarks
WHERE user_id =26 AND post_id =221;



-- Exercise 13: Updating records
UPDATE users
SET email = 'knick2022@gmail.com'
WHERE user_id = 26;



-- Exercise 14: More Querying Practice (Optional)
