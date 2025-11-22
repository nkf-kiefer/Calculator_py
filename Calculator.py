# Import dependencies
import flet as ft
import math

def main(page: ft.Page):
    page.title = "Calculator"
    page.bgcolor = "#2d2d2d"
    page.window.width = 350
    page.window.height = 300

    values = ""  # variable initially empty

    # Configure result display
    result = ft.Text(value="0", size=28, color="white", text_align="right")

    # Function to receive input values
    def append_value(e):
        nonlocal values
        values += str(e.control.text)
        result.value = values
        page.update()

    # Function to clear values
    def clear_values(e):
        nonlocal values
        values = ""
        result.value = "0"
        page.update()

    # Function to evaluate expression
    def calculate(e):
        nonlocal values
        try:
            # Receiving the value and converting to str
            result.value = str(eval(values))
            values = result.value
        except Exception:
            result.value = "Error"
            values = ""
        page.update()

    # Square root operation
    def square_root(e):
        nonlocal values
        try:
            conversion = float(values) if values else 0.0
            if conversion < 0:
                raise ValueError("Negative sqrt")
            result.value = str(math.sqrt(conversion))
            values = result.value
        except Exception:
            result.value = "Error"
            values = ""
        page.update()

    # Exponentiation operation (square)
    def square(e):
        nonlocal values
        try:
            conversion = float(values) if values else 0.0
            result.value = str(conversion**2)
            values = result.value
        except Exception:
            result.value = "Error"
            values = ""
        page.update()

    # Reciprocal operation (1/x)
    def reciprocal(e):
        nonlocal values
        try:
            conversion = float(values)
            if conversion == 0:
                raise ZeroDivisionError()
            result.value = str(1 / conversion)
            values = result.value
        except Exception:
            result.value = "Error"
            values = ""
        page.update()

    # Remove last digit
    def backspace(e):
        nonlocal values
        values = values[:-1]
        result.value = values or "0"
        page.update()

    # Result container configuration (não sobrescreva 'page')
    display_container = ft.Container(
        content=result,
        bgcolor="#37474F",
        padding=10,
        border_radius=10,
        height=70,
        alignment=ft.alignment.center_right,
    )

    # Button styles
    style_numbers = {
        "height": 60,
        "bgcolor": "#4d4d4d",
        "color": "white",
        "expand": 1,
    }

    style_operators = {
        "height": 60,
        "bgcolor": "#FF9500",
        "color": "white",
        "expand": 1,
    }

    style_clear = {
        "height": 60,
        "bgcolor": "#FF3B30",
        "color": "white",
        "expand": 1,
    }

    style_equal = {
        "height": 60,
        "bgcolor": "#34C759",
        "color": "white",
        "expand": 1,
    }

    # Define calculator buttons
    button_grid = [
        [
            ("%", style_operators, append_value),
            ("/", style_operators, append_value),
            ("*", style_operators, append_value),
            ("C", style_clear, clear_values),
        ],
        [
            ("⨉²", style_operators, square),
            ("√", style_operators, square_root),
            ("¹⁄ₓ", style_operators, reciprocal),
            ("CE", style_clear, backspace),
        ],
        [
            ("7", style_numbers, append_value),
            ("8", style_numbers, append_value),
            ("9", style_numbers, append_value),
            ("-", style_operators, append_value),
        ],
        [
            ("4", style_numbers, append_value),
            ("5", style_numbers, append_value),
            ("6", style_numbers, append_value),
            ("+", style_operators, append_value),
        ],
        [
            ("1", style_numbers, append_value),
            ("2", style_numbers, append_value),
            ("3", style_numbers, append_value),
            ("=", style_equal, calculate),
        ],
        [  # Style of the number 0
            ("0", {**style_numbers, "expand": 2}, append_value),
            (".", style_numbers, append_value),
            ("⌫", style_operators, backspace),
        ],
    ]

    # Create buttons
    rows = []
    for line in button_grid:
        line_controls = []
        for text, style, handler, *_ in line:
            btn = ft.ElevatedButton(
                text=text,
                on_click=handler,
                **style,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    padding=0,
                ),
            )
            line_controls.append(btn)
        rows.append(ft.Row(controls=line_controls, spacing=5))

    # Main layout
    main_column = ft.Column(
        controls=[
            display_container,
            ft.Column(controls=rows, spacing=5),
        ],
        spacing=10,
    )

    page.add(main_column)

ft.app(target=main)