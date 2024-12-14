# URL главной страницы
URL_MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"

# Главная страница - кнопка "Войти в аккаунт"
LOGIN_BUTTON_LOCATOR = "//button[text()='Войти в аккаунт']"

# Форма авторизации - поле ввода имени
AUTH_NAME_INPUT_LOCATOR = "//form[@class='Auth_form__3qKeq mb-20']//input[@name='name']"

# Форма авторизации - поле ввода пароля
AUTH_PASSWORD_INPUT_LOCATOR = "//form[@class='Auth_form__3qKeq mb-20']//input[@name='Пароль']"

# Форма авторизации - кнопка "Войти"
AUTH_SUBMIT_BUTTON_LOCATOR = "//form[@class='Auth_form__3qKeq mb-20']//button[text()='Войти']"

# Главная страница - кнопка "Оформить заказ"
ORDER_BUTTON_LOCATOR = "//button[text()='Оформить заказ']"

# Главная страница - кнопка "Личный кабинет"
ACCOUNT_BUTTON_LOCATOR = "//a[@href='/account']"

# Страница регистрации - кнопка "Войти"
REGISTRATION_LOGIN_BUTTON_LOCATOR = "//a[@href='/login']"

# Страница восстановления пароля - кнопка "Войти"
FORGOT_PASSWORD_LOGIN_BUTTON_LOCATOR = "//a[@href='/login']"

# URL страницы регистрации
URL_REGISTER_PAGE = "https://stellarburgers.nomoreparties.site/register"

# Форма регистрации - поле ввода имени
REGISTRATION_NAME_INPUT_LOCATOR = "(//form[@class='Auth_form__3qKeq mb-20']//input)[1]"

# Форма регистрации - поле ввода email
REGISTRATION_EMAIL_INPUT_LOCATOR = "(//form[@class='Auth_form__3qKeq mb-20']//input)[2]"

# Форма регистрации - поле ввода пароля
REGISTRATION_PASSWORD_INPUT_LOCATOR = "(//form[@class='Auth_form__3qKeq mb-20']//input)[3]"

# Форма регистрации - кнопка "Зарегистрироваться"
REGISTRATION_SUBMIT_BUTTON_LOCATOR = "//form[@class='Auth_form__3qKeq mb-20']//button[text()='Зарегистрироваться']"

# Ошибка при некорректном пароле
INVALID_PASSWORD_ERROR_LOCATOR = "//div[@class='input__container']/p[text()='Некорректный пароль']"

# URL страницы авторизации
URL_LOGIN_PAGE = "https://stellarburgers.nomoreparties.site/login"

# Поле ввода имени в форме авторизации
LOGIN_NAME_INPUT_LOCATOR = "//input[@name='name']"

# Поле ввода пароля в форме авторизации
LOGIN_PASSWORD_INPUT_LOCATOR = "//input[@name='Пароль']"

# Кнопка "Войти" в форме авторизации
LOGIN_SUBMIT_BUTTON_LOCATOR = "//button[text()='Войти']"

# Ссылка "Личный кабинет"
LK_BUTTON_LOCATOR = "//a[@href='/account']"

# Ссылка "Конструктор" в меню
CONSTRUCTOR_BUTTON_LOCATOR = "//a[@class='AppHeader_header__link__3D_hX' and @href='/']"

# Логотип Stellar Burgers
LOGO_LOCATOR = "//nav[@class='AppHeader_header__nav__g5hnF']//a[@href='/']"

# URL личного кабинета
URL_LK_PROFILE = "https://stellarburgers.nomoreparties.site/account/profile"

# URL конструктора
URL_CONSTRUCTOR = "https://stellarburgers.nomoreparties.site/"

# Класс активного раздела
ACTIVE_CLASS = "tab_tab_type_current__2BEPc"

# Локаторы разделов
BULKY_TAB_LOCATOR = "//span[text()='Булки']/.."
SAUCE_TAB_LOCATOR = "//span[text()='Соусы']/.."
NACHINKY_TAB_LOCATOR = "//span[text()='Начинки']/.."

# Кнопка "Выход" в личном кабинете
LOGOUT_BUTTON_LOCATOR = "//button[text()='Выход']"

# URL страницы после выхода (авторизации)
URL_AFTER_LOGOUT = "https://stellarburgers.nomoreparties.site/login"

