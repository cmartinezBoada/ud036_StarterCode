import webbrowser


# Python class to store the movies information
class Movie():

    # Class constructor
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Method to play the movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer)

