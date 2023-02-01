import pygame
import numpy as np
from pygame.locals import *
import random

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode([1300,800])
        self.background = pygame.image.load("background.jpg")
        self.background = pygame.transform.scale(self.background,(1300,800))
        self.running = True
        self.height = 23
        self.width = 15
        self.square_length = 25
        self.font70 = pygame.font.SysFont("Showcard Gothic", 70, False)
        self.font50 = pygame.font.SysFont("Showcard Gothic", 50, False)
        self.font30 = pygame.font.SysFont("Showcard Gothic", 30, False)

        self.board_surf1 = pygame.Surface([self.width*self.square_length,self.height*self.square_length])
        self.board_surf1.fill((0,0,0))
        self.board_rect1 = self.board_surf1.get_rect(center = (350,450))

        self.board_surf2 = pygame.Surface([self.width * self.square_length, self.height * self.square_length])
        self.board_surf2.fill((0, 0, 0))
        self.board_rect2 = self.board_surf2.get_rect(center=(950, 450))

        self.f_block1_surf = pygame.Surface([int(self.width*self.square_length/3)+5,int(self.width*self.square_length/3)+5])
        self.f_block1_surf.fill((0,0,0))
        self.f_block1_rect = self.f_block1_surf.get_rect(center = (200,75))

        self.score1_surf = self.font30.render(f"Score: {0}",True,(0,0,255))
        self.score1_rect = self.score1_surf.get_rect(center= (400,40))

        self.used_block1_surf = self.font30.render(f"Used Blocks: {0}",True,(255,0,255))
        self.used_block1_rect = self.used_block1_surf.get_rect(center = (400,100))

        self.f_block2_surf = pygame.Surface([int(self.width*self.square_length/3)+5,int(self.width*self.square_length/3)+5])
        self.f_block2_surf.fill((0, 0, 0))
        self.f_block2_rect = self.f_block2_surf.get_rect(center=(1100, 75))

        self.score2_surf = self.font30.render(f"Score: {0}", True, (0, 0, 255))
        self.score2_rect = self.score2_surf.get_rect(center=(900, 40))

        self.used_block2_surf = self.font30.render(f"Used Blocks: {0}", True, (255, 0, 255))
        self.used_block2_rect = self.used_block2_surf.get_rect(center=(900, 100))

        self.time = 0
        self.speed = 1
        self.time_of_timer = 0

        self.time_writing_surf = self.font50.render("TIME",True,(0,255,0))
        self.time_writing_rect = self.time_writing_surf.get_rect(center=(650, 50))

        self.speed_writing_surf = self.font50.render("SPEED", True, (255, 150, 0))
        self.speed_writing_rect = self.speed_writing_surf.get_rect(center=(650, 200))

        self.time_surf = self.font50.render(f"{int(self.time)}",True,(0,255,0))
        self.time_rect = self.time_surf.get_rect(center=(650, 110))

        self.speed_surf = self.font50.render("x{:.2f}".format(self.speed), True, (255, 150, 0))
        self.speed_rect = self.speed_surf.get_rect(center=(650, 310))

        self.screen.blit(self.board_surf1, self.board_rect1)
        self.screen.blit(self.f_block1_surf, self.f_block1_rect)
        self.screen.blit(self.score1_surf, self.score1_rect)
        self.screen.blit(self.used_block1_surf, self.used_block1_rect)

        self.screen.blit(self.board_surf2, self.board_rect2)
        self.screen.blit(self.f_block2_surf, self.f_block2_rect)
        self.screen.blit(self.score2_surf, self.score2_rect)
        self.screen.blit(self.used_block2_surf, self.used_block2_rect)

        self.screen.blit(self.time_writing_surf, self.time_writing_rect)
        self.screen.blit(self.time_surf, self.time_rect)
        self.screen.blit(self.speed_writing_surf, self.speed_writing_rect)
        self.screen.blit(self.speed_surf, self.speed_rect)

    def loop(self):
        self.clock = pygame.time.Clock()
        self.timer = 0
        while self.running:

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            self.time_and_speed_update()
            self.score_update()
            self.used_block_number_update()
            self.following_block_update()
            self.game_over()

            key_pressed = pygame.key.get_pressed()
            if not player1.game_over:
                player1.update(key_pressed)
            if not player2.game_over:
                player2.update(key_pressed)

            if self.timer != int(self.time_of_timer):
                self.timer = int(self.time_of_timer)



            if not player1.game_over:
                self.board_surf1.fill((0, 0, 0))
                for entity in player1.all_blocks:
                    self.board_surf1.blit(entity.surf, entity.rect)
            if not player2.game_over:
                self.board_surf2.fill((0, 0, 0))
                for entity in player2.all_blocks:
                    self.board_surf2.blit(entity.surf, entity.rect)

            pygame.display.flip()
            self.screen.blit(self.background,(0,0))
            self.time += 1/60
            self.time_of_timer += self.time//30/300 + 1/60
            self.speed = self.time//30*0.2 + 1
            self.clock.tick(60)


    def time_and_speed_update(self):
        self.time_surf = self.font50.render(f"{int(self.time)}", True, (0, 255, 0))
        self.time_rect = self.time_surf.get_rect(center=(650, 110))

        self.speed_surf = self.font50.render("x{:.2f}".format(self.speed), True, (255, 150, 0))
        self.speed_rect = self.speed_surf.get_rect(center=(650, 260))

        self.screen.blit(self.time_surf, self.time_rect)
        self.screen.blit(self.time_writing_surf, self.time_writing_rect)

        self.screen.blit(self.speed_writing_surf, self.speed_writing_rect)
        self.screen.blit(self.speed_surf, self.speed_rect)
    def score_update(self):
        self.score1_surf = self.font30.render(f"Score: {player1.score}", True, (255, 255, 255))
        self.score1_rect = self.score1_surf.get_rect(center=(400, 40))

        self.score2_surf = self.font30.render(f"Score: {player2.score}", True, (255, 255, 255))
        self.score2_rect = self.score2_surf.get_rect(center=(900, 40))

        self.screen.blit(self.score1_surf, self.score1_rect)
        self.screen.blit(self.score2_surf, self.score2_rect)
    def used_block_number_update(self):
        self.used_block1_surf = self.font30.render(f"Used Blocks: {player1.used_block}", True, (255, 0, 255))
        self.used_block1_rect = self.used_block1_surf.get_rect(center=(400, 100))

        self.used_block2_surf = self.font30.render(f"Used Blocks: {player2.used_block}", True, (255, 0, 255))
        self.used_block2_rect = self.used_block2_surf.get_rect(center=(900, 100))

        self.screen.blit(self.used_block1_surf, self.used_block1_rect)
        self.screen.blit(self.used_block2_surf, self.used_block2_rect)
    def game_over(self):
        if player1.game_over:
            surf = self.font70.render("GAME OVER",True,"red")
            rect = surf.get_rect(center= (int(self.board_rect1.width/2),int(self.board_rect1.height/2)))
            self.board_surf1.blit(surf,rect)
        if player2.game_over:
            surf = self.font70.render("GAME OVER", True, "red")
            rect = surf.get_rect(center=(int(self.board_rect2.width / 2), int(self.board_rect2.height / 2)))
            self.board_surf2.blit(surf, rect)


        self.screen.blit(self.board_surf1,self.board_rect1)
        self.screen.blit(self.board_surf2, self.board_rect2)
    def following_block_update(self):
        index = player1.used_block + 1
        shape1 = chosen_shapes_and_colors[index][0]
        color1 = chosen_shapes_and_colors[index][1]
        light_color = [int(i * 5 / 4) if int(i * 5 / 4) <= 255 else 255 for i in color1]
        dark_color = [int(i * 3 / 4) if int(i * 3 / 4) >= 0 else 0 for i in color1]
        surf1 = pygame.Surface([len(shape1)*self.square_length,len(shape1)*self.square_length])
        surf1.fill((0,0,0))
        for i in range(len(shape1)):
            for j in range(len(shape1)):
                if shape1[i,j] == 1:
                    pygame.draw.polygon(surf1, light_color, [(j*self.square_length, i*self.square_length), (j*self.square_length+self.square_length, i*self.square_length), (j*self.square_length+self.square_length, i*self.square_length+self.square_length)])
                    pygame.draw.polygon(surf1, dark_color, [(j*self.square_length, i*self.square_length), (j*self.square_length,i*self.square_length+ self.square_length), (j*self.square_length+self.square_length, i*self.square_length+self.square_length)])
                    pygame.draw.rect(surf1, color1,pygame.Rect(int(self.square_length / 6)+j*self.square_length, int(self.square_length / 6)+i*self.square_length, int(self.square_length / 6 * 4),int(self.square_length / 6 * 4) + 1))

        rect1 = surf1.get_rect(center = (int(self.f_block1_rect.width/2),int(self.f_block1_rect.height/2)) )
        self.f_block1_surf.fill((0,0,0))
        self.f_block1_surf.blit(surf1,rect1)

        index = player2.used_block + 1
        shape2 = chosen_shapes_and_colors[index][0]
        color2 = chosen_shapes_and_colors[index][1]
        light_color = [int(i * 5 / 4) if int(i * 5 / 4) <= 255 else 255 for i in color2]
        dark_color = [int(i * 3 / 4) if int(i * 3 / 4) >= 0 else 0 for i in color2]
        surf2 = pygame.Surface([len(shape2) * self.square_length, len(shape2) * self.square_length])
        surf2.fill((0,0,0))
        for i in range(len(shape2)):
            for j in range(len(shape2)):
                if shape2[i, j] == 1:
                    pygame.draw.polygon(surf2, light_color, [(j * self.square_length, i * self.square_length), (j * self.square_length + self.square_length, i * self.square_length), (j * self.square_length + self.square_length,i * self.square_length + self.square_length)])
                    pygame.draw.polygon(surf2, dark_color, [(j * self.square_length, i * self.square_length), (j * self.square_length, i * self.square_length + self.square_length), (j * self.square_length + self.square_length,i * self.square_length + self.square_length)])
                    pygame.draw.rect(surf2, color2, pygame.Rect(int(self.square_length / 6) + j * self.square_length,int(self.square_length / 6) + i * self.square_length,int(self.square_length / 6 * 4),int(self.square_length / 6 * 4) + 1))

        rect2 = surf2.get_rect(center=(int(self.f_block2_rect.width / 2), int(self.f_block2_rect.height / 2)))
        self.f_block2_surf.fill((0, 0, 0))
        self.f_block2_surf.blit(surf2, rect2)

        self.screen.blit(self.f_block1_surf, self.f_block1_rect)
        self.screen.blit(self.f_block2_surf, self.f_block2_rect)

