import webbrowser  # import webbrowser python's lib

class Movie():  
    
    def __init__(self, movie_title, movie_storie,
                 poster_image, trailer_youtube_url):  # Defining init function
                self.title= movie_title  # Attributin movie's instances data
                self.storie = movie_storie
                self.poster_image_url= poster_image
                self.trailer_youtube_url= trailer_youtube_url


