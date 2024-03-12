#!/usr/bin/python3
"""
     make a sequence of numbers from nums[n], 'n' represents the rounds.
    example first number in nums[0] is 5 we have our seq1 [1,2,3,4,5].
    => def makeList(n):
    make an other list contains only prime numbers, and this is the list,
    => def SieveOfEratosthenes(n):
    that the players will choose from we are left with [2,3,5].
    => selectOptions = SieveOfEratosthenes(nums[i])
    player 1: take 2 and we will remove any multiple of 2 from the seq1,
    and we are left with [1,3,5].
    palyer 2: takes number 3 and the result would be [1, 5].
    player 1: takes 5 rest is [1]
    player 2: can't lift a finguer.
    player 1: wins.
    repeat the process n-1 times
"""


def SieveOfEratosthenes(n):
    """
      method: SieveOfEratosthenes
      desc: extract all prime numbers until n
      attributes:
        n: int, the limit number from which it will extract all
        prime numbers until n.
      returns:
        list of prime numbers.
    """
    prime = [True for i in range(n + 1)]
    prime_number = []
    p = 2

    while (p * p <= n):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            prime_number.append(p)
    return prime_number


def isWinner(x, nums):
    """
    method: isWinner
      desc: In x rounds of the game, where n may be different for each round.
      Assuming Maria always goes first and both players play optimally,
      determine who the winner of each game is.
      attributes:
        x: int, number of rounds.
        nums: list(int), the number of the rounds.
      returns:
        the winner of the game.
    """
    if x <= 0 or nums is None or x != len(nums):
        return None
    max_num = max(nums)
    prime_numbers = SieveOfEratosthenes(max_num)
    ben_wins = 0
    maria_wins = 0
    for i in range(x):
        num_list = list(range(1, nums[i] + 1))
        for prime in prime_numbers:
            if prime > nums[i]:
                break
            num_list = [num for num in num_list if num % prime != 0]
        if len(num_list) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None
