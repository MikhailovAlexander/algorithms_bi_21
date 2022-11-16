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
## Solution
### 1 : 

$$ det A_n = 7 \cdot det A_{n-1} - 6 \cdot 2 \cdot det A_{n-2}$$

### 2 :

$$ det A_10 = 2 \cdot det A_{9} - det A_{8}$$

$$ λ^n = 2 \cdot λ^{n-1} - λ^{n-2} | ÷ λ^{n-2} $$

$$ λ^2 - 2 \cdot λ + 1 = 0  $$

$$ (λ- 1)^2 = 0  $$

$$ λ_1,2 = 1  $$

$$ det A_n = C_1 \cdot λ_1^n \cdot n +  C_2 \cdot λ_2^n $$

$$ det A_1 = 2 $$

$$ det A_2 = 2 \cdot 2 - 1 \cdot 1 = 3 $$

$$
\left\{ 
\begin{array}{c}
2= C_1 + C_2
3= 2 \cdot C_1 +  C_2 
\end{array}
\right. 
$$

$$ C_1 = 2 - C_2  $$

$$ 3 = 4 - 2 \cdot C_2 + C_2 $$

$$ 3 = 4 - 2 \cdot C_2 + C_2 $$

$$ C_2 = 1 $$

$$ C_1 = 2 - 1 = 1 $$

### 3 :

$$ det A_10 = C_1 \cdot λ_1^n \cdot 10 +  C_2 \cdot λ_2^n $$

$$ det A_10 = 1 \cdot 1^10 \cdot 10 +  1 \cdot 1^10 $$

$$ det A_10 = 10 +  1 = 11 $$



