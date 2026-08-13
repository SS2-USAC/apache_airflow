from datetime import datetime, timedelta
from airflow.decorators import dag, task


default_args = {
    "owner": "201900957",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Definición del DAG mediante el decorador @dag
@dag(
    dag_id="dag_sencillo_ejemplo",
    default_args=default_args,
    description="Un DAG básico de prueba en Airflow",
    schedule_interval="@daily", 
    start_date=datetime(2026, 1, 1),
    catchup=False,  
    tags=["ejemplo", "principiante"],
)
def mi_primer_dag():

    
    @task()
    def extraer_datos():
        print("Obteniendo información...")
        return {"datos": [10, 20, 30]}

    
    @task()
    def procesar_datos(payload: dict):
        numeros = payload["datos"]
        resultado = sum(numeros)
        print(f"La suma de los datos es: {resultado}")
        return resultado

    
    @task()
    def guardar_resultado(total: int):
        print(f"Resultado final {total} guardado exitosamente en la base de datos.")

    datos = extraer_datos()
    resultado = procesar_datos(datos)
    guardar_resultado(resultado)

dag = mi_primer_dag()