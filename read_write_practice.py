#this functions count the occurences of the provied variable in the file
def count_num_in_file(file_path, num):
    count =0
    with open(file_path,'r')as f:
        for line in f.readlines():
            tokens = line.split(',') #this code stores the numbers seperated by the ',' in a list name tokens
            for token in tokens:
                if num==int(token):
                    count+=1
    return count

#this function sum the numbers seperated by the ',' and save it in a different file
def sum_numbers(file_path):
    output_lines=[]
    with open(file_path,'r') as f:
        for line in f.readlines():
            tokens = line.split(",")
            total = sum_tokens(tokens)
            output_lines.append(f"sum: {str(total)}|{line}")
    with open('D:\data science practice\python\input2.txt', 'w') as f:
        f.writelines(output_lines)

def sum_tokens(tokens):
    sum=0
    for token in tokens:
        sum+=int(token)
    return sum

sum_numbers('D:\data science practice\python\input.txt')
print(count_num_in_file('D:\data science practice\python\input.txt', 8))