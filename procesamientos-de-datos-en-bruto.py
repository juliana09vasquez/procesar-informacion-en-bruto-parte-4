import requests

def get_to_csv(url, nombre_archivo="datos_descargados.csv"):
    response = requests.get(url)
    if response.status_code == 200:
        with open(nombre_archivo, 'w') as file:
            file.write(response.text)
        print(f"Archivo {nombre_archivo} guardado con éxito.")
    else:
        print(f"Error al descargar los datos: Código de estado {response.status_code}")

get_to_csv("https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv")