-- Script creates table on MySQL.
CREATE TABLE IF NOT EXISTS unique_id (
id INT UNIQUE DEFAULT 1,
name VARCHAR(256)
);
