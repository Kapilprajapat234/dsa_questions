SELECT p.product_id , COALESCE(ROUND(SUM(price * units) / SUM(units), 2) , 0 )AS average_price
FROM prices AS p
LEFT JOIN UnitsSold AS us
ON p.product_id = us.product_id and us.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;
