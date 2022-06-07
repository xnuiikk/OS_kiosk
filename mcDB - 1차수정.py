import sqlite3
con=sqlite3.connect("mcDB")
cur=con.cursor()

#카테고리별로 테이블 분류함
cur.execute("create table burgerTable (menuName char(20), price int, calData char(8), menuID int)")
cur.execute("create table sideTable (menuName char(20), price int, calData char(8), menuID int)")
cur.execute("create table drinkTable (menuName char(20), price int, calData char(8), menuID int)") #음료안에 맥카페 포함
cur.execute("create table dessertTable (menuName char(20), price int, calData char(8), menuID int)")
cur.execute("create table mcmorningTable (menuName char(20), price int, calData char(8), menuID int)")
cur.execute("create table happymealTable (menuName char(20), price int, calData char(8), menuID int)")
cur.execute("create table happysnackTable (menuName char(20), price int, calData char(8), menuID int)")

'''
menuID _ _ _ _

1 : 카테고리 분류코드
2 : 카테고리 내 분류코드
3,4 : 메뉴코드(카테고리 내 순서대로 부여)

카테고리 분류코드
- 버거 : 1
- 사이드 : 2
- 드링크 : 3
- 디저트 : 4
- 맥모닝 : 5
- 해피밀 : 6
- 해피스낵 : 7

카테고리 내 분류코드 / 카테고리 내 분류코드가 바뀌면 제품번호 다시 1부터 ex) 1001...~1013 후 1101부터 시작
0, 1
디저트 : 0(아이스크림) 1(파이류)
드링크 : 0(음료) 1(맥카페)

'''

#버거 및 세트
cur.execute("insert into burgerTable values('햄버거', 2000, '265Kcal', 1001)")
cur.execute("insert into burgerTable values('치즈버거', 2300, '317Kcal', 1002)")
cur.execute("insert into burgerTable values('더블치즈버거', 4400, '478Kcal', 1003)")
cur.execute("insert into burgerTable values('트리플치즈버거', 5600, '619Kcal', 1004)")
cur.execute("insert into burgerTable values('쿼터파운더 치즈', 5200, '534Kcal', 1005)")
cur.execute("insert into burgerTable values('더블 쿼터파운더 치즈', 7000, '769Kcal', 1006)")
cur.execute("insert into burgerTable values('베이컨 토마토 디럭스', 5500, '545Kcal', 1007)")
cur.execute("insert into burgerTable values('슈슈 버거', 4500, '432Kcal', 1008)")
cur.execute("insert into burgerTable values('슈비 버거', 5500, '563Kcal', 1009)")
cur.execute("insert into burgerTable values('불고기 버거', 2200, '409Kcal', 1010)")
cur.execute("insert into burgerTable values('더블 불고기 버거', 4400, '636Kcal', 1011)")
cur.execute("insert into burgerTable values('에그 불고기 버거', 3200, '492Kcal', 1012)")
cur.execute("insert into burgerTable values('맥치킨', 3300, '483Kcal', 1013)")
cur.execute("insert into burgerTable values('맥치킨 모짜렐라', 4800, '686Kcal', 1014)")
cur.execute("insert into burgerTable values('빅맥', 4600, '583Kcal', 1015)")
cur.execute("insert into burgerTable values('1955버거', 5700, '537Kcal', 1016)")
cur.execute("insert into burgerTable values('맥스파이스 상하이 버거', 4600, '494Kcal', 1017)")
cur.execute("insert into burgerTable values('필레 오 피쉬', 3500, '342Kcal', 1018)")
cur.execute("insert into burgerTable values('더블 필레 오 피쉬', 5000, '481Kcal', 1019)")
cur.execute("insert into burgerTable values('맥크리스피 클래식 버거', 5600, '584Kcal', 1020)")
cur.execute("insert into burgerTable values('맥크리스피 디럭스 버거', 6400, '594Kcal', 1021)")

#사이드
cur.execute("insert into sideTable values('맥너겟 4조각', 1800, '2001)")
cur.execute("insert into sideTable values('맥너겟 6조각', 2500, 2002)")
cur.execute("insert into sideTable values('맥너겟 10조각', 4500, 2003)")
cur.execute("insert into sideTable values('맥스파이시 치킨텐더 2조각', 2500, '176Kcal', 2004)")
cur.execute("insert into sideTable values('맥스파이시 치킨텐더 4조각', 4900, '352Kcal', 2005)")
cur.execute("insert into sideTable values('골든 모짜렐라 치즈스틱 2조각', 2200, 2006)")
cur.execute("insert into sideTable values('골든 모짜렐라 치즈스틱 4조각', 4000, 2007)")
cur.execute("insert into sideTable values('후렌치 후라이 S', 1000, 2008)")
cur.execute("insert into sideTable values('후렌치 후라이 M', 1700, 2009)")
cur.execute("insert into sideTable values('후렌치 후라이 L', 2300, 2010)")
cur.execute("insert into sideTable values('상하이 치킨 스낵랩', 2000, 2011)")
cur.execute("insert into sideTable values('소시지 스낵랩', 2100, 2012)")
cur.execute("insert into sideTable values('스위트 칠리 소스', 300, 2013)")
cur.execute("insert into sideTable values('스위트 앤 사워 소스', 300, 2014)")
cur.execute("insert into sideTable values('케이준 소스', 300, 2015)")
cur.execute("insert into sideTable values('스트링치즈', 1600, '50Kcal', 2017)")

