from src.level1 import Level1
import pygame


def test_level_create():
    pygame.init()
    window = pygame.display.set_mode((1500, 800))
    level1 = Level1(window)
    assert level1.tries == 3
    assert level1.number_of_bodies == 8
    assert level1.number_of_targets == 2
