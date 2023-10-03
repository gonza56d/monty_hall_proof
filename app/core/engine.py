from random import randint

from app.core.models import Door, Game, GamesResults


def get_games(runs: int, number_of_doors: int, player_changes_door: bool) -> list[Game]:
    games: list[Game] = []
    for run in range(1, runs + 1):
        doors: list[Door] = []
        already_correct = False

        for d in range(number_of_doors):
            is_correct = False
            if not already_correct:
                is_correct = True if d + 1 == number_of_doors else bool(randint(0, 1))
                if is_correct:
                    already_correct = True

            doors.append(
                Door(
                    number=d,
                    is_correct=is_correct,
                    has_been_opened=False
                )
            )

        games.append(Game(
            doors=doors,
            player_door=doors[randint(0, number_of_doors - 1)],
            played_changes_door=player_changes_door
        ))

    return games


def run_game(runs: int, number_of_doors: int = 3) -> GamesResults:
    if number_of_doors < 3:
        raise ValueError('Number of doors cannot be less than 3.')

    results = GamesResults(runs)
    does_change_door_games = get_games(runs, number_of_doors, True)
    does_not_change_door_games = get_games(runs, number_of_doors, False)

    for game in does_change_door_games:
        game.open_door()
        game.change_player_door()
        if game.correct_door == game.player_door:
            results.changed_corrects += 1

    for game in does_not_change_door_games:
        game.open_door()
        if game.correct_door == game.player_door:
            results.not_changed_corrects += 1

    return results
