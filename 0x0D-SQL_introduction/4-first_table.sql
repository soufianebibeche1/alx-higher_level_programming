#!/usr/bin/env bash
-- Script to create a table called first_table in the specified database

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
