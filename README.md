# Задание №3
## Задачи
1. В Файле Program.cs реализовать функцию *GeneratePermutations*, принимающую массив символов   
и возвращающую список строк всех перестановок этих символов. Каждая перестановка это строка, содержащая указанные 
символы в некотором порядке. Генерация перестановок производится рекурсивно. Порядок перестановок в возвращаемом
списке не важен. В списке должны быть однократно представлены все возможные варианты перестановок указанных символов.
2. Для получения повышенной оценки, по желанию, можно реализовать итеративный вариант генерации перестановок.
## Примечания
- Разработку вести в отдельной ветке, созданной на основе данной. В названии ветки префикс main заменить на название
  команды.
- Изменения в ветке должны быть только в файле Program.cs, различные конфигурационные файлы и кэш IDE фиксировать
  не нужно.
- Корректность работы функции *GeneratePermutations* проверить запустив модульные тесты из файла PermutationsTest.cs.

## Перестановки
Под перестановкой понимается упорядоченный набор без повторений чисел 1 ,   2 ,   … ,   n , обычно трактуемый
как биекция на множестве { 1 , 2 , … , n } которая числу i ставит в соответствие i-й элемент из набора. Число n
при этом называется длиной перестановки.

Перестановки из n элементов - это размещения по n элементов из n. Количество различных перестановок, определяет
сколькими способами можно переупорядочить элементы множества. Количество перестановок обозначается как
P<sub>n</sub>, где n - количество элементов множества.

Число перестановок определяется по формуле P<sub>n</sub> = n!

При этом 0! = 1, так как упорядочить пустое множество можно лишь одним способом - { ∅ }.

Множество из одного элемента также можно упорядочить лишь одним способом - { 1 }.

Множество из двух элементов можно упорядочить двумя способами - { 12, 21 }.

Множество из трех элементов можно упорядочить шестью способами - { 123, 132, 213, 231, 312, 321 }.