#! /usr/bin/python
#
# Coded in FR for Mr B.
# FRENCH debug - language to add in future. Maybe will TKinter it.
# PYTHON3 version - framboise-pi.fr

from PIL import Image
import requests
from io import BytesIO
import time

# PICTURE URL
url = 'http://www.tierradelfuego.org.ar/webcam/ima/2014/06/20140624-021.jpg'

# WALLPAPER FILE NAME AND FOLDER --- dont add file extension
dossier = "/home/pi/Pictures/wallpaper"

# INTERVAL IN SECONDS
intervalle = 900

# MAIN LOOP - BOUCLE PRINCIPALE
while True:
    try:
        print ('...telechargement de l image webcam')
        image_requete = requests.get(url)
        image_webcam = Image.open(BytesIO(image_requete.content))
        image_format = image_webcam.format
        image_taille = image_webcam.size
        image_mode = image_webcam.mode
        # TERMINAL FILE INFOS DEBUG - AFFICHE DANS LE TERMINAL LES INFOS FICHIER image_webcam
        if image_webcam is not None:
            print("...telechargement reussi |format:",image_format,"|taille:",image_taille,"|mode:",image_mode)
            if image_format == "JPEG":
                dossier = dossier + ".jpg"
            if image_format == "PNG":
                dossier = dossier + ".png"
            if image_format == "GIF":
                dossier = dossier + ".gif"
            print ("...nom du fichier sur disque:",dossier)
            sauvegarde = image_webcam.save(dossier)
    except ValueError:
        print("ERREUR ... probleme extension image")
    except OSError:
        print("ERREUR ... lors de l ecriture fichier")
    # SLEEP INTERVAL - INTERVALLE DE LA BOUCLE
    print("...nouvelle image dans",(intervalle/60),"minutes")
    time.sleep(intervalle)
