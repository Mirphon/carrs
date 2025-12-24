import pandas as pd
from sqlalchemy.orm import Session
from models import Car, Session as DBSession

# -----------------------------
# Настройки
# -----------------------------
csv_file = "result3.csv"
LIMIT = 500

db_session = DBSession()

# -----------------------------
# Чтение CSV
# -----------------------------
df = pd.read_csv(csv_file)

# Заменяем NaN на None
df = df.where(pd.notnull(df), None)

# -----------------------------
# Берём 500 случайных строк
# -----------------------------
if len(df) > LIMIT:
    df = df.sample(n=LIMIT, random_state=42)  # random_state — для воспроизводимости

# -----------------------------
# Добавление записей в таблицу Car
# -----------------------------
for _, row in df.iterrows():
    car = Car(
        seller_id=row.get("seller_id"),
        brand=row.get("brand"),
        model=row.get("model_name"),
        bodytype=row.get("bodyType"),
        description=row.get("description"),
        color=row.get("color"),
        engine_displacement=row.get("engineDisplacement"),
        engine_power=row.get("enginePower"),
        fuel_type=row.get("fuelType"),
        mileage=row.get("mileage"),
        production_date=row.get("productionDate"),
        vehicle_transmission=row.get("vehicleTransmission"),
        owners=row.get("owners"),
        drive_type=row.get("drivetrains"),
        wheel=row.get("wheel"),
        price=row.get("price"),
        vin=row.get("vin"),
        state_number=row.get("state_number"),
        price_range=row.get("price_range")
    )
    db_session.add(car)

# -----------------------------
# Коммит
# -----------------------------
db_session.commit()
db_session.close()

print(f"✅ Загружено {len(df)} случайных записей из {csv_file} в таблицу Car.")

