# local_storage

Опишите модуль для взаемодействия с локальным хранилищем,в качестве которого будет выступать json-файл (schema.json).

- Модуль должен создавать файл если его нет в папке с Вашим скриптом согласно темплейту(см ниже);
- Модуль должен реализовывать функциональность по извлечению и изменению данных в хранилище;
- пример вызова(консоль):
    python my_file.py --get path/to/key                             - возвращает значение по ключу
    (соответственно python my_file.py --get connections/test_connection/bucket возвращает "media bucket")

    python my_file.py --set path/to/key --val val_to_set       - присваевает значение ключу
    (соответственно python my_file.py --set connections/test_connection/bucket --val 1231  помещает значение 1231 под указанный путь)


JSON_TEMPLATE = {
    "connections": {},
    "access": []
}
