#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define DIFF_TIME 0 /* sometimes, we can have some second of difference. */
#define NB_CHALLS 100

int main() {
	unsigned int i = 0;
	int mytime = time(0);
	int srvtime = 0;
	int seed = 0;
	setvbuf(stdout, NULL, _IONBF, 0);

	puts("username");

	scanf("%d", &srvtime);

	srvtime = (srvtime * 10000) + (mytime % 10000);
	srvtime -= DIFF_TIME;
	fprintf(stderr, "my time=%1$d=0x%1$x\n", mytime);
	fprintf(stderr, "real srv time=%1$d=0x%1$x\n", srvtime);

	seed = srvtime / 10;
	fprintf(stderr, "Seed=%1$d=0x%1$x\n", seed);

	srand(seed);

	for (i = 0 ; i < NB_CHALLS ; ++i) {
		printf("%d\n", rand());
	}

	return 0;
}
