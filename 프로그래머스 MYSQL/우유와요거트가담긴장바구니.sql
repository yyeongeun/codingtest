-- 프로그래머스 lv 4 우유와 요거트가 담긴 장바구니
-- https://school.programmers.co.kr/learn/courses/30/lessons/62284

SELECT CART_ID
FROM (
    SELECT DISTINCT CART_ID, NAME
    FROM CART_PRODUCTS
    WHERE NAME IN ('Milk', 'Yogurt')
) AS C
GROUP BY CART_ID
HAVING COUNT(*) >= 2;
