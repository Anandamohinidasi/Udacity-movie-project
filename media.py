import webbrowser  # import webbrowser python's lib

class Movie():  # Creating Movie() Class
    def __init__(self, movie_title, poster_image, 
                 trailer_youtube_url):  # Defining init function
        self.title= movie_title  # Attributin movie's instances data
        self.poster_image_url= poster_image
        self.trailer_youtube_url= trailer_youtube_url

