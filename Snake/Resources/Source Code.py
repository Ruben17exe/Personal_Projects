import sys
import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()
font = pygame.font.SysFont("calibri", 16)
Point = namedtuple("Point", "x, y")

score_txt_read = open("Resources/memory_score.txt", "r")
highest_score = score_txt_read.read()
score_txt_read.close()


class Constant(Enum):
    # Directions
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    # Color: Food
    RED = (200, 0, 0)
    YELLOW = (255, 255, 0)
    # Color: Snake's Tail
    BLUE1 = (0, 0, 255)
    BLUE2 = (0, 100, 255)
    # Color: Snake's Head
    BROWN = (166, 83, 0)
    ORANGE = (255, 128, 64)
    # Color: Text
    GREEN = (128, 255, 0)

    BLOCK_SIZE = 20
    SPEED = 7


class SnakeGame:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h

        self.display = pygame.display.set_mode((self.w, self.h))
        self.background = pygame.image.load("Resources/Images/Tapete.png")
        icon = pygame.image.load("Resources/Images/Snake Icono Ventana.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

        self.direction = Constant.RIGHT

        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head,
                      Point(self.head.x-Constant.BLOCK_SIZE.value, self.head.y),
                      Point(self.head.x-(2*Constant.BLOCK_SIZE.value), self.head.y)]

        self.score = 0
        self.food = None
        self._place_food()

        pygame.draw.line(self.display, Constant.WHITE.value, (20, 20), (20, 460))

    def _place_food(self):
        x = random.randint(1, (self.w - Constant.BLOCK_SIZE.value - 20) // Constant.BLOCK_SIZE.value) * Constant.BLOCK_SIZE.value
        y = random.randint(1, (self.h - Constant.BLOCK_SIZE.value - 20) // Constant.BLOCK_SIZE.value) * Constant.BLOCK_SIZE.value

        self.food = Point(x, y)

        if self.food in self.snake:
            self._place_food()

    def play_step(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.direction != Constant.RIGHT:
                    self.direction = Constant.LEFT
                    break
                elif event.key == pygame.K_RIGHT and self.direction != Constant.LEFT:
                    self.direction = Constant.RIGHT
                    break
                elif event.key == pygame.K_UP and self.direction != Constant.DOWN:
                    self.direction = Constant.UP
                    break
                elif event.key == pygame.K_DOWN and self.direction != Constant.UP:
                    self.direction = Constant.DOWN
                    break
        print(self.direction)
        self._move(self.direction)
        self.snake.insert(0, self.head)

        game_over = False

        if self._is_collision():
            game_over = True
            print("Is collision")
            return game_over, self.score

        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()

        self._update_ui()
        self.clock.tick(Constant.SPEED.value)

        return game_over, self.score

    def _is_collision(self):
        if self.head.x > self.w - Constant.BLOCK_SIZE.value - 20 or self.head.x < 20 or self.head.y > self.h - Constant.BLOCK_SIZE.value - 20 or self.head.y < 20:
            return True
        if self.head in self.snake[1:]:
            return True

        return False

    def _update_ui(self):
        self.display.blit(self.background, (0, 0))

        for index, pt in enumerate(self.snake):
            if index == 0:
                pygame.draw.rect(self.display, Constant.BLACK.value, pygame.Rect(pt.x, pt.y, Constant.BLOCK_SIZE.value, Constant.BLOCK_SIZE.value))
                pygame.draw.rect(self.display, Constant.ORANGE.value, pygame.Rect(pt.x+4, pt.y+4, 12, 12))
            elif index % 2 == 0:
                pygame.draw.rect(self.display, Constant.BLACK.value, pygame.Rect(pt.x, pt.y, Constant.BLOCK_SIZE.value, Constant.BLOCK_SIZE.value))
                pygame.draw.rect(self.display, Constant.BLUE1.value, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))
            elif index % 2 != 0:
                pygame.draw.rect(self.display, Constant.BLACK.value, pygame.Rect(pt.x, pt.y, Constant.BLOCK_SIZE.value, Constant.BLOCK_SIZE.value))
                pygame.draw.rect(self.display, Constant.BLUE2.value, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))

        pygame.draw.circle(self.display, Constant.RED.value, (self.food.x + 10, self.food.y + 10), 10)
        pygame.draw.circle(self.display, Constant.YELLOW.value, (self.food.x + 10, self.food.y + 10), 7)

        text1 = font.render("Score: " + str(self.score), True, Constant.GREEN.value)
        self.display.blit(text1, [40, 5])

        text2 = font.render("Highest Score: " + highest_score, True, Constant.GREEN.value)
        self.display.blit(text2, [460, 5])

        pygame.display.flip()

    def _move(self, direction):
        x = self.head.x
        y = self.head.y

        if direction == Constant.RIGHT:
            x += Constant.BLOCK_SIZE.value
        elif direction == Constant.LEFT:
            x -= Constant.BLOCK_SIZE.value
        elif direction == Constant.DOWN:
            y += Constant.BLOCK_SIZE.value
        elif direction == Constant.UP:
            y -= Constant.BLOCK_SIZE.value

        self.head = Point(x, y)


if __name__ == "__main__":
    game = SnakeGame()

    while True:
        game_over, score = game.play_step()

        if game_over:
            break

    if int(highest_score) < score:
        score_txt_write = open("Resources/memory_score.txt", "w")
        score_txt_write.write(str(score))
        score_txt_write.close()

    print("Final Score = ", score)
    pygame.quit()
