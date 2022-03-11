from app import app, stop

class State:
    pass

def frame(state):
    state.count += 1
    if state.count > 100:
        stop()
    return state

def main():
    run = app((800, 600), "Test")
    state = State()
    state.count = 0
    print(state.count)
    run(frame, state)
    print(state.count)

if __name__ == '__main__':
    truc = State()
    main()