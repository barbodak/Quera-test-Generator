import os


def gen_case(case_number_str, input_str, output_str):
    # writes the given string int the input and output txt files
    input_file = open(os.path.join("in", "input") + case_number_str + ".txt", "w")
    input_file.write(input_str)
    input_file.close()
    output_file = open(os.path.join("out", "output") + case_number_str + ".txt", "w")
    output_file.write(output_str)
    output_file.close()


def init_test_gen():
    # removes if previous tests exiested otherwise generates the in and out folders
    if os.path.exists("in"):
        for file in os.listdir("in"):
            os.remove(os.path.join("in", file))
    else:
        os.mkdir("in")

    if os.path.exists("out"):
        for file in os.listdir("out"):
            os.remove(os.path.join("out", file))
    else:
        os.mkdir("out")


init_test_gen()
# here wrete code that creates your samples as a string then put them into
# files using gen_case function.
