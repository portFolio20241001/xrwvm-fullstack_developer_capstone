# モデルからCarMakeおよびCarModelをインポート
from .models import CarMake, CarModel


# 初期データを投入するための関数 `initiate`
def initiate():
    # CarMakeインスタンスに対応するデータを定義
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},  # NISSANのデータ
        {"name": "Mercedes", "description": "Great cars. German technology"},  # Mercedesのデータ
        {"name": "Audi", "description": "Great cars. German technology"},  # Audiのデータ
        {"name": "Kia", "description": "Great cars. Korean technology"},  # Kiaのデータ
        {"name": "Toyota", "description": "Great cars. Japanese technology"},  # Toyotaのデータ
    ]

    car_make_instances = []  # CarMakeインスタンスを格納するリスト

    # 各CarMakeデータを基にインスタンスを作成し、リストに追加
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(name=data['name'], description=data['description'])
        )

    # CarModelインスタンスに対応するデータを定義
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},  # Pathfinderモデル
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},  # Qashqaiモデル
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},  # XTRAILモデル
        {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},  # A-Classモデル
        {"name": "C-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},  # C-Classモデル
        {"name": "E-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},  # E-Classモデル
        {"name": "A4", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},  # A4モデル
        {"name": "A5", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},  # A5モデル
        {"name": "A6", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},  # A6モデル
        {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},  # Sorrentoモデル
        {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},  # Carnivalモデル
        {"name": "Cerato", "type": "Sedan", "year": 2023, "car_make": car_make_instances[3]},  # Ceratoモデル
        {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4]},  # Corollaモデル
        {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4]},  # Camryモデル
        {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": car_make_instances[4]},  # Klugerモデル
        # 必要に応じてCarModelインスタンスを追加可能
    ]

    # 各CarModelデータを基にインスタンスを作成
    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'], car_make=data['car_make'], type=data['type'], year=data['year']
        )
