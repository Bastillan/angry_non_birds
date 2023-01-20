import pytest
from src.game import Game
from src.game import (
    WindowSizeError,
    FpsError
)


def test_game_create_invalid_window():
    with pytest.raises(WindowSizeError):
        Game(-120, 2)


def test_game_create_invalid_fps():
    with pytest.raises(FpsError):
        Game(120, 20, -5)


def test_game_create_empty():
    game = Game()
    assert game.window.get_width() == 1500
    assert game.window.get_height() == 800
    assert game.fps == 60
    assert game.level == 'intro'
    assert game.run is True
    assert len(game.levels) == 6


def test_game_create():
    game = Game(120, 60, 30)
    assert game.window.get_width() == 120
    assert game.window.get_height() == 60
    assert game.fps == 30
    assert game.level == 'intro'
    assert game.run is True
    assert len(game.levels) == 6
