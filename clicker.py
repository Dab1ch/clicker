import pygame, random, time
pygame.init()
window = pygame.display.set_mode((500, 500)) #Создание фона и его заливка
color = (40, 40, 40)
window.fill(color)
main_font = pygame.font.Font(None, 20)
text = 'CLICK'
caption = main_font.render(text, True, (255, 255, 255))
time_font = pygame.font.Font(None, 30)
results_font = pygame.font.Font(None, 75)
caption_win = results_font.render('ПОЗДРАВЛЯЕМ!', True, (255, 255, 255))
caption_win1 = results_font.render('ВЫ ПОБЕДИЛИ!', True, (255, 255, 255))
caption_defeat = results_font.render('ВЫ ПРОИГРАЛИ!', True, (255, 255, 255))

class Area():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, y, x_length, y_length)
        pygame.draw.rect(window, (255, 255, 255), self.rect)
    def paint(self):
        pygame.draw.rect(window, fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)                                
class Label(Area):
    def text(self):
        window.blit(caption, (self.x + 30, self.y+90))
def print_time():
    caption_time = time_font.render('Время:' + str(cur_time), True, (255, 255, 255))
    window.blit(caption_time, (30, 40))
def print_points():
    caption_points = time_font.render('Очки:' + str(points), True, (255, 255, 255))
    window.blit(caption_points, (420, 40))
sprites = list()
x_length = 100
y_length = 200
for i in range(4):
    x = 20 * (i+1) + 100 * i
    y = 150
    sprites.append(Label(x, y))
x = 30
y = 30
x_length = 100
y_length = 100
sprites.append(Label(x, y))
x = 400
sprites.append(Label(x, y))
wait = 2999
fill_color = color
sprites[4].paint()
sprites[5].paint()
i = 4
start_time = time.time()
cur_time = 11
points = 0
while cur_time>0:
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(10)
    fill_color = (255, 255, 255)
    for k in range(len(sprites) - 2):
        sprites[k].paint()
    num = random.randint(0, 3)
    while num == i:
        num = random.randint(0, 3)
    fill_color = (0, 0, 0)
    sprites[num].paint()
    sprites[num].text()
    i = num
    for b in range(wait):
        new_time = time.time()
        cur_time = int(11 - new_time + start_time)
        if 11 - new_time + start_time < 0:
            break
        fill_color = color
        sprites[4].paint()
        sprites[5].paint()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for k in range(len(sprites)-2):
                    if sprites[k].collidepoint(x, y):
                        fill_color = (255, 255, 255)
                        for a in range(len(sprites)-2):
                            sprites[a].paint()
                        if k == num:
                            fill_color = (0, 255, 0)
                            sprites[k].paint()
                            points += 1
                        else:
                            fill_color = (255, 0, 0)
                            sprites[k].paint()
                            points -= 1
                        break
        
        print_time()
        print_points()
        pygame.display.update()
fill_color = color
for i in range(len(sprites)):
    sprites[i].paint()
if points>=5:
    window.blit(caption_win, (50, 110))
    window.blit(caption_win1, (50, 220))
else:
    window.blit(caption_defeat, (50, 200))
pygame.display.update()

    
    
    
        
