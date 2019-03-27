# Web_Scraping_and_MongoDB


In this program, I have built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what I have done.

1. NASA Mars News
Scraped the NASA Mars News Site and collected the latest News Title and Paragraph Text.

2. JPL Mars Space Images - Featured Image
Visited the url for JPL Featured Space Image @ https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
and got the latest featured image url

I have used splinter to navigate the site to find the image url for the current Featured Mars Image.

3. Mars Weather
Visit the Mars Weather twitter account @ https://twitter.com/marswxreport?lang=en
and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.

4. Mars Facts
Visited the Mars Facts webpage @ http://space-facts.com/mars/
and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

5. Mars Hemispheres
Visited the USGS Astrogeology site @ https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
to obtain high resolution images for each of Mar's hemispheres.

6. MongoDB and Flask Application
I have used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

I started by converting my Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that executes all of the scraping code from above and return one Python dictionary containing all of the scraped data.

Next, I create a route called /scrape that imports scrape_mars.py script and calls the scrape function.

Then, I stored the return value in Mongo as a Python dictionary, created a root route / that queries the Mongo database and passes the mars data into an HTML template to display the data.

Finally, I created a template HTML file called index.html that takes the mars data dictionary and display all of the data in the appropriate HTML elements. 

Since, the application requires an active MongoDB connection and needs to run Flask server as well, I have provided the screenshots of the webpage. 
