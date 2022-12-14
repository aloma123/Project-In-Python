# game setup
WIDTH    = 900	
HEIGTH   = 600
FPS      = 60
TILESIZE = 64
HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
	'invisible': 0}

# ui 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# weapons 
weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':'../graphics/weapons/sword/full.png'},
	'lance': {'cooldown': 400, 'damage': 30,'graphic':'../graphics/weapons/lance/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic':'../graphics/weapons/axe/full.png'},
	'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'../graphics/weapons/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 10, 'graphic':'../graphics/weapons/sai/full.png'}}

# magic
magic_data = {
	'flame': {'strength': 5,'cost': 20,'graphic':'../graphics/particles/flame/fire.png'},
	'heal' : {'strength': 20,'cost': 10,'graphic':'../graphics/particles/heal/heal.png'}}

# enemy
monster_data = {
	'bat': {'health': 60,'exp': 25, 'damage':18,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 6, 'resistance': 3, 'attack_radius': 100, 'notice_radius': 350},
	'blackwing': {'health': 120,'exp': 50,'damage':30,'attack_type': 'claw',  'attack_sound':'../audio/attack/claw.wav','speed': 5, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 400},
	'raccoon': {'health': 900,'exp': 200,'damage':85,'attack_type': 'claw',  'attack_sound':'../audio/attack/claw.wav','speed': 3, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'goldcrab': {'health': 1000,'exp': 250,'damage':90,'attack_type': 'thunder', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 150, 'notice_radius': 200},
	'icecrab': {'health': 75,'exp': 35,'damage':15,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 5, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 280},
	'lavacrab': {'health': 75,'exp': 40,'damage':15,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 5, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 280},
	'blackbear': {'health': 350,'exp': 80,'damage':35,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 70, 'notice_radius': 210},
	'icebear': {'health': 400,'exp': 100,'damage':40,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 70, 'notice_radius': 230},
	}
