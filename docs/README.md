# 🧮 Geometric Lib

A lightweight math library for basic **geometric formulas**.
Supports **square**, **rectangle**, **triangle**, and **circle** calculations.

---

## Square

### **Area**

Formula:
S = a²

**Example:**

```py
area(2)  # returns 4
```

### **Perimeter**

Formula:
P = 4a

**Example:**

```py
perimeter(2)  # returns 8
```

---

## Rectangle

### **Area**

Formula:
S = a * b

**Example:**

```py
area(2, 3)  # returns 6
```

### **Perimeter**

Formula:
P = 2(a + b)

**Example:**

```py
perimeter(2, 3)  # returns 10
```

---

## Triangle

### **Area**

Formula:
S = (a * b) / 2

**Example:**

```py
area(2, 3)  # returns 3
```

### **Perimeter**

Formula:
P = a + b + c

**Example:**

```py
perimeter(1, 2, 3)  # returns 6
```

---

## Circle

### **Area**

Formula:
S = πr²

**Example:**

```py
area(2)  # returns 4π
```

### **Perimeter (Circumference)**

Formula:
P = 2πr

**Example:**

```py
perimeter(2)  # returns 4π
```

# Testing

Library have unit tests using ```unittest``` module
## **Run tests**
```sh
python -m unittest
```

## **Tests coverage report**
```sh
pip install coverage # if you don`t have coverage module installed

python -m coverage report
```

# History

- **985dc72** -  Docs added
- **bda8f26** -  Rectangle and Triangle added
- **d078c8d** -  L-03: Docs added
- **8ba9aeb** -  L-03: Circle and square added
