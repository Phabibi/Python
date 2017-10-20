# Assignment 4.1 F
# Cookies
# Parsa Habibi
def cookies(n):
    n=int(n)
    huge_boxes=int(n//48)
    huge_cookies=n-(huge_boxes*48)
    small_boxes=int(huge_cookies//8)
    small_cookies=huge_cookies-(small_boxes*8)
    money=(huge_boxes*26)+(small_boxes*4)-(small_cookies*2)
    total_cookies=str(huge_boxes)+'..'+str(small_boxes)+'..'+str(small_cookies)+'..'+str(money)
    return total_cookies

print (cookies(7))
