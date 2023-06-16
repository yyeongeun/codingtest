-- 프로그래머스 lv 2 진료과별 총 예약 횟수 출력하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/132202

SELECT MCDP_CD AS '진료과코드', COUNT(MCDP_CD) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD
ORDER BY COUNT(MCDP_CD) ASC, MCDP_CD ASC
