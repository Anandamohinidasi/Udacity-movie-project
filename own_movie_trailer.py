import fresh_tomatoes  # import fresh_tomatoes for the html generating 
import media  # import media file that contais Movie Class

# Creating the Movie instacens
harry_potter= media.Movie("Harry Potter", 
                          "http://4.bp.blogspot.com/_roE7T9-gJ1M/S7yeL896gZI/AAAAAAAABVA/BeLZ7rLiliU/s1600/harry-potter-poster01.jpg",  # N0QA
                          "https://www.youtube.com/watch?v=nIkfYVetF0g") 
arjun = media.Movie("Arjun The Warrior Prince", 
                    "http://www.gstatic.com/tv/thumb/movieposters/9260078/p9260078_p_v8_aa.jpg",  # N0QA
                    "https://www.youtube.com/watch?v=VKeCBO11-Mo") 
piratas_do_caribe= media.Movie("Pirates of Caribean", 
                               "https://www.rvxfilmesonline.com/wp-content/uploads/2015/07/20304627.jpg-r_640_600-b_1_D6D6D6-f_jpg-q_x-xxyxx.jpg",  # N0QA
                               "https://www.youtube.com/watch?v=JvFx5cU3Sy8")  # N0QA
grande_truque= media.Movie("The Prestige",
                           "https://i.jeded.com/i/the-prestige.14577.jpg",
                "https://www.youtube.com/watch?v=X_taFutSQHw")
narnia= media.Movie("The Chronicles of Narnia",
         "https://image.tmdb.org/t/p/original/l8RKDgjl9co0IgFZblxhtIOi5Uj.jpg",  # N0QA
         "https://www.youtube.com/watch?v=pYcGFLgJ8Uo")
shaun= media.Movie("Shaun the Sheep",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BOTc1ODY5MTQ1Nl5BMl5BanBnXkFtZTgwMDM5ODI1NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # N0QA
        "https://www.youtube.com/watch?v=E6qLSo9RsaE")

# putting instacens into movies array, to be called in fresh_tomatoes methods
movies=[arjun, harry_potter, piratas_do_caribe, grande_truque, narnia, shaun]
# calling fresh tomatoes method for open the movies in the 'movies array'
fresh_tomatoes.open_movies_page(movies)
