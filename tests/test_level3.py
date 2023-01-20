from src.level3 import Level3
import pygame


def test_level_create():
    pygame.init()
    window = pygame.display.set_mode((1500, 800))
    level3 = Level3(window)
    assert level3.tries == 2
    assert level3.number_of_bodies == 13
    assert level3.number_of_targets == 3
