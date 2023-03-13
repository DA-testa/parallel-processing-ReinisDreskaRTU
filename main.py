# python3

def parallel_processing(n, m, data):
    output = []
    queue = list(range(n))
    start_times = [0] * n

    for i in range(m):
        time = data[i]
        thread_index = queue.pop(0)
        start_time = start_times[thread_index]
        output.append((thread_index, start_time))
        start_times[thread_index] += time
        queue.append(thread_index)

    return output

def main():
    n_and_m = list(map(int, input().split()))
    n = n_and_m[0]
    m = n_and_m[1]
    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    
    for thread_index, start_time in result:
        print(thread_index, start_time)



if __name__ == "__main__":
    main()