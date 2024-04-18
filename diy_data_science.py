from pathlib import Path
import web_scrap
import plotly.graph_objects as go
import numpy as np
import json

def main():
    '''A function that will illustrate the card types in 30 different winning Pokemon card decks using a 3D graph.'''
    
    # Grabbing data from Limitless using the scraping modules IF there is not already an all_decks.json file in the cwd folder.
    # Also splitting the data collected into the card types.
    json_path = Path('./all_decks.json')
    decks = []
    if json_path.is_file() is True:
        f = open('all_decks.json')
        data = json.load(f)
        for i in range(30):
            decks.append([data[str(i)]['basic_energy'], data[str(i)]['special_energy'], data[str(i)]['basic_pokemon'], data[str(i)]['stage1_pokemon'],
                        data[str(i)]['stage2_pokemon'], data[str(i)]['vstar_pokemon'], data[str(i)]['supporters'], data[str(i)]['items'], data[str(i)]['tools'],
                        data[str(i)]['stadiums']])
    else:
        data = web_scrap.data_collect()
        for i in range(30):
            decks.append([data[i]['basic_energy'], data[i]['special_energy'], data[i]['basic_pokemon'], data[i]['stage1_pokemon'],
                        data[i]['stage2_pokemon'], data[i]['vstar_pokemon'], data[i]['supporters'], data[i]['items'], data[i]['tools'],data[i]['stadiums']])
        
    # Assigning the dictionary data to an axis of the 3D graph. Also initializing the graph.
    graph = go.Figure(data=go.Surface(x = np.arange(0, 10, 1),
                                      y = np.arange(0, 30, 1),
                                      z = decks,
                                      # Setting up the surface's color scheme as well as the hover tooltip text.
                                      colorscale = [[0, 'black'], [0.5, 'rgb(204, 0, 0)'], [1, 'white']],
                                      showscale = True,
                                      hovertemplate = "Number of %{x} cards<br>in deck%{y}: %{z}<extra></extra>"
                                      ))
    
    # Setting up what the graph looks like starting with some global settings.
    graph.update_layout(font_color = 'rgb(106, 123, 175)',
                        title_font_color = 'rgb(106, 123, 175)',
                        hoverlabel = dict(bgcolor = 'rgb(204, 0, 0)',
                                          font_color = 'white'),
                        paper_bgcolor = 'rgb(255, 250, 189)',
                        title_automargin = True,
                        scene = dict(
                            # Setting up the graph size.
                            aspectmode = 'manual',
                            aspectratio = dict(x = 1.3, y = 2, z = 1.5),
                            # Setting up the x axis.
                            xaxis = dict(
                                ticktext = ['Basic Energy', 'Special Energy', 'Basic Pokemon', 'Stage 1 Pokemon',
                                            'Stage 2 Pokemon','VStar Pokemon', 'Supporters', 'Items', 'Tools', 'Stadiums'],
                                tickvals = np.arange(0, 10, 1),
                                nticks = 10,
                                tickwidth = 3,
                                tickangle = 45,
                                backgroundcolor = 'rgb(255, 222, 0)',
                                gridcolor = 'rgb(59, 76, 202)',
                                showbackground = True,
                                title = 'Card Types'),
                            # Setting up the y axis.
                            yaxis = dict(
                                ticktext = [' #1', ' #2', ' #3', ' #4', ' #5', ' #6', ' #7', ' #8', ' #9', ' #10',' #11', ' #12', ' #13', ' #14',
                                            ' #15', ' #16', ' #17', ' #18', ' #19', ' #20', ' #21', ' #22', ' #23', ' #24', ' #25', ' #26', ' #27',
                                            ' #28',' #29', ' #30'],
                                tickvals=np.arange(0, 30, 1),
                                nticks = 30,
                                tickwidth = 3,
                                backgroundcolor = 'rgb(255, 222, 0)',
                                gridcolor = 'rgb(59, 76, 202)',
                                showbackground = True,
                                title = 'All of the Decks'),
                            # Setting up the z axis.
                            zaxis = dict(
                                tick0 = 0,
                                nticks = 31,
                                tickvals = np.arange(0, 31, 1),
                                tickwidth = 3,
                                backgroundcolor = 'rgb(255, 222, 0)',
                                gridcolor = 'rgb(59, 76, 202)',
                                showbackground = True,
                                title = 'Card Quantity')
                            ))
    
    # Making it so that the tick labels don't overlap with the plot so much.
    graph.update_xaxes(autotickangles=[45, 60, 90])
    
    # Title and 3D camera controls setup.
    name = '<b>Quantity of Pokemon card type in the last<br>30 winning city league tournament decks<br>as per <a href="https://limitlesstcg.com/tournaments/jp">Limitless.com</a></b>'
    camera = dict(
        up=dict(x=0, y=0, z=1),
        center=dict(x=0, y=0, z=-0.2),
        eye=dict(x=2, y=2, z=2))
    graph.update_layout(scene_camera=camera, title=name)
    
    # Showing the graph!
    graph.show()
    
    # Saving an html copy
    path = Path('./diy_data_science.html')
    graph.write_html(path)
    
main()