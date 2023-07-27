-- 프로그래머스 lv 4 그룹별 조건에 맞는 식당 목록 출력하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131124

SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, "%Y-%m-%d") REVIEW_DATE
FROM MEMBER_PROFILE AS M JOIN REST_REVIEW AS R
ON M.MEMBER_ID = R.MEMBER_ID
-- 가장 많이 쓴 리뷰 개수를 쓴 사람 구하기
WHERE R.MEMBER_ID IN
    (SELECT MEMBER_ID FROM REST_REVIEW GROUP BY MEMBER_ID HAVING COUNT(*) =
    	-- 가장 많이 쓴 리뷰 개수 구하기
        (SELECT MAX(CNT) FROM
        	-- 리뷰 개수 구하기
            (SELECT COUNT(*) AS CNT FROM REST_REVIEW GROUP BY MEMBER_ID) AS A
        )
     )
ORDER BY R.REVIEW_DATE ASC;
