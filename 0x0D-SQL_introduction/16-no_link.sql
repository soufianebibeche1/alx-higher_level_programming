#!/usr/bin/env bash
-- Script to list all records of the second_table without rows without a name value

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
