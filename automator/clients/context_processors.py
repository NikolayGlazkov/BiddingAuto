def menu_context(request):
    menu = [
        {"title": "Войти", "url_name": "login"},
        {"title": "Главная", "url_name": "home"},
        {"title": "Список клиентов", "url_name": "clients_list"},
        {"title": "Список лотов", "url_name": "lot_list"},
        {"title": "Контакты", "url_name": "contact"},
        {"title": "О нас", "url_name": "about"},
    ]
    return {"menu": menu}
