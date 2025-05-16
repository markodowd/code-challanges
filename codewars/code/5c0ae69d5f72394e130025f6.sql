SELECT
    name,
    greeting,
    SUBSTRING(greeting FROM '#([0-9]+)') AS user_id
FROM
    greetings;

