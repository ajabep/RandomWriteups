#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define NB_CHALLS 100

int main() {
	unsigned int i = 0;
	setvbuf(stdout, NULL, _IONBF, 0);

	puts("AAABAACAADAAEAAFAAGAAHAAIAAJAAKAALAAMAANAAOAAPAAQAARAASAATAAUAAVAAWAAXAAYAAZAAaAAbAAcAAdAAeAAfAAgAAhAAiAAjAAkAAlAAmAAnAAoAApAAqAArAAsAAtAAuAAvAAwAAxAAyAAzAA1AA2AA3AA4AA5AA6AA7AA8AA9AA0ABBABCABDABEABFABGABHABIABJABKABLABMABNABOABPABQABRABSABTABUABVABWABXABYABZABaABbABcABdABeABfABgABhABiABjABkABlABmABnABoABpABqABrABsABtABuABvABwABxAByABzAB1AB2AB3AB4AB5AB6AB7AB8AB9AB0ACBACCACDACEACFACGACHACIACJACKACLACMACNACOACPACQACRACSACTACUACVACWACXACYACZACaACbACcACdACeACfACgAChACiACjACkAClACmACnACoACpACqACrACsACtACuACvACwACxACyACzAC1AC2AC3AC4AC5AC6AC7AC8AC9AC0ADBADCADDADEADFADGADHADIADJADKADLADMADNADOADPADQADRADSADTADUADVADWADXADYADZADaADbADcADdADeADfADgADhADiADjADkADlADmADnADoADpADqADrADsADtADuADvADwADxADyAAAA");

	srand(0x41414141);

	for (i = 0 ; i < NB_CHALLS ; ++i) {
		printf("%d\n", rand());
	}

	return 0;
}
