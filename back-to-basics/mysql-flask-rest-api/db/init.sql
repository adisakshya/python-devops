CREATE DATABASE my_database;
use my_database;

CREATE TABLE user_credentials (
  user_id VARCHAR(255) PRIMARY KEY,
  user_name VARCHAR(30),
  user_email VARCHAR(30),
  password VARCHAR(255)
);

