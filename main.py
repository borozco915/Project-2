# The Data Set that I selected is related to different statics of F1 drivers over the years.
# The location of the dataset is https://www.kaggle.com/datasets/petalme/f1-drivers-dataset?resource=download
#The dataset includes information from almost every F1 driver in histroy.
#This includes driver strategies, track-specific adaptations, and team dynamics.


import pandas as pd
import os
import matplotlib.pyplot as plt


# Function Definitions
def load_data(file_path):
    try:
        if os.path.exits(file_path):
            data = pd.read.csv(file_path)
            print("Data loaded sucessfully.")
            return data
        else:
            raise FileNotFoundError(f"{file_path} does not exist.")
    except Exception as e:
        print(f"Error: {e}")
        return None

def clean_data(df):
    """Performs basic cleaning and type conversion"""
    df= df.dropna(subset=['Driver', 'Race_Entries', 'Points'])
    numeric_cols =  ['Race_Entries', 'Race_Starts', 'Pole_Positions', 'Race_Wins',
                    'Podiums', 'Fastest_Laps', 'Points', 'Pole_Rate', 'Start_Rate',
                    'Win_Rate', 'Podium_Rate', 'FastLap_Rate', 'Points_Per_Entry']     
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        return df
    

# ----------- Main Program ------------
file_path = "f1.csv"
data = load_data(file_path)

if data is not None:
    data = clean_data(data)

    # Derived metric: "Legendary Driver" if they won 3 or more champions
    data['Legendary'] = data['Championships'] >=3

    # Dictionary operation: count legends by decade
    legendary_counts = data[data['Legendary'] == True]['Decade'].value_counts().to_dict()


    # Loop to display dictionary
    print("\nLegendary Drivers by Decade:")
    for decade, count in legendary_counts.items():
        print(f"{decade}: {count} drivers")
    
    # Conditional structure
    if legendary_counts:
        print("There are legendary drivers across decades.")
    else:
        print("No legendary drivers found based on criteria.")
    
    # Visualization: Top 10 drivers by win rate
    top_win_rates = data[['Driver', 'Win_Rate']].sort_values(by='Win_Rate', ascending=False).head(10)

    plt.figure(figsize=(10,6))
    plt.barh(top_win_rates['Driver'][::-1], top_win_rates['Win_Rate'][::-1], color='gold')
    plt.xlabel('Win Rate')
    plt.title(' Top 10 F1 Drivers by Win Rate')
    plt.tight_layout()
    plt.show()

"""
INSIGHT PARAGRAPH:

This project gave me a deeper appreciation of consistency and dominance in F1 history. 
Especially since a lot of my favorite F1 drivers are Ayton Senna, Michael Schumacher, and currently Carlos Sainz
By creating a 'Legendary' metric based on winning 3+ championships, I identified which 
drivers dominated their eras. I was surprised to see that some drivers with fewer championships 
had higher win rates than multi-title holders—highlighting how context and competition 
affect legacy.

As an F1 fan, this project relates directly to my passion. It helped me back up discussions 
with actual data, and made me think more critically about what defines greatness in motorsport. 
One challenge was handling missing values for older drivers due to incomplete data.

"""




"""

AI Tools Used:

Tool: ChatGpt
-How it was used: I used ChatGPT to give me an example for a generic idea of what type of category 
could be used in the dataset. Which is why it gave my the "legendary" which after that, I used to give
a generic idea of what type of code to write for tracking that data. I used to check if anything could be improved
in my code or if the outputs would be correct before I ran it.


"""