# Scraping et Envoi de données

## Introduction
Ce projet consiste à récupérer des informations sur les locations d'appartements à San Francisco sur Zillow, puis à les envoyer à un formulaire Google Forms spécifique. Cela permet de compiler des données sur les propriétés disponibles dans une région spécifique et de les stocker de manière organisée pour une analyse ultérieure.

## Fonctionnalités
- Récupère les données sur les locations d'appartements à San Francisco à partir du site Zillow.
- Envoie les informations récupérées sur chaque appartement à un formulaire Google Forms.
- Utilise Selenium pour automatiser l'ouverture du navigateur et le remplissage du formulaire avec les données extraites.

## Exigences
- Python 3.x
- Requests
- BeautifulSoup
- Selenium
- Chrome WebDriver

## Installation et Configuration
1. Assurez-vous d'avoir Python installé sur votre système.
2. Installez les bibliothèques nécessaires en utilisant pip : `pip install requests beautifulsoup4 selenium`.
3. Téléchargez le Chrome WebDriver compatible avec la version de votre navigateur Chrome.
4. Assurez-vous d'avoir un compte Google et créez un formulaire Google Forms vide.
5. Configurez les variables d'environnement `CHROME_DRIVER_PATH` avec le chemin vers l'exécutable Chrome WebDriver.
6. Modifiez les variables `form_link` et `zillow_search_URL` avec les liens appropriés du formulaire Google Forms et de la recherche Zillow.
7. Exécutez le script et observez la collecte automatisée de données sur les locations d'appartements à San Francisco !

## Exécution
Pour exécuter le script :
1. Assurez-vous d'avoir Google Chrome installé sur votre système.
2. Exécutez le script Python ("main.py"). Le script ouvrira le navigateur Chrome, accédera au site Zillow, récupérera les informations sur les locations d'appartements, puis les enverra au formulaire Google Forms spécifié.

## Remarques
- Assurez-vous que la version de Chrome WebDriver utilisée est compatible avec la version de Chrome installée sur votre système.
- Ce projet utilise la bibliothèque Selenium pour automatiser les interactions avec le navigateur.
- Assurez-vous de respecter les conditions d'utilisation des sites Web ciblés lors de la collecte de données.
- Ce projet a été réalisé dans le cadre du cours [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) d'Angela Yu sur la plateforme Udemy.
