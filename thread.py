import multiprocessing
import time

def print_square(n):
    print(f'Square: {n * n}')
    
def print_cube(n):
    print(f'Cube: {n * n * n}')

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    # Create processes
    processes = []
    for num in numbers:
        p1 = multiprocessing.Process(target=print_square, args=(num,))
        p2 = multiprocessing.Process(target=print_cube, args=(num,))
        processes.append(p1)
        processes.append(p2)
        
        # Start processes
        p1.start()
        p2.start()
    
    # Wait for processes to finish
    for p in processes:
        p.join()
