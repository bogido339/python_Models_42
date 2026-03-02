from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False

        if len(data) == 0:
            return False

        for item in data:
            if not isinstance(item, (int, float)):
                return False

        return True

    def process(self, data: Any) -> str:
        total_number = len(data)
        sum_number = sum(data)
        avg = sum_number / total_number

        return (f"Processed {total_number} numeric values, "
                f"sum={sum_number}, avg={avg:.1f}")

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if len(data) == 0:
            return False
        return True

    def process(self, data: Any) -> str:
        characters = len(data)
        words = len(data.split())

        return f"Processed text: {characters} characters, {words} words"

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str):
                return False
            log = data.split(": ")
            if len(log) != 2:
                return False
            if log[0] != 'ERROR':
                return False
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        try:
            log = data.split(": ")
            if len(log) != 2:
                return "Invalid log format"
            if log[0] == 'ERROR':
                return f"[ALERT] ERROR level detected: {log[1]}"
            return "Log processed"
        except Exception:
            return "Processing error"

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    number_data = [1, 33, 5, 1337, 20, 42]
    numbers = NumericProcessor()
    if numbers.validate(number_data):
        result = numbers.process(number_data)
        print(numbers.format_output(result))
    else:
        print("Validation failed: invalid numeric data")

    print("\nInitializing Text Processor...")
    text_data = "Hello Nexus World"
    text = TextProcessor()
    if text.validate(text_data):
        result = text.process(text_data)
        print(text.format_output(result))
    else:
        print("Validation failed: invalid text data")

    print("\nInitializing Log Processor...")
    log_data = "ERROR: Connection timeout"
    log = LogProcessor()
    if log.validate(log_data):
        result = log.process(log_data)
        print(log.format_output(result))
    else:
        print("Validation failed: invalid log data")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...\n")

    prosses = [numbers, text, log]
    data = [number_data, text_data, log_data]
    for i, obj in enumerate(prosses):
        if obj.validate(data[i]):
            res = obj.process(data[i])
            print(f"result {i + 1}: {res}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
