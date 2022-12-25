#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <cstddef>



using namespace std;

/************************/
#include "./python3.8/Python.h"
/************************/


/**
* This is an example of a c/c++ version of a few java interfaces inside of a c/c++ interpreter. 
*  This were transcribed from java code to c/c++. The CPPYY c++ cling embedding in python can interpret
*  what should have been java class code run on the JVM. Note that their will be no garbage collector if
*  one has each class destructor defined correctly.
* 
* The reason to use CPPYY with translated java code is that it will run all the same as if it were compiled
*  down into a binary. The fact that this even works is moreover the part that peaked my interests.
* And the reason to run ones code through the two websites below to get c/c++ code is because it will run directly in c/c++, it is faster, and contains
*  less overhead and less code. The second reason to do this is so that one no longer needs as many header files. The third reason is because it cuts 
* down the boilerplate & bloatware.
* 
* This also reduces the number of errors one can make. Once you've figured out what it's telling you when it fails to execute, debugging gets easier than
*  standard java programming. 
* 
* 
* 
* 
* 
* 
* 
*/

namespace java {
    namespace io {
        class Serializable{
			public:
            Serializable() {}
        };
    }
	namespace lang{
		namespace reflect{
			class Type{};
			class GenericDeclaration{};
			class TypeVariable: Type{
				public:
					virtual ~TypeVariable() = 0;
					vector<java::lang::reflect::Type*> getBounds();
					java::lang::reflect::GenericDeclaration* getGenericDeclaration();
          			string getName();
			};
		}
	}
}

class AnnotatedElement{};

using namespace java::io;
using namespace java::lang::reflect;

template<typename T>
const class Class: Serializable, GenericDeclaration, Type, AnnotatedElement {
	private:
		static const int ANNOTATION = 0x00002000;
    	static const int ENUM = 0x00004000;
    	static const int SYNTHETIC = 0x00001000;
		static void registerNatives();
		string name;
    	virtual string getName0() = 0;
	public:
		string toString(); // java::lang::String*
    	bool isInterface();
    	bool isPrimitive();
		string getName(){
        	string name = this->name;
        	if (name.empty()){ // == null/NULL --> .empty() on string type
            	this->name = name = getName0();
        	}
        	return name;
    	}
};

TypeVariable::~TypeVariable() {};
