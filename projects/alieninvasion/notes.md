#### Description:

This project is a small alien invasion created in pygame. So far, the player can move, shoot bullets, and the alien combatants move from left to right along a fixed grid. More to come!

#### Notes:

 - main.py has the core gameplay logic, and will be added to over time.
 - settings.py has the main gameplay settings and will be changed over time as new features are added to main.py
 - ship.py draws the ship to the screen.
 - game_functions.py controls and detects user inputs and other game functions.
 - Text is rendered to the screen using the pygame.font module.

#### Difficulty:

The games difficulty will increase in conujunction with the amount of waves completed, using a 1.5x modifier, as set in settings.py


 #### Settings:

 Most settings are controlled through settings.py, this includes the screen bounds, background, and ship settings, these are then imported to various files to keep everything separate and tidy.

 - self.ship_speed_factor controls the ship speed and can take decimal values.
 - The game will start inactive as default, so that a main menu can be used.


 #### Current Bugs:

