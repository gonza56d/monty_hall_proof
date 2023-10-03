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
    player_door: int
    played_changes_door: bool
