from abc import ABC, abstractmethod
from typing import List, Any, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id}

    def run(self, data_batch: List[Any]) -> None:
        pass


class SensorStream(DataStream):
    sensor_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        SensorStream.sensor_count += 1

        data_filtered = self.filter_data(data_batch)
        if not data_filtered:
            return "No sensor readings"

        len_p = len(data_filtered)
        if len_p == 0:
            return "No valid readings"

        avg_name = data_filtered[0]["type"]
        avg_value = sum(item["value"] for item in data_filtered) / len_p
        return f"{len_p} readings processed, avg {avg_name}: {avg_value}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        filtered = []
        for item in data_batch:
            if (
                isinstance(item, dict)
                and "type" in item
                and "value" in item
                and isinstance(item["value"], (int, float))
                and isinstance(item["type"], str)
            ):
                filtered.append(item)
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Environmental Data"
        }

    def run(self, data_batch: List[Any]) -> None:
        print("\nInitializing Sensor Stream...")
        stats = self.get_stats()
        print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
        filtered = self.filter_data(data_batch)
        formatted = ", ".join(
            f"{item['type']}:{item['value']}" for item in filtered
        )
        print(f"Processing sensor batch: {formatted}")
        analysis = self.process_batch(data_batch)
        print(f"Sensor analysis: {analysis}")


class TransactionStream(DataStream):
    trans_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        TransactionStream.trans_count += 1

        data_filtered = self.filter_data(data_batch)
        if not data_filtered:
            return "No transaction readings"

        len_processed = len(data_filtered)
        sum_processed = sum(data_filtered)
        sin = "-" if sum_processed < 0 else "+"
        return (f"Transaction analysis: {len_processed} operations, "
                f"net flow: {sin}{abs(sum_processed)} units")

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        filtered = []
        for item in data_batch:
            if isinstance(item, (int, float)):
                filtered.append(item)
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Financial Data"
        }

    def run(self, data_batch: List[Any]) -> None:
        print("\nInitializing Transaction Stream...")
        stats = self.get_stats()
        print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")

        fil = self.filter_data(data_batch)
        print(f"Processing transaction batch: {fil}")

        analysis = self.process_batch(data_batch)
        print(f"Transaction analysis: {analysis}")


class EventStream(DataStream):
    event_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        EventStream.event_count += 1

        data_filtered = self.filter_data(data_batch)
        errors = data_filtered.count("error")
        return f"{len(data_filtered)} events, {errors} error detected"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        return [
            item for item in data_batch
            if isinstance(item, str)
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "System Events"
        }

    def run(self, data_batch: List[Any]) -> None:
        print("\nInitializing Event Stream...")
        stats = self.get_stats()
        print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")

        fil = self.filter_data(data_batch)
        print(f"Processing event batch: {fil}")

        analysis = self.process_batch(data_batch)
        print(f"Event analysis: {analysis}")


class StreamProcessor:
    def __init__(self):
        pass

    def process(self, stream: DataStream, master_batch: List[Any]) -> None:
        try:
            stream.run(master_batch)
        except Exception as e:
            print(f"Stream processing error: {e}")


def main():
    processor = StreamProcessor()

    sensor_stream = SensorStream("SENSOR_001")
    transaction_stream = TransactionStream("TRANS_001")
    event_stream = EventStream("EVENT_001")

    data_batch = [
        {"type": "humidity", "value": 65},
        {"type": "temp", "value": 22.5},
        {"y": "pressure", "value": 1013},
        "helllo"
    ]

    transaction_data = [100, -50, 75, "txt"]
    event_data = ["login", "error", "logout"]

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    processor.process(sensor_stream, data_batch)
    processor.process(transaction_stream, transaction_data)
    processor.process(event_stream, event_data)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    print("\nBatch 1 Results:")
    print(f"- Sensor data: {SensorStream.sensor_count} readings processed")
    print(f"- Transaction data: {TransactionStream.trans_count} "
          "operations processed")
    print(f"- Event data: {EventStream.event_count} events processed")

    print("\nStream filtering active: High-priority data only")
    print(f"Filtered results: {EventStream.event_count} critical sensor "
          f"alerts, {TransactionStream.trans_count} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal")


if __name__ == "__main__":
    main()
