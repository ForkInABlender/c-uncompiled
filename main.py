import cppyy
from keystone.keystone import Ks
from keystone.keystone_const import KS_ARCH_X86, KS_MODE_64
from mmap import mmap, PAGESIZE, PROT_READ, PROT_WRITE, PROT_EXEC
from ctypes import c_int, c_void_p, addressof, CFUNCTYPE

def AssemblyFunction(i):
	ks=Ks(KS_ARCH_X86, KS_MODE_64)
	encoding, count = ks.asm(i) 
	del ks, count, i
	return bytes(encoding)

cppyy.cppdef("""
extern "C" {
	int (*f)(int);
}

int main(void) {
	return f(42);
}
""")

buf = mmap(-1, PAGESIZE, prot=PROT_READ|PROT_WRITE|PROT_EXEC)

buf.write(AssemblyFunction(b"""
  mov eax, edi
  add eax, 1
  ret
"""))

cppyy.gbl.f=CFUNCTYPE(c_int, c_int)(addressof(c_void_p.from_buffer(buf)))
print(cppyy.gbl.main())
buf.close()
