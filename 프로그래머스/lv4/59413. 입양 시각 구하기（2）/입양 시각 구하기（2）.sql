/*
WITH RECURSIVE(재귀 쿼리) : 가상의 테이블 저장

*/
WITH RECURSIVE TEMP AS (
    /* non-recursive 문장 : 첫 번째 루프에서만 실행*/
    SELECT 0 HOUR
    UNION
    /* recursive 문장 */
    SELECT HOUR + 1 FROM TEMP WHERE HOUR < 23
)

SELECT HOUR, IFNULL(C.COUNT, 0)
FROM TEMP 
NATURAL LEFT OUTER JOIN (
                        SELECT HOUR(DATETIME) HOUR, COUNT(*) COUNT
                        FROM ANIMAL_OUTS
                        GROUP BY HOUR
                        ORDER BY HOUR
) C
;
