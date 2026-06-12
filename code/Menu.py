import pygame
from pygame import Surface, Rect
from pygame.ftfont import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_YELLOW, C_WHITE, MENU_OPTION


class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuInicio.png')
        self.rect = self.surf.get_rect(left=0 , top=0)



    def run(self):
        pygame.mixer_music.load('./asset/MusicaMenu.mp3')
        pygame.mixer_music.play(-1)  # parametro -1 e para que musica não pare
        while True:

            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=130,text="COMEÇAR",text_color=C_YELLOW,text_center_pos=(WIN_WIDTH // 2, 550))
            pygame.display.flip()

            # check all event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #close screen
                    quit() #end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[0]





    # def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple) -> None:
    #     text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
    #     text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
    #     text_rect: Rect = text_surf.get_rect(center=text_center_pos)
    #     self.window.blit(source=text_surf, dest=text_rect)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        # 1. Definimos a fonte (Você pode manter a Lucida Sans ou usar uma mais pixelada)
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)

        # 2. Cor da sombra (Marrom escuro idêntico ao da imagem)
        shadow_color: tuple = (87, 0, 0)

        # 3. Renderiza e desenha a SOMBRA (deslocada 3 pixels para a direita e para baixo)
        shadow_surf: Surface = text_font.render(text, True, shadow_color).convert_alpha()
        shadow_center_pos: tuple = (text_center_pos[0] + 3, text_center_pos[1] + 3)
        shadow_rect: Rect = shadow_surf.get_rect(center=shadow_center_pos)
        self.window.blit(source=shadow_surf, dest=shadow_rect)

        # 4. Renderiza e desenha o TEXTO PRINCIPAL (por cima da sombra)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
