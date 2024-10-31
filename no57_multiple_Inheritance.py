class dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"the dance is : {self.dance}")

class singer:
    def __init__(self,song):
        self.song = song
    def show(self):
        print(f"the song is : {self.song}")

class dancerSinger(singer,dancer):
    def __init__(self, dance, song):
        self.dance = dance
        self.song = song

ds = dancerSinger("kathak","indian song")
ds.show()
print(dancerSinger.mro()) # it print if a method is call using this class so in which order it have serch this method