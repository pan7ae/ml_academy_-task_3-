# Задание 3

## Реализовать систему прогнозирования неблагоприятных погодных условий на основе датасета «Hurricanes and Typhoons, 1851-2014 Dataset»
 
Указанный датасет представляет собой набор данных, содержащий информацию о тропических циклонах (ураганах и тайфунах), зарегистрированных с 1851 по 2014 год. Этот датасет предназначен для анализа и исследования различных аспектов тропических циклонов в течение продолжительного периода времени.

## Для достижения поставленной цели вам необходимо выполнить следующие задачи:

1.	Прочитать предоставленный датасет из csv файла и провести предварительный анализ данных. Визуализировать временные ряды для получения более наглядного представления о динамике циклонов. Выявить основные характеристики временных рядов, такие как тренды, сезонность, выбросы и т.д.
2.	Провести подготовку данных временных рядов, например, методом скользящего окна. Если необходимо, проведите нормализацию данных внутри каждого окна для облегчения обучения моделей.
3.	Обучить модели семейства ARIMA (AutoRegressive Integrated Moving Average), в частности модели SARIMA и SARIMAX, для прогнозирования временных рядов. Проанализируйте результаты.
4.	Разработать и обучить нейронную сеть для прогнозирования временных рядов (выбор архитектуры должен исходить из структуры данных).
5.	Результаты также должны быть зафиксированы в облачном сервисе wandb, аналогично предыдущему заданию.
6.	На основе результатов лучшей модели постарайтесь реализовать приложение API, которое обрабатывает входящие запросы (получает на вход год после 2015) и выдает прогнозируемое число циклонов в указанном году. Тестирование метода можете выполнить через программу Postman.

## Использование программы

To run the Forecasting API, follow these steps:

1. Clone the repository or download the source code.
2. Navigate to the directory containing the source code.
3. Ensure that you have the following files in the appropriate directories:
    - SARIMA_model.pkl: Pre-trained SARIMA model for hurricane forecasting.
    - hurricanes_per_year.csv: Dataset containing historical hurricane data.
4. Open a terminal or command prompt in the directory containing the source code.
5. Run the following command to start the API server:
    ```bash
    uvicorn task_3:app --reload
    ```
    or
    ```bash
    python3 task_3.py
    ```

## Sending Requests
You can send HTTP requests to the API endpoints using tools like cURL or Postman. Here's an example request:

- **Endpoint**: `http://localhost:8000/forecast/`
- **Method**: `GET`
- **Query Parameter**:
    - `year`: The year for which you want to get the hurricane forecast.

Example request URL: `http://localhost:8000/forecast/?year=2025`

The API will respond with a JSON object containing the forecasted number of hurricanes for the specified year.

You can also run tests.py file with the command
```bash
python3 tests.py
```
