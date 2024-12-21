from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import generic_filter


# QUEST 3
image_path = "C:/Users/HP/Desktop/VA/Project_Vision_Artificielle/Images/hicham.jpg"


def convertir_en_niveaux_de_gris(image_path, nombre_bits):
    image = Image.open(image_path).convert('L') 
    image = np.array(image)
    max_val = (2 ** nombre_bits) - 1 
    image = (image / 255.0 * max_val).astype(np.uint8)  
    image_pil = Image.fromarray(image)
    return image_pil

def convertir_en_binaire(image_path):
    image = Image.open(image_path).convert('L')  
    image = np.array(image)
    image_binaire = (image > 128).astype(np.uint8) * 255  
    image_binaire_pil = Image.fromarray(image_binaire)
    return image_binaire_pil

def traiter_image(image_path):
    choix = input("Souhaitez-vous une image (binaire) ou (niveau de gris)? ").strip().lower()
    
    if choix == "niveau de gris":
        nombre_bits = int(input("Entrez le nombre de bits pour l'image en niveaux de gris (1-8): ").strip())
        if nombre_bits < 1 or nombre_bits > 8:
            print("Le nombre de bits doit être entre 1 et 8.")
            return None
        image = convertir_en_niveaux_de_gris(image_path, nombre_bits)
        image.show()
        image.save("image_niveaux_de_gris.bmp")
        print("Image en niveaux de gris sauvegardée sous 'image_niveaux_de_gris.bmp'.")
        return image
    
    elif choix == "binaire":
        image = convertir_en_binaire(image_path)
        image.show()
        image.save("image_binaire.bmp")
        print("Image binaire sauvegardée sous 'image_binaire.bmp'.")
        return image
    
    else:
        print("Choix invalide. Veuillez entrer 'binaire' ou 'niveau de gris'.")
        return None
    
# traiter_image(image_path)

# QUEST 4
def plot_histogram(image):
    histogram = image.histogram()
    plt.figure(figsize=(12, 6))
    plt.title("Histogramme de l'image convertie")
    plt.xlabel("Intensité des niveaux de gris")
    plt.ylabel("Nombre de pixels")
    
    plt.bar(range(len(histogram)), histogram, color='gray')
    
    plt.xlim([0, 255])
    plt.show()

converted_image = traiter_image(image_path)

if converted_image:
    plot_histogram(converted_image)
