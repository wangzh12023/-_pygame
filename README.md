# Team RuYou's Game  
:heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark:Game_Template is a temporory version, project_file is the final version,but it has not been finished. You can just pull Game_Template tempororily

![Static Badge](https://img.shields.io/badge/RuYou-purple)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/t/wangzh12023/RuYou_Game)
![GitHub contributors](https://img.shields.io/github/contributors-anon/wangzh12023/RuYou_Game)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/wangzh12023/RuYou_Game)

####  :tada::dizzy: _This project is a game developed by the `"RuYou"` team using the `pygame` library with the `python` language. It is a simple game that combines various game elements and game art design.Hope you can have fun in our Game!_ :kissing_heart::kissing_heart::kissing_heart:

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

### 一、Game Name :dart:
- `Marked Odyssey`
### 二、Game Type：
- 回合制战斗冒险游戏
### 三、Main Process：
- 因为某种原因，主人公需要收集散落在世界各地的三枚元素印记（草水火），三种印记在三个迷宫的最终 :imp: 手中，伴随着对印记的收集，主人公会逐渐变强，但敌人同时也会不断变强。收集完三个印记后，主人公将面对最终 :imp: ，胜利后游戏结束。
### 四、Map Settings 🗺️：
- 分为一个主地图和三个迷宫地图，游戏开始时玩家出生在主地图。
#### 1. Main Map
  - 主地图是主人公初始存在的地图，会有一个NPC :neckbeard: 提供引导主人公进入不同的地图进行行动，可以与玩家进行交互并且交代故事情节。
  - 同时还存在三个石雕，主人公通过与主地图中的石雕接近来进入不同的迷宫地图。
  - 无论打 :imp: 失败与否，在迷宫地图之旅结束后都会先传送到主地图。在玩家通过对应迷宫后该石雕上的图案会亮起，靠近后会提示该印记已经获得但无法再次进入该迷宫。否则，该石雕将不会有变化。
#### 2. Maze Map
  - 每个迷宫地图都有一些小怪和障碍物，只有消灭小怪并且找到BOSS入口才能进入BOSS战斗区与 :imp: 进行战斗。（玩家一旦进入BOSS战斗区便不能出来）
  - 迷宫的障碍物和小怪位置是随机的，会有一个检测功能来确保主人公能够抵达 :imp: 所在地。（确保迷宫是可以走出的）
  - 触碰到障碍物墙壁无法穿越。
  - BOSS可以移动并且可以向四面八方攻击，小怪是在小范围移动的并且不具备攻击能力。
### 五、 Character Moving Settings :man: ：
  - 当主人公远离地图边界时，主人公坐标始终位于镜头中央，镜头移动；靠近地图边界时镜头保持固定，主人公坐标移动。
### 六、 Battle Settings：
  - 通用设置：
    每通过一关的 :imp: ，下一关的 :imp: 血量和攻击力会增加，如果战胜 :imp: ，则人物的攻击和血量也会增加
  - 主人公设置：
    主人公的属性为血量值和攻击力。
  - 敌人设置：
    每个敌人拥有固定的血量值和攻击力，在生成所属地图的同时生成。
## Project File Arrangement

> #### This project contains some files below:
> - Main.py (run game)
> - SceneManager.py (which is used to centrally manage the following files for image generation)
>   - Map.py   (generate map)
>   - Player.py (set player's attributes)
>   - NPC.py (set NPC's attributes)
>   - Monster.py (set monster's attibutes)
>   - Diologue.py (set diologue)
>   - Battle.py (make battle effects)







