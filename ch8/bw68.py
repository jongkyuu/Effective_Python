import pickle
import copyreg

class GameState:
    def __init__(self, level=0, points=0, magic=5):
        self.level = level
        self.points = points
        self.magic = magic

# # 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# #pickle.loads(serialized)

def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    kwargs['version'] = 2
    return unpickle_game_state, (kwargs,)

def unpickle_game_state(kwargs):
    version = kwargs.pop('version', 1)
    if version == 1:
        del kwargs['lives']
    return GameState(**kwargs)

# state = GameState()
copyreg.pickle(GameState, pickle_game_state)
# print('이전:', state.__dict__)

# serialized = pickle.dumps(state)


# state_path = 'game_state.bin'
# with open(state_path, 'wb') as f:
#     pickle.dump(state, f)

# state_after = pickle.loads(serialized)
# print('이후:', state_after.__dict__)

#
class BetterGameState:
    def __init__(self, level=0, points=0, magic=5):
        self.level = level
        self.points = points
        self.magic = magic

copyreg.pickle(BetterGameState, pickle_game_state)

state_path = 'game_state.bin'
with open(state_path, 'rb') as f:
    state_after = pickle.load(f)
#pickle.loads(serialized)

print(state_after)
print(state_after.__dict__)

#copyreg.pickle(BetterGameState, pickle_game_state)

#state = BetterGameState()
#serialized = pickle.dumps(state)
#print(serialized)