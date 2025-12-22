CREATE DATABASE try;
USE try;
CREATE TABLE Employees (
Employee_ID INT AUTO_INCREMENT PRIMARY KEY, 
Name VARCHAR (100),
Position VARCHAR (100), 
Salary DECIMAL (10, 2), 
Hire_Date DATE
);
CREATE TABLE Employee_Audit (
Audit_ID INT AUTO_INCREMENT PRIMARY KEY,
Employee_ID INT,
Name VARCHAR (100),
Position VARCHAR (100), 
Salary DECIMAL (10, 2), 
Hire_date DATE,
Action_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO employees (name, Position, Salary, Hire_date) 
VALUES 
('John Doe','Software Engineer', 80000.00, '2022-01-15'),
('Jane Smith', 'Project Manager', 90000.00, '2021-05-22'),
('Alice Johnson', 'UX Designer', 75000.00, '2023-03-01');

DELIMITER $$
CREATE PROCEDURE Add_Employees (
    IN p_Name VARCHAR(100),
    IN p_Position VARCHAR(100),
    IN p_Salary DECIMAL(10,2),
    IN p_Hire_Date DATE
)
BEGIN
    INSERT INTO Employees (Name, Position, Salary, Hire_Date)
    VALUES (p_Name, p_Position, p_Salary, p_Hire_Date);

    INSERT INTO Employee_Audit (
        Employee_ID,
        Name,
        Position,
        Salary,
        Hire_Date
    )
    VALUES (
        LAST_INSERT_ID(),
        p_Name,
        p_Position,
        p_Salary,
        p_Hire_Date
    );
END$$
DELIMITER ;

CALL Add_Employees('Mark Brown', 'Data Analyst', 85000.00, '2024-02-10');
CAll Add_Employees('Dywane Bravo', 'Graphic Designer', 70000, '2024-03-6');
CAll Add_Employees('David Warner', 'Finance Manager', 95000, '2024-03-10');

Select * from Employees;
Select * from Employee_Audit;