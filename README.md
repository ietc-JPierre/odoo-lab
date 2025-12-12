 Odoo-Lab — Module Rental Property 

Odoo-Lab est un environnement d’étude conçu pour développer, tester et démontrer un module Odoo personnalisé nommé rental_property, destiné à gérer des biens immobiliers (locations de vacances, maisons, appartements, etc.) directement dans Odoo.

Ce dépôt contient :

Un module Odoo personnalisé (rental_property)

 La configuration nécessaire pour charger et tester le module

 Important :
La WebApp Python externe utilisée pour interagir avec Odoo via JSON-RPC se trouve dans un dépôt séparé (architecture professionnelle).
Lien : (à remplacer) https://github.com/<ton_username>/odoo-webapp

 Structure du Projet
odoo-lab/
│
├── addons/
│   └── rental_property/
│       ├── __init__.py
│       ├── __manifest__.py
│       ├── models/
│       │   └── rental_property.py
│       ├── security/
│       │   └── ir.model.access.csv
│       └── views/
│           └── rental_property_views.xml
│
├── docker-compose.yml
├── Dockerfile
└── README.md

 Module rental_property

Ce module étend le modèle product.template pour transformer un produit classique en bien immobilier avec des champs personnalisés, par exemple :

Nombre de chambres

Nombre de salles de bain

Capacité maximale

Adresse / localisation

Description longue

Image

Il ajoute également un menu et une vue dans Odoo pour gérer ces biens.

 Installation via Rancher

Ce projet inclut tout ce qu’il faut pour lancer un Odoo 17 complet avec ton module.

 Prérequis

Docker

Docker Compose

Git

 Cloner le projet
git clone https://github.com/<ton_username>/odoo-lab
cd odoo-lab

 Lancer l’environnement
docker compose up --build

Services inclus :
Service	Port	Description
Odoo	8069	Interface web
PostgreSQL	interne	Base de données
Accès à Odoo

URL : http://localhost:8069

Créer une base de données

Activer le mode développeur

Installer le module rental_property

 Installation du module Rental Property dans Odoo

Aller dans : Settings → Activate Developer Mode

Aller dans : Apps

Cliquez sur Update Apps List

Recherchez Rental Property

Cliquez sur Install
