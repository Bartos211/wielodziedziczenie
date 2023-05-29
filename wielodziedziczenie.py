import random

class Movies:
    def __init__(self,title,publication_date,species,number_of_plays):
        self.title=title
        self.publication_date=publication_date
        self.species=species
        self.number_of_plays=number_of_plays

    def play(self):
        self.play_counter+=1

    def __repr__(self):
        return f"{self.title} {self.publication_date}"
    
    def __str__(self):
        return f"{self.title} {self.publication_date}"


information1=Movies(title="Matrix",publication_date=1999,species="sc_fi",number_of_plays="1010")
if isinstance(information1,Movies):
     print("To jest obiekt klasy Movies")
print(information1)    

class Tv_series(Movies):
    def __init__(self,title,publication_date,species,episode_number,season_number,number_of_plays):
        super().__init__(title,publication_date,species,number_of_plays)    
        self.season_number=season_number  
        self.episode_number=episode_number
    def play(self):
       self.play_counter+=1

    def generate_views(self):
        self.playcounter *=10

    def __repr__(self):
        return f"{self.season_number} {self.episode_number}"

    def __str__(self):
        return f"{self.season_number} {self.episode_number}"
information2= Tv_series(season_number="S01 Game Of Thrones",episode_number="E01",title="Game Of Thrones",publication_date="2011",species="sc_fi",number_of_plays="1000")
if isinstance(information2,Tv_series):
    print("To jest obiekt klasy Tv_series")
print(information2) 
            
class Library:
    def __init__(self):
        self.library =[]
    def add(self,item):
        self.library.append(item)
    def get_movies(self):
        temp = []
        for item in self.library:
            if isinstance(item,Movies):
                temp.append(item)
        return temp

    def get_series(self):
        temp2 = []
        for item in self.library:
            if isinstance(item,Tv_series):
                temp2.append(item)
        return temp2
    
movie1 = Movies(title="Matrix",publication_date=1999,species="sc_fi",number_of_plays="1010")
library= Library()
library.add(movie1)

movie2 = Movies(title="John Wick",publication_date=2014,species="action",number_of_plays="2015")
library= Library()
library.add(movie2)

tv_serie = Tv_series(season_number="S01 Game Of Thrones",episode_number="E01",title="Game Of Thrones",publication_date="2011",species="sc_fi",number_of_plays="1000")
library= Library()
library.add(tv_serie)



print(library.library)


def generate_views(self):
    random.choice(self.library)
  
Title1=["Matrix","John Wick","Predator"]
Title2=["Game Of Thrones","Vikingowie","The Walking Dead"]
def search():
    for i in Title1:
        print(i)

for i in Title2:
        print(i)

name_iterator = iter(Title1)
print(name_iterator)
for i in name_iterator:
        print(i)