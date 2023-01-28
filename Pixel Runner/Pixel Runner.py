import random
import pygame
from sys import exit
from random import randint, choice


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('UltimatePygameIntro-main/graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('UltimatePygameIntro-main/graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('UltimatePygameIntro-main/graphics/Player/jump.png').convert_alpha()


        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('UltimatePygameIntro-main/audio/aah.mp3')
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -22
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()


class obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_1 = pygame.image.load('UltimatePygameIntro-main/graphics/Fly/Fly1.png').convert_alpha()
            fly_2 = pygame.image.load('UltimatePygameIntro-main/graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load('UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('UltimatePygameIntro-main/graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1100), y_pos))

    def animation(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation()
        self.rect.x -= 6
        self.destroy_obstacles()

    def destroy_obstacles(self):
        if self.rect.x <= -100:
            self.kill()


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)
            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []


def collisions(player, obstacles):
    if obstacles:
        for obstacles_rect in obstacles:
            if player.colliderect(obstacles_rect): return False
    return True

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,Obstacles_group,False):
        Obstacles_group.empty()
        return False
    else:
        return True
def player_animation():
    global player_surface, player_index

    if player_rect.bottom < 300:
        # jump
        player_surface = player_jump
    else:
        # walk
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surface = player_walk[int(player_index)]


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pixel Runner')
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('UltimatePygameIntro-main/audio/الذبابة.mp3')
bg_music.play(loops= -1)
bg_music.set_volume(0.1)
# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

Obstacles_group = pygame.sprite.Group()

# sky import
sky_surface = pygame.image.load('UltimatePygameIntro-main/graphics/Sky.png').convert()

# ground import
ground_surface = pygame.image.load('UltimatePygameIntro-main/graphics/ground.png').convert()

# text
test_font = pygame.font.Font('UltimatePygameIntro-main/font/Pixeltype.ttf', 50)

# Snail
snail_frame_1 = pygame.image.load('UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('UltimatePygameIntro-main/graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frames_index = 0
snail_surface = snail_frames[snail_frames_index]

# Fly
fly_frame1 = pygame.image.load('UltimatePygameIntro-main/graphics/Fly/Fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('UltimatePygameIntro-main/graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frames_index = 0
fly_surface = fly_frames[fly_frames_index]

obstacle_rect_list = []

# player import
player_walk_1 = pygame.image.load('UltimatePygameIntro-main/graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('UltimatePygameIntro-main/graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('UltimatePygameIntro-main/graphics/Player/jump.png').convert_alpha()

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

# intro screen
player_stand = pygame.image.load('UltimatePygameIntro-main/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 70))

game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 330))

# timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if player_rect.bottom == 300:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player_rect.collidepoint(event.pos):
                        player_gravity = -22

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player_gravity = -22

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
        if game_active:
            if event.type == obstacle_timer:
                Obstacles_group.add(obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
                # if randint(0,2):
                #     obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900,1100),300)))
                # else:
                #     obstacle_rect_list.append(fly_surface.get_rect(bottomright=(randint(900, 1100), 210)))

            if event.type == snail_animation_timer:
                if snail_frames_index == 0:
                    snail_frames_index = 1
                else:
                    snail_frames_index = 0
                snail_surface = snail_frames[snail_frames_index]

            if event.type == fly_animation_timer:
                if fly_frames_index == 0:
                    fly_frames_index = 1
                else:
                    fly_frames_index = 0
                fly_surface = fly_frames[fly_frames_index]
    if game_active:
        # sky
        screen.blit(sky_surface, (0, 0))
        # ground
        screen.blit(ground_surface, (0, 300))
        # score
        score = display_score()
        # player
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 300: player_rect.bottom = 300
        # player_animation()
        # screen.blit(player_surface, player_rect)
        player.draw(screen)
        player.update()

        Obstacles_group.draw(screen)
        Obstacles_group.update()

        # obstacle movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collision
        game_active = collision_sprite()
        # game_active = collisions(player_rect, obstacle_rect_list)
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
    # update screen
    pygame.display.update()
    # framerate
    clock.tick(60)
