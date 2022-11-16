PRAGMA INTEGRITY_CHECK

CREATE TABLE IF NOT EXIST table1 (fname TEXT NOT NULL, lname TEXT NOT NULL);

INSERT INTO table1 VALUES ('John', 'Smith');
INSERT INTO table1 VALUES ('Johnson', 'Gartner');
INSERT INTO table1 VALUES ('Michael', 'Jackson');
INSERT INTO table1 VALUES ('Michael', 'Johnson');
INSERT INTO table1 VALUES ('Sam', 'Smith');
INSERT INTO table1 VALUES ('Mitchel', 'Peterson');


SELECT * FROM table1 WHERE fname IS 'Johnson';

SELECT * FROM table1 WHERE lname LIKE '%son';

SELECT rowid , fname , lname FROM table1 WHERE fname LIKE 'Mi%';

DELETE FROM table1 WHERE rowid=2;

ALTER TABLE table1 ADD COLUMN phone_number TEXT;

ALTER TABLE table1 RENAME TO old_table;

UPDATE old_table SET phone_number = '555-123-123' WHERE rowid=3;

UPDATE old_table SET phone_number = '555-555-555';