import rti.connextdds as dds
import time
import random
from SensorData import SensorData  

participant = dds.DomainParticipant(0) 

topic = dds.Topic(participant, "SensorDataTopic", SensorData)

qos = dds.DataWriterQos()
qos.reliability.kind = dds.ReliabilityKind.RELIABLE  
qos.deadline.period = dds.Duration(seconds=1)        
qos.history.kind = dds.HistoryKind.KEEP_LAST         
qos.history.depth = 1

writer = dds.DataWriter(participant.implicit_publisher, topic, qos)

sensor_id = "TEMP_002"
sensor_type = "temperature"

try:
    while True:
        data = SensorData()
        data.sensor_id = sensor_id
        data.sensor_type = sensor_type
        data.value = round(random.uniform(20.0, 30.0), 2)  
        data.timestamp = int(time.time() * 1000) 

        writer.write(data)
        print(f"Publicado: {sensor_id}, {sensor_type}, {data.value}, {data.timestamp}")

        time.sleep(1)
except KeyboardInterrupt:
    print("Encerrando o publisher...")