SELECT
    name,
    greeting,
    regexp_replace(greeting, '.*#([0-9]+)', '\1') AS user_id
FROM
    greetings;