class Single_block(pygame.sprite.Sprite):
    def __init__(self,position,color,shape_size,player):
        super().__init__()
        self.length = game.square_length
        self.surf = pygame.Surface([self.length,self.length])
        self.moving = True
        self.color = color
        self.player = player1 if player == 1 else player2
        self.button = self.player.button
        self.position = np.array(position)
        self.arr = np.zeros((shape_size,shape_size))
        self.arr[self.position[0],self.position[1]] = 1
        self.rect = self.surf.get_rect()
        self.rect.left = (int(game.width/2)+position[1]-1)*self.length
        self.rect.top = position[0]*self.length
        self.location = [position[0],int(game.width/2)+position[1]-1]
        self.player.board[self.location[0],self.location[1]] = 1
        self.draw()
        self.left_move = 0
        self.right_move = 0
        self.down_move = 0
        self.rotating = 0
    def draw(self):
        light_color = [int(i*5/4) if int(i*5/4) <= 255 else 255 for i in self.color ]
        dark_color = [int(i*3/4) if int(i*3/4) >= 0 else 0 for i in self.color ]
        pygame.draw.polygon(self.surf,light_color,[(0,0),(self.length,0),(self.length,self.length)])
        pygame.draw.polygon(self.surf, dark_color, [(0, 0), (0, self.length), (self.length, self.length)])
        pygame.draw.rect(self.surf, self.color, pygame.Rect(int(self.length/6), int(self.length/6), int(self.length/6*4), int(self.length/6*4)+1))

    def update(self,key_pressed,right,left,rotate):
        self.player.board[self.location[0], self.location[1]] = 0
        if self.moving:
            fall = False
            if game.timer != int(game.time_of_timer):
                self.rect.move_ip(0, self.length)
                self.location[0] += 1
                fall = True

            if key_pressed[self.button[1]] and not fall:
                self.down_move += 1
                if self.down_move == 2:
                    self.down_move = 0
                    self.rect.move_ip(0, self.length)
                    self.location[0] += 1
            else: self.down_move = 0
        if key_pressed[self.button[0]] and left:
            self.left_move += 1
            if self.left_move == 3 or not self.moving:
                self.left_move = 0
                self.rect.move_ip(-self.length, 0)
                self.location[1] -= 1
        else: self.left_move = 0
        if key_pressed[self.button[2]] and right:
            self.right_move += 1
            if self.right_move == 3 or not self.moving:
                self.right_move = 0
                self.rect.move_ip(self.length, 0)
                self.location[1] += 1
        else: self.right_move = 0
        if key_pressed[self.button[3]] and rotate:
            self.rotating += 1
            if self.rotating == 10:
                self.rotating = 0
                self.rotate()

    def location_after_rotate(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr)):
                if np.rot90(self.arr)[i,j] == 1:
                    new_position = np.array([i,j])
                    return new_position

    def rotate(self):
        self.player.board[self.location[0],self.location[1]] = 0
        new_position = self.location_after_rotate()
        self.arr = np.rot90(self.arr)
        move = new_position - self.position
        self.rect.move_ip(move[1]*self.length,move[0]*self.length)
        self.position = new_position
        self.location[0] += move[0]
        self.location[1] += move[1]

