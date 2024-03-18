import numpy as np
import matplotlib.pyplot as plt

class Fourier:
    __a = 0
    __b = 0
    __t_list = []
    __ft_list = []
    __transformed_list = []
    __ftransformed_list = []
    __func_type = 1
    __transformed_view_borders = 0

    def __init__(self, a, b, func_type, transformed_view_borders=(2 * np.pi)):
        self.__a = a
        self.__b = b
        self.__func_type = func_type
        self.__transformed_view_borders = transformed_view_borders


    def __func_rect(self, value):
        return np.where((value >= -self.__b) & (value <= self.__b), self.__a, 0)

    def __func_triangle(self, value):
        return np.where((value >= -self.__b) & (value <= self.__b), self.__a - np.abs((self.__a * value) / self.__b), 0)

    def __func_sinc(self, value):
        return self.__a * np.sinc(self.__b * value)

    def __func_gaussian(self, value):
        return self.__a * np.exp(-self.__b * (value ** 2))

    def __func_attenuation(self, value):
        return self.__a * np.exp(-self.__b * np.abs(value))

    def __func_transformed_rect(self, value):
        return ((2 * self.__a) / (value * np.sqrt(2*np.pi))) * np.sin(value * self.__b)

    def __func_transformed_triangle(self, value):
        return ((1 / np.sqrt(2 * np.pi)) *
                ((-2 * self.__a * np.cos(self.__b * value) + 2 * self.__a) / (self.__b * (value ** 2))))

    def __func_transformed_sinc(self, value):
        return (self.__a / (np.sqrt(2 * np.pi) * np.abs(self.__b)) *
                np.where(((value / (2 * np.pi * self.__b)) >= -0.5) & ((value / (2 * np.pi * self.__b)) <= 0.5), 1, 0))

    def __func_transformed_gaussian(self, value):
        return (1 / np.sqrt(2 * np.pi)) * (np.sqrt(np.pi) * self.__a * np.exp(-(value ** 2) / (4 * self.__b))) / np.sqrt(self.__b)

    def __func_transformed_attenuation(self, value):
        return (1 / np.sqrt(2 * np.pi)) * ((2 * self.__a * self.__b) / (value ** 2 + self.__b ** 2))

    def __get_func(self):
        return [self.__func_rect, self.__func_triangle, self.__func_sinc,
                self.__func_gaussian, self.__func_attenuation][self.__func_type - 1]

    def __get_transformed_func(self):
        return [self.__func_transformed_rect, self.__func_transformed_triangle, self.__func_transformed_sinc,
                self.__func_transformed_gaussian, self.__func_transformed_attenuation][self.__func_type - 1]

    def __calculate_t(self):
        self.__t_list = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        self.__transformed_list = np.linspace(-self.__transformed_view_borders, self.__transformed_view_borders, 1000)

    def __calculate_ft(self):
        self.__ft_list = [self.__get_func()(item) for item in self.__t_list]

    def __calculate_transformed(self):
        self.__ftransformed_list = [self.__get_transformed_func()(item) for item in self.__transformed_list]

    def __check_parseval(self):
        ordinary = np.trapz([item ** 2 for item in self.__ft_list], self.__t_list)
        transformed = np.trapz([item ** 2 for item in self.__ftransformed_list], self.__transformed_list)
        print(f"Проверка равенства Парсеваля погрешностью 0.1: {np.isclose(ordinary, transformed, atol=1e-1)}")

    def __draw(self):
        plt.figure(figsize=(12, 6))
        plt.subplot(121)
        plt.plot(self.__t_list, self.__ft_list, label='f(t)')
        plt.title('Исходная функция')
        plt.xlabel('t')
        plt.ylabel('f(t)')
        plt.grid(True)
        plt.legend()

        plt.subplot(122)
        plt.plot(self.__transformed_list, self.__ftransformed_list, label='f(ω)')
        plt.title('Фурье-образ функции')
        plt.xlabel('ω')
        plt.ylabel('f(ω)')
        plt.grid(True)
        plt.legend()

        plt.show()

    def run(self):
        self.__calculate_t()
        self.__calculate_ft()
        self.__calculate_transformed()
        self.__check_parseval()
        self.__draw()

if __name__ == "__main__":
    # Function 1
    # fourier = Fourier(2, 3, 1)
    # fourier = Fourier(4, 5, 1)
    # fourier = Fourier(6, 7, 1)

    # Function 2
    # fourier = Fourier(2, 3, 2)
    # fourier = Fourier(4, 5, 2)
    # fourier = Fourier(6, 7, 2)

    # Function 3
    fourier = Fourier(2, 3, 3, 15)
    # fourier = Fourier(4, 5, 3, 25)
    # fourier = Fourier(6, 7, 3, 30)

    # Function 4
    # fourier = Fourier(2, 3, 4)
    # fourier = Fourier(4, 5, 4)
    # fourier = Fourier(.5, .5, 4)

    # Function 5
    # fourier = Fourier(2, 3, 5)
    # fourier = Fourier(4, 5, 5)
    # fourier = Fourier(6, 7, 5)
    fourier.run()
