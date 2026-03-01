import pandas as pd
import numpy as np


def get_player_string(name, player, team=False):

    breakdown = None
    if not np.isnan(player['Year 1']):
        breakdown = f'({player["Year 1"]:.2f}'
    if not np.isnan(player['Year 2']):
        breakdown += f', {player["Year 2"]:.2f}'
    if not np.isnan(player['Year 3']):
        breakdown += f', {player["Year 3"]:.2f}'
    if not np.isnan(player['Year 4']):
        breakdown += f', {player["Year 4"]:.2f}'
    if not np.isnan(player['Year 5']):
        breakdown += f', {player["Year 5"]:.2f}'
    if breakdown is not None:
        breakdown += ')'
    if not team:
        player_string = f'{name},'
    else:
        player_string = f'[b]{player.Team}[/b]:'
    player_string += f' {int(player.Years)}'
    player_string += f' year{"s" if player.Years > 1 else ""}'
    player_string += f' at {player.Avg:.2f} per year'
    if breakdown is not None:
        player_string += f' {breakdown}'
    return player_string


def parse_bids(division):
    bids = pd.read_csv(f'SSDL Raw Bids - {division}.csv')
    by_player = dict()
    by_team = {val: [] for val in bids['Team'].unique()}
    player_cols = list(bids.columns)
    player_cols.remove('Player')
    players = bids['Player'].unique()
    for player in players:
        by_player[player] = []
        player_df = bids.loc[
            bids['Player'] == player, bids.columns != 'Player'
        ].sort_values(['Avg', 'Years', 'Year 1', 'Order'],
                      ascending=(False, False, False, True)
                      )
        player_info = player_df.iloc[0]
        by_team[player_info.Team].append(get_player_string(
            player, player_info
        ))
        for _, player_info in player_df.iterrows():
            by_player[player].append(get_player_string(
                player, player_info, True
            ))

    return by_team, by_player


if __name__ == '__main__':
    division = 'NL East'
    by_team, by_player = parse_bids(division)
    with open(f'{division} by Player.csv', 'w') as f:
        for k, v in by_player.items():
            f.write(f'[b]{k}[/b]\n')
            for elem in v:
                f.write(f'{elem}\n')
            f.write('\n')

    with open(f'{division} by Team.csv', 'w') as f:
        for k, v in by_team.items():
            if len(v):
                f.write(f'[b]{k}[/b]\n')
                for elem in v:
                    f.write(f'{elem}\n')
                f.write('\n')
