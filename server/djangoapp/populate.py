# モデルからCarMakeおよびCarModelをインポート
from .models import CarMake, CarModel

# 初期データを投入するための関数 `initiate`
def initiate():
    # CarMakeインスタンスに対応するデータを定義
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},  # 日本の技術を活かしたNISSANの車
        {"name": "Mercedes", "description": "Great cars. German technology"},  # ドイツの技術を活かしたMercedesの車
        {"name": "Audi", "description": "Great cars. German technology"},  # ドイツの技術を活かしたAudiの車
        {"name": "Kia", "description": "Great cars. Korean technology"},  # 韓国の技術を活かしたKiaの車
        {"name": "Toyota", "description": "Great cars. Japanese technology"},  # 日本の技術を活かしたToyotaの車
    ]

    car_make_instances = []  # CarMakeインスタンスを格納するリスト

    # 各CarMakeデータを基にインスタンスを作成し、リストに追加
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(name=data['name'], description=data['description'])
        )

    # CarModelインスタンスに対応するデータを定義
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},  # NISSANのPathfinder（SUV）
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},  # NISSANのQashqai（SUV）
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},  # NISSANのXTRAIL（SUV）
        {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},  # MercedesのA-Class（SUV）
        {"name": "C-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},  # MercedesのC-Class（SUV）
        {"name": "E-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},  # MercedesのE-Class（SUV）
        {"name": "A4", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},  # AudiのA4（SUV）
        {"name": "A5", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},  # AudiのA5（SUV）
        {"name": "A6", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},  # AudiのA6（SUV）
        {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},  # KiaのSorrento（SUV）
        {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},  # KiaのCarnival（SUV）
        {"name": "Cerato", "type": "Sedan", "year": 2023, "car_make": car_make_instances[3]},  # KiaのCerato（セダン）
        {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4]},  # ToyotaのCorolla（セダン）
        {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4]},  # ToyotaのCamry（セダン）
        {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": car_make_instances[4]},  # ToyotaのKluger（SUV）
        # 必要に応じてCarModelインスタンスを追加可能
    ]

    # 各CarModelデータを基にインスタンスを作成
    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'], car_make=data['car_make'], type=data['type'], year=data['year']
        )
