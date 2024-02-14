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

    S = -(5/10*u.log2(5/10)+5/10*u.log2(5/10))
    smoking_entropy = -(5/10)*(4/5*u.log2(4/5)+1/5*u.log2(1/5))-(5/10)*(1/5*u.log2(1/5)+4/5*u.log2(4/5))
    smoking_gain = S - smoking_entropy

    level1["smoking"] = 1
    level1["smoking_info_gain"] = smoking_gain

    cough_entropy = -(7/10)*(4/7*u.log2(4/7)+3/7*u.log2(3/7))-(3/10)*(1/3*u.log2(1/3)+2/3*u.log2(2/3))
    cough_gain = S - cough_entropy
    level1["cough"] = -1
    level1["cough_info_gain"] = -1

    radon_entropy = -(2/10)*(2/2*u.log2(2/2)+0)-(8/10)*(3/8*u.log2(3/8)+5/8*u.log2(5/8))
    radon_gain = S - radon_entropy
    level1["radon"] = -1
    level1["radon_info_gain"] = -1

    weight_entropy = -(5/10)*(3/5*u.log2(3/5)+2/5*u.log2(2/5))-(5/10)*(2/5*u.log2(2/5)+3/5*u.log2(3/5))
    weight_gain = S - weight_entropy
    level1["weight_loss"] = -1
    level1["weight_loss_info_gain"] = -1

    level2_left["smoking"] = -1
    level2_left["smoking_info_gain"] = -1
    level2_right["smoking"] = -1
    level2_right["smoking_info_gain"] = -1

    radon_left_gain = -(4/5)*(3/4*u.log2(3/4)+1/4*u.log2(1/4))-(1/5)*(1/1*u.log2(1/1)+0)
    level2_left["radon"] = 1
    level2_left["radon_info_gain"] = radon_left_gain

    cough_left_gain = -(4/5)*(4/4*u.log2(4/4)+0)-(1/5)*(1/1*u.log2(1/1)+0)
    level2_left["cough"] = -1
    level2_left["cough_info_gain"] = -1

    weight_left_gain = -(3/5)*(2/3*u.log2(2/3)+1/3*u.log2(1/3))-(2/5)*(2/2*u.log2(2/2)+0)
    level2_left["weight_loss"] = -1
    level2_left["weight_loss_info_gain"] = -1

    level2_right["radon"] = -1
    level2_right["radon_info_gain"] = -1

    cough_right_gain = -(2/5)*(1/2*u.log2(1/2)+1/2*u.log2(1/2))-(3/5)*(3/3*u.log2(3/3)+0)
    level2_right["cough"] =-1
    level2_right["cough_info_gain"] = -1

    weight_right_gain = -(2/5)*(2/2*u.log2(2/2)+0)-(3/5)*(1/3*u.log2(1/3)+2/3*u.log2(2/3))
    level2_right["weight_loss"] = 1
    level2_right["weight_loss_info_gain"] = weight_right_gain

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    def construct_tree():
        tree = u.BinaryTree("Tobacco Smoking")
        A = tree.insert_left("Radon Exposure")
        B = tree.insert_right("Weight Loss")
        A.insert_left("n")
        A.insert_right("y")
        B.insert_left("n")
        B.insert_right("y")
        training_error = 6/10
        return tree, training_error

    # Fill up `construct_tree`
    tree, training_error = construct_tree()
    answer["tree"] = tree
    answer["training_error"] = training_error

    return answer

# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    total_entropy = - (.41*u.log2(.41)+.46*u.log2(.46)+.13*u.log2(.13))

    answer["(a) entropy_entire_data"] = total_entropy

    # Info gain
    entropy = -.2*(0+.16/.2*u.log2(.16/.2)+.04/.2*u.log2(.04/.2))-.8*(.41/.8*u.log2(.41/.8)+.3/.8*u.log2(.3/.8)+.09/.8*u.log2(.09/.8))
    answer["(b) x <= 0.2"] = total_entropy - entropy

    entropy = -.7*(.2*u.log2(.2)+.46*u.log2(.46)+.04*u.log2(.04))-.3*(.21*u.log2(.21)+0+.09*u.log2(.09))
    answer["(b) x <= 0.7"] = total_entropy - entropy

    entropy = -.4*(.32*u.log2(.32)+.04*u.log2(.04)+.04*u.log2(.04))-.6*(.09*u.log2(.09)+.42*u.log2(.42)+.09*u.log2(.09))
    answer["(b) y <= 0.6"] = total_entropy - entropy

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = "y<=6"

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("y<=6")
    answer["(d) full decision tree"] = tree

    return answer

