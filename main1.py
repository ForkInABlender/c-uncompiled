import cppyy
from ctypes import CFUNCTYPE, c_int
cppyy.cppdef("""extern "C" {
	int (*m)(int);
}
int m2(int c){
	return m(c);
}""")

m_data = 0x1000
@CFUNCTYPE(c_int, c_int)
def add_int_py(i):
	return m_data + i

cppyy.cppdef("""class MyClass {
public:
    MyClass(int i) : m_data(i) {}
    virtual ~MyClass() {}
    virtual int add_int(int i) { return m_data + i; }
    int m_data;
};""")

class x(cppyy.gbl.MyClass):
	pass

cppyy.gbl.m = add_int_py
print(cppyy.gbl.m2(-3))
