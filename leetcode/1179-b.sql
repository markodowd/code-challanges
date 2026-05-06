SELECT
    id,
    SUM(revenue) FILTER (WHERE month = 'Jan') AS Jan_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Feb') AS Feb_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Mar') AS Mar_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Apr') AS Apr_Revenue,
    SUM(revenue) FILTER (WHERE month = 'May') AS May_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Jun') AS Jun_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Jul') AS Jul_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Aug') AS Aug_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Sep') AS Sep_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Oct') AS Oct_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Nov') AS Nov_Revenue,
    SUM(revenue) FILTER (WHERE month = 'Dec') AS Dec_Revenue
FROM
    Department
GROUP BY
    id;

