
# coding: utf-8

# In[117]:


from requests import get
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('--compare', type=eval, default=False)
parser.add_argument('--visualize', type=eval, default=False)
parser.add_argument('--add', type=int, default=None)
parser.add_argument('--remove', type=int, default=None)
parser.add_argument('--save', type=eval, default=False)
parser.add_argument('--saveas', type=str, default=None)
parser.add_argument('--load', type=str, default=None)
args = parser.parse_args()


def player_stats(p):
    player = get('https://suggest.svc.nhl.com/svc/suggest/v1/minactiveplayers/'+p+'/99999')
    player_data = json.loads(player.text)
    print(player_data)
    x = input("Player ID: ")
    nhl = get('https://statsapi.web.nhl.com/api/v1/people/'+x+'/stats/?expand=person.stats&stats=yearByYear')
    nhl_data = json.loads(nhl.text)
    #print(nhl_data)
    df = pd.io.json.json_normalize(nhl_data['stats'], record_prefix='_',
                              record_path='splits', errors='ignore',
                              meta=['season', ['_league', 'name'], ['_stat', 'assists']])
    df_league = pd.DataFrame(df["_league"].values.tolist())
    df_league = df_league.drop(['id', 'link'], axis=1)
    df_league = df_league.rename({'name':'league'}, axis='columns')

    df_team = pd.DataFrame(df["_team"].values.tolist())
    df_team = df_team.drop(['id', 'link'], axis=1)
    df_team = df_team.rename({'name':'team'}, axis='columns')

    df_stats = pd.DataFrame(df["_stat"].values.tolist())
    df_stats = df_stats[['goals', 'assists', 'points', 'games']]

    df_season = pd.DataFrame(df["_season"].values.tolist())
    df_season = df_season.rename({0: "season"}, axis='columns')
    df_season = pd.to_numeric(df_season['season'])

    result = pd.concat([df_season, df_league, df_team, df_stats], axis=1, sort=False)

    result = result.loc[result['league'] == "National Hockey League"]

    result['Points/Game'] = result['points']/result['games']
    result['Player'] = p
    return(result)

def visualize_comp(df):
    y = input("how do you want to compare these players (goals, assists, points, OR Points/Game): ")
    #df_comp.groupby('Player')['season', y].plot(legend=True, title=y)
    fig, ax = plt.subplots(figsize=(20,10))
    cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
    i = 0
    for label, group in df.groupby('Player'):

        group.plot(x='season', y=y, title="Comparing "+y, ax=ax, label=label, color=cycle[i])
        mean_val = round(group[y].mean(), 2)
        print(mean_val)
        ax.annotate(mean_val, xy=(group['season'].iloc[1], mean_val), xytext=(group['season'].iloc[2], mean_val*1.1),
                    arrowprops=dict(facecolor=cycle[i], shrink=0.05))
        # vertical dotted line originating at mean value
        plt.axhline(mean_val, linestyle='dashed', linewidth=2, color=cycle[i])
        i+=1
    plt.savefig('./comparison.png')

def compare_players():
    num_players = input('How many players do you want to look at: ')
    appended_data = []
    for i in range (int(num_players)):
        p = input("which player do you want to look at: ")
        pp = player_stats(p)
        appended_data.append(pp)
    df_comp = pd.concat(appended_data, axis=0)
    visualize_comp(df_comp)
    if args.save or args.saveas is not None:
        save_df(df_comp)
    return df_comp

def add_player(df):
    p = input("which player do you want to look at: ")
    pp = player_stats(p)
    df = pd.concat([df, pp], axis=0)
    if args.save or args.saveas is not None:
        save_df(df)
    return df

def remove_player(df):
    p = input("which player do you want to remove: ")
    df = df[df.Player != p]
    if args.save or args.saveas is not None:
        save_df(df)
    return df

def save_df(df, filename="player_comparison.pkl"):
    if args.saveas is not None:
        filename = args.saveas
    df.to_pickle(filename)



if args.load is not None:
    df = pd.read_pickle(args.load)
    if args.save:
        save_df(df)

if args.compare:
    df = compare_players()

if args.visualize:
    visualize_comp(df)

if args.add:
    for i in range(args.add):
        df = add_player(df)

if args.remove:
    for i in range(args.remove):
        df = remove_player(df)