class Player:
    def __init__(self,index,player):
        self.used_block = 0
        self.length = game.square_length
        self.shape = chosen_shapes_and_colors[self.used_block][0]
        self.color = chosen_shapes_and_colors[self.used_block][1]
        self.player = player
        self.button = [K_a,K_s,K_d,K_w] if self.player == 1 else [K_LEFT,K_DOWN,K_RIGHT,K_UP]
        self.board = np.zeros((game.height,game.width))
        self.all_blocks = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.first = True
        self.game_over = False
        self.score = 0

    def update(self,key_pressed):
        if self.first:
            self.first = False
            self.new_block()
        right = True
        left = True
        moving = True
        rotate = True

        block_locations = []
        for block in self.blocks:
            block_locations.append(block.location)




        for block in self.blocks:
            try:
                if self.board[block.location[0] + 1, block.location[1]] == 1 and [block.location[0] + 1,block.location[1]] not in block_locations:
                    moving = False
                    break
            except:
                moving = False
                break

        for block in self.blocks:
            move = block.location_after_rotate() - block.position
            if block.rect.left + move[1]*self.length < 0:
                rotate = False
                break
            elif block.rect.right + move[1]*self.length > game.width*self.length:
                rotate = False
                break
            elif block.rect.bottom + move[0]*self.length > game.height*self.length:
                rotate = False
                break
            else:
                block.rect.move_ip(move[1]*self.length,move[0]*self.length)
                sprite_list = pygame.sprite.spritecollide(block,self.all_blocks,False)
                for i in sprite_list:
                    if i not in self.blocks:
                        rotate = False
                        break
                block.rect.move_ip(-move[1] * self.length, -move[0] * self.length)
                if not rotate:
                    break


        for block in self.blocks:
            try:
                if self.board[block.location[0], block.location[1] + 1] == 1 and [block.location[0], block.location[1] + 1] not in block_locations:
                    right = False
                    break
            except:
                right = False
                break
            if block.location[0] + 1 != len(self.board):
                if key_pressed[self.button[2]] and key_pressed[self.button[1]]:
                    if self.board[block.location[0]+1, block.location[1] + 1] == 1 and [block.location[0]+1, block.location[1] + 1] not in block_locations:
                        right = False
                        break
            else:
                continue


        for block in self.blocks:
            if not block.location[1] - 1 < 0:
                if self.board[block.location[0], block.location[1] - 1] == 1 and [block.location[0], block.location[1] - 1] not in block_locations:
                    left = False
                    break
                if key_pressed[self.button[0]] and key_pressed[self.button[1]] and left:
                    try:
                        if self.board[block.location[0]+1, block.location[1] - 1] == 1 and [block.location[0]+1, block.location[1] - 1] not in block_locations:
                            left = False
                            break
                    except:
                        continue
            else:
                left = False
                break

        if not moving:
            for block in self.blocks:
                block.moving = False



        self.blocks.update(key_pressed,right,left,rotate)

        for block in self.blocks:
            self.board[block.location[0],block.location[1]] = 1

        if not moving:
            block_locations = []
            for block in self.blocks:
                block_locations.append(block.location)

            moving = True
            for block in self.blocks:
                try:
                    if self.board[block.location[0] + 1, block.location[1]] == 1 and [block.location[0] + 1,block.location[1]] not in block_locations:
                        moving = False
                        break
                except:
                    moving = False
                    break

            if moving:
                for block in self.blocks:
                    block.moving = True

        if not moving:
            combo = 0
            for index, row in enumerate(self.board):
                if np.all(row == 1):
                    combo += 1
                    self.board[:index + 1, :] = 0
                    for block in self.all_blocks:
                        if block.location[0] == index:
                            block.kill()
                        elif block.location[0] < index:
                            block.location[0] += 1
                            block.rect.move_ip(0, self.length)
                            self.board[block.location[0], block.location[1]] = 1
            if combo == 1: c1.play()
            elif combo == 2: c2.play()
            elif combo == 3: c3.play()
            elif combo == 4: c4.play()
            elif combo == 5: c5.play()
            if combo > 0:
                self.score += 25 * 2 ** (combo - 1) * combo
            self.blocks.empty()
            self.used_block += 1
            self.score += 5
            if self.board[2].any():
                self.game_over = True
            self.shape = chosen_shapes_and_colors[self.used_block][0]
            self.color = chosen_shapes_and_colors[self.used_block][1]
            try:
                chosen_shapes_and_colors[self.used_block + 1]
            except:
                chosen_shapes_and_colors.append([random.choice(shapes), random.choice(colors)])
            if not self.game_over:
                self.new_block()



    def new_block(self):
        for i in range(len(self.shape)):
            for j in range(len(self.shape)):
                if self.shape[i,j] == 1:
                    new = Single_block([i,j],self.color,len(self.shape),self.player)
                    self.all_blocks.add(new)
                    self.blocks.add(new)


