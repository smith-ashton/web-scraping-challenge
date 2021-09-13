from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    title_url = 'https://redplanetscience.com/'
    browser.visit(title_url)
    title_html = browser.html
    soup = BeautifulSoup(title_html, 'lxml')


    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text


    image_url = 'https://spaceimages-mars.com/'
    browser.visit(image_url)

    image_html = browser.html
    soup = BeautifulSoup(image_html, 'html.parser')
    image = soup.find('img', class_='headerimage fade-in')
    image_src = image['src']
    featured_image_url = image_url + image_src

    browser.quit()

    facts_url = 'https://galaxyfacts-mars.com'
    tables = pd.read_html(facts_url)

    df1 = tables[0]
    new_header = df1.iloc[0] 
    df1 = df1[1:] 
    df1.columns = new_header
    df1=df1.drop(labels="Earth",axis=1)
    df2 = tables[1]
    df2=df2.rename(columns={0:"Mars - Earth Comparison",1:"Mars"})
    dataframe=df1.append(df2)
    dataframe=dataframe.rename(columns={"Mars - Earth Comparison":"Facts"})
    html_table = dataframe.to_html()
    html_table = html_table.replace('\n', '')

    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced.tif"},
    {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/cerberus_enhanced.tif"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced.tif"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced.tif"}
    ]

    needed = {"title":news_title, "para":news_p, "feat_img":featured_image_url,"table":html_table, "img_list":hemisphere_image_urls}
    return needed
