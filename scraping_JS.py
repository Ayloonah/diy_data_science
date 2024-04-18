from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import re

def card_info(url, each_card):
    '''Grabbing information on the cards for a given deck.
    Args:
    url: This should be a deck's URL as a string.
    each_card: This is an empty dictionary to store the card URLs and types.
    
    Returns:
    all_type_counts: A dictionary for which the keys are the 10 card types.
                     The values are the total quantity (integers) of cards of each type for a given deck. '''
    
    # Grabbing the HTML/Javascript from the deck page.
    session = HTMLSession()
    response = session.get(url)
    response.html.render()
    soup = bs(response.html.html, 'html.parser')
    
    # Collecting the URLs for each individual card
    all_links = []
    for url in soup.find_all('a', class_='card-link'):
        link = 'https://limitlesstcg.com' + url.get('href')
        all_links.append(link)
    
    # Finding the quantity of each card.
    all_quantities = []
    for count in soup.find_all('span', class_='card-count'):
        quantity = str(count)
        quantity = int(re.sub("[^0-9]", "", quantity))
        all_quantities.append(quantity)
    
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
    
    # Grabbing the card type from each card's page, and then adding the count per type.
    for i in range(len(all_links)):
        
        # If statement to see if that card's type is already stored.
        if all_links[i] in each_card.keys():
            type = each_card[all_links[i]]
        else:
            html = session.get(all_links[i])
            html.html.render()
            more_soup = bs(html.html.html, 'html.parser')
            type_code = more_soup.find('p', class_='card-text-type')
            type = str(type_code)
            each_card[all_links[i]] = type
        
        # For pokemon type: 
        if 'Pokémon' in type:
            if 'VSTAR' in type:
                all_type_counts['vstar_pokemon'] += all_quantities[i]
            elif 'Stage 2' in type:
                all_type_counts['stage2_pokemon'] += all_quantities[i]
            elif 'Stage 1' in type:
                all_type_counts['stage1_pokemon'] += all_quantities[i]
            # Basic pokemon type:
            else:
                all_type_counts['basic_pokemon'] += all_quantities[i]
        elif 'Trainer' in type:
            if 'Supporter' in type:
                all_type_counts['supporters'] += all_quantities[i]
            elif 'Item' in type:
                all_type_counts['items'] += all_quantities[i]
            elif 'Stadium' in type:
                all_type_counts['stadiums'] += all_quantities[i]
            # Tool trainer type:
            else:
                all_type_counts['tools'] += all_quantities[i]
        # Energy card type:
        else:
            if 'Special Energy' in type:
                all_type_counts['special_energy'] += all_quantities[i]
            # Basic energy type:
            else:
                all_type_counts['basic_energy'] += all_quantities[i]
        
    return all_type_counts