#음료
cur.execute("insert into drinkTable values('생수', 1200, 3001)")
cur.execute("insert into drinkTable values('우유', 1500, 3002)")
cur.execute("insert into drinkTable values('바닐라 쉐이크 M', 2500, 3003)")
cur.execute("insert into drinkTable values('딸기 쉐이크 M', 2500, 3004)")
cur.execute("insert into drinkTable values('초코 쉐이크 M', 2500, 3005)")
cur.execute("insert into drinkTable values('자두 칠러 S', 2000, 3006)")
cur.execute("insert into drinkTable values('자두 칠러 M', 2700, 3007)")
cur.execute("insert into drinkTable values('자두 칠러 L', 3700, 3008)")
cur.execute("insert into drinkTable values('애플망고 칠러 S', 2000, 3009)")
cur.execute("insert into drinkTable values('애플망고 칠러 M', 2700, 3010)")
cur.execute("insert into drinkTable values('애플망고 칠러 L', 3700, 3011)")
cur.execute("insert into drinkTable values('제주 한라봉 칠러 S', 2000, 3012)")
cur.execute("insert into drinkTable values('제주 한라봉 칠러 M', 2700, 3013)")
cur.execute("insert into drinkTable values('제주 한라봉 칠러 L', 3700, 3014)")
#쉐이크는 m사이즈만 존재, 칠러는 걍 사이즈별로 나눠서 써놓음
#그 외 음료는 기본m사이즈에 사이즈업시 +-500원씩 적용
cur.execute("insert into drinkTable values('코카 콜라 M', 1300, 3015)")
cur.execute("insert into drinkTable values('코카 콜라 제로 M', 1300, 3016)")
cur.execute("insert into drinkTable values('스프라이트 M', 1300, 3017)")
cur.execute("insert into drinkTable values('환타 M', 1300, 3018)")
cur.execute("insert into drinkTable values('체리 맥피즈 스프라이트 M', 1900, 3019)")
cur.execute("insert into drinkTable values('체리 맥피즈 콜라 M', 1900, 3020)")

#음료-맥카페
cur.execute("insert into drinkTable values('아메리카노 M', 2200, 3101)")
cur.execute("insert into drinkTable values('디카페인 아메리카노 M', 2300, 3102)")
cur.execute("insert into drinkTable values('아이스 아메리카노 M', 2200, 3103)")
cur.execute("insert into drinkTable values('디카페인 아이스 아메리카노 M', 2300, 3104)")
cur.execute("insert into drinkTable values('에스프레소', 1500, 3105)")
cur.execute("insert into drinkTable values('디카페인 에스프레소', 1600, 3106)")
cur.execute("insert into drinkTable values('카페라떼 M', 2500, 3107)")
cur.execute("insert into drinkTable values('디카페인 카페라떼 M', 2600, 3108)")
cur.execute("insert into drinkTable values('아이스 카페라떼 M', 2500, 3109)")
cur.execute("insert into drinkTable values('디카페인 아이스 카페라떼 M', 2600, 3110)")
cur.execute("insert into drinkTable values('드립 커피 M', 1500, 3111)")
cur.execute("insert into drinkTable values('아이스 드립 커피 M', 1000, 3112)")
cur.execute("insert into drinkTable values('카푸치노 M', 2500, 3113)")
cur.execute("insert into drinkTable values('디카페인 카푸치노 M', 2600, 3114)")

