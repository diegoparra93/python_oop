# Лабораторная работа 1

# Laboratorio 1: Clase User

## Autor: Diego Parra

---

## 1. Мыслительный процесс создания класса / Thought process for creating the class

**Русский:**
1. **Анализ задачи**: Мне нужно было создать класс, представляющий пользователя с личными данными (имя, группа крови, вес, возраст, email, город). Главное требование — данные должны быть валидными.

2. **Выбор атрибутов**: Я выбрал 6 атрибутов, которые обычно используются в системах управления пользователями: имя, группа крови, вес, возраст, email, город.

3. **Инкапсуляция**: Я сделал атрибуты закрытыми (с _), чтобы к ним нельзя было обратиться напрямую. Для доступа я использовал свойства (@property).

4. **Валидация**: Для каждого атрибута я создал отдельный метод валидации (_validate_email, _validate_blood_type и т.д.), который проверяет:
   - Email должен содержать @
   - Группа крови должна быть из списка допустимых
   - Вес и возраст должны быть положительными
   - Город не может быть пустым

5. **Магические методы**:
   - `__str__`: для красивого вывода информации о пользователе
   - `__eq__`: для сравнения пользователей по email

6. **Бизнес-метод**: `is_adult()` проверяет, является ли пользователь совершеннолетним (возраст >= 18).

7. **Атрибут класса**: `total_users` считает, сколько всего пользователей было создано.

**Español:**
1. **Análisis de la tarea**: Necesitaba crear una clase que representara un usuario con datos personales (nombre, tipo de sangre, peso, edad, email, ciudad). El requisito principal era que los datos fueran válidos.

2. **Selección de atributos**: Elegí 6 atributos que se usan comúnmente en sistemas de gestión de usuarios: nombre, tipo de sangre, peso, edad, email, ciudad.

3. **Encapsulación**: Hice los atributos privados (con _) para que no se pudieran acceder directamente. Para el acceso usé propiedades (@property).

4. **Validación**: Para cada atributo creé un método de validación separado (_validate_email, _validate_blood_type, etc.) que verifica:
   - El email debe contener @
   - El tipo de sangre debe estar en la lista permitida
   - El peso y la edad deben ser positivos
   - La ciudad no puede estar vacía

5. **Métodos mágicos**:
   - `__str__`: para mostrar información del usuario de forma legible
   - `__eq__`: para comparar usuarios por email

6. **Método de negocio**: `is_adult()` verifica si el usuario es mayor de edad (edad >= 18).

7. **Atributo de clase**: `total_users` cuenta cuántos usuarios se han creado en total.

---

## 2. Ответы на 5 вопросов с Практического занятия №1 / Answers to 5 questions from Practical Class №1

**Вопрос 1: Что такое инкапсуляция и зачем она нужна?**  
**Ответ:** Инкапсуляция — это сокрытие внутренних данных объекта и предоставление доступа к ним только через методы. Это нужно для защиты данных от некорректного изменения и контроля над ними.

**Pregunta 1: ¿Qué es la encapsulación y para qué sirve?**  
**Respuesta:** La encapsulación es ocultar los datos internos de un objeto y proporcionar acceso a ellos solo a través de métodos. Sirve para proteger los datos de modificaciones incorrectas y tener control sobre ellos.

---

**Вопрос 2: Чем отличается атрибут класса от атрибута экземпляра?**  
**Ответ:** Атрибут класса принадлежит самому классу и общий для всех объектов. Атрибут экземпляра принадлежит конкретному объекту. В моём коде `total_users` — это атрибут класса, а `_name`, `_email` — атрибуты экземпляра.

**Pregunta 2: ¿Cuál es la diferencia entre un atributo de clase y un atributo de instancia?**  
**Respuesta:** El atributo de clase pertenece a la clase y es compartido por todos los objetos. El atributo de instancia pertenece a un objeto específico. En mi código, `total_users` es un atributo de clase, mientras que `_name`, `_email` son atributos de instancia.

---

**Вопрос 3: Для чего нужен декоратор @property?**  
**Ответ:** @property позволяет определить метод, к которому можно обращаться как к атрибуту. Это нужно, чтобы контролировать доступ к данным и добавлять логику при чтении или изменении значения.

**Pregunta 3: ¿Para qué sirve el decorador @property?**  
**Respuesta:** @property permite definir un método al que se puede acceder como si fuera un atributo. Sirve para controlar el acceso a los datos y agregar lógica al leer o modificar un valor.

---

**Вопрос 4: Чем отличается __str__ от __repr__?**  
**Ответ:** `__str__` используется для вывода информации для пользователя (например, в print). `__repr__` используется для отладки и должен показывать более техническое представление объекта. В моём коде реализован только `__str__`.

**Pregunta 4: ¿Cuál es la diferencia entre __str__ y __repr__?**  
**Respuesta:** `__str__` se usa para mostrar información al usuario (por ejemplo, en print). `__repr__` se usa para depuración y debe mostrar una representación más técnica del objeto. En mi código solo implementé `__str__`.

---

**Вопрос 5: Как обрабатывать ошибки при создании объекта?**  
**Ответ:** В конструкторе класса нужно проверять входные данные и вызывать исключение ValueError, если данные некорректны. В демонстрационном коде нужно использовать try/except, чтобы перехватывать эти ошибки и показывать понятные сообщения.

**Pregunta 5: ¿Cómo se manejan los errores al crear un objeto?**  
**Respuesta:** En el constructor de la clase hay que validar los datos de entrada y lanzar una excepción ValueError si los datos son incorrectos. En el código de demostración hay que usar try/except para capturar estos errores y mostrar mensajes claros.

---

## 3. Скриншоты работы demo.py / Screenshots of demo.py execution

### Сценарий 1: Успешное создание объектов / Scenario 1: Successful object creation
![Успешное создание](images/lab01/ejecucion_demo.png)
*На скриншоте видно создание двух пользователей, вывод их данных, проверку возраста, сравнение и общее количество пользователей.*

### Сценарий 2: Обработка ошибок валидации / Scenario 2: Validation error handling
![Валидация](images/lab01/validaciones.png)
*На скриншоте показано, как программа перехватывает ошибки при попытке создать пользователя с неверным email, пустым городом и отрицательным возрастом.*

---

## 4. Как запустить код / How to run the code

```bash
cd src/lab01
python demo.py