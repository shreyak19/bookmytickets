CREATE DATABASE bookmytickets;
USE bookmytickets;

CREATE TABLE tickets(T_id INT NOT NULL, T_row INT, T_col INT, T_Price INT, PRIMARY KEY(T_id));
CREATE TABLE userinfo(User_id INT NOT NULL,Name VARCHAR(50), Gender VARCHAR(6), Age INT, Contact VARCHAR(10),T_id INT, PRIMARY KEY(User_id),FOREIGN KEY(T_id) REFERENCES tickets(T_id));


DESC tickets;
DESC userinfo;
