from apii import PetFriends
from settingss import valid_email, valid_password, invalid_password, invalid_email, invalid_auth_key
import os

pf = PetFriends()


# 1
def test_add_new_pet_with_valid_data_without_photo(name='Кот', animal_type='британец',
                                                   age='4'):
    """Проверяем что можно добавить питомца с корректными данными без фото"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


# 2
def test_add_photo_of_pet(pet_photo='image/british.jpg'):
    """Проверяем что можно добавить только фото питомца"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

        # Проверяем что статус ответа = 200
        assert status == 200
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


# 3
def test_get_api_key_for_invalid_user(email=invalid_email, password=valid_password):
    """ Проверяем что запрос api ключа с некорректным значением email
    возвращает статус не равным 200 """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status != 200


# 4
def test_get_api_key_with_invalid_password(email=valid_email, password=invalid_password):
    """ Проверяем что запрос api ключа с некорректным значением пароля
    возвращает статус не равным 200"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status != 200


# 5
def test_unsuccessful_delete_other_pet():
    """Проверяем что нельзя удалить питомца, которого создал другой пользователь"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, all_pets = pf.get_list_of_pets(auth_key, "")
    pet_id = all_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Проверяем что статус ответа не равен 200 и в списке питомцев есть id питомца
    assert status != 200
    # assert pet_id in all_pets.values()


# 6
def test_get_all_pets_with_invalid_key(filter=''):
    """ Проверяем что запрос не возвращает список питомцев при неверном api ключе.
    """
    # Присваиваем переменной auth_key некорректное значение api ключа
    auth_key = invalid_auth_key
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status != 200
    # assert len(result['pets']) == 0


# 7
def test_add_new_pet_with_valid_data_long_name(name='Кот'*50, animal_type='британец',
                                               age='2', pet_photo='image/british.jpg'):
    """Проверяем, получится ли добавить питомца если у него очень длинное имя"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


# 8
def test_add_new_pet_with_valid_data_long_type(name='Кот', animal_type='британец'*50,
                                               age='2', pet_photo='image/british.jpg'):
    """Проверяем, получится ли добавить питомца если у него очень длинный animal_type"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['animal_type'] == animal_type


# 9
def test_add_new_pet_with_valid_data_long_age(name='Кот', animal_type='британец',
                                              age='2'*100, pet_photo='image/british.jpg'):
    """Проверяем, получится ли добавить питомца если у него очень длинный возраст"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['age'] == age


# 10
def test_add_new_pet_with_empty_data_without_photo(name='', animal_type='', age=''):
    """Проверяем что нельзя добавить питомца с пустыми данными и без фото"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 200
