
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


sns.set(style="whitegrid")


# print("hpyi")

st.title("deploy model")
st.markdown("Markdown understand heart issue")

diamonds = sns.load_dataset("diamonds")
d=diamonds.head()

st.write(d)

f, ax = plt.subplots(figsize=(6.5,6.5))

sns.despine(f, left=True, bottom=True)

clarity_ranking = ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"]
sns.scatterplot(x="carat", y="price",
                hue="clarity", size="depth",
                palette="ch:r=-.2, d=.3_r",
                hue_order=clarity_ranking,
                sizes=(1,8), linewidth=0,
                data=diamonds, ax=ax)

st.pyplot(f)
