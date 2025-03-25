#include <stdio.h>
int main() {
  double a,b,c=0;

  scanf("%lf %lf",&a, &b);
  
  c=a/b;

  printf("%.9lf",c);

	return 0;
}