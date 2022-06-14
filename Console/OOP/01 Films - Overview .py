class Film:
    def __init__(self, title, director, date, imdbscore, rottenscore):
        self.title = title
        self.director = director
        self.date = date
        self.imdbscore = imdbscore
        self.rottencore = rottenscore
        self.real = None

    def realscore(self):
        self.real = (self.imdbscore + self.rottencore / 10) / 2
        return self.real

    def dogtag(self):
        #self.realscore()
        dogtag = "The film " + self.title + " was directed by " + self.director + " and was released in " + self.date + \
                 ". its imdb score is " + str(self.real)
        return dogtag
    def __repr__(self):
        return "{}, {}, {}, {}, {} hell yeah".format(self.title, self.director, self.date, self.imdbscore, self.rottencore)

    def __add__(self, other):
        return self.imdbscore + other.imdbscore



film1 = Film("The Shining", "Stanley Kubrick", "1980", 8.4, 95)
film2 = Film("'Andrei Rublev'", "Andrei Tarkovsky", "1966", 8.1, 87)
film3 = Film("Persona", "Ingmar Bergman", "1966", 8.1, 99)
#print(film3.realscore())
#print(film3.dogtag())
print(film3)
#print(film3 + film2)
#print(film2.dogtag())