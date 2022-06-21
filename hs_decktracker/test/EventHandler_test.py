import sys ; sys.path.append('../src/')
import entities.Player as Player
import EventHandler

logfile = open('./log_test.txt')
playerTurnString = 'ZoneChangeList.FireCompleteCallback() - m_id=6 m_taskList=38 m_changes.Count=9 m_complete=True m_completeCallback=(not null)'

def test_gameStart():
    assert 63 == eventHandler.getGameStart(logfile), "Should be line 63"

def test_playerTurn():
    assert True == eventHandler.checkPlayerTurn(playerTurnString, player), "Should be true"


eventHandler = EventHandler.EventHandler()
player = Player.Player(coin=True)

if __name__ == "__main__":
    print("Starting testing...")
    test_gameStart()
    test_playerTurn()
    print("Testing done!")


