import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = updatables
    Shot.containers = (updatables, drawables, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            # window close button
            if event.type == pygame.QUIT:
                return
            
        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.isColliding(player):
                raise SystemExit("Game Over!")
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.isColliding(shot):
                    asteroid.kill()
                    shot.kill()
                    asteroid.split()

        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    



if __name__ == "__main__":
    main()
