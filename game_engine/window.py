import pygame

class Window:

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def key_check(self, key):
        keys = pygame.key.get_pressed()
        if (keys[key]):
            return True

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

    def clear(self):
        self.screen.fill((0,0,0))
