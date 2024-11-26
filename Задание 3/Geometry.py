import math

class GeometricFigure:
    def calculate_area(self):
        raise NotImplementedError("Метод calculate_area должен быть переопределен в соответствующий класс.")


class Pryamougolnik(GeometricFigure):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами.")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Krug(GeometricFigure):
    def __init__(self, radius):
        """Инициализация круга."""
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом.")
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2


class Romb(GeometricFigure):
    def __init__(self, diagonal1, diagonal2):
        if diagonal1 <= 0 or diagonal2 <= 0:
            raise ValueError("Диагонали должны быть положительными числами.")
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def calculate_area(self):
        return 0.5 * self.diagonal1 * self.diagonal2


def get_figure_data(figure_type):
    if figure_type == "pryamougolnik":
        width = float(input("Введите ширину прямоугольника: "))
        height = float(input("Введите высоту прямоугольника: "))
        return width, height
    elif figure_type == "krug":
        radius = float(input("Введите радиус круга: "))
        return radius
    elif figure_type == "romb":
        diagonal1 = float(input("Введите длину первой диагонали ромба: "))
        diagonal2 = float(input("Введите длину второй диагонали ромба: "))
        return diagonal1, diagonal2
    else:
        return None


if __name__ == "__main__":
    figure_type = input("Введите тип фигуры (oryamougolnik, krug, romb): ").lower()
    data = get_figure_data(figure_type)

    try:
        if figure_type == "pryamougolnik":
            figure = Pryamougolnik(*data)
        elif figure_type == "krug":
            figure = Krug(*data)
        elif figure_type == "romb":
            figure = Romb(*data)
        else:
            print("Неизвестный тип фигуры.")
            exit()

        area = figure.calculate_area()
        print(f"Площадь {figure_type}: {area:.2f}")

    except ValueError as e:
        print(f"Ошибка: {e}")