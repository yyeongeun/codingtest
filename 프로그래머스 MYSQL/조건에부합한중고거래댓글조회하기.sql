-- 프로그래머스 LV1 조건에 부합한 중고거래 댓글 조회하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/164673

SELECT a.TITLE, a.BOARD_ID, b.REPLY_ID, b.WRITER_ID, b.CONTENTS,
    DATE_FORMAT(b.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE 
FROM USED_GOODS_BOARD a 
JOIN USED_GOODS_REPLY b
ON a.BOARD_ID = b.BOARD_ID
WHERE a.CREATED_DATE like '2022-10%'
ORDER BY b.CREATED_DATE asc, a.TITLE asc
