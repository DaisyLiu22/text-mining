from imdb import Cinemagoer
from collections import defaultdict

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# search movie


def movie_search():
    """Prompt the user to input a movie they would like to see reviews about.
    Prints the first movie review in a string"""
    search_movie = input(
        "Which movie would you like to search reviews about? ")
    movie = ia.search_movie(search_movie)[0]
    movie_reviews = ia.get_movie_reviews(movie.movieID)
    return movie_reviews['data']['reviews'][0]['content']


# Inspired by our class material lyrics.py
def histogram(word_list):
    """convert a word list to a dictionary counting words"""
    d = dict()
    for word in word_list:
        d[word] = d.get(word, 0) + 1
    return d


def print_hist(h):
    """print items in a dictionary"""
    for c in h:
        print(c[0], c[1])


def print_reviews_hist():
    """print word frequency in movie review and output result to a text file"""
    text = movie_search()
    reviews = text.lower()
    reviews = (
        reviews.replace(',', ' ')
        .replace('-', ' ')
        .replace('(', ' ')
        .replace(')', ' ')
        .replace('!', ' ')
        .replace('.', ' ')
        .replace('"', ' ')
    )
    word_list = reviews.split()
    h = histogram(word_list)
    h = sorted(h.items(), key=lambda word: word[1], reverse=True)
    print_hist(h)


def main():
    print_reviews_hist()


if __name__ == "__main__":
    main()
