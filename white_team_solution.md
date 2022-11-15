### Условие
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
Порядок матрицы _n_ = 8

### Решение
$$ det A_n = -8 \cdot det A_{n-1} - 15\cdot 1 \cdot det A_{n-2}$$
#### Характеристическое уравнение
$$ λ^n = -8 \cdot λ^{n-1} - 15 \cdot λ^{n-2} | ÷ λ^{n-2} $$

$$λ^2 = -8 \cdot λ - 15 $$

$$λ^2 + 8 \cdot λ + 15 = 0$$

$$λ_1=-3 $$

$$λ_2= -5$$
#### Общая формула
$$ det A_n = C_1 \cdot -3^n + C_2 \cdot -5^n $$
#### Определители 1 и 2 порядка
$$ det A_1 = -8 $$

$$ det A_2 = 49 $$
#### Нахождение констант

$$
\left\{
\begin{array}{c}
-8= -3 \cdot C_1 - 5 \cdot C_2 | \cdot 5\\
49= 9 \cdot C_1 + 25 \cdot C_2
\end{array}
\right.
$$

$$
\left\{
\begin{array}{c}
-40= -15 \cdot C_1 - 25 \cdot C_2 \\
49= 9 \cdot C_1 + 25 \cdot C_2
\end{array}
\right.
$$
$$ 9= -6 \cdot C_1 $$

$$ C_1 = -1,5 $$

$$C_2 = 2,5 $$
#### Окончательное решение
$$ det A_n = -1,5 \cdot -3^n + 2,5 \cdot -5^n$$

$$det A_8 = -1,5 \cdot -3^8 + 2,5 \cdot -5^8=966721$$




