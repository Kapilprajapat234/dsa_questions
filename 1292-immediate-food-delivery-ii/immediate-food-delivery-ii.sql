SELECT round(im / total * 100 , 2 ) AS immediate_percentage 
FROM (
    SELECT
        SUM(order_date = customer_pref_delivery_date) AS im,
        COUNT(delivery_id) AS total
    FROM (
        SELECT
            *,
            RANK() OVER (
                PARTITION BY customer_id
                ORDER BY order_date
            ) AS rnk
        FROM Delivery
    ) t
    WHERE rnk = 1
) x;