import streamlit as st
import numpy as np


st.set_page_config(
    page_title="IAD Random Number Generator",
    page_icon="🎲",
    layout="centered"
)

st.title("🎲 Random Number Generator")

st.write(
    "Enter the population range and sample size, then click "
    "**Generate Random Sample**."
)


population_range = st.number_input(
    "Population Range",
    min_value=1,
    value=100,
    step=1
)

sample_size = st.number_input(
    "Sample Size",
    min_value=1,
    value=10,
    step=1
)


if st.button("🎲 Generate Random Sample", type="primary"):

    if sample_size > population_range:
        st.error(
            "Sample size cannot be greater than the population range."
        )

    else:
        seed = np.random.default_rng().integers(
            0,
            2**32 - 1
        )

        rng = np.random.default_rng(seed)

        sample = rng.choice(
            np.arange(1, population_range + 1),
            size=sample_size,
            replace=False
        )

        sample = np.sort(sample)

        st.success("Random sample generated successfully!")

        st.subheader("Results")

        col1, col2 = st.columns(2)

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

        st.subheader("Generated Sample")

        st.code(
            ", ".join(map(str, sample)),
            language=None
        )

        st.subheader("Random Seed")

        st.code(str(seed), language=None)

        st.info(
            "Save the random seed to reproduce the sample if necessary."
        )
