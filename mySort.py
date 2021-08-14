import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation, PillowWriter
import algorithms
from randomInput import randomInput
from txtInput import readFile
from ascendingInput import ascInput

# Main Program
elements = int(input("Enter the number of elements:"))
values = []

methodChoice = int(input("Input Type:\n 1.Random \n 2.Ascending to Element Amount(1,2,...) \n 3.Text File \n "
                         "4.Commandline Input \n "))
if (methodChoice == 1):
    values = randomInput(elements)
elif (methodChoice == 2):
    values = ascInput(elements)
elif (methodChoice == 3):
    values = readFile(elements)
elif (methodChoice == 4):
    print("List of all elements to sort, separated with a space")
    values = input("Values: ").split(" ")
    for i in range(elements):
        values[i] = int(values[i])
    print(values)
else:
    randomInput(elements)

# Let user choose an algorithm to visualize
algorithm = int(input("Pick an Algorithm:  \n 1.Bubble Sort \n 2.Selection Sort \n 3.Insertion Sort \n 4.Bucket Sort "
                      "\n 5.Heap Sort \n 6.Shell Sort \n 7.Quick Sort \n"))

# Algo is a generator object containing all the states of the array during the sort, these will be frames in the animation
if (algorithm == 1):
    title = "Bubble Sort"
    algo = algorithms.bubbleSort(values)
elif (algorithm == 2):
    title = "Selection Sort"
    algo = algorithms.selectionSort(values)
elif (algorithm == 3):
    title = "Insertion Sort"
    algo = algorithms.insertionSort(values)
elif (algorithm == 4):
    title = "Bucket Sort"
    algo = algorithms.bucketSort(values, elements)
elif (algorithm == 5):
    title = "Heap Sort"
    algo = algorithms.heapSort(values)
elif (algorithm == 6):
    title = "Shell Sort"
    algo = algorithms.shellSort(values, elements)
elif (algorithm == 7):
    title = "Quick Sort"
    algo = algorithms.quickSort(values, 0, (elements - 1 ))

# Create the Figure
figure, axis = plt.subplots()
axis.set_title(title)

#Settings
text = axis.text(0.02, 0.95, "", transform=axis.transAxes)
bar_sub = axis.bar(range(len(values)), values, align="edge", color="#ae24d1")
axis.set_xlim(0, elements)
axis.set_ylim(0, max(values))
axis.axhline(0, color='grey', linewidth=0.8)

# Will keep track of how many times values are compared to another
comparisons = [0]


# Helper Function
def update(values, rectangles, comparisons):
    # updates each frame in the plot on the graph
    # pairs each bar with its value from the array and updates as it is being organized
    for rect, val in zip(rectangles, values):
        rect.set_height(val)
        # plt.text((rect.get_x() + rect.get_width() / 2), val, val)
        # axis.text(val, 0.005, val, ha='center', weight='bold')
    comparisons[0] += 1
    text.set_text(("Frames:", comparisons))

# Creating animation object
DSanimation = animation.FuncAnimation(
    figure,
    func=update,
    fargs=(bar_sub, comparisons),
    frames=algo,
    repeat=False,
    blit=False,
    interval=15,
    save_count=90000,
)

# gifTitle = title+"_demoGIF.gif"
# writer = PillowWriter(fps=15)
# DSanimation.save(gifTitle, writer=writer)

# for showing the animation on screen
plt.show()

plt.close()

