area_code = {"서울": "02", "부산": "051", "대구": "053", "광주": "062"}

for key in area_code:  # 반복루프레서 key는 area_code의 키를 의미
    print("%s 지역번호:%s" % (key, area_code[key]))

    # 서식: for변수 in 딕셔너리:
    # ...
    # 딕셔너리[변수]
