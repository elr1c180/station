from sqlalchemy import Table, Column, Integer, String, MetaData, insert, select, update,desc
from sqlalchemy import create_engine

engine = create_engine(
    url="sqlite:///main.db",
    pool_size=5,
    max_overflow=10
)

metadata_obj = MetaData()

station = Table(
    'station',
    metadata_obj,
    Column("id",  Integer, primary_key=True, unique=True),
    Column("image", String),
    Column("name", String),
    Column("square", String),
    Column("station_type", String),
    Column("power", String),
    Column("voltage", String),
    Column("population", String),
    Column("count_connect", String),
    Column("connect_type", String),
    Column("is_military", String),
    Column("k", String)
)

k = Table(
    'k',
    metadata_obj,
    Column("id", Integer, primary_key=True, unique=True),
    Column("count_connect", String),
    Column("station_type", String),
    Column("population", String),
    Column("power", String),
    Column("voltage", String),
    Column("square", String),
    Column('is_military', String)
)

metadata_obj.create_all(engine)

def k_find(count_connect=1, population=1, power=1, volatge=1, square=1):
    with engine.connect() as conn:
        query = select(k)
        res = conn.execute(query)

        data = []
        for i in res.all()[0]:
            data.append(i)
        
        count_connect_value = data[1]
        station_type_value = data[2]
        population_value = data[3]
        power_value = data[4]
        voltage_value = data[5]
        square_value = data[6]

        k_num = (float(count_connect) * float(count_connect_value)) + float(station_type_value) + (float(population) * float(population_value)) + (float(power) * float(power_value)) + (float(volatge) * float(voltage_value)) + (float(square) * float(square_value))
        return k_num

def add_station(image, name, square, station_type, power, voltage, population, count_connect, connect_type, is_military ,k):
    with engine.connect() as conn:

        

        stmt = insert(station).values(
            image=image,
            name=name,
            square=square,
            station_type=station_type,
            power=power,
            voltage=voltage,
            population=population,
            count_connect=count_connect,
            connect_type=connect_type,
            is_military=is_military,
            k=k
        )


        conn.execute(stmt)
        conn.commit()

