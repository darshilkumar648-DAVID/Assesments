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
CREATE TRIGGER After_Employee_Insert
AFTER INSERT ON Employees
FOR EACH ROW
BEGIN
    INSERT INTO Employee_Audit (
        Employee_ID,
        Name,
        Position,
        Salary,
        Hire_Date
    )
    VALUES (
        NEW.Employee_ID,
        NEW.Name,
        NEW.Position,
        NEW.Salary,
        NEW.Hire_Date
    );
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE Add_Employee (
    IN p_Name VARCHAR(100),
    IN p_Position VARCHAR(100),
    IN p_Salary DECIMAL(10,2),
    IN p_Hire_Date DATE
)
BEGIN
    DECLARE last_emp_id INT;
    -- Insert into Employees table
    INSERT INTO Employees (Name, Position, Salary, Hire_Date)
    VALUES (p_name, p_position, p_salary, p_hire_date);
    -- Get the newly inserted Employee_ID
    SET last_emp_id = LAST_INSERT_ID();
    -- Insert into Employee_Audit table
    INSERT INTO Employee_Audit (
        Employee_ID,
        Name,
        Position,
        Salary,
        Hire_Date
    )
    VALUES (
        last_emp_id,
        p_name,
        p_position,
        p_salary,
        p_hire_date
    );
END$$
DELIMITER ;

CALL Add_Employee('Mark Brown', 'Data Analyst', 85000.00, '2024-02-10');
CAll Add_Employee('Dywane Bravo', 'Graphic Designer', 70000, '2024-03-6');

Select * from Employees;
Select * from Employee_Audit;