from predict import prediction, preprocess
from typing import List



def diseasePredict(dataFrame: List[str]):
    processed = preprocess(dataFrame)
    predict = prediction(processed)
    return predict

if __name__ == "__main__":
    if(len(sys.argv) != 2):
      print("Enter the name of input file")
    else:
      input = open(sys.argv[1],"r")
      output = diseasePredict(input)
      print("The disease identified using the symptoms is "+output)
