import random
import pandas as pd
from tqdm import tqdm

def generate(input_file, start, last, output_file):
    """Generate big files
    input_file: this csv file should contains data in it to generate the others
    start: the end of the previous file numbering 
    last: the end of the new file numbering
    output_file: final csv file
    """
    data = pd.read_csv(input_file, delimiter=';')
    names = data.Name.to_list()
    sex = data.Sex.to_list()
    sib_sp = data.SibSp.to_list()
    parch = data.Parch.to_list()
    ticket = data.Ticket.to_list()
    embarked = data.Embarked.to_list()
    fare = data.Fare.to_list()
    cabin = data.Cabin.to_list()
    #Generate dictionnaries stored in a list to feed the dataframe
    entries = []
    for passenger_id in tqdm(range(start, last)):
        survived = random.randint(0, 1)
        passenger_class = random.randint(1, 3)
        passenger_age = random.randint(15, 50)
        survived = random.randint(0, 1)
        # if passenger_id % 1000 == 0:
        #     print("Items remaining: %d" % (passenger_id_last - passenger_id))        
        entries.append({'PassengerId':passenger_id, 'Survived': survived,
                        'Pclass': passenger_class, 
                        'Name':names[passenger_id%len(names)],
                        'Sex':sex[passenger_id%len(sex)], 'Age':passenger_age,
                        'SibSp':sib_sp[passenger_id%len(sib_sp)], 
                        'Parch':parch[passenger_id%len(parch)], 
                        'Ticket':ticket[passenger_id%len(ticket)], 
                        'Fare':fare[passenger_id%len(fare)], 'cabin':cabin[passenger_id%len(cabin)], 
                        'Embarked':embarked[passenger_id%len(embarked)]}) 
    print("Generating Dataframe from the list ...")
    data2 = pd.DataFrame(entries)

    #del entries
    #del data
    print("Appending the newly generated dataframe to the old one ...")
    big_one = data.append(data2,sort=False)
    
    #del data2
    print("Generating the final cvs file ...")
    big_one.to_csv(output_file,index=False,sep='#')

    #del big_one

def main():
    START = 99999
    LAST = 30000000
    generate('train_test.csv', START, LAST, 'temp.csv')

#if __name__ == "main":
main()


