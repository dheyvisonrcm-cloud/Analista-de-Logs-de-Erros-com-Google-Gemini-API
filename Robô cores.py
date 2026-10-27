import cv2 as cv #só estética e questao de eficiência
import numpy as np #só estética e questao de eficiência

camera = cv.VideoCapture(0) #0=webcam, 1 pra outra câmera 

#DICIONÁRIO DE CORES: Definimos os intervalos HSV para Vermelho, Verde e Azul
cores_hsv = {
    #'vermelho': (np.array([0, 100, 100]), np.array([10, 255, 255])),# na ordem, (H) cor no círculo,(S)saturação, (V) brilho
    
    'verde': (np.array([35, 60, 60]), np.array([85, 255, 255])),
    'azul': (np.array([90, 60, 60]), np.array([130, 255, 255]))
}

# Variável de estado para saber qual cor estamos buscando (começa no vermelho)
cor_atual = 'vermelho'

while True:
    try:
        with open('cor_alvo.txt', 'r') as f:
            conteudo = f.read().strip().upper() # assim vai Lê R, G, B ou M
            
            if conteudo == 'M':
                # OpenCV para de analisar a imagem e ignora os alvos (pelo que eu entendi da descrição do aúdio de Grazi, era esse o intuíto do M)
                cor_atual = 'manual' # Ativa o modo manual sem travar o vídeo (coloquei um "continue" antes, e percebi que iria travar o vídeo, então troquei) 
            elif conteudo == 'R':   cor_atual = 'vermelho'
            elif conteudo == 'G': cor_atual = 'verde'
            elif conteudo == 'B':  cor_atual = 'azul'
    except FileNotFoundError:
        with open('cor_alvo.txt', 'w') as f:
            f.write('M')
        cor_atual = 'manual' # caso não tenha um no código do davi, nessa parte o código já cria um e ativa o modo manual para não travar o vídeo
    isTrue, frame = camera.read()

    if not isTrue:
        break
    # 1. INTERAÇÃO POR TECLADO: Captura a tecla pressionada #Grazi alterou o codigo da barbara 
    key = cv.waitKey(1) & 0xFF
    
    if key == ord('r'):   # Pressione 'r' para mudar para vermelho (Red)
        cor_atual = 'vermelho'
    elif key == ord('g'): # Pressione 'g' para mudar para verde (Green)
        cor_atual = 'verde'
    elif key == ord('b'): # Pressione 'b' para mudar para azul (Blue)
        cor_atual = 'azul'
    elif key == ord('d'): # Mantém o seu 'd' para fechar o programa
        break    
        
    hsv_camera = cv.cvtColor(frame, cv.COLOR_BGR2HSV) #converte cada frame pra hsv
    
    # 2. SELEÇÃO DINÂMICA DA COR: Buscamos os limites baseados na cor_atual
    if cor_atual=='vermelho':
        mask1=cv.inRange(hsv_camera,np.array([0, 100, 100]),np.array([10, 255, 255]))
        mask2=cv.inRange(hsv_camera,np.array([170, 100, 100]),np.array([179, 255, 255]))

        mask = mask1 + mask2

    else:
        lower_bound, upper_bound = cores_hsv[cor_atual]
        
        # Cria a máscara dinamicamente para a cor selecionada
        mask = cv.inRange(hsv_camera, lower_bound, upper_bound) 
        
    kernel = np.ones((5,5), np.uint8) #o pincel
    mask_limpa = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel) #fecha os buracos
    
    contornos, _ = cv.findContours(mask_limpa, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    comando = 'P' #comando P quando parado / não encontra nada
    

    
    if len(contornos) > 0: #se achar o balão
        maior_contorno = max(contornos, key=cv.contourArea)
        if cv.contourArea(maior_contorno) > 3000:
            x, y, largura, altura = cv.boundingRect(maior_contorno)
            
            # Teste: Muda a cor do retângulo desenhado na tela para combinar com a cor detectada
            cor_bgr = (0, 0, 255) # Padrão Vermelho
            if cor_atual == 'verde':   cor_bgr = (0, 255, 0)
            elif cor_atual == 'azul':  cor_bgr = (255, 0, 0)
                
            cv.rectangle(frame, (x, y), (x + largura, y + altura), cor_bgr, 2)
            
            centro_x = x + (largura // 2)
            if centro_x < 220:
                print(f'Balao {cor_atual} na esquerda==vire p/ ESQUERDA')
                comando = 'E'
            elif centro_x > 420:   
                print(f'Balao {cor_atual} na direita==vire p/ DIREITA')
                comando = 'D'     
            else:
                print(f'Balao {cor_atual} no centro==siga em FRENTE')
                comando = 'F'
    
    with open('comando.txt', 'w') as arquivo: #comunicação com o programa do Davi
        arquivo.write(comando)
    
    # Escreve na tela qual modo de cor está ativo por cima do vídeo da câmera
    cv.putText(frame, f"Modo: {cor_atual.upper()}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    cv.imshow('camera', frame) #mostra a webcam normal
    cv.imshow('Mascara Limpa', mask_limpa) #mostra o binário da cor atual
    

camera.release()
cv.destroyAllWindows()