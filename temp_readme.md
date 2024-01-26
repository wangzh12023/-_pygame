# Team RuYou's Game  
![Static Badge](https://img.shields.io/badge/RuYou-purple)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/t/wangzh12023/RuYou_Game)
![GitHub contributors](https://img.shields.io/github/contributors-anon/wangzh12023/RuYou_Game)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/wangzh12023/RuYou_Game)

####  :tada::dizzy: _This project is a game developed by the `"RuYou"` team using the `pygame` library with the `python` language. It is a simple game that combines various game elements and game art design.Hope you can have fun in our Game!_ :kissing_heart::kissing_heart::kissing_heart:

## Content 📑：
> - [Team Introduction](## "Our Team Members")
> - [Project Introduction](## "Poject introduction")
>   - [Game Name](### "1、Game Name :dart:")
>   - [Project File Arrangement](### "Project File Arrangement")
>   - [Game Composition](### "Game Composition(A version of the reference `teafrogsf` 's slides) :triangular_flag_on_post:")



## Our Team Members
Here are the contributors :clap::arrow_down:

<!-- ![](https://contrib.rocks/image?repo=wangzh12023/RuYou_Game) -->
<a href="https://contrib.rocks/image?repo=wangzh12023/RuYou_Game">
  <img src="https://contrib.rocks/image?repo=wangzh12023/RuYou_Game">
</a>
<br><br>

> ![Static Badge](https://img.shields.io/badge/1-blue) :bust_in_silhouette: **王子涵**
> 
> &nbsp;&nbsp;&nbsp;&nbsp; :email: wangzh12023@shanghaitech.edu.cn
>
> ![Static Badge](https://img.shields.io/badge/2-blue) :bust_in_silhouette: **匡鹏昊**
> 
> &nbsp;&nbsp;&nbsp;&nbsp; :email: kuangph2023@shanghaitech.edu.cn
> 
> ![Static Badge](https://img.shields.io/badge/3-blue) :bust_in_silhouette: **陈亦乐**
>
> &nbsp;&nbsp;&nbsp;&nbsp; :email: chenyl2023@shanghaitech.edu.cn

## Poject introduction 
> - Game Brief Introduction
> - Project File Arrangement
> - Game Composition

### Game Brief Introduction
#### 1、Game Name :dart:
- `冤申`
#### 2、Game Type：
- 实时战斗冒险游戏
#### 3、Background：
- 在黑暗的地狱之中，主人公发现自己被困在一片迷宫中。这个迷宫被神秘的力量分成了三个区域，每个区域都寄宿着一枚珍贵的元素印记：草、水、火。这些印记被分散在世界各地，它们的力量似乎是主人公唯一逃脱地狱的钥匙。主人公知道，只有当他收集齐这三枚印记并带回最终迷宫的深处，才能打破被困的诅咒，离开这片阴森的地方。但地狱不是轻松的考验，而是一个充满危险和谜团的领域。随着主人公逐渐收集到草水火三种元素印记，他的力量也在不断增强。草印记赋予他自然的恢复能力，水印记让他能够掌握水的流动和净化之力，火印记则点燃了他的武力，使他能够驾驭熊熊的烈焰。然而，随着主人公的成长，地狱中的敌人也逐渐察觉到他的存在。他们开始变得更加狡猾和强大，随着时间的推移，地狱中的每个角落都弥漫着危险。主人公必须谨慎行事，不断提升自己的实力，以抵御即将到来的更为恶劣的挑战。在这片深邃的地狱，主人公的命运和三枚元素印记交织在一起，谜题的答案隐匿在每个迷宫的深处。只有通过勇气、智慧和力量的融合，主人公才能解开这场神秘的诅咒，带着元素印记的力量迎接最终的考验，摆脱地狱的束缚，回到属于他的世界。
#### 4、Map Settings 🗺️：
- 分为一个主地图和三个迷宫地图以及三个boss地图，游戏开始时玩家出生在主地图,并且玩家可以通过不同的传送门进入不同的迷宫地图，在迷宫地图，玩家可以打小怪并且需要通过自己的智慧找到boss们入口。
##### a) Main Map
  - 主地图是主人公初始存在的地图，会有多个NPC :neckbeard: 提供引导主人公进入不同的地图进行行动，可以与玩家进行交互并且交代故事情节。
  - 同时存在商店，供玩家购买。
  - 同时还存在三个传送门，主人公通过与主地图中的石雕接近来进入不同的迷宫地图。
  - 无论打 :imp: 失败与否，在迷宫地图之旅结束后都会先传送到主地图。在玩家通过对应迷宫后该传送门会消失。
##### b) Maze Map
  - 每个迷宫地图都有一些小怪和障碍物，只有消灭小怪并且找到BOSS入口才能进入BOSS地图与 :imp: 进行战斗。（玩家一旦进入BOSS战斗区便不能出来）
  - 迷宫的障碍物和小怪位置是随机的，会有一个检测功能（`BFS`）来确保主人公能够抵达 :imp: 所在地。（确保迷宫是可以走出的）
  - 触碰到障碍物墙壁无法穿越。
  - BOSS可以移动并且可以向四面八方攻击，小怪是在小范围移动的并且不具备攻击能力。
  - 含有宝箱
  - ❗请尽可能多的击杀小怪以获得更多的金币提高防御、血量或者攻击值，否则在下一关的boss对战中可能会很困难。
##### c) Boss Map
  - 不同的地图Boss不同，并且会有不同的攻击方式：
    - 碰撞攻击：与Boss接触后会损失血量值
    - 技能攻击：被Boss发出的攻击波击中会损失血量值
    - Boss技能：移速增快，发出攻击波，在地图中随机生成旋涡波。
#### 5、 Character Moving Settings :man: ：
  - 当主人公远离地图边界时，主人公坐标始终位于镜头中央，镜头移动；靠近地图边界时镜头保持固定，主人公坐标移动。
#### 6、 Battle Settings：
  - 通用设置：
    每通过一关的 :imp: ，下一关的 :imp: 血量和攻击力会增加，如果战胜 :imp: ，则人物的攻击和血量也会增加
  - 主人公设置：
    主人公的属性为血量值和攻击力。
  - 敌人设置：
    每个敌人拥有固定的血量值和攻击力，在生成所属地图的同时生成。
#### 7、Game Operation :dart:
##### :o: You can click "Q" in game to check some basic game operation rules
- Move: "W","A","S","D" (Represents respectely up,left,down,right)
- Attack: "⬆️","⬇️","⬅️","➡️" (Represents respectely up,left,down,right)
- Help: "Q"
- In dialogbox, you can use "ENTER" to go next
- In shop, you can use "W","S" to choose what you want

### Project File Arrangement
- Attributes.py
    - It is aimed to determine whether the event `collide` occurs
        - Tips : classes maybe collided : obstacle / npc / boss / monster / portal
           
- BgmPlayer.py
    - It is aimed to play 3 different BGMs : CITY / WILD_GRASS / BOSS_GRASS.
        - Tips : The BGM played now determined with current SceneType of the player.
        
- GameManager.py
    - The most important part,which is aimed to manage the whole game,such as:
        - update  all  scenes / characters / events / BMGs
        - render all scenes / characters / events
        - flush or reset scenes, if your SceneType changes
        - and so on

- Guide.py
    - It is aimed to generate and update the guideboard at the left top corner.
    - such as:“ 按‘Q’打开操作指南 ”

- Main.py
    - The main manager of the game,which is aimed to update the display window / call GameManager to update and render the game
    
- Maps.py
    - It is aimed to generate:
        - Maps for different scenes
        - Obstacles for different sences
    - Moreover,we use Breadth-First Search to determine whether the random-generated obstacles are appropriate

- NPCs.py
    - It is aimed to generate four types of NPC characters:
        - DialogNpc, which can talk with player
        - ShopNPC, which can transaet with player
        - Monster, which moves randomly and player will lose HP if collided with them
        - Boss, which always moves towards the player and can attack player with bullet

- Player.py
    - It is aimed to define all characteristics of the player and update it.Such as:
        - Parameters : HP / speed / directions and so on
        - Special images : Hold and turns the direction of guns according to the moving direction and so on
        - Abilities : Attack with gun / dialog with NPC and so on
        - and so on

- PopUpBox.py
    - It is aimed to generate dialogbox / shopbox and update them.

- Portal.py
    - It is aimed to generate Portals in different maps:
        - in CITY_MAP : Transmit player to the corresponding WILD_MAP
        - in WILD_MAP : Transmit player to the BOSS_MAP
        - in BOSS_MAP : Transmit player to the CITY_MAP

- Scene.py
    - It is aimed to generate all the things related to scenes of the game.Such as:
        - The updating of the camara
        - CityScene / WildScene / BossScene
        - GameOverScene
        - StartCG : “冤申”
        - StartMenu : “Press To Enter”

- Settings.py
    - It is aimed to define all the settings of the game, such as some basic attirbutes and some numbers.

- StatusBar.py
    - It is aimed to generate and update all the states of characters. Such as:
        - HP / Money / Attack / Defence of the player
        - The Blood-State-Bar of the boss




### Game Composition(A version of the reference `teafrogsf` 's slides) :triangular_flag_on_post:

#### Characters :triangular_flag_on_post:
- #### A main character :boy: ➡️ A knight  with a gun :gun: 
- #### Two different friendly NPCs :neckbeard: ➡️ You can see in the main map
- #### A simple enemy :imp: ➡️ Some monsters in wild map
- #### A special enemy :imp: ➡️ Three bosses in boss map

#### Game Machanics :wrench:
- Core mechanics ➡️ We use `EVENT` to determine which state the player is in and to finish generating the right scene.
- Collision system ➡️ When player, npcs and the monsters collide with some barriers, they will stay still or just change the directions.
- Resource system ➡️ We use the `random` module to generate the map,obstacles and monsters. And at the same time, we use `'BFS'` to ensure the player can reach the `boss map`.
#### Gameplay ⚔️
- Main menu ➡️ When you start the game, the window will automatically display a tween animation `冤申`, after which you can see the game starter page.
- BGM ➡️ When you enter different maps, the bgmplayer will play different music. So, enjoy your fantastic tour in our game!
#### Code 📖
- In each file, we have some brief introductions of the code, illustrating the `classes and funciton`  🌟
- We adopt a strategy of code encapsulation, which can help you understand our code more easily 🌟












