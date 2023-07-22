# 매개변수: first_name, last_name


def print_name(first_name, last_name):
    name = first_name + last_name
    print("이름:", name)


print_name("홍", "정원")  # 인수: "홍", "정원"

# 만약


def print_name(first_name, last_name):  # 매개변수는 2개
    name = first_name + last_name
    print("이름:", name)


print_name("최")  # 인수는 1개

# 실행결과 = 에러
