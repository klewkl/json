import json

nearest_station_adv = """{
  "title": "iPhone X",
  "price": 100,
  "location": {
    "address": "город Самара, улица Мориса Тореза, 50",
    "metro_stations": ["Спортивная", "Гагаринская"]
  }
}"""

dog_category_ad = """ {
  "title": "Вельш-корги",
  "price": 1000,
  "class": "dogs",
  "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
  }
}"""

iphone_ad = json.loads(nearest_station_adv)
category_ad = json.loads(dog_category_ad)


class ColorizeMixin():
  
  """
   Меняет цвет текста при выводе на консоль
  """
  
  def __init__(self, code):
    self.code = code
    print(f'\033[1;{self.code};40m')


class Advert(ColorizeMixin):
  
  """
   Класс, который динамически создает атрибуты экземпляра
   класса из атрибутов JSON объекта 
  """

  repr_color_code = 32
  color = ColorizeMixin(repr_color_code)
  
  def __init__(self, file):
    self.file = file
    
    for attr, val in file.items():
        setattr(self, attr, self.compute_attr_value(val))

  def compute_attr_value(self, value):
    if isinstance(value, list):
      return [self.compute_attr_value(x) for x in value]
    elif isinstance(value, dict):
      return json_to_python(value)
    else:
      return value

  def __repr__(self):
    return f'{self.title} | {self.price} ₽'

# add_phone = Advert(iphone_ad)
# add_phone.title, add_phone.price, add_phone.location.address

# add_dog = Advert(category_ad)
# add_dog, add_dog.title, add_dog.price, add_dog.location.address
