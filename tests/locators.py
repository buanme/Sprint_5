class Locators:
    # Главная страница - кнопка "Войти в аккаунт"
    LOGIN_BUTTON = "//button[text()='Войти в аккаунт']"

    # Форма авторизации - поле ввода имени
    AUTH_NAME_INPUT = "//form[@class='Auth_form__3qKeq mb-20']//input[@name='name']"

    # Форма авторизации - поле ввода пароля
    AUTH_PASSWORD_INPUT = "//form[@class='Auth_form__3qKeq mb-20']//input[@name='Пароль']"

    # Форма авторизации - кнопка "Войти"
    AUTH_SUBMIT_BUTTON = "//form[@class='Auth_form__3qKeq mb-20']//button[text()='Войти']"

    # Главная страница - кнопка "Оформить заказ"
    ORDER_BUTTON = "//button[text()='Оформить заказ']"

    # Главная страница - кнопка "Личный кабинет"
    ACCOUNT_BUTTON = "//a[@href='/account']"

    # Страница регистрации - кнопка "Войти"
    REGISTRATION_LOGIN_BUTTON = "//a[@href='/login']"

    # Страница восстановления пароля - кнопка "Войти"
    FORGOT_PASSWORD_LOGIN_BUTTON = "//a[@href='/login']"

    # Форма регистрации - поле ввода имени
    REGISTRATION_NAME_INPUT = "(//form[@class='Auth_form__3qKeq mb-20']//input)[1]"

    # Форма регистрации - поле ввода email
    REGISTRATION_EMAIL_INPUT = "(//form[@class='Auth_form__3qKeq mb-20']//input)[2]"

    # Форма регистрации - поле ввода пароля
    REGISTRATION_PASSWORD_INPUT = "(//form[@class='Auth_form__3qKeq mb-20']//input)[3]"

    # Форма регистрации - кнопка "Зарегистрироваться"
    REGISTRATION_SUBMIT_BUTTON = "//form[@class='Auth_form__3qKeq mb-20']//button[text()='Зарегистрироваться']"

    # Ошибка при некорректном пароле
    INVALID_PASSWORD_ERROR = "//div[@class='input__container']/p[text()='Некорректный пароль']"

    # Поле ввода имени в форме авторизации
    LOGIN_NAME_INPUT = "//input[@name='name']"

    # Поле ввода пароля в форме авторизации
    LOGIN_PASSWORD_INPUT = "//input[@name='Пароль']"

    # Кнопка "Войти" в форме авторизации
    LOGIN_SUBMIT_BUTTON = "//button[text()='Войти']"

    # Ссылка "Личный кабинет"
    LK_BUTTON = "//a[@href='/account']"

    # Ссылка "Конструктор" в меню
    CONSTRUCTOR_BUTTON = "//a[@class='AppHeader_header__link__3D_hX' and @href='/']"

    # Логотип Stellar Burgers
    LOGO = "//nav[@class='AppHeader_header__nav__g5hnF']//a[@href='/']"

    # Класс активного раздела
    ACTIVE_CLASS = "tab_tab_type_current__2BEPc"

    # Локаторы разделов
    BULKY_TAB = "//span[text()='Булки']/.."
    SAUCE_TAB = "//span[text()='Соусы']/.."
    NACHINKY_TAB = "//span[text()='Начинки']/.."

    # Кнопка "Выход" в личном кабинете
    LOGOUT_BUTTON = "//button[text()='Выход']"

