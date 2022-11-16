
# Вычисление ленточного определителя (трехдиагональной матрицы)  
В условиях задачи для каждой команды указана трехдиагональная матрица порядка   
*n*. Для решения задачи требуется:  
1. Вывести рекуррентное соотношение для предложенной матрицы.  
2. Составить и решить характеристическое уравнение.  
3. Вывести формулу общего решения.  
4. Рассчитать на основе полученной формулы значение определителя матрицы   
порядка порядка *n*.  
5. ## Условия задачи для команд:  
### White Team:  

$$    
A =     
 \begin{pmatrix}    
  -8 & 1 & 0 & \cdots & 0 & 0 \\    
  15 & -8 & 1 & \cdots & 0 & 0 \\    
  0 & 15 & -8 & \cdots & 0 & 0 \\    
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\    
  0 & 0 & 0 & \cdots & -8 & 1 \\    
  0 & 0 & 0 & \cdots & 15 & -8     
 \end{pmatrix}    
$$

Порядок матрицы *n* = 8

### Spirits Team:  

$$    
A =     
 \begin{pmatrix}    
  2 & 1 & 0 & \cdots & 0 & 0 \\    
  1 & 2 & 1 & \cdots & 0 & 0 \\    
  0 & 1 & 2 & \cdots & 0 & 0 \\    
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\    
  0 & 0 & 0 & \cdots & 2 & 1 \\    
  0 & 0 & 0 & \cdots & 1 & 2     
 \end{pmatrix}    
$$

Порядок матрицы *n* = 10

### Yellow Team:  

$$    
A =     
 \begin{pmatrix}    
  11 & 2 & 0 & \cdots & 0 & 0 \\    
  14 & 11 & 2 & \cdots & 0 & 0 \\    
  0 & 14 & 11 & \cdots & 0 & 0 \\    
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\    
  0 & 0 & 0 & \cdots & 11 & 2 \\    
  0 & 0 & 0 & \cdots & 14 & 11     
 \end{pmatrix}    
$$

Порядок матрицы *n* = 12

### Pink Team:  

$$    
A =     
 \begin{pmatrix}    
  3 & 2 & 0 & \cdots & 0 & 0 \\    
  1 & 3 & 2 & \cdots & 0 & 0 \\    
  0 & 1 & 3 & \cdots & 0 & 0 \\    
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\    
  0 & 0 & 0 & \cdots & 3 & 2 \\    
  0 & 0 & 0 & \cdots & 1 & 3     
 \end{pmatrix}    
$$

Порядок матрицы *n* = 7

### Orange Team:  

$$    
A =     
 \begin{pmatrix}    
  6 & -3 & 0 & \cdots & 0 & 0 \\    
  9 & 6 & -3 & \cdots & 0 & 0 \\    
  0 & 9 & 6 & \cdots & 0 & 0 \\    
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\    
  0 & 0 & 0 & \cdots & 6 & -3 \\    
  0 & 0 & 0 & \cdots & 9 & 6     
 \end{pmatrix}    
$$

Порядок матрицы *n* = 11

### Green Team:  

$$    
A =     
 \begin{pmatrix}    
  7 & 6 & 0 & \cdots & 0 & 0 \\    
  2 & 7 & 6 & \cdots & 0 & 0 \\    
  0 & 2 & 7 & \cdots & 0 & 0 \\    
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\    
  0 & 0 & 0 & \cdots & 7 & 6 \\    
  0 & 0 & 0 & \cdots & 2 & 7     
 \end{pmatrix}    
$$

Порядок матрицы *n* = 10

### Red Team:  

$$    
A =     
 \begin{pmatrix}    
  10 & 5 & 0 & \cdots & 0 & 0 \\    
  5 & 10 & 5 & \cdots & 0 & 0 \\    
  0 & 5 & 10 & \cdots & 0 & 0 \\    
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\    
  0 & 0 & 0 & \cdots & 10 & 5 \\    
  0 & 0 & 0 & \cdots & 5 & 10     
 \end{pmatrix}    
$$

Порядок матрицы *n* = 13

### Blue Team:  

$$    
A =     
 \begin{pmatrix}    
  6 & 5 & 0 & \cdots & 0 & 0 \\    
  1 & 6 & 5 & \cdots & 0 & 0 \\    
  0 & 1 & 6 & \cdots & 0 & 0 \\    
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\    
  0 & 0 & 0 & \cdots & 6 & 5 \\    
  0 & 0 & 0 & \cdots & 1 & 6     
 \end{pmatrix}    
$$

Порядок матрицы *n* = 8


### Black Team:

$$    
A =     
 \begin{pmatrix}    
  4 & 3 & 0 & \cdots & 0 & 0 \\    
  -4 & 4 & 3 & \cdots & 0 & 0 \\    
  0 & -4 & 4 & \cdots & 0 & 0 \\    
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\    
  0 & 0 & 0 & \cdots & 4 & 3 \\    
  0 & 0 & 0 & \cdots & -4 & 4     
 \end{pmatrix}    
$$

Порядок матрицы *n* = 9

### Purple Team:

$$    
A =     
 \begin{pmatrix}    
  9 & 2 & 0 & \cdots & 0 & 0 \\    
  9 & 9 & 2 & \cdots & 0 & 0 \\    
  0 & 9 & 9 & \cdots & 0 & 0 \\    
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\    
  0 & 0 & 0 & \cdots & 9 & 2 \\    
  0 & 0 & 0 & \cdots & 9 & 9     
 \end{pmatrix}    
$$

Порядок матрицы *n* = 6