print(question2())
# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    gini_a = 1 - ((10/20)**2 + (10/20)**2)
    answer["(a) Gini, overall"] = gini_a

    # float
    answer["(b) Gini, ID"] = 0.

    gini_c = (10/20)*(1-(6/10)**2-(4/10)**2)+(10/20)*(1-(4/10)**2-(6/10)**2)
    answer["(c) Gini, Gender"] = gini_c

    gini_d = (4/20)*(1-(1/4)**2-(3/4)**2)+(8/20)*(1-(0/8)**2-(8/8)**2)+(8/20)*(1-(1/8)**2-(7/8)**2)
    answer["(d) Gini, Car type"] = gini_d

    gini_e = (5/20)*(1-(3/5)**2-(2/5)**2)+(7/20)*(1-(3/7)**2-(4/7)**2)+(4/20)*(1-(2/4)**2-(2/4)**2)+(4/20)*(1-(2/4)**2-(2/4)**2)
    answer["(e) Gini, Shirt type"] = gini_e

    answer["(f) attr for splitting"] = "Car Type"

    # Explanatory text string
    answer["(f) explain choice"] = ("Car type has the lowest gini index and indicates the "
                                    "attribute with the highest purity split. Customer ID technically has "
                                    "the lowest gini, but tells us no information about the Class values "
                                    "because every new record in the table will be assigned a new ID.")

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
    answer["b: explain"] = "There can be zero light."

    answer["c"] = ["discrete", "qualitative", "ordinal"]
    answer["c: explain"] = ""

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
    explain["a"] = "Model 2"
    explain["a explain"] = ("Model 1 is not pruned and is over-fitting the training data, which is why dataset B "
                            "(the testing data) has such a low accuracy compared to the accuracy in Model 2, "
                            "which is pruned and therefore is combating over-fitting.")

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = ("Model 1 is still over-fitting dataset A. Therefore, when tested against both dataset "
                            "A and B combined, the accuracy is much higher because it's so accustomed to the data "
                            "in dataset A. If we were to introduce unseen data, Model 2 would perform better "
                            "than Model 1.")

    explain["c similarity"] = "Both prevent over-fitting."
    explain["c similarity explain"] = ("Both MDL and Pessimistic Error Estimate have some sort of method that "
                                       "discourages a tree to grow complex and over-fit training data and "
                                       "encourages it to stay simple.")

    explain["c difference"] = ("MDL aims mainly at reducing the complexity of the tree whereas Pessimistic Error "
                               "Estimate aims to reduce the error rate through penalties.")
    explain["c difference explain"] = ("MDL wants to create a tree which has the shortest total "
                                       "length of the tree and the smallest training errors. Pessimistic Error "
                                       "Estimate adds penalty terms that increases alongside the complexity of "
                                       "the tree in order to decrease error.")

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
    answer["a, level 2, right"] = ""
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

    entropy = -((10/20)*u.log2(10/20)+(10/20)*u.log2(10/20))
    id_gain = entropy-0
    # float
    answer["a, info gain, ID"] = id_gain

    entropy_left = -((9/10)*u.log2(9/10)+(1/10)*u.log2(1/10))
    entropy_right = -((1/10)*u.log2(1/10)+(9/10)*u.log2(9/10))
    weighted_entropy_subsets = (10/20)*entropy_left+(10/20)*entropy_right
    h_gain = entropy-weighted_entropy_subsets
    answer["b, info gain, Handedness"] = h_gain

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"

    info = -20*(1/20*u.log2(1/20))
    id_gain_ratio = id_gain / info
    # answer is a float
    answer["d, gain ratio, ID"] = id_gain_ratio

    info = -(10/20*u.log2(10/20)+10/20*u.log2(10/20))

    h_gain_ratio= h_gain/info
    answer["e, gain ratio, Handedness"] = h_gain_ratio

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

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
