# Game Introduction  

## Content 📑：

- [Game Operation](## "Game Operation :dart:" )
- [Game Composition](## "Game Composition :triangular_flag_on_post:")
- [Game File Manage](## "Game File Manage :rocket: ")

## Game Operation :dart:

##### :o: You can clck "Q" in game to check some basic game operation rules
- Move: "W","A","S","D" (Represents respectely up,left,down,right)
- Attack: "I","J","M","K" (Represents respectely up,left,down,right)
- Help: "Q"


## Game Composition :triangular_flag_on_post:
### Characters :triangular_flag_on_post:
- #### A main character :boy: ➡️ A knight  with a gun :gun: 
- #### Two different friendly NPCs :neckbeard: ➡️ You can see in the main map
- #### A simple enemy :imp: ➡️ Some monsters in wild map
- #### A special enemy :imp: ➡️ Three bosses in boss map

### Game Machanics :wrench:
- Core mechanics ➡️ 
- Collision system ➡️ When player, npcs and the monsters collide with some barriers, they will stay still or just change the directions.
- Resource system ➡️ 
### Gameplay ⚔️
- Main menu ➡️ When you start the game, the window will automatically display a tween animation `冤申`, after which you can see the game starter page.
- BGM ➡️ When you enter different maps, the bgmplayer will play different music. So, enjoy your fantastic tour in our game!

### Code 📖
- Very nice! 🌟

## Game File Manage :rocket: 
- Attributes.py
    - It is aimed to determine whether the event:collide occurs
        - Tips : classes maybe collided : obstacle / npc / boss / monster / portal        
- BgmPlayer.py
    - It is aimed to play 3 different BGMs : CITY / WILD_GRASS / BOSS_GRASS.
        - Tips : The BGM played now determined with current SceneType of the player.
- GameManager.py
    - The most important part,which is aimed to manage the whole game,such as:
        - update  all  scenes / characters / events / BMGs
        - render all scenes / characters / events
        - flush or reset scenes,if your SceneType changes
        - and so on

- Guide.py
- Main.py
    - The main manager of the game,which is aimed to update the display window / call GameManager to update and render the game
- Maps.py
- NPCs.py
- Player.py
- PopUpBox.py
- Portal.py
- Scene.py
- Settings.py
- StatusBar.py


