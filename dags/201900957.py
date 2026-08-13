from datetime import datetime, timedelta
from airflow.sdk import dag, task

default_args = {
    'owner': '201900957',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

@dag(
    dag_id='mi_primer_dag_sencillo',
    default_args=default_args,
    description='Un DAG básico de ejemplo usando TaskFlow API',
    schedule='@daily',  # En Airflow 2.4+ y Airflow 3 se usa 'schedule'
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=['ejemplo', 'inicio'],
)
def mi_primer_dag():

    @task()
    def extraer_datos():
        datos = [10, 20, 30]
        print(f"Datos extraídos: {datos}")
        return datos

    @task()
    def procesar_datos(datos: list):
        total = sum(datos)
        print(f"El total procesado es: {total}")
        return total

    @task()
    def enviar_notificacion(resultado: int):
        print(f"¡Proceso completado con éxito! Resultado final: {resultado}")

    datos = extraer_datos()
    resultado = procesar_datos(datos)
    enviar_notificacion(resultado)

mi_dag = mi_primer_dag()