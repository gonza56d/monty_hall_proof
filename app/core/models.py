from dataclasses import dataclass

from app.core.exceptions import WrongStateError


@dataclass
class Door:

    number: int
    is_correct: bool
    has_been_opened: bool

    def open(self) -> bool:
        """Open door and check if it's correct."""
        if self.has_been_opened:
            raise WrongStateError('Door has been already opened.')
        return self.is_correct


@dataclass
class Game:

    doors: list[Door]
    player_door: Door
    played_changes_door: bool

    def __post_init__(self):
        count = len(list(filter(lambda d: d.is_correct, self.doors)))
        if count != 1:
            raise WrongStateError(f'Only one door can be the correct one. Found {count} correct.')

        for door in self.doors:
            if door is self.player_door:
                break
        else:
            raise WrongStateError('Player door was not present in game doors.')

    @property
    def correct_door(self) -> Door:
        try:
            return list(filter(lambda d: d.is_correct, self.doors))[0]
        except KeyError:
            raise WrongStateError('Game had no correct door')
