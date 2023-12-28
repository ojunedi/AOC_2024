#include<iostream>
#include<fstream>
#include<set>
#include<unordered_map>
using namespace std;



class Solver {


    private:

        set<string> partial_words = {
            "on", 
            "tw",
            "th",
            "thr",
            "thre",
            "fo",
            "fou",
            "fi",
            "fiv",
            "si",
            "se",
            "sev",
            "seve",
            "ei",
            "eig",
            "eigh",
            "ni",
            "nin",
            "o", 
            "t",
            "f",
            "s",
            "e",
            "n"
        };
        set<string> full_words = {
            "one",
            "two", 
            "three",
            "four", 
            "five",
            "six",
            "seven", 
            "eight",
            "nine"
        };
        unordered_map<string, string> words_to_digit = {
            {"one", "1"},
            {"two", "2"},
            {"three", "3"},
            {"four", "4"},
            {"five", "5"},
            {"six", "6"},
            {"seven", "7"},
            {"eight", "8"},
            {"nine", "9"},
        };


    public:


        int solve_part_1() {

            fstream fin;
            fin.open("input.txt");
            string line;
            int res = 0;
            
            while (fin >> line) {
                string calibration_value = "";

                for (size_t i = 0; i < line.size(); i++) {
                    if (isdigit(line[i])) {
                        calibration_value += line[i];
                        break;
                    }
                }

                for (size_t j = line.size() - 1; j >= 0; --j) {
                    if (isdigit(line[j])) {
                        calibration_value += line[j];
                        break;
                    }
                }
                res += stoi(calibration_value);

            }

            return res;

        }




        bool starts_digit(char c) {
            return (c == 'o' || c == 't' || c == 'f' || c == 's' || c == 'e' || c == 'n');
        }


        string promising_word(string line, string word, size_t j) {

            size_t n = line.size();
            string res = "";

            while (partial_words.find(word) != partial_words.end() && j < n - 1) {
                word += line[++j];
            }
            
            if (full_words.find(word) != full_words.end()) {
                res = words_to_digit[word];
            }


            return res;

            
        }


        int solve_part_2() {


            fstream fin;
            fin.open("input.txt");
            string line;
            int res = 0;

            while (fin >> line) {

                string calibration_value = "";
                size_t index_of_first_digit = 0;

                // first digit of calibration value
                for (size_t i = 0; i < line.size(); ++i) {

                    if (isdigit(line[i])) {
                        calibration_value += line[i];
                        index_of_first_digit = i;
                        break;
                    }
                    else if (starts_digit(line[i])) {
                        string word = "";
                        word += line[i];
                        word = promising_word(line, word, i);
                        if (word != "") {
                            calibration_value += word;
                            index_of_first_digit = i;
                            break;
                        }
                    }
                }
                string second_value;
                for (size_t j = index_of_first_digit; j < line.size(); ++j) {

                    if (isdigit(line[j])) {
                        second_value = line[j];
                    }
                    else if (starts_digit(line[j])) {
                        string word = "";
                        word += line[j];
                        word = promising_word(line, word, j);
                        if (word != "") {
                           second_value = word;
                        }
                    }
                }

                calibration_value += second_value;
                res += stoi(calibration_value);
            }

            return res;
        }

        };




int main() {


    Solver s;
    cout << s.solve_part_1() << endl;
    cout << s.solve_part_2() << endl;


    return 0;

}