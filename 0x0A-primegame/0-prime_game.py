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
    prime = [True for _ in range(n + 1)]
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


def makeList(n):
    """
      method: makeLst
      desc: make a list from 1 until n + 1
      attributes:
        n: int, max number.
      returns:
        list of numbers.
    """
    return [num for num in range(1, n + 1)]


def removeMultiples(nums, prime):
    """
      method: removeMultiples
      desc: removes the multiples of a given prime number from a list
      attributes:
        nums: list of ints.
        prime: prime number.
      returns:
        list free from multiples of prime.
    """
    return list({num for num in nums if num % prime != 0})


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
    maria_wins, marias_round = 0, True
    ben_wins, bens_round = 0, False
    for roundC in range(x):
        num_list = makeList(nums[roundC])
        prime_numbers_list = SieveOfEratosthenes(nums[roundC])
        if not prime_numbers_list:
            ben_wins += 1
        else:
            for i in range(len(prime_numbers_list)):
                if marias_round:
                    num_list = removeMultiples(num_list, prime_numbers_list[i])
                    marias_round, bens_round = False, True
                elif bens_round:
                    num_list = removeMultiples(num_list, prime_numbers_list[i])
                    marias_round, bens_round = True, False
            if marias_round:
                ben_wins += 1
            else:
                maria_wins += 1
            marias_round, bens_round = True, False
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
