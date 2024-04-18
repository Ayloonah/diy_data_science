from urllib.request import urlopen as uo
from scraping_JS import card_info
from alive_progress import alive_bar
import json

def data_collect():
    '''Collecting deck cards data from Limitless.
    Returns:
    all_decks: A dictionary for which the keys are numbers between 0 to 30.
               Each value stored is another dictionary for which the keys are the card types.
               The values stored are the quantity (integers) of cards of each type.
    all_type_counts: A dictionary for which the keys are the 10 card types.
               The values are the total quantity (integers) of cards of each type for all 30 decks.
    '''
    
    def get_html(url):
        '''Collecting the content of the HTML code for a given page.
        Args:
        url: The URL of the page you need the HTML code from.
        
        Returns:
        A string containing the HTML code of the provided URL.'''
        page = uo(url)
        html_bytes = page.read()
        return html_bytes.decode("utf-8")
    
    def scraping(html, list):
        '''Collecting the list of deck URLs.
        Args:
        html: The HTML code of a given URL.
        list: A list where we will store the URLs of each separate winning decks.'''
        occurrences = html.count('"https://limitlesstcg.com/decks/list/jp/')
        position = -1
        with alive_bar(occurrences) as bar:
            for occurence in range(occurrences):
                bar.title(f'Collecting deck URLs: ')
                position = html.find('"https://limitlesstcg.com/decks/list/jp/', position + 1)
                url = (html[position:position + 46])
                if url.find('>') != -1:
                    url = url.replace('>', ' ').strip().replace('"', '')
                list.append(url)
                bar()
                            
    # Collecting the HTML code of the first deck page.
    url1 = 'https://limitlesstcg.com/tournaments/jp'
    html1 = get_html(url1)

    # Collecting the HTML code of the second deck page.
    url2 = 'https://limitlesstcg.com/tournaments/jp?page=2'
    html2 = get_html(url2)
    
    # Initializing the deck URLs list.
    deck_urls = []
    
    # Grabbing the deck URLs and adding them to the list, removing any decks that show up twice, and deleting the last 20 decks, leaving us with 30 deck URLs.
    scraping(html1, deck_urls)
    scraping(html2, deck_urls)
    deck_urls = list(set(deck_urls))
    del deck_urls[30:50]
    
    # Making a dict to store each card type and their quantities
    all_type_counts = {
        'basic_energy' : 0,
        'special_energy' : 0,
        'basic_pokemon' : 0,
        'stage1_pokemon' : 0,
        'stage2_pokemon' : 0,
        'vstar_pokemon' : 0,
        'supporters' : 0,
        'items' : 0,
        'tools' : 0,
        'stadiums' : 0}
    
    all_decks = {}
    # Also making a dict with URLs and card type to avoid having to check the type each time a card is encountered.
    each_card = {}
    
    # Collecting the card types and quantities for each deck.
    with alive_bar(30) as bar:
        for i in range(30):
            bar.title(f'Collecting card types and quantities for deck # {i + 1}')
            types = card_info(deck_urls[i], each_card)
            all_decks[i] = types
            bar()
            
    with open('all_decks.json', 'w') as f:
        json.dump(all_decks, f)
    
    return all_decks