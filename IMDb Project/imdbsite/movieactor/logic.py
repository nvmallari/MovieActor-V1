from imdb import Cinemagoer
#from movieactor.views import movieactor_home
ia = Cinemagoer()

# defining function search_movie. search_movie is a function that takes the first result out of a typed input query.
# search_movie outputs the movie ID, movie title, year of release date, plot, and 5 top actors in the movie.

def search_movie(query):
# searches movie based on keyword and prints out title and movie ID
    #movies = ia.search_movie(query, results=10)
    #result = movies[0:10]
    movies = ia.search_movie(query)
    result = movies[0]
    movie = ia.get_movie(result.movieID)
    #movieList = []
    #for i in result:
        #movie = ia.get_movie(i.movieID)
        #movieList.append(movie)
    #return movieList
    #print(movieList)
   
# prints movie cast and role
    #def cast(movieQuery):
    def cast():
        #casting = movieQuery.get('cast')
        casting = movie.get('cast')
        actors = []
        for actor in casting[0:10]:
            name = actor['name']
            actors.append(name)
        return actors
    cast = cast()
    return cast
    #supercast=[[]]
    #for i in movieList:
        #supercast.append(cast(i))
    #return supercast
    #print(supercast)

# ask() function. prompts user to type two inputs.
def ask(query1, query2):
    search_movie(query1)
    search_movie(query2)
    castA = search_movie(query1)
    castB = search_movie(query2)
    return castA, castB

# compare() function. takes two lists of actors and compares to find intersecting (common) actor.
def compare(a, b):
    common = set(a).intersection(b)
    print("Common actor: "+ str(common))
    return common

movieA = str("")
movieB = str("")



# crossReference() function. Takes intersecting value of two lists(commonActor), and looks up actor again into Cinemagoer via personID.
def crossReference(commonActor):
    imdbActor = ia.search_person(commonActor)
    foundActor = imdbActor[0]
    chosenActor = ia.get_person(foundActor.personID)
    actorName = chosenActor['name']
    actorBirth = chosenActor['birth date']
    print("Common actor: " + actorName + ", " + "Date of Birth: " + actorBirth)
    print("Filmography:")
    actorJobs = []
    for job in chosenActor['filmography'].keys():
        jobRoles = []
        print('# Job: ', job, '--------------------------------------------------------------------------------------------------------')
        for works in chosenActor['filmography'][job]:
            #jobRoles.append(works)
            specificRole = ('%s (role: %s)' % (works['title'], works.currentRole))
            jobRoles.append(specificRole)
            print(specificRole)
        actorJobs.append(jobRoles)
    return actorJobs

if movieA and movieB != str(""):
    castA, castB = ask(movieA, movieB)
    thatOneActor = compare(castA, castB)
    crossReference(thatOneActor)







# Notes:
# Search any movie: birdbox
# 11307514
# Birdbox
# Traceback (most recent call last):
#  File "test.py", line 31, in <module>
#    ask()
#  File "test.py", line 29, in ask
#    ask()
#  File "test.py", line 29, in ask
#    ask()
#  File "test.py", line 29, in ask
#    ask()
#  File "test.py", line 28, in ask
#    search_movie(query)
#  File "test.py", line 16, in search_movie
#    plot = movie['plot'][0]
#  File "/Users/nickmallari/Library/Python/3.7/lib/python/site-packages/imdb/utils.py", line 1506, in __getitem__
#    rawData = self.data[key]
#KeyError: 'plot'
#nickmallari@MacBook-Air-2 IMDb Project % 
# Figure out what happened



