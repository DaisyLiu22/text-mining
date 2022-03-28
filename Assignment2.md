1. Project Overview [~1 paragraph] What data source(s) did you use and what technique(s) did you use analyze/process them? What did you hope to learn/create?

    The data source I used was IMDB movie reviews. I analyzed the first movie review from the user's search of movies. I hope to learn the frequency of words by in the reivew.

2. Implementation [~2-3 paragraphs] Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice you did.

    First of all, I acquired the data from IMDB using the code given in the instructions. I wrapped the code into the functionmovie_search() and changed it in a way that allows users to search for a movie to see its first review by inputting a movie name. After the user input a movie name, the movie ID will be generated to return the movie review. It returns a string. After that, I cleaned up the punctuations and turned upper-cased letters into lower-cased, and created a word list. Last but not least, I converted the word list into a dictionary and counted the frequency of words as the value. The final output is to print the frequency of words with keys and values in a descending order based on values.

3. Results [~2-3 paragraphs + figures/examples] Present what you accomplished:

If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

    From the frequency of words on movie reviews, I found that people tend to summarize the movie rather than commenting. Although there are word indicators of good and bad, in general, movie reviews are much more sophisticated and less straight-forward than product reviews.

4. Reflection [~1 paragraph] From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for testing? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?

    I had a hard time picking a data source at first. However, I was able to identify the one that interests me and that I can handle well. I tried other data source as well, but ended up ditching because I could not handle it well. I was able to make a connection between the data source and text analysis. 