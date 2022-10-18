from custom_exception import ArgumentException


def invest_distribution(profit_matrix: list[list[int]]) -> dict[str: int, str: list[int]]:
    """Calculates the optimal distribution of investments between several
    projects. Investments are distributed in predetermined parts.

    :param profit_matrix: an integer matrix with profit values, investment
    levels as rows and the project index as columns;
    :raise ArgumentException: when parameter is not an integer rectangle matrix.
    :return: a dictionary with keys: profit - the max profit value, parts -
    a list with the part of investments for each project. The result example:
    {'profit': 73, 'parts': [1, 1, 2, 1]}
    """
    if table_has_errors(profit_matrix):
        raise ArgumentException('parameter is not an integer rectangle matrix')
    all_max_profits = calculate_for_profit(profit_matrix)
    itog_profit = all_max_profits[-1][-1]
    profit = itog_profit['get']
    distribution=find_distribution(itog_profit,all_max_profits)
    return{'profit': profit, 'parts': distribution}

def table_has_errors(profit_matrix:list[list[int]])->bool:
    if profit_matrix is None or profit_matrix==[]:
        return True
    row_idx=len(profit_matrix[0])
    for row in profit_matrix:
        if row_idx!=len(row):
            return True
    for value in row:
        if type(value)!=int:
            return True
    return False
def calculate_for_profit(profit_matrix:list[list[int]])-> list[dict[str,int]]:
    help_matrix=[[0]*len(profit_matrix[0])for i in range(len(profit_matrix)+1)]
    for i in range (1,len(help_matrix)):
        for j in range(len(help_matrix[0])):
            help_matrix[i][j]=profit_matrix[i-1][j]
    max_profits_with_shares=[[{'get': 0, 'share': 0}for value in row]for row in help_matrix]
    for i in range(len(help_matrix[0])):
        for j in range(len(help_matrix)):
            max_profit=0
            share_for_max=0
            for k in range(j+1):
                share=j-k
                profit=help_matrix[share][i]
                profit_before=max_profits_with_shares[k][i-1]['get']
                sum_profit=profit+profit_before
                if max_profit<sum_profit:
                    max_profit=sum_profit
                    share_for_max=share
            max_profits_with_shares[j][i] = {'get': max_profit, 'share': share_for_max}
    return max_profits_with_shares

def find_distribution(itog_profit, max_profits_with_shares):
    share=itog_profit['share']
    projects=len(max_profits_with_shares[0])
    distribution=[share]
    share_before=len(max_profits_with_shares)-share-1
    for i in range(projects-2,-1,-1):
        distribution.append(max_profits_with_shares[share_before][i]['share'])
        share_before-=max_profits_with_shares[share_before][i]['share']
    distribution.reverse()
    return distribution

def main():
    profit_matrix = [[15, 18, 16, 17],
                    [20, 22, 23, 19],
                    [26, 28, 27, 25],
                    [34, 33, 29, 31],
                    [40, 39, 41, 37]]
    print(invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()