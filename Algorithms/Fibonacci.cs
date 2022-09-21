namespace Algorithms;

public class Fibonacci
{
    /// <summary>
    /// Returns the fibonacci number according to the number specified in the parameter.
    /// Recursive implementation.
    /// </summary>
    /// <param name="num">the ordinal number of the fibonacci number</param>
    /// <returns>a fibonacci number</returns>
    /// <exception cref="ArgumentException"> When the ordinal number is not a positive integer</exception>
    public static int FibonacciRec(int num)
    {
        CheckNum(num);
        
        switch (num)
        {
            case 1:
                return 0;
            case 2:
                return 1;
            default:
                return FibonacciRec(num - 1) + FibonacciRec(num - 2);
        }
    }
    
    /// <summary>
    /// Returns the fibonacci number according to the number specified in the parameter.
    /// Iterative implementation.
    /// </summary>
    /// <param name="num">the ordinal number of the fibonacci number</param>
    /// <returns>a fibonacci number</returns>
    /// <exception cref="ArgumentException"> When the ordinal number is not a positive integer</exception>
    public static int FibonacciIter(int num)
    {
        CheckNum(num);

        int previous = 0;
        int next = 1;

        for (int i = 1; i < num; i++)
        {
            int temp = previous;
            previous = next;
            next += temp;
        }

        return previous;
    }

    private static void CheckNum(int num)
    {
        switch (num)
        {
            case < 0:
                throw new ArgumentException("Can't be negative");
            case 0:
                throw new ArgumentException("Can't be zero");
        }
    }
}