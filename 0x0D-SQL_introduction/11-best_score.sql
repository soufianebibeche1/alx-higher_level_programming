#!/usr/bin/env bash
-- Script to list all records with a score >= 10 in the second_table
-- Pass the database name as an argument to the mysql command

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
