import os
import json

class config_handler:
    def __init__(self):
        self.db = {
            'host': None,
            'user': None,
            'password': None,
            'database': None
        }
        self.raw_data_csv = None
        self.raw_data_json = None
        self.parsed_data_json = None

        if os.path.exists("config.json"):
            print("Fichier de configuration existant ")
            self.load_config()
        else:
            print("Fichier de configuration non trouvé. Création en cours...")
            self.create_config()

    def load_config(self):
        with open("config.json", 'r') as fichier:
            data = json.load(fichier)

        missing_keys = []

        for key in ['raw_data_csv', 'raw_data_json', 'parsed_data_json']:
            if key in data:
                setattr(self, key, data[key])
            else:
                missing_keys.append(key)

        if 'database' in data:
            for db_key in ['host', 'user', 'password', 'database']:
                if db_key in data['database']:
                    self.db[db_key] = data['database'][db_key]
                else:
                    missing_keys.append(f"database.{db_key}")
        else:
            missing_keys.append('database')

        if missing_keys:
            raise KeyError(f"Erreur de configuration : clés manquantes -> {', '.join(missing_keys)}")

    def create_config(self):
        self.raw_data_csv = input("Entrez le chemin du fichier CSV brut : ")
        self.raw_data_json = input("Entrez le chemin du fichier JSON brut : ")
        self.parsed_data_json = input("Entrez le chemin du fichier JSON parsé : ")

        self.db['host'] = input("Entrez l'hôte de la base de données : ")
        self.db['user'] = input("Entrez l'utilisateur de la base de données : ")
        self.db['password'] = input("Entrez le mot de passe de la base de données : ")
        self.db['database'] = input("Entrez le nom de la base de données : ")

        config_data = {
            'raw_data_csv': self.raw_data_csv,
            'raw_data_json': self.raw_data_json,
            'parsed_data_json': self.parsed_data_json,
            'database': self.db
        }

        with open("config.json", 'w') as fichier:
            json.dump(config_data, fichier, indent=4)
        
        print("Fichier de configuration créé avec succès")

try :
 config = config_handler()
except Exception as e:
        print(f"Unexpected error: {e}")