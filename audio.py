import pygame

def init_audio():
    pygame.mixer.init()

def play_sound():
    try:
        pygame.mixer.music.load("sonido.mp3")
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Error al reproducir sonido: {e}")

if __name__ == "__main__":
    init_audio()
    play_sound()
    while pygame.mixer.music.get_busy():  # Espera a que termine la reproducción
        pygame.time.Clock().tick(10)