import requests
from keys import API_KEY

def get_response(category = 'technology', country = 'us'):
    """
    Comments
    
    """
    url = 'https://newsapi.org/v2/top-headlines?country={0}&category={1}&apiKey={2}'
    user_api_key = API_KEY
    
    while len(user_api_key) != 32:
        user_api_key = input('Insert correct API KEY')
    
    
    available_categories = ['technology','business','entertainment','general','health','science','sports','technology']
 
    category = input("""
    Pick category:
    Technology
    Business
    Entertainment
    General
    Health
    Science
    Sports
    
    Press enter for 'general' headlines
    """)
    
    category = category.lower()

    if category == '':
        print("\nRetrieving General headlines\n")
        response = requests.get(url.format(country, 'general', user_api_key))
    elif category not in available_categories:
        print("\nCategory not found")
        print("Retrieving General headlines")
        response = requests.get(url.format(country, 'general', user_api_key))
    else:
        response = requests.get(url.format(country, category , user_api_key))

        
    if response:
        return response.json()
    else:
        return None


def get_articles():
    raw_articles_list = get_response()['articles']
    articles_list = list()
    
    for article in raw_articles_list:
        title = article['title']
        source = article['source']['name']
        author = article['author']
        url = article['url']
        
        dictionary = {'title':title, 'source':source, 'author':author, 'url':url}
        
        articles_list.append(dictionary)
        
    return articles_list
        
        


def export_articles():
    
    data = get_articles()
    n = input('How many articles do you want?\n\n')
    
    try:
        n = int(n)
        if n <= 0:
            raise Exception
    except:
        print('You need to pick an integer between 1 and 100\n')
        print('Restarting program'+ '.'*20+'\n')
        export_articles() #Using recursion
        
    total_articles = len(data)
    
    if n > total_articles:
        print(f"\nThere are only {total_articles} articles available!\n")
         
        print(f"\nExporting {total_articles} articles\n")
        final_data =  data[:total_articles]
    
    else:
        final_data = data[:n]
    
    with open('articles.txt','w') as file:
        i = 1
        for article in final_data:
            file.write(f"Article {i}\n{article['title']} \n{article['author']}\n{article['source']}\n{article['url']}\n\n")
            i += 1
        

