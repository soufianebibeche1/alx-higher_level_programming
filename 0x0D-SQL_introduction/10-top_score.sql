#!/usr/bin/env bash
-- Script to list all records of the table second_table ordered by score

SELECT score, name FROM second_table ORDER BY score DESC;
