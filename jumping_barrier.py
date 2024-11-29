import pygame

class Barrier:
    def __init__(self, ground):
        # Random Size
        self.barrier_size1_x = 40
        self.barrier_size1_y = 50
        # self.barrier_size2_x = random.randint(30, 50)
        # self.barrier_size2_y = random.randint(30, 50)

        # Positions
        self.ground = ground
        self.barrier1_x, barrier1_y = 300, 233
        # self.barrier2_x, barrier2_y = 200, ground

        # Barrier Images
        self.barrier1 = pygame.transform.scale(pygame.image.load("jumping_photo/triangle1.png"),
                                          (self.barrier_size1_x, self.barrier_size1_y))
        # self.barrier2 = pygame.transform.scale(pygame.image.load("jumping_photo/triangle2.png"),
        #                                   (self.barrier_size2_x, self.barrier_size2_y))