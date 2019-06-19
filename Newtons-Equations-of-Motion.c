#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(int argc, char **argv)
{
	int ti = 0;
	int tf = atoi(argv[2]);

	double q0 = 1.34;
	double p0 = 2.5;


	FILE *fp = fopen("out.csv","w");

	double qc = q0;
	double pc = p0;

	double m = 3;

	double Hc = 2*qc + pc*pc/m*0.5;

	for (ti = atoi(argv[1]) ; ti <= tf; ++ti)
	{
		fprintf(fp, "%d,%15.10f,%15.10f,%15.10f\n",ti,qc,pc,Hc);
		double F = -2;
		pc += F * (float) ti;
		double v = pc / m;
		qc += v * (float) ti;
		Hc = 2*qc + pc*pc/m*0.5;
	}

	fclose(fp);
	return 0;
}
