games_playtime = {
  'Ghost Recon Wildlands':'96 hours',
  'Overwatch':"78 hours",
  'Call of Duty Modern Warfare 2019':"150 hours",
  'Minecraft':"320 hours",
  'Dishonored':'100 hours',
  'It Takes Two':'30 hours',
  'Assassins Creed Valhalla':'96 hours',
  'The Division':'52 hours',
  'For Honor':'82 hours',
}

for games, playtime in games_playtime.items():
  print(f'{games}:{playtime}')

user_games = input('Which of these games do you like? ')

print(f'My personal playtime on {user_games} is {games_playtime[user_games]}')

if user_games == 'Ghost Recon Wildlands':
  print('This is one of my favorite games, me and my friends still play it sometimes.')
elif user_games == "Overwatch":
  print('I enjoy Overwatch but there are games I would rather play.')
elif user_games == "Call of Duty Modern Warfare 2019":
  print('The best cod in years, I miss Black Ops 2 but I really enjoy this.')
elif user_games == "Minecraft":
  print('One of the best games ever made but I played it so much that I get bored of it easily now unless I have someone to play with.')
elif user_games == "Dishonored":
  print('My favorite game of all time, I want to get a tattoo of the Mark of The Outsider that Corvo has.')
elif user_games == "It Takes Two":
  print('Very good game, I played through it multiple times with different people. Fun with friends or your romantic partner.')
elif user_games == "Assassins Creed Valhalla":
  print('A lot of people are upset that Assassins Creed is an RPG now but I really enjoy it. I also love Norse mythology and the entire game is built around it.')
elif user_games == "The Division":
  print('Underated in my opinion, it is a very fun RPG if you have friends to play with. I can see it being boring single player though.')
elif user_games == "For Honor":
  print('Ahh, this game, I have a very big love/hate relationship with this game. It is very unbalanced and it annoys me but I continue to play it because the gameplay is good.')
  //Great games
