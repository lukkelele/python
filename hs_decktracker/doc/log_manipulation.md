## Log manipulation

---

### TODO
- Find keywords for player events in the output logs 

---
### Keywords 
1. Game start -> SERVER\_GAME\_STARTED event
2. Hero -> cardId=HERO_[insert id]
3. IDs   
   id=1 -> GameEntity, tag=STATE, value=RUNNING  
   id=2 -> Player, tag=PLAYSTATE, value=PLAYING, entity=[PLAYERNAME]  
   id=3 -> Opponent, tag=PLAYSTATE, value=PLAYING, entity=UNKNOWN HUMAN PLAYER  
4. ZoneChangeList.UpdateDirtyZones() -> START and END for loading purposes. Finishes with ZoneChangeList.Finish()


---
### Notes
- Heroes and hero powers are also represented (lastly) in the initial card transitions for both players

