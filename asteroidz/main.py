import pygame
import sys
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,PLAYER_RADIUS
from logger import log_state,log_event
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    VERSION = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = int(SCREEN_WIDTH / 2)
    y = int(SCREEN_HEIGHT / 2)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.container = (shots)
    player = Player(x,y)    
    field = AsteroidField()
    print(f"Player Radius: {player.radius}")
    print(f"Player XY: {player.position}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        updatable.update(dt)
        for aster in asteroids:
            if aster.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000
        
        
if __name__ == "__main__":
    main()
