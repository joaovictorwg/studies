import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função para redimensionar a imagem para corresponder ao tamanho da outra
def redimensionar_imagem(imagem, tamanho):
    return cv2.resize(imagem, (tamanho[1], tamanho[0]))

# Carregue as imagens
imagem1 = cv2.imread('Kevin-hart.jpg')
imagem2 = cv2.imread('red.png')

# Verifique se as imagens foram carregadas corretamente
if imagem1 is None or imagem2 is None:
    raise ValueError("Uma ou ambas as imagens não foram carregadas corretamente. Verifique os caminhos.")

# Converta as imagens de BGR para RGB (OpenCV usa BGR por padrão, enquanto o Matplotlib usa RGB)
imagem1_rgb = cv2.cvtColor(imagem1, cv2.COLOR_BGR2RGB)
imagem2_rgb = cv2.cvtColor(imagem2, cv2.COLOR_BGR2RGB)

# Obtenha as dimensões das imagens
altura1, largura1 = imagem1.shape[:2]
altura2, largura2 = imagem2.shape[:2]

# Redimensione a segunda imagem para o tamanho da primeira imagem
imagem2_redimensionada = redimensionar_imagem(imagem2_rgb, (largura1, altura1))

# Adicione as imagens
imagem_adicionada = cv2.add(imagem1_rgb, imagem2_redimensionada)

# Salve a imagem adicionada localmente
cv2.imwrite('imagem_adicionada.jpg', cv2.cvtColor(imagem_adicionada, cv2.COLOR_RGB2BGR))

# Configurações de exibição
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Exiba a imagem 1
axes[0].imshow(imagem1_rgb)
axes[0].set_title('Imagem 1')
axes[0].axis('off')

# Exiba a imagem 2 redimensionada
axes[1].imshow(imagem2_redimensionada)
axes[1].set_title('Imagem 2 Redimensionada')
axes[1].axis('off')

# Exiba a imagem resultante
axes[2].imshow(imagem_adicionada)
axes[2].set_title('Imagem Adicionada')
axes[2].axis('off')

# Exiba o gráfico
plt.tight_layout()
plt.show()
