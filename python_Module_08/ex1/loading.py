import sys
import importlib


def check_dependency(package_name):
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {package_name} ({version})")
        return module
    except ImportError:
        print(f"[MISSING] {package_name}")
        return None


def main():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:\n")

    pandas = check_dependency("pandas")
    numpy = check_dependency("numpy")
    matplotlib = check_dependency("matplotlib")

    if not all([pandas, numpy, matplotlib]):
        print("\nSome dependencies are missing.")
        print("Install them using:\n")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
        sys.exit(1)

    print("\nAnalyzing Matrix data...")

    data_points = 1000
    signal = numpy.random.normal(0, 1, data_points)
    time = numpy.arange(data_points)

    df = pandas.DataFrame({
        "time": time,
        "signal": signal
    })

    print("Generating visualization...")
    print(f"Processing {data_points} data points...")

    import matplotlib.pyplot as plt

    plt.plot(df["time"], df["signal"])
    plt.title("Matrix Signal")
    plt.xlabel("Time")
    plt.ylabel("Signal")

    output_file = "matrix_analysis.png"
    plt.savefig(output_file)

    print("\nAnalysis complete!")
    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    main()
