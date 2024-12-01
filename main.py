import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
# Stuff before the game loop starts
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock = pygame.time.Clock()

   updatable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroids = pygame.sprite.Group()
   shots = pygame.sprite.Group()

   Player.containers = (updatable, drawable)
   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

   Asteroid.containers = (updatable, drawable, asteroids)
   Shot.containers = (shots, updatable, drawable)

   AsteroidField.containers = (updatable)
   asteroid_field = AsteroidField()


   dt = 0
   
# Game loop
   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return
         
      for obj in updatable:
         obj.update(dt)

      for asteroid in asteroids:
         if player.collision(asteroid):
            print("Game Over!")
            exit()

         for shot in shots:
            if shot.collision(asteroid):
               asteroid.split()
               shot.kill()


      screen.fill("black")

      for obj in drawable:
         obj.draw(screen)

      pygame.display.flip()

         # limit the frame rates to 60 fps.
      dt = clock.tick(60) / 1000


# Stuff after the game loop ends



# Run the main function
if __name__ == "__main__":
   main()