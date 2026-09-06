import flet as ft
import random
import string

def main(page: ft.Page):
    page.title = "Генератор паролей"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.window_width = 360
    page.window_height = 640

    # Поле для вывода пароля
    password_field = ft.TextField(
        label="Ваш пароль",
        read_only=True,
        text_align=ft.TextAlign.CENTER,
        text_style=ft.TextStyle(size=18, weight=ft.FontWeight.BOLD),
    )

    # Ползунок длины пароля (от 6 до 30 символов)
    length_slider = ft.Slider(
        min=6,
        max=30,
        divisions=24,
        value=12,
        label="{value} симв."
    )
    
    length_text = ft.Text("Длина пароля: 12")

    def slider_changed(e):
        length_text.value = f"Длина пароля: {int(length_slider.value)}"
        page.update()

    length_slider.on_change = slider_changed

    # Чекбоксы (галочки) для настроек
    use_digits = ft.Checkbox(label="Цифры (0-9)", value=True)
    use_letters = ft.Checkbox(label="Буквы (a-Z)", value=True)
    use_symbols = ft.Checkbox(label="Спецсимволы (!@#$)", value=False)

    # Текст для уведомления о копировании
    copy_status = ft.Text("", color="green", size=12)

    # Функция генерации пароля
    def generate_password(e):
        chars = ""
        if use_letters.value:
            chars += string.ascii_letters
        if use_digits.value:
            chars += string.digits
        if use_symbols.value:
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

        if not chars:
            password_field.value = "Выберите хотя бы один тип!"
            page.update()
            return

        length = int(length_slider.value)
        generated = "".join(random.choice(chars) for _ in range(length))
        password_field.value = generated
        copy_status.value = ""
        page.update()

    # Функция копирования в буфер обмена
    def copy_to_clipboard(e):
        if password_field.value and password_field.value != "Выберите хотя бы один тип!":
            page.clipboard.set(password_field.value)
            copy_status.value = "Пароль скопирован в буфер!"
            page.update()

    # Актуальные кнопки для версии 0.80+ через content
    gen_button = ft.TextButton(
        content="Сгенерировать", 
        on_click=generate_password,
        width=200
    )
    
    copy_button = ft.TextButton(
        content="Копировать", 
        on_click=copy_to_clipboard,
        width=200
    )

    # Собираем всё на экран
    page.add(
        ft.Column(
            [
                ft.Text("Генератор паролей", size=22, weight=ft.FontWeight.BOLD),
                ft.Container(height=5),
                password_field,
                copy_status,
                ft.Divider(height=20),
                length_text,
                length_slider,
                ft.Container(height=5),
                use_letters,
                use_digits,
                use_symbols,
                ft.Divider(height=20),
                gen_button,
                copy_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.run(main)