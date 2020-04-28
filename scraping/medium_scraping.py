from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# I will use my medium profile page, it's open so you can try too
MEDIUM_URL = "https://medium.com/@ProfessionProgrammer"
HEADER = {'User-Agent': 'Mozilla/5.0', "accept-language": "en-US"}

def scraping_medium():
    # Get the URL content
    request = Request(MEDIUM_URL, headers=HEADER)    
    response = urlopen(request, timeout=10)

    # Get the content from the response, and set as default encoder 'utf-8'
    page_content = response.read().decode('utf-8')

    # Parse the data using Beautifulsoup
    parsed_data = BeautifulSoup(page_content, 'html.parser')
    
		# This will get the main part of the code that has our posts
    main_div = parsed_data.find('div', class_="fd y")
    
    # This will get only the 'div' tha has my posts 
    posts_div = main_div.find_all('div', class_="r s y")
    
    for item in posts_div:
        try:
            title = item.h1.text
            post_link = item.a['href']
        
            # This is only intended for debug not for production
            print(title)
            print(post_link)
            print("")
        except:
            # If you are using this in production, you should have a log layer that you log when this happens
            print("No tag found")
        