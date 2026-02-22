#Scrabble Project
#Code by NOVA_TAGO
#This is a project from Codecademy "Python 3" Course
#Go through and use dictionaries to add up "points" provided from a list
#Does not insert values for new words but tallies up totals from a prior game



#This is the list of letters in the alphabet provided as strings, only available as capital letters
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#This provides a 1D list of points for each letter, corresponding to the order of the alphabet
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Creates a dictionary using the zip function for both lists "letters" and "points"
letter_to_points = {
  key: value 
  for key, value 
  in zip(letters, points)}

#adds a point value for empty spaces to prevent errors
letter_to_points[" "] = 0

#CODE CHECK
#prints dictionary created above
#print(letter_to_points)

#function created called score_word that adds up total points for each word supplied
def score_word(word):
  #Initializes the point_total variable by setting it equal to zero
  point_total = 0
  #This is the for loop that looks at each letter in the supplied word and adds its worth from the dictionary "letter_to_points" from above
  #This uses the .get command in case if special characters are accidently added, they will automatically get 0 points
  for letter in word:
    #sets default for any character outside "letter_to_points" as 0 to prevent unexpected errors
    point_total += letter_to_points.get(letter, 0)
  #returns the point_total variable after adding up its value for use outside of the function
  return point_total


#CODE CHECK
#Creates a word "BROWNIE" and inserts it into the function above called "score_word"
#This allows the word to be tallied and stored as a variable called "brownie_points""
#brownie_points = score_word("BROWNIE")
#Checkies to see if BROWNIE was added correctly
#print(brownie_points)



#The next lines of code are to tally points for a game of four people
#The words they used in their game are shown below
player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

#Initializes a new dictionary as empty
player_to_points = {}

#Creates a for loop that utilizes both the key as "player" and the value as "word" using the .items method for dictionaries
#This for loop looks at each player in the dictionary "player_to_words"
for player, words in player_to_words.items():
  #Initializes a variable "player_points" for each loop of each player performed on
  player_points = 0
  #Sub for loop that goes through each word provided for the specific player looked at
  for word in words:
    #This passes the word looked at to the function "sorce_words", which adds up the points, and takes its value and adds it to the player_points variable
    player_points += score_word(word)
  #Outside of the inner for loop, after each word is added up for the specific player, but not outside of the outer for loop, it adds a new entry to the player_to_points dictionary.
  #Here, the key added is the player name using the "player" keyword from the outer for loop above and the "player_points"" as the value for the dictionary
  player_to_points[player] = player_points

#CODE CHECK
#Prints out the player_to_points dictionary created above.
print(player_to_points)
