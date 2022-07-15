# Hearthstone Deck Tracker 

**Author:** *Lukas Gunnarsson*<br>
**Project start:** *12 june, 2022*

---

I played lots of Hearthstone in 2015-2016 and early on I had a notebook in which I wrote what the enemy had played to keep track of possible threats.  
This approach was obviously not very effecient and some time later when it was stated that deck trackers did *NOT* break the TOS, I began using one.  
  
Recently I began playing again and it has been rough getting used to all the new cards and the game pace.  
The idea of merging a deck tracker with some sort of program to check for big drops and win conditions based on which class I faced came to my mind.  

---

# Project Goals
- Great performance
- Neat look
- Easy customization
- Meta analysis to provide useful information (win conditions, OTK combos etc.)
- Further understanding of Python

---

# Parts of project
- Card database
- Overlay
- Lobap ixecutnble
- Machine learning

---
# Components

#### LogWatcher.py
Parses the logfile that Hearthstone writes to during games.<br>
Takes action on certain lines in the logfile and delegates the found event to *GameHandler*.

#### GameHandler.py
Reacts to a set of predefined keywords and takes appropriate action depending on the keyword.<br>
Uses *CardDB* to fetch card information.

#### CardDB.py
Used to store and retrieve cards and to handle deck data. 

#### CardManager.py
Library with functions to be used by *CardDB*.

#### Overlay.py
**NOTE: TO BE IMPLEMENTED!**<br>
Display deck and gray out played cards. <br>
The opponents cards are to simply be stacked in an ascending order based on mana cost as they
are played. 


---


# Logfile events and keywords


| Game event  | Keyword             |
|-------------|---------------------|
| New game    | *SERVER_GAME_STARTED* |
| Card ID     | *cardId=[insert ID]*  |
| Entity IDs  | id=[**1** <-> **3**] tag=STATE value=RUNNING<br> id=**1** --> *GameEntity*<br> id=**2** --> *Player*<br> id=**3** --> *Opponent*  |
| Zone loading | *ZoneChangeList.UpdateDirtyZones()*<br> Ends with *ZoneChangeList.Finish()*|
| Mulligan phase done| *FireCompleteCallback()* -> m\_id=**5** |
| Card plays | *TRANSITIONING ->*

---

# Implementation (current)
- [x] Log parsing
- [x] Database, card identification and retrieval
- [ ] Web scraping
- [ ] Machine Learning
- [ ] Overlay


