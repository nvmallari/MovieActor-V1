from imdb import Cinemagoer

ia = Cinemagoer()

# defining function search_movie. search_movie is a function that takes the first result out of a typed input query.
# search_movie outputs the movie ID, movie title, year of release date, plot, and 5 top actors in the movie.

def search_movie(query):
# searches movie based on keyword and prints out title and movie ID

    def goYear(e):
        return e['year']

    movies = ia.search_movie(query)

    #print(movies)
    sortedMovies = sorted(movies,key= lambda movies: movies.id,reverse=True)
    #def mySort():
        #sorting = movies.get('title')
        #titles = []
        #for trial in sorting[0:10]:
            #year = trial[year]
            #titles.append(year)
        #return titles
   # mySort = mySort()
    #return mySort
    print(sortedMovies)

    #sortedMovies = sorted(movies,key= lambda movies: movies.year,reverse=True)
    #print(mySort)
    #print(movies)
