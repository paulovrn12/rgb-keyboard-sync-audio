import sounddevice as sd
import numpy as np
import pyautogui
import time

# Configurações de captura de áudio
SAMPLE_RATE = 44100
DURATION = 0.1  # Duração da captura em segundos
VOLUME_THRESHOLD = 0.1  # Limite para ativar a mudança de cor

# Perfis de cor (criados previamente no software do teclado)
profiles = ['F1', 'F2', 'F3']  # Atalhos para mudar o perfil de cor

# Função de callback para capturar o áudio
def audio_callback(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm > VOLUME_THRESHOLD:
        # Escolhe um perfil aleatório baseado no volume
        profile = profiles[int(volume_norm) % len(profiles)]
        print(f"Alterando para o perfil: {profile}")
        pyautogui.press(profile)

# Iniciar a captura de áudio
with sd.InputStream(callback=audio_callback, channels=1, samplerate=SAMPLE_RATE):
    print("Capturando áudio... Pressione Ctrl+C para sair.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Encerrando...")
