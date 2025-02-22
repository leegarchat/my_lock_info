
def get_version_info():
    # https://media.githubusercontent.com/media/leegarchat/my_lock_info/refs/heads/main/updates/versionV2.py
    main_url = "https://github.com/leegarchat/my_lock_info/raw/refs/heads/main/updates/"
    VER = 17
    data = {
        "acces_export_new_order": False,
        "update_info": {
            "LINUX": {
                "Ver": 17,
                "Url": f"https://sourceforge.net/projects/cdek-my/files/LinuxA{VER}/download"
                },
            "WINDOWS": {
                "Ver": 17,
                "Url": f"https://sourceforge.net/projects/cdek-my/files/WinA{VER}.exe/download"
                }
        },
        "changelog": {
            'text': (
                '(Версия v13 перестанет работать с 17.02)\n'
                'v14 (Перестанет работать с 22.02):\n'
                '- Убрана возможность по умолчанию отправлять СЗ с все офисы\n'
                '  Доступ по умолчанию в ЦФО и центральный офис МСК\n\n'
                'v15:\n'
                '- Исправлено дублирующие окно обновления\n'
                '- Временно убрана выгрузка накладных в статусе создано на МСК\n'
                '.  (Парметр может быть изменен онлайн)\n\n'
                '- Уменьшено обращений к северу для проверок доступа\n'
                '- Добавлено сообщение об изменение перед обновлением\n'
                '- Добавлено сообщение об сроке работы текущей версии программы перед обновлением\n'
                'v16:\n'
                '- Исправления для linx\n'
                'v17:\n'
                '- Миграция на другой сервер\n'
                    )
        },
        "avalable_ver": {
            "11": True,
            "12": True,
            "13": True,
            "14": True,
            "15": True,
            "16": True,
            "17": True,
            "18": True,
            "19": True,
            "20": True,
            "21": True,
        },
        "acces_users": [
            "Семерня Анна Андреевна",
            "СИЧИНАВА ГЕННАДИЙ ГИЗОЕВИЧ",
            "Мальцева Анна Сергеевна",
            "Шейченко Алексей Сергеевич",
            "Заяц Павел Сергеевич",
            "Гарманов Максим Игоревич",
            "Пицель Виктор Николаевич",
            "Ловущев Александр Анатольевич",
            "Суворов Станислав Дмитриевич",
            "Шурчков Александр Анатольевич",
            "Ельмаков Евгений Анатольевич",
            "Бушуев Александр Владимирович",
            "Оганнисян Алик Тигранович",
            "Турков Владислав Игоревич",
            "Шустов Алексей Сергеевич",
            ],
        "acces_users_prime": [
            "СИЧИНАВА ГЕННАДИЙ ГИЗОЕВИЧ",
            "Мальцева Анна Сергеевна",
            ],
        "acces_gazes": [
            "Газ 2",
            "Газ 3",
            "Газ 5",
            "Газ 6",
            "Газ 7",
            "Газ 9",
            "Газ 11",
            "Газ 12",
            "Газ 15",
            "Газ 17",
            "Газ 18",
            "Газ 19",
            ],
        "acces_gazes_prime": [
            "Газ 2",
            "Газ 3",
            "Газ 5",
            "Газ 6",
            "Газ 7",
            "Газ 9",
            "Газ 11",
            "Газ 12",
            "Газ 15",
            "Газ 17",
            "Газ 18",
            "Газ 19",
            ],
    }
    return data
