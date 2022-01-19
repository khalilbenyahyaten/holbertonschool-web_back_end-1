-- dummy comment dummy comment dummy comment
-- dummy comment dummy comment dummy comment
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80
AND ISNULL(last_meeting)
OR last_meeting < ADDDATE(CURDATE(), INTERVAL -1 MONTH);
