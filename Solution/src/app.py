import streamlit as st
from montly_hall import simpulate_game
import time

st.set_page_config(
    page_title="Monty Hall Simulation",
    page_icon="🐐",
    layout="wide",  
    initial_sidebar_state="expanded"
)
st.markdown(
    """
    <style>
    .block-container {
        max-width: 1200px;
        margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title(":zap: Monty Hall Simplation")

num_games = st.number_input(
  "Enter Number of Games to Simulate", 
  min_value = 1, 
  max_value = 1000, 
  value = 100)

col1, col2 = st.columns(2)
col1.subheader("Win Percentage without Switching")
col2.subheader("Win Percentage with Switching")

chart1 = col1.line_chart(x=None, y=None, height=400)
chart2 = col2.line_chart(x=None, y=None, height=400)

wins_no_switch = 0
wins_switch = 0
for i in range(num_games):
  num_win_with_switching, num_win_without_swiching = simpulate_game(1)
  wins_no_switch += num_win_without_swiching
  wins_switch += num_win_with_switching
  
  chart1.add_rows([wins_no_switch/ (i + 1)])
  chart2.add_rows([wins_switch/ (i + 1)])

  time.sleep(0.001)