!pip install transformers

from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(text, max_length=500, min_length=100):
  
  summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
  return summary[0]['summary_text']

from bs4 import BeautifulSoup
import requests

def scrape_website(url):
  try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    return text
  except requests.exceptions.RequestException as e:
    print(f"Error scraping website: {e}")
    return None

url_to_scrape = input("Enter the url:") 
scraped_text = scrape_website(url_to_scrape)

if scraped_text:
  summary = summarize_text(scraped_text)
  print("Summary:", summary)
