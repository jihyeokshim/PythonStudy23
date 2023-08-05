eng_dict = {
    "house": "집",
    "piano": "피아노",
    "christmas": "크리스마스",
    "friend": "친구",
    "bread": "빵",
}


def english(a):
    if a == item:
        return True
    else:
        return False


for item in eng_dict:
    ans = eng_dict[item]
    s = input("%s에 맞는 영어단어는?" % ans)
    if english(s) == True:
        print("참 잘했어요!")
    else:
        print("틀렸어요!")
