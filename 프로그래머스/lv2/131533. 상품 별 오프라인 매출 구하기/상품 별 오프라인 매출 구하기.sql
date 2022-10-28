SELECT P.PRODUCT_CODE, (O.AMOUNT * P.PRICE) AS SALES
FROM PRODUCT P
JOIN (
        SELECT PRODUCT_ID, SUM(SALES_AMOUNT) AS AMOUNT 
        FROM OFFLINE_SALE 
        GROUP BY PRODUCT_ID
) O
ON P.PRODUCT_ID = O.PRODUCT_ID
ORDER BY SALES DESC, P.PRODUCT_CODE;