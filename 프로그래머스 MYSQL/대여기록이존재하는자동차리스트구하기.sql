-- 프로그래머스 lv 3 대여 기록이 존재하는 자동차 리스트 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/157341

SELECT DISTINCT(B.CAR_ID)
FROM CAR_RENTAL_COMPANY_CAR AS A
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS B
ON A.CAR_ID = B.CAR_ID
WHERE A.CAR_TYPE = "세단" AND DATE_FORMAT(START_DATE,"%m") = 10
ORDER BY B.CAR_ID DESC;
