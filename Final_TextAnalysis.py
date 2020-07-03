import glob
import os
import pandas as pd
from nltk.corpus import stopwords
from datetime import datetime, date, time

path = "/Users/arpitasaha/Desktop/BigDataExtraAsgn/Agile_Therapeutics_Inc1/"

#List all text files from respective folders
all_files = glob.glob(os.path.join(path, "*.txt"))

#Create data frame with only column names
column_names = ['FirstName','LastName','AnalystsFirm(Brokker)','FirmName','AnalysisReportTime','Score_StrongModal','Score_Negative','Score_Litigious','Score_Uncertainity','Score_Positive','Score_ModerateModal','Score_WeakModal','Score_Constraining']
df = pd.DataFrame(columns = column_names)

#defining global variables
Modal_Score = 0
Negative_Score = 0 
Litigious_Score = 0
Uncertainity_Score = 0
Positive_Score = 0
Mmodal_Score = 0
Wmodal_Score = 0
Constraining_Score = 0

#Function to calculate scores
def calculateScores(words):

    #1)   Read all strong modal
    from collections import Counter
    smodal_file = open('/Users/arpitasaha/Desktop/BigDataExtraAsgn/Lexicons/arpita_saha_strong_modal.txt')
    smodal_lexicons = smodal_file.read().split()
    Sum_modal = 0
    word_freq = Counter(words)


    for strmodal_word in smodal_lexicons:
        Sum_modal += word_freq[strmodal_word]
    global Modal_Score    
    Modal_Score = (Sum_modal/total_wordcount)
    

    #2)  read all negative lexicons
    negative_file = open('/Users/arpitasaha/Desktop/BigDataExtraAsgn/Lexicons/arpita_saha_negative.txt')
    negative_lexicons = negative_file.read().split()

    #code to calculate negative score
    Sum_negative = 0

    for neg_word in negative_lexicons:
        Sum_negative += word_freq[neg_word]
    
    global Negative_Score
    Negative_Score = (Sum_negative/total_wordcount)

    #3)  read all litigious lexicons
    litigious_file = open('/Users/arpitasaha/Desktop/BigDataExtraAsgn/Lexicons/arpita_saha_litigious.txt')
    litigious_lexicons = litigious_file.read().split()

    #code to calculate litigious score
    Sum_litigious = 0

    for lit_word in litigious_lexicons:
        Sum_litigious += word_freq[lit_word]
    
    global Litigious_Score
    Litigious_Score = (Sum_litigious/total_wordcount)
    
    #4)   read all uncertainity lexicons
    uncertainity_file = open('/Users/arpitasaha/Desktop/BigDataExtraAsgn/Lexicons/arpita_saha_uncertainty.txt')
    uncertainity_lexicons = uncertainity_file.read().split()

    #code to calculate uncertainity score
    Sum_uncertainity = 0

    for unc_word in uncertainity_lexicons:
        Sum_uncertainity += word_freq[unc_word]
    
    global Uncertainity_Score
    Uncertainity_Score = (Sum_uncertainity/total_wordcount)
 
    #5)   read all positive lexicons
    positive_file = open('/Users/arpitasaha/Desktop/BigDataExtraAsgn/Lexicons/arpita_saha_positive.txt')
    positive_lexicons = positive_file.read().split()

    #code to calculate uncertainity score
    Sum_positive = 0


    for pos_word in positive_lexicons:
        Sum_positive += word_freq[pos_word]
    
    global Positive_Score
    Positive_Score = (Sum_positive/total_wordcount)

    #6)   read all moderate modal lexicons
    mmodal_file = open('/Users/arpitasaha/Desktop/BigDataExtraAsgn/Lexicons/arpita_saha_moderate_modal.txt')
    mmodal_lexicons = mmodal_file.read().split()

    #code to calculate mmodal score
    Sum_mmodal = 0

    for mmodal_word in mmodal_lexicons:
        Sum_mmodal += word_freq[mmodal_word]
    
    global Mmodal_Score
    Mmodal_Score = (Sum_mmodal/total_wordcount)

    #7)   read all weak modal lexicons
    wmodal_file = open('/Users/arpitasaha/Desktop/BigDataExtraAsgn/Lexicons/arpita_saha_weak_modal.txt')
    wmodal_lexicons = wmodal_file.read().split()

    #code to calculate wmodal score
    Sum_wmodal = 0

    for wmodal_word in wmodal_lexicons:
        Sum_wmodal += word_freq[wmodal_word]
    
    global Wmodal_Score
    Wmodal_Score = (Sum_wmodal/total_wordcount)

    #8)   read all constraining lexicons
    constraining_file = open('/Users/arpitasaha/Desktop/BigDataExtraAsgn/Lexicons/arpita_saha_constraining.txt')
    constraining_lexicons = constraining_file.read().split()

    #code to calculate constraining score
    Sum_constraining = 0

    for cons_word in constraining_lexicons:
        Sum_constraining += word_freq[cons_word]
    
    global Constraining_Score
    Constraining_Score = (Sum_constraining/total_wordcount)



#Extract column names for data frames
for file in all_files:
    # get Filename
    file_name = os.path.splitext(os.path.basename(file))[0]
    file_name = file_name.replace(' - ',' ')
    # Split based on space
    split_elements = file_name.split('-')
    if len(split_elements[4]) <= 1:
        split_elements[4] = datetime.strptime(split_elements[5], '%m%d%Y')
        date_field = split_elements[4].strftime("%m/%d/%y")
    else:
        split_elements[4] = datetime.strptime(split_elements[4], '%m%d%Y')
        date_field = split_elements[4].strftime("%m/%d/%y")
        
    
    # calculate and create last column #for one .txt file now
    file_i = open(file,mode='r')
    complete_file = file_i.read()
    
    from nltk.tokenize import word_tokenize
    tokens = word_tokenize(complete_file)

    # convert to lower case
    tokens = [w.lower() for w in tokens]

    # remove punctuation from each word
    import string
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]

    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]

    # filter out stop words (CONFIRM)
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]


    # count total words
    total_wordcount= len(words)
    
    # calculate 8 scores for each file and write to dataframe
    calculateScores(words)
    df = df.append({'FirstName': split_elements[0],'LastName': split_elements[1],'AnalystsFirm(Brokker)':split_elements[2],'FirmName':split_elements[3],'AnalysisReportTime': date_field,'Score_Negative': Negative_Score,'Score_Litigious': Litigious_Score,'Score_Uncertainity': Uncertainity_Score,'Score_Positive': Positive_Score,'Score_ModerateModal': Mmodal_Score,'Score_WeakModal': Wmodal_Score,'Score_Constraining': Constraining_Score,'Score_StrongModal': Modal_Score},ignore_index=True)      
    
       
Output_file = '/Users/arpitasaha/Desktop/BigDataExtraAsgn/Agile_Therapeutics_Inc1/output_file.csv'
df.to_csv(Output_file, sep=',', encoding='utf-8')
#print(df)