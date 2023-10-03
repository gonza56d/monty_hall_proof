from random import randint

from app.core.models import Door, Game


def get_games(runs: int, number_of_doors: int, player_changes_door: bool) -> list[Game]:
    games: list[Game] = []
    for run in range(1, runs + 1):
        doors: list[Door] = []
        already_correct = False

        for d in range(number_of_doors):
            is_correct = False
            if not already_correct:
                is_correct = True if d + 1 == number_of_doors else bool(randint(0, 1))

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


def run_game(runs: int, number_of_doors: int = 3):
    if number_of_doors < 3:
        raise ValueError('Number of doors cannot be less than 3.')

    does_change_door_games = get_games(runs, number_of_doors, True)
    does_not_change_door_games = get_games(runs, number_of_doors, False)

