import lyricsgenius
artist = input("Enter artist:") 
song = input("Enter Song Name:")
genius = lyricsgenius.Genius("j-cudRyJRuE-qo9xLK7vjZg8WkFFUGj7tVQ6q3yBxn7UxmuHQ6M1M372cM498Pkw")
artist = genius.search_artist(artist, max_songs=0, sort="title")
song = artist.song(song)
song.save_lyrics(filename="lyrics", extension="txt", overwrite=True, verbose=False)


goodwords = ["happy","love","good","dance","god","thank","promiscuous","fun","beautiful","entrusted","guap","excitin","exciting","diamonds","thank god","roll","opps","shawty","blowin'","runnin","party","sunflower"]
badwords = ["red-handed","creeping","lost","alone","killer","It's the pain pills","downfall","confusion","suffer","bleed","beat", "hate you","remember","dying","dyin'","cruel","unkind","Poppin' pills"]
file = open('lyrics.txt')
s=" "
happy = 0
sad = 0
L= file.readlines()

for i in L:
        L2=i.split()
        for j in goodwords:
            if j in L2:
              happy =+ 1
for i in L:
        L2=i.split()
        for j in badwords:
            if j in L2:
             sad =+ 1

if happy > sad:
    print("This song is sad")
elif sad > happy:
    print("This song is happy")
