# Main class.

import sys
import XMath

if __name__ == '__main__':
    data = [int(value) for value in sys.argv[1:]]
    
    total_sum = XMath.xsum(data)
    print(f'Sum: {total_sum}')

    total_max = XMath.xmax(data)
    print(f'Max: {total_max}')

    total_min = XMath.xmin(data)
    print(f'Min: {total_min}')

    total_avg = XMath.xavg(data)
    print(f'AVG: {total_avg:.2f}')