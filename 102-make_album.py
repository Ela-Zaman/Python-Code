def make_album(artist_name,title):
    dictionary={"name" : artist_name,
                "title": title,}
    return dictionary






while True:
    print("\n Please Enter Album'artist name and title")
    print("\n Enter quit to terminate the program")
    albums_artist = input("Artist name")
    if albums_artist == "quit":
        break
    albums_title = input("title")
    if albums_title == "quit":
        break
    dictionary=make_album(albums_artist,albums_title)
    print("This is your dictionary : \n",dictionary)
