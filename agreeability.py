def create_template_list(duration):
    return [0] * int(duration * 1000)

def get_end_time(file_input):
    with open(file_input, "r") as f:
        bTime = 0.0
        eTime = 0.0
        aTime = 0.0
        for line in f:
            line = line.split("\t")
            del line[1]
            line[-1] = line[-1].strip("\n")
            line[1] = float(line[1])
            line[2] = float(line[2])
            line[3] = float(line[3])
            if line[0] == "default":
                continue
            if (line[0] == "Behavioral_Engagement") and line[2] > bTime:
                bTime = line[2]
            elif line[0] == "Attention_Engagement" and line[2] > aTime:
                aTime = line[2]
            elif line[0] == "Emotional_Engagement" and line[2] > eTime:
                eTime = line[2]
    return bTime, aTime, eTime

def import_data(file_name):
    bTime, aTime, eTime = get_end_time(file_name)
    Behavioral_Engagement = create_template_list(bTime)
    Attention_Engagement = create_template_list(aTime)
    Emotional_Engagement = create_template_list(eTime)
    with open(file_name, "r") as f:
        for line in f:
            line = line.split("\t")
            del line[1]
            line[-1] = line[-1].strip("\n")
            if line[4] == "off-tsak" or line[4] == "distarcted" or line[4] == "Bored":
                tag = 1
            if line[4] == "on-task" or line[4] == "idle" or line[4] == "Confused":
                tag = 2
            if line[4] == "Satisfied" or line[4] == "focused":
                tag = 3
            start = int(float(line[1]) * 1000) - 1
            stop = int(float(line[2]) * 1000)
            if line[0] == "Behavioral_Engagement":
                for i in range(start, stop):
                    Behavioral_Engagement[i] = tag
            elif line[0] == "Attention_Engagement":
                for i in range(start, stop):
                    Attention_Engagement[i] = tag
            elif line[0] == "Emotional_Engagement":
                for i in range(start, stop):
                    Emotional_Engagement[i] = tag
    return Behavioral_Engagement, Attention_Engagement, Emotional_Engagement

def get_agreeability(file1,file2):
    bTime, aTime, eTime = (get_end_time(file1))
    if isinstance(file1,list): #there is no use case where a single file will be compared to a list; the lengths wouldnt match
        b1,a1,e1 = import_multiple(file1)
        b2,a2,e2 = import_multiple(file2)
    else:
        b1,a1,e1 = import_data(file1)
        b2,a2,e2 = import_data(file2)
    bA, aA, eA = 0,0,0
    for elem1,elem2 in zip(b1,b2):
        if elem1 == elem2:
            bA += 1
    for elem1,elem2 in zip(a1,a2):
        if elem1 == elem2:
            aA += 1
    for elem1,elem2 in zip(e1,e2):
        if elem1 == elem2:
            eA += 1
    return bA/(bTime*1000), aA/(aTime*1000), eA/(eTime*1000)
    
def import_multiple(files):
    b,a,e = [],[],[]
    for f in files:
        b1,a1,e1 = import_data(f)
        b.append(b1)
        a.append(a1)
        e.append(e1)
    return b,a,e

def get_agreeability_multiple(files1,files2):
    bTime, aTime, eTime = (get_end_time(files1[0]))
    b1,a1,e1 = import_multiple(files1)
    b2,a2,e2 = import_multiple(files2)
    for elem1,elem2 in zip(b1,b2):
        if elem1 == elem2:
            bA += 1
    for elem1,elem2 in zip(a1,a2):
        if elem1 == elem2:
            aA += 1
    for elem1,elem2 in zip(e1,e2):
        if elem1 == elem2:
            eA += 1
    return bA/(bTime*1000), aA/(aTime*1000), eA/(eTime*1000) 
    
if __name__ == "__main__":
    print(get_agreeability('resources/P01_S02_wellness_Emily.txt','resources/p01_s02.txt'))
    # print(get_agreeability('resources_test/tester1.txt','resources_test/tester2.txt'))
    # print(get_agreeability('resources_test/tester3.txt','resources_test/tester4.txt'))