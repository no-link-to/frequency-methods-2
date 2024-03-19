import numpy as np
import matplotlib.pyplot as plt

class Fourier:
    __a = 0
    __b = 0
    __c = 0
    __t_list = []
    __ft_list = []
    __transformed_list = []
    __ftransformed_list = []

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def __func(self, value):
        return np.where((value >= -(self.__b + self.__c)) & (value <= (self.__b - self.__c)), self.__a, 0)

    def __func_transformed(self, value):
        return (((2 * self.__a) / (value * np.sqrt(2*np.pi))) * np.sin(value * self.__b) *
                np.exp(1j * value * self.__c))

    def __calculate_t(self):
        self.__t_list = np.linspace(-15, 15, 1000)
        self.__transformed_list = np.linspace(-15, 15, 1000)

    def __calculate_ft(self):
        self.__ft_list = [self.__func(item) for item in self.__t_list]

    def __calculate_transformed(self):
        self.__ftransformed_list = [self.__func_transformed(item) for item in self.__transformed_list]

    def __draw(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.__t_list, self.__ft_list, label='g(t)')
        plt.title('Исходная функция')
        plt.grid(True)
        plt.legend()
        plt.show()

    def __draw_transformed(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.__transformed_list, [item.imag for item in self.__ftransformed_list], label='Im g(ω)')
        plt.plot(self.__transformed_list, [item.real for item in self.__ftransformed_list], label='Re g(ω)')
        plt.title('Фурье-образ функции')
        plt.grid(True)
        plt.legend()

        plt.show()

    def __draw_transformed_module(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.__transformed_list,
                 [np.sqrt(item.imag ** 2 + item.real ** 2) for item in self.__ftransformed_list],
                 label='|g(ω)|')
        plt.title('Модуль Фурье-образа функции')
        plt.grid(True)
        plt.legend()

        plt.show()

    def run(self):
        self.__calculate_t()
        self.__calculate_ft()
        self.__calculate_transformed()
        self.__draw()
        self.__draw_transformed()
        self.__draw_transformed_module()


if __name__ == "__main__":
    # Function 1
    # fourier = Fourier(2, 3, -2)
    # fourier = Fourier(2, 3, 4)
    fourier = Fourier(2, 3, 6)

    fourier.run()
