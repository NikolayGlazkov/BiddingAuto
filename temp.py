import turtle

# Настройка окна
window = turtle.Screen()
window.title("Пример с Turtle")
window.bgcolor("lightblue")

# Настройка черепахи
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(1) # Скорость от 1 (самая медленная) до 10 (самая быстрая)

# Рисование квадрата
for _ in range(4):
    my_turtle.forward(100) # Двигаться вперед на 100 единиц
    my_turtle.right(90) # Повернуть на 90 градусов вправо

# Завершение работы
turtle.done()
