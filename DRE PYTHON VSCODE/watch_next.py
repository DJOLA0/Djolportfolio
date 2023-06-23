import spacy

nlp = spacy.load('en_core_web_md')

# create a variable with the hulk description to compare
planet_hulk = "Will he save their earth or destroy it? When the hulk becomes too dangerous for the earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator"
with open("movies.txt",'r') as file:
    movies = file.readlines()

# create a function to return which movie a user would watch next
def suggestion(movies,description): # loop through all movies in list
    count = 0
    for movie in movies:
        movie_nlp = nlp(movie)
        if movie_nlp.similarity(description) > count:
            count = movie_nlp.similarity(description) # count becomes recommendation
            closest_movie = movie_nlp
            
    print(f"Because you watched Planet Hulk, we reccommend you watch {closest_movie.text}")
            

# add the planet hulk movie description to a function
suggestion(movies,nlp(planet_hulk)) # this prints the similarity with all the different movies in the list

