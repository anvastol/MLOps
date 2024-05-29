import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Генерируем случайные данные для обучения модели
X = np.random.rand(100, 1)
y = 5 * X.squeeze() + np.random.randn(100)

# Создаем модель и обучаем ее
model = LinearRegression()
model.fit(X, y)

# Сохраняем модель в файл
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)