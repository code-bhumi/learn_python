def cube():
  for i in range(1,6):
    solution = pow(i, 3)
    print(f'Current Number is : {i} and the cube is {solution}')

if __name__ == '__main__':
  cube()