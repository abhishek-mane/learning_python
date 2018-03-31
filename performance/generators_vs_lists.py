import memory_profiler
import random
import time

names = ['Abhishek', 'Swapil', 'Pravin', 'Sandesh', 'Ashish']
majors = ['Math', 'Engineering', 'CompScien', 'Arts', 'Business']

print("Memory [before] : {} Mb".format(
    memory_profiler.memory_usage()[0]
))


def people_list(num_people):
    result = []

    for i in range(num_people):
        result.append({
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors),
        })

    return result


def people_generator(num_people):
    for i in range(num_people):
        yield {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors),
        }


# list
t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()

# generators
# t1 = time.clock()
# people = people_generator(1000000)
# t2 = time.clock()

print("Memory [after ] : {} Mb".format(
    memory_profiler.memory_usage()[0]
))

print("Took {} Seconds".format(t2-t1))
