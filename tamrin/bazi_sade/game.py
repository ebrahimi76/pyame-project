import sys
import pygame


class Game:
    def __init__(self):  # سازنده کلاس Game
        pygame.init()  # سازنده pygame
        self.size = self.width, self.height = 320 * 2, 240 * 2  # اندازه و پهنا و ارتفاع صفحه‌ی بازی
        self.speed = [1, 1]  # سرعت توپ
        self.black = 0, 0, 0  # رنگ قالب سیستم
        self.screen = pygame.display.set_mode(self.size)  # ذخیره صفحه‌ی بازی
        self.ball, self.ballrect = self.load_image("sq.png")  # ذخیره توپ و مختصات توپ بازی

    @staticmethod
    def load_image(image_name):  # تابع بارگذار تصویر
        ball = pygame.image.load(image_name)  # توپ
        return ball, ball.get_rect()  # مورد دوم: مختصات

    def move_ball(self):  # تابع محرک توپ
        ballrect = self.ballrect.move(self.speed)  # توپ را به اندازه سرعتش حرکت می‌دهد
        if ballrect.left < 0 or ballrect.right > self.width:  # اگر مختصات افقی توپ از صفحه خارج شده بود
            self.speed[0] = -self.speed[0]  # حرکت افقی منفی
        if ballrect.top < 0 or ballrect.bottom > self.height:  # اگر مختصات عمودی از صفحه خارج شده بود
            self.speed[1] = -self.speed[1]  # حرکت عمودی منفی
        self.ballrect = ballrect

    def draw(self):  # تابع بروزرسان
        self.screen.fill(self.black)  # ابتدا صفحه بازی را پاک کرده
        self.screen.blit(self.ball, self.ballrect)  # اضافه کردن توپ با مختصات جدید
        pygame.display.update()  # بروزرسانی

    @staticmethod
    def handle_events():  # تابع کنترل‌کننده
        #  همه‌ی رویدادهای جدید را بررسی می‌کند و اگر رویدادی از نوع Quit در بین آنها وجود داشت، برنامه را می‌بندد
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
