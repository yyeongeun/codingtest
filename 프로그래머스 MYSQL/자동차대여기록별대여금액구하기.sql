-- 프로그래머스 lv 4 자동차 대여 기록 별 대여 금액 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/151141

SELECT HISTORY_ID,
ROUND(DAILY_FEE*
    (CASE
     WHEN DATEDIFF(END_DATE,START_DATE)+1 < 7 THEN 1
     WHEN DATEDIFF(END_DATE,START_DATE)+1 < 30 THEN 0.95
     WHEN DATEDIFF(END_DATE,START_DATE)+1 < 90 THEN 0.92
     ELSE 0.85
     END)
     *(DATEDIFF(END_DATE,START_DATE)+1)) AS FEE

FROM CAR_RENTAL_COMPANY_CAR AS A
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS B
ON A.CAR_ID = B.CAR_ID
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS C
ON A.CAR_TYPE = C.CAR_TYPE

WHERE C.CAR_TYPE = "트럭"
GROUP BY HISTORY_ID
ORDER BY FEE DESC, HISTORY_ID DESC;
