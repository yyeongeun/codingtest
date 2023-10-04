-- 프로그래머스 lv 4 헤비 유저가 소유한 장소
-- https://school.programmers.co.kr/learn/courses/30/lessons/77487

SELECT * FROM PLACES
WHERE HOST_ID IN(
    SELECT HOST_ID FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(ID) >= 2
)
ORDER BY ID ASC;
