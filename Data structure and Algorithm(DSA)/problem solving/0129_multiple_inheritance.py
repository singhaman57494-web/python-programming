#                          multiple inheritance

class Cemera:
    def take_photo(self):
        return "photo clicked!"

class MusicPlayer:
    def play_music(self):
        return "music playing...."

class Smartphone(Cemera, MusicPlayer):
    pass

phone = Smartphone()
print(phone.take_photo())
print(phone.play_music())
