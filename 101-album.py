def make_album(artist_name, album_title,number_of_songs=None):
    album={"name": artist_name,
           "title":album_title,}
    if number_of_songs:
        album["no_songs"] = number_of_songs
    return album
    
dictionary_1= make_album("Lany", "ILY")
print(dictionary_1)
dictionary_2 = make_album("Lauv", "Super-hero")
print(dictionary_2)
dictionary_3 = make_album("Dharshan", "Vula Dena")
print(dictionary_3)
dictionary_4 = make_album("Arijit", "kafirana", 10)
print(dictionary_4)


