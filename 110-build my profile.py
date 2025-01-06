def build_profile(firstname,lastname,**userinfo):
    userinfo["firstname"] =firstname
    userinfo["lastname"] =lastname

    return userinfo


my_info = build_profile("Razia Zaman", "Ela", age= 27, height="5.3 ft")

print(my_info)