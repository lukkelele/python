## Log manipulation

---

### TODO
- Find keywords for player events in the output logs 

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

