-- create database then table, make id unique, auto generated, an primary key.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE `states`(`id` INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` VARCHAR(256) NOT NULL);
