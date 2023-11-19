from fractions import Fraction
import numpy


def point_process(val: list) -> None:
    numpy.set_printoptions(precision=10, suppress=True)
    for i in val:
        print(Fraction(i).limit_denominator(100), sep="", end="  ")
    print("\n")


def order_check(a: int, b: int) -> None:
    if a <= 0 or b <= 0:
        print("No.of rows and columns must be greater than 0")
        exit(0)
    else:
        return 0


def element_check(a: list, rows: int, columns: int) -> None:
    if len(a) != rows * columns:
        print("Insufficient or Excess elements given as elements")
        exit(0)
    else:
        return 0


def second_matrix(arr):
    print("Input second matrix")
    rows = int(input("Enter rows:"))
    columns = int(input("Enter columns:"))
    order_check(rows, columns)
    a = list(map(int, input("Enter the elements:").split()))
    element_check(a, rows, columns)
    arr_1 = numpy.array(a).reshape(rows, columns)
    if arr_1.shape != arr.shape:
        print("Order of both the dimensions should be same")
        exit(0)
    print("Second matrix is\n", arr_1)
    return arr_1


print("Input the matrix")
rows = int(input("Enter the no.of rows:"))
columns = int(input("Enter the no.of columns:"))
order_check(rows, columns)
a = list(map(int, input("Enter the elements:").split()))
element_check(a, rows, columns)
arr = numpy.array(a).reshape(rows, columns)
print("The given matrix is\n", arr)
while " ":
    print(
        """
    1.Det
    2.Transpose
    3.Eigen values and Vectors                                          
    4.Trace
    5.Inverse
    6.Addition of two matrices
    7.subtraction of a matrix
    8.Matrix multiplication
    9.Matrix exponentiation
    10.Exit
        """
    )
    choice = int(input("Enter choice:"))
    match choice:
        case 1:
            print("Det of the given matrix is", numpy.linalg.det(arr))
        case 2:
            print("The transpose of the given matrix is\n", numpy.transpose(arr))
        case 3:
            val, vec = numpy.linalg.eig(arr)
            print("Eigen values are:")
            point_process(val)
            print("Eigen vectors are:")
            for i in range(rows):
                point_process(vec[i][0:columns])
        case 4:
            print("The Trace of the matrix is", numpy.trace(arr))
        case 5:
            if numpy.linalg.det(arr) == 0:
                print("Can't calculate inverse to a singular matrix")
            else:
                print("The inverse of the matrix is\n", numpy.linalg.inv(arr))
        case 6:
            print("First matrix is\n", arr)
            print(arr + second_matrix(arr))
        case 7:
            print("First matrix is\n", arr)
            print(arr - second_matrix(arr))
        case 8:
            print("First matrix is\n", arr)
            print(arr * second_matrix(arr))
        case 9:
            print("Matrix exponentiation")
            pow = int(input("Input the matrix exponentiation value"))
            print(numpy.linalg.matrix_power(arr, pow))
        case 10:
            exit(0)
        case _:
            print("Input Valid choice")
