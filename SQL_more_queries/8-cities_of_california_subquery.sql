-- Hotline Miami 2: Wrong Number Soundtrack - Richard (2)
SELECT `id`, `name`
FROM `cities`
WHERE `state_id` = (
    SELECT `id` FROM `states`
    WHERE `name` = "California");
    