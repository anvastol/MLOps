# Импорт необходимых библиотек
import numpy as np
from sklearn.linear_model import LinearRegression

# Создание и обучение модели линейной регрессии
X = np.array([[1], [2], [3], [4], [5]]) # Входные признаки
y = np.array([2, 4, 6, 8, 10]) # Целевая переменная

model = LinearRegression()
model.fit(X, y)

# Функция для предсказания значений
def predict_value(input_value):
    return model.predict([[input_value]])[0]

# Пример использования модели
print(predict_value(6)) # Предсказание для входного значения 6