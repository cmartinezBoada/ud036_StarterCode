import media
import fresh_tomatoes

# Instances of that Python Class to represent movies
star_wars = media.Movie("Star Wars",
                        "The Imperial Forces hold Princess Leia hostage...",
                        "https://images-na.ssl-images-amazon.com/images/"
                        "I/81P3lDJbjCL._SL1347_.jpg",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k")

the_lord_of_the_rings = media.Movie("The Lord of the rings",
                                    "Frodo needs to carry the ring"
                                    "to destroy it",
                                    "https://images-na.ssl-images-amazon.com/"
                                    "images/I/51Qvs9i5a%2BL.jpg",
                                    "https://www.youtube.com/"
                                    "watch?v=Pki6jbSbXIY")
arrival = media.Movie("Arrival",
                      "Aliens arrive to the Earth,"
                      "a woman tries to learn their language",
                      "https://images-na.ssl-images-amazon.com/"
                      "images/I/71wApjGQt4L._SL1094_.jpg",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

the_shape_of_water = media.Movie("The shape of water",
                                 "A cleaning woman starts to get"
                                 "contact and interest with a "
                                 "particular monster",
                                 "https://images-na.ssl-images-amazon.com/"
                                 "images/I/61AOfZOzLCL._SL1481_.jpg",
                                 "https://www.youtube.com/watch?v=XFYWazblaUA")

blade_runner = media.Movie("Blade runner",
                           "In 2019 Los Angeles, former police"
                           "officer Rick Deckard, whose job "
                           "as a blade runner is"
                           "to track and distroy the replicats...",
                           "https://images-na.ssl-images-amazon.com/"
                           "images/I/51ZmDpb2QfL.jpg",
                           "https://www.youtube.com/watch?v=eogpIG53Cis")

manhattan = media.Movie("Manhattan",
                        "Stories of some couples in Manhattan",
                        "https://images-na.ssl-images-amazon.com/"
                        "images/I/41Wnfy6B14L.jpg",
                        "https://www.youtube.com/watch?v=Ck0ENY4eawQ")
"""List of movies to be used
by the function open_movies_page inside fresh_tomatoes."""
movies = [star_wars, the_lord_of_the_rings, arrival,
          the_shape_of_water, blade_runner, manhattan]
fresh_tomatoes.open_movies_page(movies)

