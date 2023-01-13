from main import generate_certificate
import os
import shutil
import pandas as pd

def set_params():
    # Image (Certificate) name
    image_list = ['mdhack-participant.png', 'mdhack-3rd.png', 'mdhack-2nd.png', 'mdhack-1st.png', 'mdhack-mentor.png', 'mdhack-judge.png']

    # Award Name
    award = "Hello Coders Mentorship Program - S1 2022"

    # Reason/Date
    reason = "16th February - 8th April 2022"

    csv_list = ['names-participant', 'name-3rd', 'name-2nd', 'name-1st', 'names-mentor', 'names-judge']

    generate_certificate(image_list, award, reason, csv_list)

def create_folder():

    dir = "generated-certificates/"
    for f in os.listdir(dir):
        shutil.rmtree(os.path.join(dir, f))

    team_names = pd.read_csv("csv/teams.csv")
    team_names = team_names["Team"].tolist()

    for i in range(len(team_names)):
        os.mkdir(os.path.join(dir, team_names[i]))


if __name__ == "__main__":
    create_folder()
    set_params()
    print("Certificates Generated!")
