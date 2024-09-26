import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode, ColumnsAutoSizeMode, JsCode

# サンプルのデータフレームを作成
df_kawa = pd.read_csv('kawaguchi.csv')
df_ise = pd.read_csv('isezaki.csv')
df_hama = pd.read_csv('hamamatsu.csv')
df_ii = pd.read_csv('iizuka.csv')
df_san = pd.read_csv('sanyo.csv')

# データフレームをリストにまとめる
df = pd.concat([df_kawa, df_ise, df_hama, df_ii, df_san])

# チェックボックス列
df['☑️'] = [False] * len(df)
df = df[['☑️'] + [col for col in df.columns if col != '☑️']]

"""
### 選手特徴一覧
"""

# 検索バーを追加
search_text = st.text_input('検索', '')

# 検索機能の実装: 検索テキストが入力されている場合、フィルタリング
if search_text:
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_text, case=False).any(), axis=1)]
else:
    filtered_df = df

# 初期化：セッションステートにチェック状態を保存するリストを作成
if 'selected_states' not in st.session_state:
    st.session_state['selected_states'] = df['☑️'].tolist()

# テーブルの表示と編集可能にするための設定
gb = GridOptionsBuilder.from_dataframe(filtered_df)
gb.configure_pagination(paginationAutoPageSize=True)  # ページネーションを設定
gb.configure_default_column(editable=True)  # すべての列を編集可能に設定
gb.configure_grid_options(enableHorizontalScroll=True)
grid_options = gb.build()

# データグリッドを表示
grid_response = AgGrid(
    filtered_df,
    gridOptions=grid_options,
    update_mode=GridUpdateMode.MODEL_CHANGED,  # モデルが変更されたときに更新
    data_return_mode=DataReturnMode.FILTERED_AND_SORTED,  # フィルタリングとソートの状態を保持
    editable=True,
)

# 更新されたデータを取得
updated_df = pd.DataFrame(grid_response['data'])

# チェックボックスの状態をセッションステートに保存
st.session_state['selected_states'] = updated_df['☑️'].tolist()

# チェックされている行を取得
selected_rows = updated_df[updated_df['☑️']]
selected_rows = selected_rows.drop(columns=['☑️'])

# チェックされたデータを表示
if len(selected_rows) > 0:
    st.subheader('選手比較')
    st.write(selected_rows)
else:
    st.write("選手未選択")



import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import matplotlib_fontja

# 取得したデータをもとにグラフを表示
if not selected_rows.empty:
    # 表示するチャートの数
    n_charts = min(len(selected_rows), 8)  # 最大8つのチャートを表示
    cols = 2  # 横に2つ表示
    rows = (n_charts + cols - 1) // cols  # 行数を計算

    # サブプロットの作成
    fig, axs = plt.subplots(rows, cols, figsize=(10, 5 * rows), subplot_kw=dict(polar=True))

    # 各名前ごとにグラフを描画
    for i in range(n_charts):
        # 各行のインデックスを計算
        ax = axs[i // cols, i % cols] if rows > 1 else axs[i % cols]  # 2つずつ横並び、行数が1の場合は1次元として扱う

        name = selected_rows['名前'].iloc[i]  # 名前を取得

        # 特定の名前のデータを取得
        data = selected_rows[selected_rows['名前'] == name].drop(columns='名前').values.flatten()
        data = data[:-1]  # 必要なデータを選択

        # クラスのlabel_listと取得したデータを設定
        label_list = ['スタート', '独走力', '追い込み力', '雨巧拙']

        # 取得したデータを使って精度のリストを作成
        acc_list = data.tolist()  # データをリストに変換
        acc_list += acc_list[:1]  # チャートを閉じるために最初の値を末尾に追加

        # レーダーチャートを描画するためのangle_listを計算
        angle_list = [n / float(len(label_list)) * 2 * np.pi for n in range(len(label_list))]
        angle_list += angle_list[:1]  # チャートを閉じるために最初の値を末尾に追加

        # matplotlibでレーダーチャートを描画
        ax.set_xticks(angle_list[:-1])
        ax.set_xticklabels(label_list, color='grey', size=20)

        # Y軸の範囲を固定
        ax.set_ylim(0, 5)  # Y軸の範囲を0から5に設定
        ax.set_yticks(np.arange(0, 6, 1))  # 目盛りを0から5まで1刻みで設定
        ax.set_yticklabels([])  # メモリラベルを消す

        # プロット線を描画
        ax.plot(angle_list, acc_list, linewidth=2, linestyle='solid', label=name)  # 名前をラベルとして使用
        ax.fill(angle_list, acc_list, 'blue', alpha=0.2)

        # タイトルを設定
        ax.set_title(name, size=30)

    # チャートを表示
    plt.tight_layout()  # 自動でレイアウトを調整
    st.pyplot(fig)  # pltではなくfigを使って表示
else:
    st.write("データがありません。")
