import streamlit as st
import numpy as np


st.set_page_config(
    page_title="IAD Random Number Generator",
    page_icon="🎲",
    layout="centered"
)

st.title("🎲 IAD Random Number Generator")

st.write(
    "Enter the population range and sample size. "
    "You may optionally enter a seed to reproduce a previous sample."
)


# User inputs
population_range = st.number_input(
    "Population Range",
    min_value=1,
    value=100,
    step=1,
    help="For example, entering 100 will generate numbers from 1 to 100."
)

sample_size = st.number_input(
    "Sample Size",
    min_value=1,
    value=10,
    step=1
)

# Optional seed input
seed_input = st.text_input(
    "Random Seed (Optional)",
    placeholder="Leave blank to generate a random seed",
    help="Enter a previous seed to reproduce the same random sample."
)


if st.button("🎲 Generate Random Sample", type="primary"):

    # Validate sample size
    if sample_size > population_range:
        st.error(
            "Sample size cannot be greater than the population range."
        )

    else:
        # Determine seed
        if seed_input.strip():
            try:
                seed = int(seed_input)

            except ValueError:
                st.error(
                    "Seed must be a valid whole number."
                )
                st.stop()

        else:
            seed = np.random.default_rng().integers(
                0,
                2**32 - 1
            )

        # Create random number generator
        rng = np.random.default_rng(seed)

        # Generate unique random samples
        sample = rng.choice(
            np.arange(1, population_range + 1),
            size=sample_size,
            replace=False
        )

        # Sort the results
        sample = np.sort(sample)

        # Display results
        st.success("Random sample generated successfully!")

        st.subheader("Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Population Range",
                f"1 to {population_range}"
            )

        with col2:
            st.metric(
                "Sample Size",
                sample_size
            )

        with col3:
            st.metric(
                "Random Seed",
                seed
            )

        st.subheader("Generated Sample")

        st.code(
            ", ".join(map(str, sample)),
            language=None
        )

        st.info(
            "Save the random seed if you need to reproduce this sample later."
        )
