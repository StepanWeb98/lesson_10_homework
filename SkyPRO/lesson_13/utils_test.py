# circle_test.py

import pytest

from utils import Player

class TestCircle:

    # def get_player(self):
    #
    #     name = Player.name

    def test_get_radius(self):
        circle = Player("Петр")
        work_origin = circle.name
        word = circle.change_name("Игорь")
        assert word != work_origin, "Ошибка в  радиусе"

    def test_get_diameter(self):
        circle = Player("Петр")
        points_origin = circle.points
        assert circle.add_points(5) > points_origin, "Ошибка в диаметре"

    def test_get_perimeter(self):
        circle = Player("Петр")
        assert circle.get_points() == 5, "Ошибка в периметре"

    def test_init_type_error(self):
        with pytest.raises(TypeError):
            circle = Player(78)

    def test_init_value_error(self):
        with pytest.raises(ValueError):
            circle = Player(["куку"])