import pygame
import random
import sys

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.width = 400
        self.height = 400
        self.block_size = 20
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 35)
        self.small_font = pygame.font.SysFont(None, 25)
        self.reset_game()

    def reset_game(self):
        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = (0, -self.block_size)
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False

    def generate_food(self):
        while True:
            x = random.randint(0, (self.width // self.block_size) - 1) * self.block_size
            y = random.randint(0, (self.height // self.block_size) - 1) * self.block_size
            if (x, y) not in self.snake:
                return (x, y)

    def draw_grid(self):
        for x in range(0, self.width, self.block_size):
            pygame.draw.line(self.screen, (200, 200, 200), (x, 0), (x, self.height))
        for y in range(0, self.height, self.block_size):
            pygame.draw.line(self.screen, (200, 200, 200), (0, y), (self.width, y))

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), (*segment, self.block_size, self.block_size))

    def draw_food(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (*self.food, self.block_size, self.block_size))

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))

    def draw_game_over(self):
        game_over_text = self.font.render("Game Over!", True, (255, 0, 0))
        restart_text = self.small_font.render("Press R to Restart or Q to Quit", True, (0, 0, 0))
        self.screen.blit(game_over_text, (self.width // 2 - 80, self.height // 2 - 50))
        self.screen.blit(restart_text, (self.width // 2 - 120, self.height // 2))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if self.game_over:
                        if event.key == pygame.K_r:
                            self.reset_game()
                        elif event.key == pygame.K_q:
                            running = False
                    else:
                        if event.key == pygame.K_UP and self.direction != (0, self.block_size):
                            self.direction = (0, -self.block_size)
                        elif event.key == pygame.K_DOWN and self.direction != (0, -self.block_size):
                            self.direction = (0, self.block_size)
                        elif event.key == pygame.K_LEFT and self.direction != (self.block_size, 0):
                            self.direction = (-self.block_size, 0)
                        elif event.key == pygame.K_RIGHT and self.direction != (-self.block_size, 0):
                            self.direction = (self.block_size, 0)

            if not self.game_over:
                new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
                if (new_head in self.snake or
                    new_head[0] < 0 or new_head[0] >= self.width or
                    new_head[1] < 0 or new_head[1] >= self.height):
                    self.game_over = True
                else:
                    self.snake.insert(0, new_head)
                    if new_head == self.food:
                        self.score += 1
                        self.food = self.generate_food()
                    else:
                        self.snake.pop()

            self.screen.fill((255, 255, 255))
            self.draw_grid()
            self.draw_snake()
            self.draw_food()
            self.draw_score()
            if self.game_over:
                self.draw_game_over()
            pygame.display.flip()
            self.clock.tick(5)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
