import numpy as np


def generate_random_sample():
    # Generate a random seed
    seed = np.random.default_rng().integers(0, 2**32 - 1)

    # Create a random number generator using the seed
    rng = np.random.default_rng(seed)

    try:
        # Get user inputs
        population_range = int(input("Please input the population range: "))
        sample_size = int(input("Please input the sample size: "))

        # Validate inputs
        if population_range <= 0:
            print("Error: Range must be greater than 0.")
            return

        if sample_size <= 0:
            print("Error: Sample size must be greater than 0.")
            return

        if sample_size > population_range:
            print("Error: Sample size cannot be greater than the population range.")
            return

        # Generate the random sample
        sample = rng.choice(
            population_range,
            size=sample_size,
            replace=False
        )

        # Sort the results
        sample = np.sort(sample)

        # Display results
        print("\n" + "=" * 40)
        print("RANDOM SAMPLE GENERATOR")
        print("=" * 40)
        print(f"Seed: {seed}")
        print(f"Population Range: 1 to {population_range}")
        print(f"Sample Size: {sample_size}")
        print(f"Samples: {sample.tolist()}")
        print("=" * 40)

    except ValueError:
        print("Error: Please enter valid whole numbers.")


if __name__ == "__main__":
    generate_random_sample()
