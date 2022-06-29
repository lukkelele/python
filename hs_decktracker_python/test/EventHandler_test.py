import sys ; sys.path.append('../src/')
import entities.Player as Player
import re
import EventHandler

logfile = open('./log_test.txt')
playerTurnString = 'ZoneChangeList.FireCompleteCallback() - m_id=6 m_taskList=38 m_changes.Count=9 m_complete=True m_completeCallback=(not null)'
eventDetails_test1 = 'change=powerTask=[power=[type=TAG_CHANGE entity=[id=2 cardId= name=VBUCKS] tag=2166 value=17 ]'
eventDetails_TRANSITION_test = '[entityName=Lightbomb id=23 zone=HAND zonePos=2 cardId=CORE_GVG_008 player=1]'


def test_gameStart():
    assert 63 == eventHandler.getGameStart(logfile), "Should be line 63"

def test_playerTurn():
    assert True == eventHandler.checkPlayerTurn(playerTurnString, player), "Should be true"

def test_gettingEventDetails():
    print("Getting event details..")
    #assert "" == eventHandler.getEventDetails(eventDetails_test1)
    assert "CORE_GVG_008" == eventHandler.getEventDetails(eventDetails_TRANSITION_test)[0]
    assert "HAND" == eventHandler.getEventDetails(eventDetails_TRANSITION_test)[1]
    assert 1 == eventHandler.getEventDetails(eventDetails_TRANSITION_test)[2]


eventHandler = EventHandler.EventHandler()
player = Player.Player(coin=True)

if __name__ == "__main__":
    print("Starting testing...")
    test_gameStart()
    test_playerTurn()
    test_gettingEventDetails()
    print("Testing done!")


