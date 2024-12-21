# -*- coding: utf-8 -*-

from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import generic_filter

def creer_bmp_image(matrix, file_path):
    height = len(matrix)
    width = len(matrix[0])
    image = Image.new('1', (width, height))
    for y in range(height):
        for x in range(width):
            image.putpixel((x, y), matrix[y][x])
    image.save(file_path)



# Defining matrix_I1 and matrix_I2
matrix_I1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

matrix_I2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Save images with corrected paths
creer_bmp_image(matrix_I1, "/Users/mbelouar/Desktop/Project_VA/Images/Image_I1.bmp")
creer_bmp_image(matrix_I2, "/Users/mbelouar/Desktop/Project_VA/Images/Image_I2.bmp")

# write the matrices to text files
output_file_path = "/Users/mbelouar/Desktop/Project_VA/BinMatrix/Image_I1.txt"
with open(output_file_path, 'w') as file:
    file.write("M1\n")
    file.write("# Image I1\n")
    file.write(f"{len(matrix_I1)} {len(matrix_I1[0])}\n")
    for row in matrix_I1:
        file.write(" ".join(str(cell) for cell in row) + "\n")

output_file_path = "/Users/mbelouar/Desktop/Project_VA/BinMatrix/Image_I2.txt"
with open(output_file_path, 'w') as file:
    file.write("M2\n")
    file.write("# Image I2\n")
    file.write(f"{len(matrix_I2)} {len(matrix_I2[0])}\n")
    for row in matrix_I2:
        file.write(" ".join(str(cell) for cell in row) + "\n")



# QUEST 1-a
def add_matrices(matrix_I1, matrix_I2):
    height = len(matrix_I1)
    width = len(matrix_I1[0])
    result = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            result[y][x] = min(matrix_I1[y][x] + matrix_I2[y][x], 1)

    return result

result_matrix = add_matrices(matrix_I1, matrix_I2)

creer_bmp_image(result_matrix, "/Users/mbelouar/Desktop/Project_VA/Images/Addition_Image.bmp")

# Write the result matrix to a text file in the desired format
output_file_path = "/Users/mbelouar/Desktop/Project_VA/BinMatrix/Addition_Matrix.txt"
with open(output_file_path, 'w') as file:
    file.write("Result Image\n")
    file.write("# Addition of matrices I1 and I2\n")
    file.write(f"{len(result_matrix)} {len(result_matrix[0])}\n")
    for row in result_matrix:
        file.write(" ".join(str(cell) for cell in row) + "\n")

# QUEST 1-b
def soustract_matrice(matrix_I1, matrix_I2):
    height = len(matrix_I1)
    width = len(matrix_I1[0])
    result = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            result[y][x] = max(matrix_I1[y][x] - matrix_I2[y][x], 0)

    return result

result_matrix1 = soustract_matrice(matrix_I1, matrix_I2)

creer_bmp_image(result_matrix1, "/Users/mbelouar/Desktop/Project_VA/Images/Soustraction_Image.bmp")

output_file_path = "/Users/mbelouar/Desktop/Project_VA/BinMatrix/Soustraction_Matrix.txt"
with open(output_file_path, 'w') as file:
    file.write("Result Image\n")
    file.write("# Soustraction of matrices I1 and I2\n")
    file.write(f"{len(result_matrix1)} {len(result_matrix1[0])}\n")
    for row in result_matrix1:
        file.write(" ".join(str(cell) for cell in row) + "\n")

# QUEST 1-c
matrix_I = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 3, 4, 4, 5, 5, 6, 0],
    [0, 3, 3, 4, 4, 5, 5, 6, 0],
    [0, 6, 6, 5, 5, 4, 4, 3, 0],
    [0, 7, 8, 9, 7, 8, 9, 7, 0],
    [0, 9, 9, 8, 8, 7, 7, 7, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def multiply_matrice_by2(matrix_I):
    height = len(matrix_I)
    width = len(matrix_I[0])
    result = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            result[y][x] = min(matrix_I[y][x] *2, 15)

    return result

result_matrix2 = multiply_matrice_by2(matrix_I)

output_file_path = "/Users/mbelouar/Desktop/Project_VA/BinMatrix/Multiplication_Matrix.txt"
with open(output_file_path, 'w') as file:
    file.write("Result Image\n")
    file.write("# Multiplication of matrix I by 2\n")
    file.write(f"{len(result_matrix2)} {len(result_matrix2[0])}\n")
    for row in result_matrix2:
        file.write(" ".join(f'{cell:2}' for cell in row) + "\n")


# QUEST 2
def plot_color_histogram(image_path):
    image = Image.open(image_path)
    
    red_channel = image.getchannel('R')
    green_channel = image.getchannel('G')
    blue_channel = image.getchannel('B')

    red_hist = red_channel.histogram()
    green_hist = green_channel.histogram()
    blue_hist = blue_channel.histogram()

    plt.figure(figsize=(12, 6))
    plt.title("Histogramme des canaux de couleur")
    plt.xlabel("Niveaux de couleur")
    plt.ylabel("Fréquence")
    
    plt.plot(red_hist, color='red', label='Rouge')
    plt.plot(green_hist, color='green', label='Vert')
    plt.plot(blue_hist, color='blue', label='Bleu')
    
    plt.xlim([0, 255])
    plt.legend()
    plt.show()

image_path = "/Users/mbelouar/Desktop/Project_VA/Images/BELOUARRAQ.jpg" 
plot_color_histogram(image_path)

