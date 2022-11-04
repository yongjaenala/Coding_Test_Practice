-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N')
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID ASC;

-- 패턴 일치 LIKE
-- '%' 패턴 : 공백 OR 한 글자 이상
--변수 LIKE %패턴% : '패턴' 포함
--변수 LIKE %패턴 : '패턴'으로 끝남
--변수 LIKE 패턴% : '패턴'으로 시작

-- '_' 패턴 : 한 글자
--변수 LIKE _패턴_ : 한 글자 + '패턴'+ 한 글자
--변수 LIKE _패턴 : 한 글자 + '패턴'
--변수 LIKE 패턴_ : '패턴'+ 한 글자
