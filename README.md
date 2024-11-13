Asteroids Game
A classic asteroid-shooter game built with Python and Pygame. Destroy asteroids while avoiding collisions in a dynamic space environment! Inspired by the classic arcade game, this version includes bullet physics, asteroid splitting mechanics, and a player-controlled spaceship with a firing cooldown.

Table of Contents
Game Objective
Features
Installation
How to Play
Controls
Game Mechanics
Asteroids
Bullets
Project Structure
Future Enhancements
License
Game Objective
Navigate your spaceship through space while shooting and destroying asteroids. Each large asteroid breaks into smaller, faster-moving asteroids, increasing the challenge as you progress. The goal is to survive as long as possible and rack up a high score by destroying asteroids.

Features
Asteroid Splitting: Large asteroids split into two medium-sized asteroids, and medium asteroids split into small ones.
Bullet Mechanics: The player has a cooldown between shots, preventing continuous shooting.
Collision Detection: Bullets destroy asteroids, and collisions with asteroids end the game.
Dynamic Difficulty: Smaller asteroids move faster, adding to the challenge.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/asteroids_game.git
Navigate to the directory:

bash
Copy code
cd asteroids_game
Create a virtual environment (optional but recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the game:

bash
Copy code
python main.py
How to Play
Move your spaceship to avoid oncoming asteroids.
Shoot at the asteroids to destroy them, but beware: large and medium asteroids split into smaller, faster ones when hit.
Survive as long as you can without colliding with any asteroids!
Controls
Left Arrow / A: Rotate the spaceship left
Right Arrow / D: Rotate the spaceship right
Spacebar: Shoot bullets (with a cooldown of 0.3 seconds)
Game Mechanics
Asteroids
Asteroids come in three sizes: large, medium, and small.

Large Asteroids: Split into two medium asteroids when destroyed.
Medium Asteroids: Split into two small asteroids when destroyed.
Small Asteroids: Disappear when destroyed.
Each smaller asteroid moves slightly faster than the previous one, making the game progressively challenging.

Bullets
Bullets are shot in the direction the player is facing.
A bullet can only be fired every 0.3 seconds due to a cooldown mechanism.
Bullets destroy asteroids upon collision, with larger asteroids splitting into smaller ones.
Project Structure
plaintext
Copy code
asteroids_game/
├── asteroid.py          # Contains the Asteroid class and splitting mechanics
├── asteroidfield.py     # Manages the spawning of initial asteroids
├── constants.py         # Holds game constants (e.g., screen size, speeds)
├── main.py              # Main game loop and initialization
├── player.py            # Contains the Player class with movement and shooting mechanics
├── shot.py              # Bullet class with collision handling
├── circleshape.py       # Base class for circular game objects (Player, Asteroids, Shots)
└── README.md            # Game description and setup instructions
Future Enhancements
Scoring System: Add a scoring system to display points for each asteroid destroyed.
Lives or Shields: Add a limited number of lives or temporary shields for more dynamic gameplay.
Enhanced Graphics: Use textures or sprites for the spaceship and asteroids to improve visual appeal.
Background Music and Sound Effects: Add sound effects for shooting, explosions, and background music to enhance the gaming experience.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Additional Notes
Feel free to modify the game and experiment with new features! Contributions are welcome, so if you have ideas or improvements, please open an issue or submit a pull request.
