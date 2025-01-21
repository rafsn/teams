import streamlit as st

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[df_data["Club"] == club]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(f"{player_stats['Name']}")

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"**Idade**: {player_stats['Age']}")
col2.markdown(f"**Altura**: {player_stats['Height']}")
col3.markdown(f"**Peso**: {player_stats['Weight'] * 0.4563:.2f}")

st.divider()
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

