import streamlit as st
import pandas as pd
import numpy as np

# ページ設定
st.set_page_config(
    page_title="Streamlit App Deploy Demo",
    page_icon="🚀",
    layout="wide"
)

# タイトル
st.title("🚀 Streamlit App Deploy Demo")

# サイドバー
st.sidebar.header("設定")
num_points = st.sidebar.slider("データポイント数", 10, 1000, 100)

# メインコンテンツ
st.header("ランダムデータ可視化")

# データ生成
data = pd.DataFrame({
    'x': np.random.randn(num_points),
    'y': np.random.randn(num_points),
    'category': np.random.choice(['A', 'B', 'C'], num_points)
})

# データ表示
col1, col2 = st.columns(2)

with col1:
    st.subheader("散布図")
    st.scatter_chart(data, x='x', y='y', color='category')

with col2:
    st.subheader("データテーブル")
    st.dataframe(data)

# 統計情報
st.header("統計情報")
st.write(f"総データポイント数: {len(data)}")
st.write(f"カテゴリA: {len(data[data['category'] == 'A'])}")
st.write(f"カテゴリB: {len(data[data['category'] == 'B'])}")
st.write(f"カテゴリC: {len(data[data['category'] == 'C'])}")

# フッター
st.markdown("---")
st.markdown("Streamlitで作成されたデモアプリです 🎉")
