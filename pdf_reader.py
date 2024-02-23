import pyttsx3
import fitz

# Get Pdf Section to read

my_path = "Evaluation_of_Machine_Learning_Algorithms_using_Feature_Selection_Methods_for_Network_Intrusion_Detection_Systems.pdf"                    # declare PDF path here
doc = fitz.open(my_path)
page_num = 2
page = doc[page_num]                                #   declare page number here
text = page.get_text()


# Start reading Pdf

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)            #   for male voice set 0
engine.say(text)
engine.runAndWait()