#디저트
cur.execute("insert into dessertTable values('베리스트로베리 맥플러리', 2500, 4001)")
cur.execute("insert into dessertTable values('허쉬 프레첼 맥플러리', 2900, 4002)")
cur.execute("insert into dessertTable values('오레오 맥플러리', 2500, 4003)")
cur.execute("insert into dessertTable values('딸기 오레오 맥플러리', 2500, 4004)")
cur.execute("insert into dessertTable values('초코 오레오 맥플러리', 2500, 4005)")
cur.execute("insert into dessertTable values('오레오 아포가토', 3000, 4006)")
cur.execute("insert into dessertTable values('아이스크림콘', 700, 4007)")
cur.execute("insert into dessertTable values('초코콘', 900, 4008)")
cur.execute("insert into dessertTable values('스트로베리콘', 900, 4009)")
cur.execute("insert into dessertTable values('초코 선데이 아이스크림', 1500, 4010)")
cur.execute("insert into dessertTable values('딸기 선데이 아이스크림', 1500, 4011)")
cur.execute("insert into dessertTable values('바닐라 선데이 아이스크림', 1500, 4012)")
cur.execute("insert into dessertTable values('애플 파이', 1200, 4101)")
cur.execute("insert into dessertTable values('콘파이 파이', 1200, 4102)")
cur.execute("insert into dessertTable values('블루베리 파이', 1200, 4103)")
cur.execute("insert into dessertTable values('타로 파이', 1200, 4104)")
cur.execute("insert into dessertTable values('리치초콜릿 파이', 1200, 4105)")


#맥모닝
cur.execute("insert into mcmorningTable values('핫케익 2조각', 2300, 5001)")
cur.execute("insert into mcmorningTable values('핫케익 3조각', 3000, 5002)")
cur.execute("insert into mcmorningTable values('디럭스 브렉퍼스트', 4800, 5003)")
cur.execute("insert into mcmorningTable values('디럭스 브렉퍼스트 세트', 5800, 5004)")
cur.execute("insert into mcmorningTable values('상하이 치킨 스낵랩', 1500, 5005)")
cur.execute("insert into mcmorningTable values('소시지 에그 맥머핀', 3000, 5006)")
cur.execute("insert into mcmorningTable values('소시지 에그 맥머핀 콤보', 3400, 5007)")
cur.execute("insert into mcmorningTable values('소시지 에그 맥머핀 세트', 4000, 5008)")
cur.execute("insert into mcmorningTable values('베이컨 에그 맥머핀', 3000, 5009)")
cur.execute("insert into mcmorningTable values('베이컨 에그 맥머핀 콤보', 3400, 5010)")
cur.execute("insert into mcmorningTable values('베이컨 에그 맥머핀 세트', 4000, 5011)")
cur.execute("insert into mcmorningTable values('에그 맥머핀', 2500, 5012)")
cur.execute("insert into mcmorningTable values('에그 맥머핀 콤보', 2900, 5013)")
cur.execute("insert into mcmorningTable values('에그 맥머핀 세트', 3500, 5014)")
cur.execute("insert into mcmorningTable values('치킨 치즈 머핀', 3200, 5015)")
cur.execute("insert into mcmorningTable values('치킨 치즈 머핀 세트', 4200, 5016)")
cur.execute("insert into mcmorningTable values('베이컨 토마토 에그 머핀', 3600, 5017)")
cur.execute("insert into mcmorningTable values('베이컨 토마토 에그 머핀 세트', 4500, 5018)")
cur.execute("insert into mcmorningTable values('소시지 토마토 에그 소프트 번', 3800, 5019)")
cur.execute("insert into mcmorningTable values('소시지 토마토 에그 소프트 번 세트', 4800, 5020)")
cur.execute("insert into mcmorningTable values('베이컨 토마토 에그 소프트 번', 3600, 5021)")
cur.execute("insert into mcmorningTable values('베이컨 토마토 에그 소프트 번 세트', 4600, 5022)")

#해피밀
cur.execute("insert into happymealTable values('해피밀 에그 맥머핀', 3500, 6001)")
cur.execute("insert into happymealTable values('해피밀 베이컨 에그 맥머핀', 3800, 6002)")
cur.execute("insert into happymealTable values('해피밀 소시지 에그 맥머핀', 3800, 6003)")
cur.execute("insert into happymealTable values('해피밀 핫케익 2조각', 3800, 6004)")

#해피스낵
cur.execute("insert into happysnackTable values('아이스 아메리카노 L', 2400, 7001)")
cur.execute("insert into happysnackTable values('치즈버거', 2300, 7002)")
cur.execute("insert into happysnackTable values('에그 불고기 버거', 2500, 7003)")
cur.execute("insert into happysnackTable values('골든 모짜렐라 치즈스틱 2조각', 1500, 7004)")
cur.execute("insert into happysnackTable values('필레 오 피쉬', 2500, 7005)")
cur.execute("insert into happysnackTable values('소시지 스낵랩', 2400, 7006)")
cur.execute("insert into happysnackTable values('체리 맥피즈 스프라이트 M', 1900, 7007)")
cur.execute("insert into happysnackTable values('체리 맥피즈 콜라 M', 1900, 7008)")


con.commit()
con.close()