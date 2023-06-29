-- 프로그래머스 lv 3 조건별로 분류하여 주문상태 출력하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131113

SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE,"%Y-%m-%d") AS OUT_DATE, 
CASE 
WHEN DATE_FORMAT(OUT_DATE,"%Y-%m-%d") <= "2022-05-01" THEN "출고완료"
WHEN DATE_FORMAT(OUT_DATE,"%Y-%m-%d") > "2022-05-01" THEN "출고대기"
ELSE "출고미정"
END
AS "출고여부"

FROM FOOD_ORDER
ORDER BY ORDER_ID;
