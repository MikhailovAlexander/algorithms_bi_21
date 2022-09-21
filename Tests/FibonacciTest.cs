using Algorithms;

namespace Tests;

internal delegate int FibonacciFunc(int num);

public class FibonacciTest
{
    private readonly FibonacciFunc _fibonacci = new FibonacciFunc(Fibonacci.FibonacciRec)
                                                + new FibonacciFunc(Fibonacci.FibonacciIter);

    [Fact]
    public void TestZero()
    {
        Assert.Throws<ArgumentException>(() => this._fibonacci(0));
    }

    [Fact]
    public void TestNegative()
    {
        Assert.Throws<ArgumentException>(() => this._fibonacci(-1));
    }

    [Fact]
    public void TestNumbers()
    {
        int[] numbers =
        {
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711
        };
        for (var i = 1; i < numbers.Length + 1; i++)
        {
            Assert.Equal(numbers[i - 1], this._fibonacci(i));
        }
    }
}