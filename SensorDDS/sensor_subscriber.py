import rti.connextdds as dds
from SensorData import SensorData
import time# Importa o tipo gerado pelo IDL

# Configurar o participante do domínio DDS
participant = dds.DomainParticipant(0)

# Criar o tópico com o tipo SensorData
topic = dds.Topic(participant, "SensorDataTopic", SensorData)

# Configurar QoS para o DataReader
qos = dds.DataReaderQos()
qos.reliability.kind = dds.ReliabilityKind.RELIABLE  # Entrega garantida
qos.deadline.period = dds.Duration(seconds=1)        # Espera dados a cada 1s
qos.history.kind = dds.HistoryKind.KEEP_LAST
qos.history.depth = 1

# Criar o DataReader
reader = dds.DataReader(participant.implicit_subscriber, topic, qos)

# Função para processar os dados recebidos
def process_data(data):
        print(f"Recebido: {data.sensor_id}, {data.sensor_type}, {data.value:.2f}, {data.timestamp}")

try:
    # Loop para ler dados continuamente
    while True:
        # Ler amostras disponíveis
        samples = reader.take()
        for sample in samples:
            if sample.info.valid:  # Verifica se os dados são válidos
                process_data(sample.data)
        time.sleep(0.1)  # Pequena pausa para evitar uso excessivo de CPU
except KeyboardInterrupt:
    print("Encerrando o subscriber...")