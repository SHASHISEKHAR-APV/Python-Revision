# Reference vs Copy demonstration (modified version)

import copy

def display(label, data):
    print(f"{label} -> {data}")
    print(f"{label} memory id: {id(data)}")
    print("=" * 35)

# --- Immutable type example ---
print("INTEGER BEHAVIOR:")
x_val = 50
y_val = x_val   # behaves like value copy

display("x_val", x_val)
display("y_val", y_val)

y_val = 99  # change only y_val

print("After updating y_val:")
display("x_val", x_val)
display("y_val", y_val)

# --- Mutable type (reference sharing) ---
print("\nLIST REFERENCE BEHAVIOR:")
data_a = [10, 20, 30]
data_b = data_a   # same reference

display("data_a", data_a)
display("data_b", data_b)

data_b.append(40)  # affects both

print("After modifying data_b:")
display("data_a", data_a)
display("data_b", data_b)

# --- Creating a real copy ---
print("\nLIST COPY (NEW MEMORY):")
data_c = copy.copy(data_a)

display("data_a", data_a)
display("data_c", data_c)

data_c.append(777)

print("After modifying data_c:")
display("data_a", data_a)
display("data_c", data_c)