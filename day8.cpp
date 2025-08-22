#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

string reverseWords(string s) {
    stringstream ss(s);
    string word;
    vector<string> words;


    while (ss >> word) {
        words.push_back(word);
    }

    
    reverse(words.begin(), words.end());


    string result;
    for (int i = 0; i < words.size(); i++) {
        result += words[i];
        if (i != words.size() - 1) result += " ";
    }
    return result;
}

int main() {
    string input;
    cout << "Enter a string: ";
    getline(cin, input);

    string output = reverseWords(input);
    cout << "Reversed string: " << output << endl;

    return 0;
}
