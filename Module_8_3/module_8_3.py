# Домашнее задание по теме "Создание исключений".
# Цель: освоить навык создания пользовательских исключений и
# использовать его в решении задачи. Повторить тему ООП и принцип инкапсуляции.


class IncorrectVinNumber(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


class IncorrectRegPlate(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


class Car:
    def __init__(self, model: str, vin, reg_plate):
        # self.__vin = None
        if self.__is_valid_vin(vin):
            self.__vin = vin

        if self.__is_valid_reg_plate(reg_plate):
            self.__reg_plate = reg_plate

        self.model = model


    def __is_valid_vin(self, vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номера', f'Передан VIN {vin}')
        if vin > 9999999 or vin < 1000000:
            raise IncorrectVinNumber('Некорректный диапазон для vin номера', f'Передан VIN {vin}')
        return True


    def __is_valid_reg_plate(self, reg_plate):
        if not isinstance(reg_plate, str):
            raise IncorrectRegPlate('Некорректный тип данных для регистрационного знака',
                                    f'Передано: {reg_plate}')
        if len(reg_plate) != 6:
            raise IncorrectRegPlate('Некорректная длина регистрационного знака',
                                    f'Передано: {reg_plate}')
        return True

    def get_vin(self):
        return self.__vin




try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectRegPlate as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectRegPlate as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectRegPlate as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')