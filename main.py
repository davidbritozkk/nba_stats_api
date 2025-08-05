from nba_api.stats.static import players
from nba_api.stats.endpoints import playerdashboardbyshootingsplits

player_input = input("Type the player's name: ")

player_found = players.find_players_by_full_name(player_input)[0]
player_found_id = player_found['id']

season = input("Type the season (format 'YYYY-YY', ex: '2024-25'): ")

print(f"Statistics for {player_found['full_name']} (id: {player_found_id})\n")

stats = playerdashboardbyshootingsplits.PlayerDashboardByShootingSplits(player_id=player_found_id, season=season, season_type_playoffs='Regular Season')

df = stats.get_data_frames()[1]

print (df[['GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT']].rename(columns={'GROUP_VALUE': 'Shot Zone', 'FGM': 'Field Goals Made', 'FGA': 'Field Goals Attempted', 'FG_PCT': 'Field Goal Percentage'}))

df_export = df[['GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT']].rename(columns={'GROUP_VALUE': 'Shot Zone', 'FGM': 'Field Goals Made', 'FGA': 'Field Goals Attempted', 'FG_PCT': 'Field Goal Percentage'})
df_export.to_csv(f'sheets/{player_found["full_name"]}_shooting_splits_{season}.csv', index=False)
print(f"\nExported {player_found['full_name']}'s shooting splits to '{player_found['full_name']}_shooting_splits_{season}.csv'.")
