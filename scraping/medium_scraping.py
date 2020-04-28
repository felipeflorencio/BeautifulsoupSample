from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from extensions.database import db
from model.medium_model import MediumModel

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

            # We create our model
            post = MediumModel(title=title, post_link=post_link)
            
            # We add to our db session
            db.session.add(post)
            
            # This is only intended for debug not for production
            print(title)
            print(post_link)
            print("")
        except:
            # If you are using this in production, you should have a log layer that you log when this happens
            print("No tag found")
        
    # after all the loop is done we just persist into our database
    db.session.commit()
    

def fetch_medium_posts():
    postList = MediumModel.query.order_by(MediumModel.date_created).all()
    
    serialized_list = list(map(lambda post : post.to_dict(), postList))

    return serialized_list