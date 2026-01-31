# Step Project: Аналіз рейтингу кави ☕📊

## Мета проєкту
Завантажити та проаналізувати набір даних рейтингу кави, побудувати візуалізації та відповісти на ключові запитання щодо якості кави, країни походження, кольору зерен та впливу висоти над рівнем моря.

Дозволяється використовувати додаткові типи графіків (matplotlib, seaborn), якщо вони допомагають краще відповісти на запитання.

---

## Джерело даних
Набір даних доступний за посиланням:  

- [ ] [https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-07/coffee_ratings.csv]


Опис набору даних можна знайти у репозиторії **TidyTuesday**.

---

## Підготовка даних

1. Перевіряється наявність файлу `coffee_ratings.csv` у поточному каталозі за допомогою `os.path.exists()`.
2. Якщо файл **існує** — програма продовжує виконання.
3. Якщо файл **відсутній**:
   - Виконується HTTP-запит за допомогою бібліотеки `requests`.
   - Якщо `status_code == 200`, вміст зберігається у файл `coffee_ratings.csv`.
4. Дані зчитуються у `DataFrame` за допомогою `pandas.read_table()` або `pandas.read_csv()`.

---

## Завдання 1. Великі експортери кави 🌍

**Питання:**  
Які країни є найбільшими експортерами кави?

**Підхід:**
- Підрахувати кількість записів або сумарний обсяг експорту за країнами.
- Відібрати **топ-10 країн**.

**Можливі візуалізації:**
1. Вертикальна або горизонтальна стовпчаста діаграма (top-10 експортерів).
2. Стовпчаста діаграма з градієнтними кольорами.
3. Кругова діаграма з відсотковим співвідношенням.
4. Власний варіант.

**Результат:**  
Графік має чітко показувати топ-10 експортерів кави та їхній внесок.

---

## Завдання 2. Кореляції між показниками оцінки 📈

**Питання:**  
Які кореляції існують між різними показниками оцінки кави?

**Підхід:**
1. Обчислити **матрицю кореляцій Пірсона** для числових показників.
2. Побудувати **теплову карту (heatmap)** кореляцій.
3. Відібрати атрибути з кореляцією **≥ 0,65**.
4. За рекомендацією можна виключити:
   - `sweetness`
   - `uniformity`
   - `clean_cup`
5. Побудувати окрему heatmap лише для відібраних атрибутів.

**Варіанти heatmap:**
- Повністю зафарбована матриця.
- Матриця, зафарбована лише до діагоналі.

---

## Завдання 3. Вплив кольору зерен на загальну оцінку 🎨

**Питання:**  
Чи впливає колір зерен на загальний сорт кави?

**Підхід:**
- Згрупувати дані за `species` та `color`.
- Обчислити середнє значення `total_cup_points`.

**Можливі візуалізації:**
1. Heatmap середніх значень `total_cup_points`.
2. Стовпчикова діаграма для порівняння кольорів зерен у межах кожного виду кави.
3. Scatter plot із середніми значеннями.
4. Власний варіант.

**Використання кольорових палітр** обовʼязкове для кращого візуального розрізнення.

# Step Project 1 — Coffee Ratings Analysis

## Description
Analysis of coffee quality ratings dataset using Python.

# Step Project 1 — Coffee Ratings Analysis (Pandas + Matplotlib / Seaborn)

## 1. Project goal
The goal of this project is to analyze the Coffee Quality Institute dataset (TidyTuesday: Coffee Ratings) using **pandas** for data processing and **matplotlib/seaborn** for visualization.

We answer the following questions:
1. Which countries can be considered the largest coffee exporters (using dataset proxies)?
2. What correlations exist between coffee quality attributes?
3. Is there any effect of bean color on total cup score (within species)?
4. Does country of origin influence coffee quality?
5. Does altitude influence coffee quality (visual density analysis)?

Dataset source:
- `coffee_ratings.csv` from TidyTuesday (2020-07-07)

---

## 2. Environment / requirements
- Python 3.x
- pandas
- numpy
- matplotlib
- requests
- seaborn (used for Task 5 KDE plot)

Install:
```bash
pip install pandas numpy matplotlib requests seaborn

## How to run
```bash
cd "Step project 1"
python3 -m src.main