import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""

        #ai_game input gives Ship access to all the game resources defined in AlienInvasion
        #(AlienInvasion is a class defined in alien_invasion.py)
        self.screen = ai_game.screen #Accessing the screen attribute of the AlienInvasion class
        #^This allows us to easily access it with the methods of this class
        self.screen_rect = ai_game.screen.get_rect() #Accessing the screen's rect attribute, allowing us to place the ship at the correct position

        # Load the ship image and get its rect.
        self.image = pygame.image.load('Project1_AlienInvasion/images/ship.bmp')
        self.rect = self.image.get_rect() #Getting the ship's 'rectangle' values so we can better position it 

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom #Assigning a variable of the middle bottom of the ship as the middle bottom of the screen 

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right:
            self.rect.x += 1

        if self.moving_left:
            self.rect.x -= 1
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) #'Draws' the ship at the position determined
        #'blit' essentially means 'draw on top of'
        #blit is an inbuilt method of the Pygame library in Python