pygame.init()
pygame.mixer.init()
game = Game()
pygame.mixer.music.load("Giorno's_theme.mp3")
c1 = pygame.mixer.Sound("c1.wav")
c2 = pygame.mixer.Sound("c2.wav")
c3 = pygame.mixer.Sound("c3.mp3")
c4 = pygame.mixer.Sound("c4.mp3")
c5 = pygame.mixer.Sound("c5.mp3")

shapes1 = [np.array([[1]])]
shapes = [np.array([[0,0,1,0],
                    [0,0,1,0],
                    [0,0,1,0],
                    [0,0,1,0]],)
          ,np.array([[0, 0, 0],
                    [1, 1, 0],
                    [0, 1, 1]])
          ,np.array([[0,0,0],
                    [0,1,1],
                    [1,1,0]])
          ,np.array([[0, 1, 0],
                    [0, 1, 0],
                    [0, 1, 1]])
          ,np.array([[0,1,0],
                    [0,1,0],
                    [1,1,0]])
          ,np.array([[0,0,0],
                    [0,1,0],
                    [1,1,1]])
          ,np.array([[0,0,0],
                    [1,1,1],
                    [0,0,0]])
          ,np.array([[1,1],
                    [0,1]])
          ,np.array([[1,1],
                    [1,1]])
          ,np.array([[0, 0, 1, 0,0],
                    [0, 0, 1, 0,0],
                    [0, 0, 1, 0,0],
                    [0, 0, 1, 0,0],
                    [0, 0, 1, 0,0]])
          ]

colors = [(222,78,111),(79,86,221),(74,225,82),(230,218,70),(216,72,227),(79,197,221),(190,233,224),(240,151,79)]

chosen_shapes_and_colors = [[random.choice(shapes),random.choice(colors)],[random.choice(shapes),random.choice(colors)]]

player1 = Player(0,1)
player2 = Player(0,2)



game.loop()



