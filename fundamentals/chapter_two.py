from collections import Counter, defaultdict


def apply_to_one(f):
    return f(1)


def double(x):
    return x * 2


double_it = double
x = apply_to_one(double_it)
# Lambda function
y = apply_to_one(lambda x: x + 4)

print(x, y)


## Lists

integer_list = [1, 2, 3, 4]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]

print(f"list lenght: {len(integer_list)}")
print(f"list lenght: {len(list_of_lists)}")

print(f"list sum: {sum(integer_list)}")


# Tuples

ex_tuple = (1, 2)

try:
    ex_tuple[1] = 0
except TypeError:
    print("You can not modify a tuple")


def sum_and_product(x, y) -> tuple:
    return (x + y), (x * y)


sp = sum_and_product(2, 3)
s, p = sum_and_product(4, 5)

print(sp)
print(s, p)


## Dict

words = [
    "python",
    "código",
    "computador",
    "dados",
    "código",
    "tecnologia",
    "internet",
    "rede",
    "dados",
    "informação",
    "inteligência",
    "aprendizado",
    "tecnologia",
    "programação",
    "código",
    "computação",
    "rede",
    "machine",
    "dados",
    "web",
]


word_counts = {}

## ! bad way

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

## * simple way

for word in words:
    previous = word_counts.get(word, 0)
    word_counts[word] = previous + 1


word_counts = defaultdict(int)
for w in words:
    word_counts[word] += 1

w_counter = Counter(words)

for w, c in w_counter.most_common(5):
    print(w, c)
