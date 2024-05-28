from matplotlib import pyplot as plt

from NumericalSolution import NumericalSolution
from AnalyticalSolution import AnalyticalSolution


class Plot:
    def __init__(self, numerical_solution: NumericalSolution, analytical_solution: AnalyticalSolution) -> None:
        self.__numerical_solution: NumericalSolution = numerical_solution
        self.__analytical_solution: analytical_solution = analytical_solution

    def plot_trajectory(self) -> None:
        numerical_x_values, numerical_y_values = self.__numerical_solution.get_trajectory()
        analytical_x_values, analytical_y_values = self.__analytical_solution.get_trajectory()

        fig, ax = plt.subplots()

        ax.set_title("Траектория движения подводной лодки без учета сопротивления воды")
        ax.plot(numerical_x_values, numerical_y_values, label='Численное решение', color='blue')
        ax.plot(analytical_x_values, analytical_y_values, label='Аналитическое решение', color='red')

        ax.grid(True)
        ax.legend()
        ax.set_xlabel('x')
        ax.set_ylabel('y')

        plt.show()

    def plot_depth_versus_time(self) -> None:
        numerical_t_values, numerical_y_values = self.__numerical_solution.get_depth_versus_time()
        analytical_t_values, analytical_y_values = self.__analytical_solution.get_depth_versus_time()

        fig, ax = plt.subplots()

        ax.set_title("Зависимость глубины от времени без учета сопротивления воды")
        ax.plot(numerical_t_values, numerical_y_values, label='Численное решение', color='blue')
        ax.plot(analytical_t_values, analytical_y_values, label='Аналитическое решение', color='red')

        ax.grid(True)
        ax.legend()
        ax.set_xlabel('t')
        ax.set_ylabel('y')

        plt.show()
    

if __name__ == '__main__':
    numerical_solution1 = NumericalSolution(500.0, 300.0, 1_000, 20_000.0, 18_700_000, 10.0, 16.5, 30)
    analytical_solution1 = AnalyticalSolution(500.0, 300.0, 20_000, 18_700_000.0, 10, 16.5)

    plot = Plot(numerical_solution1, analytical_solution1)
    plot.plot_depth_versus_time()
    plot.plot_trajectory()