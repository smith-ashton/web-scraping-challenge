# web-scraping-challenge

## Scraping

In this project, I used Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter to scrape the following websites:

<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-https://redplanetscience.com
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-https://spaceimages-mars.com
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-https://galaxyfacts-mars.com
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-https://marshemispheres.com

<br/>I was able to obtain the title and summary of the most recent article, the latest featured image, a table of mars facts, and the urls of high resolution images of the four hempispheres of mars.

## MongoDB and Flask Application
After writing the script to scrape the above information, an applcication, as well as a corresponding html file, was created to display the information on one page. The application writes the scaped information to a MongoDb database and retrieves it for display purposes. The page features a button to call the scrape script for the latest information.
