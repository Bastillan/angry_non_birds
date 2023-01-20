import pygame


class GameStage:
    """
    Class GameStage.
    Contains attributes:

    :param wall_color: background wall's color
    :type wall_color: str

    :param window: pygame's window
    :type window: pygame.Surface

    :param width: window's width
    :type width: int

    :param height: window's height
    :type height: int
    """
    def __init__(self, window: pygame.Surface) -> None:
        """
        Creates instance of the GameStage.
        """
        self._wall_color = 'white'
        self._window = window
        width, height = pygame.display.get_window_size()
        self._width = width
        self._height = height

    def draw(self) -> None:
        """Displays GameStage on window."""
        self.window.fill(self.wall_color)
        pygame.display.update()

    def action(self, event: pygame.event.Event) -> str:
        """
        Handles events.
        Returns 'next_level' if mouse was clicked otherwise eturns 'level'
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            return 'next_level'
        return 'level'

    @property
    def wall_color(self) -> str:
        """Returns background color."""
        return self._wall_color

    @property
    def window(self) -> pygame.Surface:
        """Returns window."""
        return self._window

    @property
    def width(self) -> int:
        """Returns width."""
        return self._width

    @property
    def height(self) -> int:
        """Returns height."""
        return self._height
