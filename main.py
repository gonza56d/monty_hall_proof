from app.core.engine import run_game

if __name__ == '__main__':
    runs = 1000
    results = run_game(runs)
    print(f'{results.changed_corrects} out of {runs} victory games with player changing the door.')
    print(f'{results.not_changed_corrects} out of {runs} victory games with player NOT changing the door.')
