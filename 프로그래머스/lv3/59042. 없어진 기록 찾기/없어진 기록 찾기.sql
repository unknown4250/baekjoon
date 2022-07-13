-- 입양 기록 O, 보호소 입소 기록 X (IN ANIMAL_INS, NOT IN ANIMAL_OUTS)
SELECT ANIMAL_ID, NAME
FROM ANIMAL_OUTS
WHERE ANIMAL_ID NOT IN (SELECT DISTINCT(ANIMAL_ID) FROM ANIMAL_INS);