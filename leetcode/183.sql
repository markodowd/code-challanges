SELECT
    name AS Customers
FROM
    Customers c1
    LEFT OUTER JOIN Orders o1 ON c1.id = o1.customerId
WHERE
    o1.id IS NULL;

