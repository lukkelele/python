# Hearthstone Deck Tracker 
#### Author: Lukas Gunnarsson
#### Created 12/6-2022

---

I played lots of Hearthstone in 2015-2016 and early on I had a notebook in which I wrote what the enemy had played to keep track of possible threats.  
This approach was obviously not effecient and a while later when it was stated that deck trackers did *NOT* break the TOS, I began using one.  
  
Recently I began playing again and it has been rough getting used to all the new cards and the game pace.  
The idea of merging a deck tracker with some sort of program to check for big drops and win conditions based on which class I faced came to my mind.  

---

### Project Goals
- Great performance
- Neat look
- Easy customization
- Meta analysis to provide useful information (win conditions, OTK combos etc.)

---
### Parts of project
- Card database
- Overlay
- Web scraping
- Local executable

---
### Software 
#### Card database, CardDB.py
Used to store and retrieve cards and deck data.  

---

### Keywords 
1. Game start -> SERVER\_GAME\_STARTED event
2. Hero -> cardId=HERO_[insert id]
3. IDs of entities     
   id=1 -> GameEntity, tag=STATE, value=RUNNING  
   id=2 -> Player, tag=PLAYSTATE, value=PLAYING, entity=[PLAYERNAME]  
   id=3 -> Opponent, tag=PLAYSTATE, value=PLAYING, entity=UNKNOWN HUMAN PLAYER  
4. ZoneChangeList.UpdateDirtyZones() -> START and END for loading purposes. Finishes with ZoneChangeList.Finish()
5. FireCompleteCallback() m\_id -> the end of mulligan phase and the first round begins with an id=5
6. ProcessChanges() logs information about cards being transitioned in to play, tag=**JUST_PLAYED** shows played card with its information 

---

### Notes
- Heroes and hero powers are also represented (lastly) in the initial card transitions for both players
- The mulligan phase begins with the players info. The opponent information only contains *UNKNOWN ENTITY* and only keeps track of the unknown cards *zone* position (index of the placement in hand)
- The player who starts with coin is assigned a turn ID that is even.  
PLAYER with *COIN* -> *even* turn IDs
- Game setup and mulligan continues until m\_id == 5.


