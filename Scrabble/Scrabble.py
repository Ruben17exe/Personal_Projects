letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]

letter_to_points = {key:value for key, value in zip(letters, points)}

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points[letter]
  return point_total

names_players = []
words_players = []

num_players = int(input("Welcome! Entry the number of players: "))
count = 0
while count < num_players:
  names_players.append(input("\nYour name: "))
  words = []
  print("    Now entry three words in CAPITAL letters")
  for i in range(3):
    words.append(input("        Word {}: ".format(i + 1)))
  words_players.append(words)
  count += 1

player_to_words = {key:value for key, value in zip(names_players, words_players)}
player_to_points = {}

for key, value in player_to_words.items():
  player_points = 0
  for i in value:
    player_points += score_word(i)
  player_to_points[key] = player_points

for key, value in player_to_points.items():
  winner, points = key, value
  if value > points:
    winner, points = key, value
    
print("\n The winner is {} with {} points. Congratulations!".format(winner, points))
