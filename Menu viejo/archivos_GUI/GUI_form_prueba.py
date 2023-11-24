import pygame
from pygame.locals import *

from archivos_GUI.GUI_button_image import *
from archivos_GUI.GUI_button import *
from archivos_GUI.GUI_slider import *
from archivos_GUI.GUI_textbox import *
from archivos_GUI.GUI_label import *
from archivos_GUI.GUI_form import *
from archivos_GUI.GUI_form_menu_score import *

class FormPrueba(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.1
        self.flag_play = True

        pygame.mixer.init()

        # -----------------------------      CONTROLES  ------------------------------------------ #
        self.text_box = TextBox(self._slave, x, y, 50, 50, 150, 30, "Gray", "White", "Red", "Blue", 2, font = "Comic Sans", font_size = 15, font_color = "Black")
        self.play_button = Button(self._slave, x, y, 100, 100, 100, 50, "Red", "Blue", self.button_play_click, "Nombre", "Pause music", font = "Verdana", font_size = 15, font_color = "White")
        self.label_volumen = Label(self._slave, 650, 190, 100, 50, "10%", "Comic Sans", 15, "White", r"Menu\recursos\table.png")
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 500, 15, self.volumen, "Blue", "White")
        self.tabla_button = Button_Image(self._slave, x, y, 255, 100, 50, 50, r"Menu\recursos\button_score.png", self.button_tabla_click, "Boton para ir a la Tabla...")
        # ---------------------------------  AGREGO LOS CONTROLES A LA LISTA --------------------- #
        self.lista_widgets.append(self.text_box)
        self.lista_widgets.append(self.play_button)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.tabla_button)


        pygame.mixer.music.load(r"Menu\recursos\song (Metal Gear Rising REVENGEANCE Main Menu).mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.render()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()                
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def render(self):
        self._slave.fill(self._color_background)

    def button_play_click(self, texto):
        # print(texto) Para probar que funciona!
        if self.flag_play:
            pygame.mixer.music.pause()
            self.play_button._color_background = "Cyan"
            self.play_button._font_color = "Black"
            self.play_button.set_text("Play music")
        else:
            pygame.mixer.music.pause()
            self.play_button._color_background = "Red"
            self.play_button._font_color = "White"
            self.play_button.set_text("Pause music")
        self.flag_play = not self.flag_play

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def button_tabla_click(self, texto):
        # print(texto) Para probar que funciona!
        lista_diccionario_score = [
                             {"Jugador": "Coco", "Score": 1000},
                             {"Jugador": "Coca", "Score": 900},
                             {"Jugador": "Pepsi", "Score": 750}
                            ]
        form_puntaje = FormMenuScore(self._master,
                                     250,
                                     25,
                                     500,
                                     550,
                                     (220,0,220),
                                     "White",
                                     True,
                                     r"Menu\recursos\window.png",
                                     lista_diccionario_score,
                                     100,
                                     10,
                                     10
                                    )
        self.show_dialog(form_puntaje)