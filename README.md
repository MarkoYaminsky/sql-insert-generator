# SQL INSERT generator

Інструкція з роботи з генератором виразів INSERT

Ввести в словник tables дані своїх таблиць в форматі: </br>
`"table_name": "column_1 column_2 column_3..."` </br>
**ВАЖЛИВО** - стовпці мають бути перелічені строго через пробіл </br>
Дані вводити в тому порядку, як ви заповнювали б свою базу даних </br>(тобто спочатку поля без foreign key, а потім вже залежні від них)

Далі скопіювати свої дані з таблиць і вставити в файл data
Копіювати дані в MySQL Workbench так:
 1. Відкриваємо таблицю з даними
 2. Натискаємо мишкою на перший рядок перший стовпець своєї таблиці
 3. Затискаємо клавішу shift і натискаємо мишкою на останній рядок останній стовець своєї таблиці
 4. Ctrl (command) + c
Послідовність вставки даних в файл data має бути ідентичним
До послідовності наведення таблиць у словнику tables </br>

**ВАЖЛИВО** - в кінці файлу data не має бути жодного пустого рядка

Запускаємо код і звіряємо, чи послідовність запитів INSERT збігається
З послідовністю внесення даних в файл data
Якщо так, то копіюємо вивід і користуємося в своїх цілях
Якщо ні, то скоріше за все у вас версія пайтону 3.8<
(Бо там, здається, не впорядковані словники - але це не точно)

На цьому все, успіхів у виконанні 3 лабораторної!

P.S: Залишаю дані з словника tables і файлу data для прикладу - їх треба замінити на свої
