hearts = 13
diamonds = 13
facecards = 12  
diamondface = 3 
spadeface = 3
queens = 4

totalcards = 52
red_cards = 26

p_red = red_cards / totalcards
print(f"\nQ1: P(Red card) = {red_cards}/{totalcards} = {p_red:.4f}")
 
p_heartgivenred = hearts / red_cards
print(f"Q2: P(Heart | Red) = {hearts}/{red_cards} = {p_heartgivenred:.4f}")
 
p_diamond_given_face = diamondface / facecards
print(f"Q3: P(Diamond | Face) = {diamondface}/{facecards} = {p_diamond_given_face:.4f}")

q_spadesface = 1
favorable = spadeface + queens - q_spadesface  
p_spade_or_queen_given_face = favorable / facecards
print(f"Q4: P(Spade or Queen | Face) = {favorable}/{facecards} = {p_spade_or_queen_given_face:.4f}")
