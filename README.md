# Задание №9 
## Задача  
В Файле tasks.md решить четвертую модельную задачу 
## Постановка задачи
- количество заданий произвольно
- каждое задание имеет свою длительность;
- задания независимы (т.е. их можно выполнять одновременно);
- разрешены прерывания при выполнении заданий;
- количество работников произвольно (но не больше числа заданий);
- работники универсальны (т.е. каждый может выполнять любое задание);
- у каждого работника своя производительность;
- требуется построить расписание выполнения всех заданий в кратчайшие сроки.
## Примечание:
Работники могут отличаться пронзводительностью. Это означает, что одно и то же задание может выполняться быстрее или медленнее в зависимости от 
работника, которому оно было назначено. А поскольку в данной задаче разрешены прерывания, то нам разрешено менять исполнителей одного и того же задания. 
Например, начать выполнять задание может исполнитель с низкой производительностью, а завершить - исполнитель с более высокой производительностью, или 
наоборот. Оказывается, за счёт правильного выбора моментов прерываний и правильного подбора исполнителей можно существенно сократить общее время 
выполнения всех заданий. Для нас важно, что правильное решение можно найти с помощью эффективного (т.е. быстрого и точного) алгоритма.
