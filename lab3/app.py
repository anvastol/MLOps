# Импорт библиотек
from flask import Flask, request, jsonify

app = Flask(__name__)

# Роут для принятия запросов и возврата предсказаний
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json() # Получение данных из запроса
    input_value = data['input_value'] # Получение входного значения

    # Предсказание на основе входных данных
    prediction = predict_value(input_value)

    return jsonify({'prediction': prediction}) # Возврат предсказания

if __name__ == '__main__':
    app.run(debug=True) # Запуск Flask приложения