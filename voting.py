import streamlit as st # type: ignore
import sqlite3
import matplotlib.pyplot as plt # type: ignore

# Connect to database (or create it if it doesn't exist)
conn = sqlite3.connect('votes.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS votes (
        option TEXT
    )
''')
conn.commit()

# Voting options
options = ["Python", "Java", "C++", "JavaScript", "Go"]

# Streamlit app UI
st.set_page_config(page_title="Voting App", page_icon="🗳️")
st.title("🗳️ Voting App")
st.write("Vote for your favorite programming language!")

# Voting section
vote = st.radio("Choose one:", options)
if st.button("Submit Vote"):
    c.execute("INSERT INTO votes (option) VALUES (?)", (vote,))
    conn.commit()
    st.success(f"Thanks for voting for {vote}!")

# Results section
st.subheader("📊 Current Results")
c.execute("SELECT option, COUNT(*) FROM votes GROUP BY option")
results = c.fetchall()

if results:
    options_voted = [row[0] for row in results]
    votes_count = [row[1] for row in results]

    fig, ax = plt.subplots()
    ax.bar(options_voted, votes_count, color='skyblue')
    ax.set_ylabel('Votes')
    ax.set_xlabel('Options')
    ax.set_title('Live Voting Results')
    st.pyplot(fig)
else:
    st.info("No votes yet. Be the first to vote!")

# Close connection at the end
conn.close()
