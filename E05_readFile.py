days = ['Monday','Tuesday','Wednesday',
        'Thursday','Friday','Saturday',
        'Sunday']
title = 'Days of the Week'
filename = 'days.txt'  # enter your file path

def writeData():
    days_file = open(filename,'w')
    days_file.write(title + '\n')
    for item in days:
        days_file.write(item + '\n')
    days_file.close()

def readData():
    days_file = open(filename,'r')
    content = days_file.readlines() # reads all lines into list of strings
    days_file.close()
    content_edit = [ a.strip('\n') for a in content ]
    return content_edit

def readData2():
    content = [line for line in open(filename,'r')]
    return content

def main():
    print('Main function has been called.')
    writeData()
    readData()
    
if __name__ == "__main__":main()