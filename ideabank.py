from re import X
import sys
import keyboard as keyboard

def ask_for_idea():
    idea_list()
    while True:
        idea = input("What is your new idea? ")
        with open("ideas.txt", "a+") as file:
            file.write(f"{idea}\n")
           


def delete_lines():           
    with open("ideas.txt", "r") as file: 
        lines = file.readlines()
        print(lines)
        del lines[int(sys.argv[2])-1]
        print(lines)
        
    with open("ideas.txt", "w") as file:
        for line in lines:
            file.write(line)

def idea_list():
    with open("ideas.txt" ,"r") as file:
        for i, line in enumerate(file):
            print(f"{i+1}.idea: {line}")



if len(sys.argv) == 1:
    ask_for_idea()
if sys.argv[1] == "--list":
    idea_list()
if sys.argv[1] == "--delete":
    if len(sys.argv) < 3:
        print("error")
    else:
        delete_lines()        
        line = ""
        line == int(sys.argv[2])
        print(line)
       
   

    # while True:
    #     try:
    #          if keyboard.is_pressed('Ctrl+k'):
    #             print('Goodbye')
    #             print(idea)
    #             sys.exit()
    #     except:   
    #         break


# def create_a_file():
#     with open("ideas.txt", "r") as file:
#         if file not exist:
#          with open("ideas.txt", "a") as file:
#     # with open ("ideas.txt", "a") as file:
    #  with open('ideas.txt', 'r') as file:
#         lines = file.read()
#         print(lines)
    

# # create_a_file()
# ask_for_idea()
# def main():
#     ask_for_idea()
#     delete_lines()
# # #     create_a_file()
# #     pass

# if __name__ == '__main__':
#     main()
