from PIL import Image
import numpy as np
from scipy.ndimage import generic_filter

# Fonction pour appliquer le filtre de Nagao
def nagao_filter(block):
    block = block.reshape((5, 5))

    regions = [
        block[:3, :3],  # Haut-gauche 3x3
        block[:3, 1:4], # Haut-centre 3x3
        block[:3, 2:],  # Haut-droite 3x3
        block[1:4, :3], # Milieu-gauche 3x3
        block[1:4, 1:4],# Centre 3x3
        block[1:4, 2:], # Milieu-droite 3x3
        block[2:, :3],  # Bas-gauche 3x3
        block[2:, 1:4], # Bas-centre 3x3
        block[2:, 2:]   # Bas-droite 3x3
    ]

    # Calculer la variance et la moyenne de chaque région
    min_variance = float('inf')
    mean_value = 0
    for region in regions:
        variance = np.var(region)
        if variance < min_variance:
            min_variance = variance
            mean_value = np.mean(region)

    return mean_value

input_image_path = "/Users/mbelouar/Desktop/Project_VA/image_niveaux_de_gris.bmp"
output_image_path = "/Users/mbelouar/Desktop/Project_VA/Images/nagao_filtered_image.png"

try:
    # Ouvrir l'image et convertir en niveaux de gris
    image = Image.open(input_image_path).convert('L')

    # Convertir l'image en tableau NumPy
    image_array = np.array(image)

    # Appliquer le filtre de Nagao
    filtered_image_array = generic_filter(image_array, nagao_filter, size=(5, 5))

    # Convertir le tableau filtré en image
    filtered_image = Image.fromarray(filtered_image_array.astype(np.uint8))

    # Sauvegarder et afficher l'image
    filtered_image.save(output_image_path)
    filtered_image.show()

    print(f"L'image filtrée a été sauvegardée sous '{output_image_path}'.")

except Exception as e:
    print(f"Erreur lors du traitement : {e}")
