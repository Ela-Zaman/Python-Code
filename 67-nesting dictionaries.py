users={
    'aeinstein' : {
        'first' : 'albert',
        'last'  : 'aeinstein',
        'location': "princeton"
    },
    'mcurie' : {
        'first' : "marie",
        'last'  : 'curie',
        'location': "paris"
    },
}

for username,userinfo in users.items():
    print(f"\n Username: {username}")
    fullname=f"{userinfo["first"]} {userinfo["last"]}"
    location=userinfo["location"]

    print(f"\t Full name: {fullname.title()}")
    print(f"\t Location: {location.title()}")
