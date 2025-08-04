"""
Hacker Rank Array manipulation deallign with a 6x6 grid and calculating the sium of an hr glass shape
https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""


def hourglassSum(arr):
    # Write your code here
    max_total = float('-inf') # max is 63 but this is safe and better
    for x in range(4):
        for y in range(4):
            top = arr[x][y] + arr[x][y+1] + arr[x][y+2]
            mid = arr[x+1][y+1]
            bot = arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
            hourglass_sum = top + mid + bot
            max_total = max(max_total,hourglass_sum)
    return max_total

  
 