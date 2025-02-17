import pygame
import pygame.gfxdraw


class WinnerDisplay:
    def __init__(self, screen_width, screen_height):
        self.WIDTH = screen_width
        self.HEIGHT = screen_height
        self.animation_frames = 45

        self.button_width = 160
        self.button_height = 50
        self.play_color = (46, 204, 113)
        self.play_hover_color = (39, 174, 96)
        self.close_color = (231, 76, 60)
        self.close_hover_color = (192, 57, 43)

    def create_banner_alpha(self, surface, color, alpha):
        banner_height = 140
        banner_y = 20

        banner_surf = pygame.Surface((self.WIDTH, banner_height), pygame.SRCALPHA)
        pygame.draw.rect(banner_surf, (*color, alpha), (0, 0, self.WIDTH, banner_height))

        surface.blit(banner_surf, (0, banner_y))

    def draw_button(self, surface, text, color, x_position):
        button_y = 100

        pygame.draw.rect(surface, color,
                         (x_position, button_y, self.button_width, self.button_height),
                         border_radius=10)

        font = pygame.font.Font(None, 36)
        text_surf = font.render(text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=(x_position + self.button_width // 2, button_y + self.button_height // 2))
        surface.blit(text_surf, text_rect)

        return pygame.Rect(x_position, button_y, self.button_width, self.button_height)

    def display_winner(self, screen, winner):
        font = pygame.font.Font(None, 48)
        winner_text = font.render(f"{winner} Wins!", True, (255, 255, 255))
        text_rect = winner_text.get_rect(center=(self.WIDTH // 2, 60))

        spacing = 40
        total_width = 2 * self.button_width + spacing
        start_x = (self.WIDTH - total_width) // 2

        play_again_rect = pygame.Rect(
            start_x,
            100,
            self.button_width,
            self.button_height
        )

        close_rect = pygame.Rect(
            start_x + self.button_width + spacing,
            100,
            self.button_width,
            self.button_height
        )

        for alpha in range(self.animation_frames):
            screen_copy = screen.copy()

            banner_alpha = min(160, int(alpha * 3.5))
            self.create_banner_alpha(screen_copy, (0, 0, 0), banner_alpha)

            text_alpha = min(255, int(alpha * 5.66))
            winner_text.set_alpha(text_alpha)
            screen_copy.blit(winner_text, text_rect)

            screen.blit(screen_copy, (0, 0))
            pygame.display.flip()
            pygame.time.delay(16)

        while True:
            mouse_pos = pygame.mouse.get_pos()
            screen_copy = screen.copy()

            self.create_banner_alpha(screen_copy, (0, 0, 0), 160)
            screen_copy.blit(winner_text, text_rect)

            play_color = self.play_hover_color if play_again_rect.collidepoint(mouse_pos) else self.play_color
            close_color = self.close_hover_color if close_rect.collidepoint(mouse_pos) else self.close_color

            play_again_rect = self.draw_button(screen_copy, "Play Again", play_color, start_x)
            close_rect = self.draw_button(screen_copy, "Close", close_color, start_x + self.button_width + spacing)

            screen.blit(screen_copy, (0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_again_rect.collidepoint(event.pos):
                        return True
                    if close_rect.collidepoint(event.pos):
                        return False

            pygame.time.delay(16)