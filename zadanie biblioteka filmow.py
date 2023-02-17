class movies:
   def __init__(self,title,publication_date,species,number_of_plays):
     self.title=title
     self.publication_date=publication_date
     self.species=species
     self.number_of_plays=number_of_plays=0
   def __repr__(self):
     return f"(self.title,self.publication_date,self.species,self.number_of_plays)"
   def __play__(self):
     self.play_counter +=1
   def generate_views(self):
      self.play_counter *=10
      movies=title(name="Matrix",publication_date="1999")
   def __str__(self):
       return f'{self.name} {self.publication_date}'
       print(movies)       
      
class tv_series:
    def __init__(self,title,publication_date,species,episode_number,season_number,number_of_plays):
        self.title=title
        self.publication_date=publication_date
        self.species=species
        self.episode_number=episode_number    
        self.season_number=season_number  
        self.number_of_plays=number_of_plays=0
    def __repr__(self):
        return f"(self.title,publication date,species,episode_number,season_number,number_of_plays)"
    def __play__(self):
        self.play_counter +=1
        series=episode(episode_number="Game_of_throne_S01",season_number="E01")
    def __str__(self):
        return f'{self.episode_number} {self.season_number}'
        print(series)
class Library:
    def __init__(self):
        self.library =[]
    def add(self, movies):
        self.movies=movies
        self.library.append(movies)
    def add(self, series):
        self.series=series
        self.library.append(series)     
    def get_movies(self):
          return [i for i in self.library if type(i) == movies]         
    
    def get_series(self):
          return [i for i in self.library if type(i) == tv_series]
    def generator_views(self):      
          r = random.choice(self.library)
    def search(self,title):
        self.title=title
    def __repr__(self):
        title_movie = ('Matrix')
        title_tv_serie = ('Game_of_throne')

        list_of_objects = [title_movie,title_tv_serie]

        match = None
    for objects in list_of_objects:
        if objects.title == 'Matrix''Game_of_throne':
            match = objects
            break
        print(match)

        if match is not None:
            print(title.movie)
            print(title.tv_serie)    
            