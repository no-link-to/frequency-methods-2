import librosa
import numpy as np
from scipy.integrate import trapz
import matplotlib.pyplot as plt


class AudioFourier:
    __audio_file_path = None
    __t_list = []
    __transformed_list = []
    __ft_list = []
    __ftransformed_list = []

    def __init__(self, audio_file_path):
        self.__audio_file_path = audio_file_path

    def __calculate_t_ft(self):
        self.__ft_list, sr = librosa.load(self.__audio_file_path)
        self.__t_list = np.arange(0, len(self.__ft_list)) / sr

    def __calculate_transformed(self):
        omega = np.linspace(0, 2 * np.pi / (self.__t_list[1] - self.__t_list[0]), len(self.__t_list))

        self.__ftransformed_list = [trapz(self.__ft_list * np.exp(-1j * freq * self.__t_list), self.__t_list)
                                    for i, freq in enumerate(omega)]

        self.__transformed_list = omega / (2 * np.pi)

    def __draw(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.__t_list, self.__ft_list)
        plt.xlabel('t')
        plt.ylabel('f(t)')
        plt.title('Исходная функция')
        plt.show()

    def __draw_fourier(self):
        plt.plot(self.__transformed_list, np.abs(self.__ftransformed_list))
        plt.xlabel('v')
        plt.ylabel('|f(v)|')
        plt.title('Модуль Фурье-образа функции')
        plt.show()

    def run(self):
        self.__calculate_t_ft()
        self.__calculate_transformed()
        self.__draw()
        self.__draw_fourier()


if __name__ == "__main__":
    audio = AudioFourier("Аккорд (23).mp3")
    audio.run()
