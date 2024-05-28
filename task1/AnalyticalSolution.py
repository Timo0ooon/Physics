import math


class AnalyticalSolution:
    def __init__(self, path_length: float, height: float, body_volume: float, body_weight: float, k: float, speed: float) -> None:
        self.__path_length: float = path_length   # длина пути
        self.__height: float = height             # глубина
        self.__g: float = 9.8                     # ускорение свободного падения
        self.__density_of_water: float = 1000.0   # плотность воды
        self.__body_volume: float = body_volume   # объем подводной лодки
        self.__body_weight: float = body_weight   # масса подводной лодки
        self.__k: float = k                       # константа
        self.__speed: float = speed               # скорость
        self.__body_density = self.__body_weight / self.__body_volume  # объем тела

        self.__t_values: list[float] = list()     # время 
        self.__x_values: list[float] = list()     # значения x
        self.__y_values: list[float] = list()     # значения y
        self.__lift_time = self.__path_length / self.__speed  # время подъема
        self.__delta_t = 0.1                      # шаг

    def  __generate_t_values(self) -> None:
        time: float = 0

        while time <= self.__lift_time:
            
            self.__t_values.append(
                time
            )

            time += self.__delta_t

    def __generate_x_values(self) -> None:
        if len(self.__t_values) == 0:
            self.__generate_t_values()

        for time in self.__t_values:
            self.__x_values.append(
                time * self.__speed   
            )

    def __generate_y_values(self) -> None:
        if len(self.__t_values) == 0:
            self.__generate_t_values()

        for time in self.__t_values:
            self.__y_values.append(
                self.__g*(self.__density_of_water-self.__body_density)*time**2/(2*self.__body_density) - self.__height
            )                             

    def get_trajectory(self) -> tuple[list[float], list[float]]:
        if len(self.__x_values) == 0:
            self.__generate_x_values()

        if len(self.__y_values) == 0:
            self.__generate_y_values()

        return self.__x_values, self.__y_values
    
    def get_depth_versus_time(self) -> tuple[list[float], list[float]]:
        if len(self.__x_values) == 0:
            self.__generate_t_values()

        if len(self.__y_values) == 0:
            self.__generate_y_values()

        return self.__t_values, self.__y_values