-- 프로그래머스 lv 2 가격이 제일 비싼 식품의 정보 출력하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131115

SELECT *
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1;
