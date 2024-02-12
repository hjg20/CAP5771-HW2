# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u
import pandas as pd

# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    
    df = pd.DataFrame()
    df['Tobacco Smoking'] = ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No']
    df['Radon Exposure'] = ['Yes', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No']
    df['Chronic Cough'] = ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No']
    df['Weight Loss'] = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes']
    df['Lung Cancer'] = ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'No']
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}
    
    # Total Entropy of Table
    class_counts = df['Lung Cancer'].value_counts()
    total_samples = df.shape[0]
    H = 0
    for count in class_counts:
        probability = count / total_samples
        H -= probability * u.log2(probability)
        
    def information_gain(attribute):
        categories = df[attribute].unique()
        conditional_entropies = {}
        for category in categories:
            subset = df[df[attribute] == category]['Lung Cancer']
            counts = subset.value_counts()
            entropy = 0
            for count in counts:
                probability = count / counts.sum()
                entropy -= probability * u.log2(probability)
            conditional_entropies[category] = entropy
        weighted_entropy = 0
        for category, entropy in conditional_entropies.items():
            weight = df[df[attribute] == category].shape[0] / total_samples
            weighted_entropy += weight * entropy
        information_gain = H - weighted_entropy
        return information_gain


    level1["smoking"] = 0.
    level1["smoking_info_gain"] = information_gain("Tobacco Smoking")

    level1["cough"] = 0.
    level1["cough_info_gain"] = information_gain("Chronic Cough")

    level1["radon"] = 0.
    level1["radon_info_gain"] = information_gain("Radon Exposure")

    level1["weight_loss"] = 0.0
    level1["weight_loss_info_gain"] = information_gain("Weight Loss")

    level2_left["smoking"] = 0.
    level2_left["smoking_info_gain"] = 0.
    level2_right["smoking"] = 0.
    level2_right["smoking_info_gain"] = 0.

    level2_left["radon"] = 0.
    level2_left["radon_info_gain"] = 0.

    level2_left["cough"] = 0.
    level2_left["cough_info_gain"] = 0.

    level2_left["weight_loss"] = 0.
    level2_left["weight_loss_info_gain"] = 0.

    level2_right["radon"] = 0.
    level2_right["radon_info_gain"] = 0.

    level2_right["cough"] = 0.
    level2_right["cough_info_gain"] = 0.

    level2_right["weight_loss"] = 0.
    level2_right["weight_loss_info_gain"] = 0.

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    tree = u.BinaryTree("root")  # MUST STILL CREATE THE TREE *****
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0  

    return answer

print(question1())
# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    total_entropy = -(2/6)*u.log2(2/6)-(2/6)*u.log2(2/6)-(2/6)*u.log2(2/6)
    
    answer["(a) entropy_entire_data"] = 0.
    # Infogain
    answer["(b) x <= 0.2"] = 0.
    answer["(b) x <= 0.7"] = 0.
    answer["(b) y <= 0.6"] = 0.

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = ""  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("Root")
    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}


    # float
    gini_a = 1 - (.5)**2 - (.5)**2
    answer["(a) Gini, overall"] = gini_a

    # float
    answer["(b) Gini, ID"] = 0.0
    
    gini_c = .5*(1-2*.5**2)+.5*(1-2*.5**2)
    answer["(c) Gini, Gender"] = gini_c
    
    answer["(d) Gini, Car type"] = 0.
    answer["(e) Gini, Shirt type"] = 0.

    answer["(f) attr for splitting"] = ""

    # Explanatory text string
    answer["(f) explain choice"] = ""

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ["binary", "qualitative", "nominal"]

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = "Only two options, AM or PM, makes it binary."

    answer["b"] = ["continuous", "quantitative", "ratio"]
    answer["b: explain"] = ""

    answer["c"] = ["discrete", "qualitative", "ordinal"]
    answer["c: explain"] = "If people are choosing from a finite number of options."

    answer["d"] = ["continuous", "quantitative", "ratio"]
    answer["d: explain"] = ""

    answer["e"] = ["discrete", "qualitative", "ordinal"]
    answer["e: explain"] = ""

    answer["f"] = ["continuous", "quantitative", "ratio"]
    answer["f: explain"] = "There can be a zero point of 0 feet above sea level."

    answer["g"] = ["discrete", "quantitative", "ratio"]
    answer["g: explain"] = ""

    answer["h"] = ["discrete", "qualitative", "ordinal"]
    answer["h: explain"] = "Books in the library are ordered by their ISBN."

    answer["i"] = ["discrete", "qualitative", "ordinal"]
    answer["i: explain"] = "There is order by the level of light coming through."

    answer["j"] = ["discrete", "qualitative", "ordinal"]
    answer["j: explain"] = ""

    answer["k"] = ["continuous", "quantitative", "ratio"]
    answer["k: explain"] = ""

    answer["l"] = ["continuous", "quantitative", "interval"]
    answer["l: explain"] = "There is no known substance with zero mass, therefore there is no zero point for density."

    answer["m"] = ["discrete", "qualitative", "ordinal"]
    answer["m: explain"] = "There is an order because people who get coats checked first have lower numbers."

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = ""
    explain["a explain"] = ""

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = ""
    explain["b explain"] = ""

    explain["c similarity"] = ""
    explain["c similarity explain"] = ""

    explain["c difference"] = ""
    explain["c difference explain"] = ""

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = ""
    answer["a, level 2, right"] =""
    answer["a, level 2, left"] = ""
    answer["a, level 3, left"] = ""
    answer["a, level 3, right"] = ""

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("root note")

    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 0.
    answer["b, info gain, Handedness"] = 0.

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = ""

    # answer is a float
    answer["d, gain ratio, ID"] = 0.
    answer["e, gain ratio, Handedness"] = 0.

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = ""

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

