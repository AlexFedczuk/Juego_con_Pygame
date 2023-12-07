import pygame

class Mixer():
    def __init__(self) -> None:
        pygame.mixer.init()
        self.mixer = pygame.mixer

    def stop_sound(sound:pygame.mixer.Sound):
        sound.stop()

    def play_sound(self, sound_file_path:str):
        sound_louded = self.mixer.Sound(sound_file_path)
        sound_louded.play()

    def set_mixer_volume(self, sound:pygame.mixer, volume:float):
        sound.set_volumen(volume)

    def set_back_ground_music(self, music_file_path:str):
        self.back_ground_music = self.mixer.Sound(music_file_path)
        self.back_ground_music.play(-1)