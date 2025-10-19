from machine import Pin, I2C
import time
import ssd1306
import math


DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 64
LINE_LENGTH = 16
MIN_SCORE_POINTS = 5
MAX_SCORE_POINTS = 50
INITIAL_SCORE_POINTS = 10
ROW_SPACING = 11
SEPARATOR_HEIGHT = 1
I2C_FREQ = 400_000
I2C_SCL_PIN = 1
I2C_SDA_PIN = 0
OLED_I2C_ADDR = 0x3C
BUTTON_DEBOUNCE_DELAY = 0.15


i2c = I2C(0, scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN), freq=I2C_FREQ)
oled = ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c, addr=OLED_I2C_ADDR)

button_increase = Pin(2, Pin.IN, Pin.PULL_DOWN)
button_decrease = Pin(3, Pin.IN, Pin.PULL_DOWN)


grade_ranges = [
    {'grade': 1, 'min_percent': 0, 'max_percent': 30},
    {'grade': 2, 'min_percent': 31, 'max_percent': 50},
    {'grade': 3, 'min_percent': 51, 'max_percent': 74},
    {'grade': 4, 'min_percent': 75, 'max_percent': 89},
    {'grade': 5, 'min_percent': 90, 'max_percent': 98},
    {'grade': 6, 'min_percent': 99, 'max_percent': 100},
]


current_points = INITIAL_SCORE_POINTS


def round_half_up(value):  # round to the nearest 0.5 upwards
    return round(math.ceil(round(value, 1) * 2) / 2, 1)


def round_half_down(value): # round to the nearest 0.5 downwards
    return round(math.floor(round(value, 1) * 2) / 2, 1)


def rjust(text, width, fillchar=' '):  # same as string.rjust
    return fillchar * (width - len(text)) + text if len(text) < width else text


def as_integer_if_whole(number):
    return int(number) if int(number) == number else number


while True:  # main loop
    if button_increase.value():
        current_points = min(MAX_SCORE_POINTS, current_points + 1)
        time.sleep(BUTTON_DEBOUNCE_DELAY)

    elif button_decrease.value():
        current_points = max(MIN_SCORE_POINTS, current_points - 1)
        time.sleep(BUTTON_DEBOUNCE_DELAY)


    oled.fill(0)  # clear the display

    last_max_points = -1
    for index, grade_info in enumerate(grade_ranges):
        grade = grade_info['grade']
        min_percent = grade_info['min_percent']
        max_percent = grade_info['max_percent']

        min_points = round_half_down(min_percent / 100 * current_points)
        max_points = round_half_down(max_percent / 100 * current_points)

        if last_max_points == min_points:
            min_points += 0.5
        last_max_points = max_points

        min_points = as_integer_if_whole(min_points)
        max_points = as_integer_if_whole(max_points)

        if min_points == max_points:
            points_text = f'{max_points}'
        else:
            points_text = f'{min_points} - {max_points}'

        line_text = points_text + right_justify(str(grade), LINE_LENGTH - len(points_text))
        y_position = len(grade_ranges) * ROW_SPACING - (index + 1) * ROW_SPACING

        # draw
        oled.text(line_text, 0, y_position)
        oled.rect(0, (index * ROW_SPACING) - 2, DISPLAY_WIDTH - 1, SEPARATOR_HEIGHT, 1)

    oled.show()

