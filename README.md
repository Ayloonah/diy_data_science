HOW TO USE: First, make sure that all the files are in the same folder. If you just want to test out the code, keep the .json file in there as it will bypass the web scraping portion of the code. 
            If you would like to use the code in its entirety including the web scraping portion of it, delete the .json file before you start, but noteed that the code will take around 10 minutes to run in this way.
            The html file is there for a preview of the code's results.
            This code makes use of the following libraries: pathlib, plotly, numpy, bs4, requests_html, re, urllib.request, alive_progress, json.
            When you're ready to run the program, run diy_data_science.py.
            Note that running the program will generate an html file as well as a .json file (if ran without one).

Hello,

For my introduction to programming class in college, I was given the task to use Python code to create an illustration, or visualization of some data I collect. It could be any kind of data presented using any form of data visualization I deemed fit.

What I have decided on was to use competitive Pokemon card decks. More specifically, I looked up the winner decks for the last 30 city tournaments as per https://limitlesstcg.com/tournaments/jp, and I collected information on how many of each type of cards each deck has:
basic energies, special energies, items, stadiums, supporters, basic pokemons, stage 1 pokemons, and stage 2 pokemons. 

Here is my takeaway from this project:

Positive:

- To implement the web scraping, I taught myself about the BeautifulSoup, requests_html, and urllib.request libraries.
- To track the progress of a specific task, I taught myself about the alive_progress library which provides the user with progress bars.
- Because I wanted a way to bypass the web scraping for testing purposes, I researched .json files and how to export data into such a file as well as import data from them using the json library.
- Finally, to complete the project, I taught myself how to use Plotly to make 3D (as well as 2D) graphs. I was able to figure out how to customize almost everything, even the hover tooltip label, so I'm very happy with that!

Negative:

- When it comes to 3D graphs, Plotly has some limitations that I couldn't find a way to resolve. The one that bothers me the most is how, only for 3D graphs, there is no way that I could find in the documentation or on Google to avoid the overlap of my tick labels with both the plot and the axis title.
  That is my one annoyance with the way my final graph looks! I also wanted to use URLs in the tick labels, but couldn't figure out the way to do it. Maybe some day!
- Because of the web scraping, the code takes a good 10 minutes to generate a graph, hence the need for a progress bar.
  I was able to bypass that with a .json file that I generate through the code for later use so that both my professir and I didn't have to sit here waiting for 10 minutes just to test the code, but I wish I could've figured out how to make it faster without having to result to that. 
- My console output gives me an error message as it generates the graph. This is something caused by a specific library I use for the web scraping part of my code. It doesn't prevent anything from working as it should, but it annoys me; I'd much rather have it be clear of issues!
  I decided to give up on trying to find the resolution as I had already put 30+ hours on this project, but I am certain I could have figured it out with a bit more time.

Ultimately though, I'm pretty happy with the results and very proud of myself for getting it done to that extent!
