import importlib.util
from importlib import metadata


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    dependencies = [
        "pandas",
        "numpy",
        "matplotlib",
        "requests",
    ]

    missing = False

    for dep in dependencies:
        if importlib.util.find_spec(dep) is None:
            print(f"[MISSING] {dep}")
            missing = True
        else:
            try:
                version = metadata.version(dep)
                print(f"[OK] {dep} ({version})")
            except metadata.PackageNotFoundError:
                print(f"[OK] {dep}")

    if missing:
        print("\nSome dependencies are missing.")
        print("Install them with:")
        print("pip install -r requirements.txt")
    else:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        print("\nAnalyzing Matrix data...")

        data = np.random.randn(1000)
        df = pd.DataFrame({"values": data})

        print("Processing 1000 data points...")

        df.plot(title="Matrix Signal Analysis")
        plt.savefig("matrix_analysis.png")

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
