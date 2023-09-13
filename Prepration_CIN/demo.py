from load_model import load_model
from rectify import inference

"""
1. load_model()
Selon le type de modèle, importez les fichiers de modèle stockés sur le disque dur vers la mémoire interne.

Paramètres:
aucun

Retour:
- modèle : {VGG16RNN}
Objet de modèle, y compris les couches de modèle et les paramètres pré-formés.
- appareil : {appareil}
L'objet de classe torch.device représente l'appareil affecté à torch.Tensor pour l'opération. Contient le type de périphérique ("cpu" ou "cuda") et l'ordinal du périphérique.

Exemple:
de load_model importer load_model
modèle, appareil = load_model()


2. inferecne (chemin_entrée, chemin_sortie, modèle, périphérique)
Raisonnement de correction, correction d'une seule image.

Paramètres:
- chemin_entrée : {str}
Chemin de l'image à corriger

- chemin_sortie : {str}
chemin d'enregistrement de l'image

- modèle : {UNetRNN}
Objet de modèle, y compris les couches de modèle et les paramètres pré-formés.

- appareil : {appareil}
L'objet de classe torch.device représente l'appareil affecté à torch.Tensor pour l'opération. Contient le type de périphérique ("cpu" ou "cuda") et l'ordinal du périphérique.

Exemple:
de rectifier l'inférence d'importation
de load_model importer load_model
input = 'exemple/3.jpg'
output = 'résultat/3.png'
modèle, appareil = load_model()
inférence (entrée, sortie, modèle_formé, appareil)
"""

if __name__ == "__main__":
    """
    Demo
    """
    input1 = 'example/3.jpg'
    input2 = 'example/10.jpg'
    output1 = 'result/33.png'
    output2 = 'result/100.png'

    trained_model, device = load_model()
    inference(input1, output1, trained_model, device)
    inference(input2, output2, trained_model, device)

    print("Done CIN.")
