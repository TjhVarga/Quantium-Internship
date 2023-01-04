import requests
from bs4 import BeautifulSoup

def get_article_text(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  article_text = soup.find_all('p')
  return '\n'.join([paragraph.get_text() for paragraph in article_text])



#main
if __name__ == '__main__':
    # Get the text of the article
    article_text = get_article_text('https://www.theguardian.com/lifeandstyle/2023/jan/04/truth-behind-10-of-the-biggest-health-beliefs')
    # Print the first 100 characters of the article
    print(article_text[:100])
