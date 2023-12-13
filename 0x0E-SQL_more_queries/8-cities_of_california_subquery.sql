#!/usr/bin/env bash
-- Use the database
USE hbtn_0d_usa;

-- List all cities of California without using JOIN
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
