from enum import Enum

class State(Enum):
    OFF: int = 0
    ON: int = 1

state: State = State.ON

if state == State.ON:
    print('The device is turned on')
elif state == state.OFF:
    print('The device is turned off')
else:
    print('Unknown input...')
