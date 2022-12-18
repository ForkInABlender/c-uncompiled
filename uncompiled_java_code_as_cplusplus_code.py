import cppyy

"""

Please, do not be fooled into thinking this is c/c++ code by default. it is c/c+ code, but a transpiled version of java-code. Please, don't confuse it 
 for jvm jni code. It isn't and bypasses even needing javac.

Why compile what runs, much less something disguised as something else?


https://www.javainuse.com/java2cpp
https://kalkicode.com/ai/java-to-cplusplus-converter-online

"""


cppyy.cppdef("""
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class m {
    public:
        static void main(vector<string> args) {
    		int i = 0;
    		for (string a : args) {
        		cout << i + 1 << " " << a << endl;
        		i++;
    		}
		}
	//
};
""")

cppyy.gbl.m.main(__import__("sys").argv)
