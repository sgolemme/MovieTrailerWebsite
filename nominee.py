import webbrowser

class Nominee():
    def __init__(self, name, video, picture, winner):
        self.name = name
        self.video = video
        self.picture = picture
        self.winner = winner

    def show_video(self):
        webbrowser.open(self.video)

class Movie(Nominee):
    def __init__(self, name, video, picture, winner, producers, synopsis):
        Nominee.__init__(self, name, video, picture, winner)
        self.producers = producers
        self.synopsis = synopsis

class Actor(Nominee):
    def __init__(self, name, video, picture, winner, film, role, history):
        Nominee.__init__(self, name, video, picture, winner)
        self.film = film
        self.role = role
        self.history = history
    
class Category():
    def __init__(self, categoryName, nominees):
        self.categoryName = categoryName
        self.nominees = nominees
