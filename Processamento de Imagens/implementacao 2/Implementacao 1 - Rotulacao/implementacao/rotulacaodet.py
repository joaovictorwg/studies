import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função para transformar a imagem em binária
def binarize_image(image, threshold=127):
    _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return binary_image

# Função para rotular componentes conectados com conectividade 4
def label_connected_components(binary_image):
    rows, cols = binary_image.shape
    labels = np.zeros_like(binary_image, dtype=int)
    next_label = 1
    label_equivalence = {}

    def find_label(label):
        while label in label_equivalence:
            label = label_equivalence[label]
        return label

    def union_labels(label1, label2):
        root1 = find_label(label1)
        root2 = find_label(label2)
        if root1 != root2:
            label_equivalence[root2] = root1

    for i in range(rows):
        for j in range(cols):
            if binary_image[i, j] == 255:  # Pixel é parte de um objeto
                label_left = labels[i, j - 1] if j > 0 else 0
                label_top = labels[i - 1, j] if i > 0 else 0
                
                if label_left == 0 and label_top == 0:
                    # Novo rótulo
                    labels[i, j] = next_label
                    next_label += 1
                elif label_left != 0 and label_top == 0:
                    # Somente o rótulo à esquerda existe
                    labels[i, j] = label_left
                elif label_left == 0 and label_top != 0:
                    # Somente o rótulo acima existe
                    labels[i, j] = label_top
                else:  # label_left != 0 and label_top != 0
                    if label_left == label_top:
                        labels[i, j] = label_left
                    else:
                        labels[i, j] = min(label_left, label_top)
                        union_labels(label_left, label_top)

    # Corrigir rótulos equivalentes
    for i in range(rows):
        for j in range(cols):
            if labels[i, j] > 0:
                labels[i, j] = find_label(labels[i, j])

    return labels

# Carregar a imagem em escala de cinza
image = cv2.imread('te1.png', cv2.IMREAD_GRAYSCALE)

# Transformar a imagem em binária
binary_image = binarize_image(image)

# Rotular os componentes conectados
labeled_image = label_connected_components(binary_image)

# Visualizar as imagens
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(binary_image, cmap='gray')
plt.title('Imagem Binária')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(labeled_image, cmap='nipy_spectral')
plt.title('Imagem Rotulada')
plt.axis('off')

plt.show()
