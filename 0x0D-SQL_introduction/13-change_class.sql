#!/usr/bin/env bash
-- Script to remove all records with a score <= 5 in the second_table

DELETE FROM second_table WHERE score <= 5;
