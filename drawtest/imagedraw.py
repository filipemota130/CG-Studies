from PIL import Image
import matplotlib.pyplot as plt

def change_pixel_color(image_path, pixels_to_change):
    # Abrir a imagem
    image = Image.open(image_path)

    for x, y, new_color in pixels_to_change:
        try:
            # Definir o novo valor de cor do pixel na imagem
            image.putpixel((x, y), new_color)
        except IndexError:
            print(f"A coordenada ({x}, {y}) está fora dos limites da imagem.")
            continue
        
    # Definir o novo valor de cor do pixel
    new_pixel = new_color

    # Definir o novo valor de cor do pixel na imagem
    image.putpixel((x, y), new_pixel)

    # Salvar a imagem resultante
    image.save("imagem_alterada.png")

    print("Imagem resultante salva como 'imagem_alterada.png'.")
    
def show_image(image_path):
    # Abrir e exibir a imagem
    image = Image.open(image_path)
    plt.imshow(image)
    plt.axis('off')  # Remover os eixos da imagem
    plt.show()

# Exemplo de uso:
change_pixel_color("imagem.png", [(100, 200, (255, 0, 0)), (150, 250, (0, 255, 0))])  # Altera o pixel na posição (100, 200) para vermelho
show_image("imagem_alterada.png")