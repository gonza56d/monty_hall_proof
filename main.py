from app.core.engine import run_game

if __name__ == '__main__':
    results = run_game(runs=1000)
    print(f'{results.changed_corrects} victory games with player changing the door.')
    print(f'{results.not_changed_corrects} victory games with player NOT changing the door.')
