-- 프로그래머스 LV 3 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/164671

SELECT 
CONCAT("/home/grep/src/",B.BOARD_ID,"/",B.FILE_ID,B.FILE_NAME,B.FILE_EXT) 
AS FILE_PATH

FROM USED_GOODS_BOARD AS A
JOIN USED_GOODS_FILE AS B
ON A.BOARD_ID = B.BOARD_ID
WHERE VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY B.FILE_ID DESC;
