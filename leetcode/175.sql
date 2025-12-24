SELECT
    person.firstName,
    person.lastName,
    addr.city,
    addr.state
FROM
    Person person
    LEFT JOIN Address addr ON person.personId = addr.personId;

