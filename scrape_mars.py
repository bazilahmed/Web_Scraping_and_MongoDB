#!/usr/bin/env python
# coding: utf-8

# Program to scrape various websites for data related to the Mission to Mars 
# and displays the information in a single HTML page. 

# Import the dependencies
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests as r
from pprint import pprint
from splinter import Browser
import re

def scrape():
    ########################################################
    # Scrape news data from Mars website - https://mars.nasa.gov/news/
    # get the response for the url to create a html object
    url = "https://mars.nasa.gov/news/"


    # Scrape the web page and get the title and the article summary 
    # time to use splinter to automate 
    # input just the filename if the .exe is in the same folder esle the full path
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # open the url in splinter browser
    browser.visit(url)


    # get the html page from the browser using browser.html and save it using soup
    soup = BeautifulSoup(browser.html, "html.parser")


    # Loop through the page to find all the titles and articles
    news_title = soup.find('div', class_='content_title').text.strip()
    news_summary = soup.find('div', class_='article_teaser_body').text.strip()

    print(news_title)
    print(news_summary)

    ########################################################
    # getting the featured  image from nasa website - JPL Mars Space Images - Featured Image
    jpl_base_url = "https://www.jpl.nasa.gov/"
    url_search = "spaceimages/?search=&category=Mars" 

    # complete the url 
    jpl_url = f"{jpl_base_url}{url_search}"

    # open the url in splinter browser
    browser.visit(jpl_url)

    # get the html page from the browser using browser.html and save it using soup
    soup = BeautifulSoup(browser.html, "html.parser")

    # retreive the image url from the homepage
    image_container = soup.find('article', class_="carousel_item")

    # save the attributes to retrieve the url from the style attribute of article tag
    image_cont_attrs = image_container.attrs

    #  get the style attr values
    image_style = image_cont_attrs['style']

    # use regex to retrieve the url from style attr
    text = image_style
    pattern = r"background-image: url\(\'(.*)\'\);"
    x = re.search(pattern, text) 

    # get the matched value with group command
    featured_image_url = x.group(1)

    # append the base url 
    featured_image_url =  f"{jpl_base_url}{featured_image_url}"

    print(featured_image_url)

    ########################################################
    # scrape the mars weather website for their latest tweet
    twitter_url = "https://twitter.com/marswxreport?lang=en"

    # open the url in splinter browser
    browser.visit(twitter_url)

    # get the html page from the browser using browser.html and save it using soup
    soup = BeautifulSoup(browser.html, "html.parser")


    # retreive the weather tweet
    mars_weather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text.strip()

    print(mars_weather)

    ########################################################
    # scrape the mars facts website table contents using Pandas
    mars_facts_url = 'https://space-facts.com/mars/'
    table = pd.read_html(mars_facts_url)

    print(table)

    # convert the returned list to a df
    mars_facts_df = table[0]


    # convert the df to a html table by transposing
    mars_facts_df.columns = ["Column Name", "Value"]
    mars_facts_df = mars_facts_df.set_index("Column Name").T

    # Convert dataframe into html table
    mars_facts_html = mars_facts_df.to_html(index = False)

    # strip unwanted newlines from html table
    mars_facts_html = mars_facts_html.replace('\n', '')


    pprint(mars_facts_html)

    ########################################################
    # scrape the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
    usgs_astro_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # base url 
    usgs_base_url = "https://astrogeology.usgs.gov"

    # open the url in splinter browser
    browser.visit(usgs_astro_url)

    # get the html page from the browser using browser.html and save it using soup
    soup = BeautifulSoup(browser.html, "html.parser")

    # creating an empty list to store the image urls 
    hemisphere_img_urls = []

    # retreive the html tag and the urls
    hemisphere_results = soup.find_all('div', class_='description')
    # hemisphere_results

    # Loop through the results scrape the image url and title to append to the hemisphere_img_urls array
    for result in hemisphere_results:
        title = result.find('h3').text.strip()
        image_url = result.find('a')['href']
        image_full_url = usgs_base_url + image_url
        browser.visit(image_full_url)    
        soup = BeautifulSoup(browser.html, "html.parser")
        image_downloads = soup.find('div', class_='downloads')
        full_image_url = image_downloads.find('a')['href']
        hemisphere_img_urls.append({"title" : title, "urls": full_image_url})

    # Print the array
    pprint(hemisphere_img_urls)


    ########################################################
    # create a dictionary to return from the function
    mars_data = {
        "news_title": news_title,
        "news_summary": news_summary,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "mars_facts_html": mars_facts_html,
        "hemisphere_img_urls": hemisphere_img_urls
    }

    return mars_data



