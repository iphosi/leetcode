from typing import List


def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    answer = [0] * (n + 1)

    for booking in bookings:
        answer[booking[0] - 1] += booking[2]
        answer[booking[1]] -= booking[2]

    answer.pop()

    for i in range(1, n):
        answer[i] += answer[i - 1]

    return answer
