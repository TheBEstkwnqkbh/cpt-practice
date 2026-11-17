# What is main()?
#   main() is a procedure that holds your whole program's plan.
#   It runs the steps in order: get input, call your procedure,
#   show output. The last line of the file, main(), starts it.
#   The name "main" isn't required by Python, but programmers use
#   it so anyone can find where the program begins.

# Top-down design:
#   Start with the big picture (the TOP), then fill in the
#   details (the BOTTOM). Like writing an essay outline before
#   the paragraphs.
#     TOP    = main(): the steps your program follows, in order.
#     BOTTOM = your procedure: the detailed algorithm for one step.
#   Don't start with the algorithm! Plan main() first, so you
#   know exactly what your procedure needs to do.

# ---------- DATA ----------
# A list stores many values under one name.
# Replace this list with YOUR data.
# What group of things does your program use?

my_list = ["apple", "banana", "cherry", "grape", "mango", "orange"]

# ---------- PROCEDURE ----------
# A procedure is a set of steps with a name.
# Rename it to say what it does.
# The parameter (word) is the info you give it.
# Tip: start with  return "test"  and fill it in later.

def my_procedure(word):

    # 1. Check the input. Keep asking if it's not a string or it's blank.
    print(type(word))
    while type(word) != str: #use int for integers
        print("Please enter a word")
        word = input("Type the word: ")

        # ===== YOUR ALGORITHM GOES HERE =====
    # This is the "bottom" of top-down design: the detailed steps.
    # Replace steps 2-4 with your own algorithm.
    # It must use a loop AND an if statement, and the if
    # should depend on the parameter.
    # Ideas: check a quiz answer, add up a score, find the
    # highest number, count matches, filter a list.

    # 2. Make an empty list for the results.
    matches = []

    # 3. Loop through the list.
    for item in my_list: 
        # 4. Decide: does this item contain the user's word?
        if word == item: 
            matches.append(item)

        # ===== END OF YOUR ALGORITHM =====

    # 5. Send the answer back to main().
    return matches


def main(): 

# What this program does:
#   The user types a word. The program searches a list of fruits
#   and shows every fruit that contains that word.
#   To help the user get started, it suggests a random fruit.

    #put code here
    print("Hi there! Welcome to my program!!!")

    word = input("Type a word")

    result = my_procedure(word)

    print(result)


main()