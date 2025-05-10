#include<stdio.h>
int balance=0; //Global Variables
int n1=0;
int n2=0;
//Function Check for Balance checking
void Check(){
	FILE *fp;
	fp=fopen("Bank.txt","w");
	if(fp==NULL){
		printf("Unable to open!");
	}
	printf("Yours Current Balance is Rs.%d",balance);
	fprintf(fp,"U had Deposited [%d] times. :)",n1);
	fprintf(fp,"\nU had Withdrew [%d] times. :(",n2);
	fprintf(fp,"\nTotal Transactions = %d.",n1+n2);
	fprintf(fp,"\nYours Current Balance is Rs.%d",balance);
}

//Function Deposit for Money Deposit
void Deposit(){
	int depo;
	printf("Enter the Amounts u wanna deposit=Rs.");
	scanf("%d",&depo);
while(1){
	if(depo<=0){
	printf("Plz enter the amounts > 0");
	printf("\nEnter the Amounts u wanna deposit again =Rs.");
	scanf("%d",&depo);
}
else{
		printf("You have deposited Rs.%d",depo);
		balance+=depo;
		n1+=1; //For Counting the Deposit's Transaction
		printf("\nYours Account's Balance has been Updated. :)");
		break;
}
   }
}

//Function Withdraw for Money Withdraw
void Withdraw(){
	int withd;
	printf("Enter the amounts u wanna Withdraw= Rs.");
	scanf("%d",&withd);
while(1){
  if(withd<=0 || withd>balance){
	printf("Enter the valid amounts!");
	printf("\nEnter the amounts u wanna Withdraw again = Rs. ");
	scanf("%d",&withd);
	}
  else{
			printf("You've withdrawn Rs.%d",withd);
			balance-=withd;
			n2+=1; //For Counting the Withdraw's transaction
			printf("\nYours Account's Balance has been updated. :(");
			break;
		}
 }
}

//Main function section	
int main(){
	int n,i,j;
	char name[40];
	printf("What's your Name ?\nPlzz Enter your Name : ");
	scanf("%[^\n]",name);
	printf("Nice to Meet u :) Mr/Mrs.%s\n\n\n",name);
	printf("*************************Bank's simulation*************************:");
	printf("\n\t\t1. Balance check");
	printf("\n\t\t2. Money Deposit");
	printf("\n\t\t3. Money withdraw");
	printf("\n\t\t4. Exit");
while(1){
	printf("\n\nChoose a number (1-4)[1:Balance_Check 2:Money_Deposit 3:Money_Withdraw 4:Exit] for Transaction:");
	scanf("%d",&n);
  if(n>0&&n<5){
		if(n==1)
		Check();
		else if(n==2)
		Deposit();
		else if(n==3)
		Withdraw();
		else if(n==4){
		printf("\n");
		printf("\nYour Account's New-Updated Balance has been saved in a file.\n\n");
		for(i=1;i<3;i++){
			for(j=1;j<11;j++){
				if(i==2){
					if(j==10){
						printf("\n");
						printf("\t\t\t");
						printf("Byee %s",name);	
				}
					else{
						printf("\n");
						printf("\t\t\t");
						printf("Byee");	
				}
			}
				else{
					printf("Byee ");
				}
			}
		}
		printf("\n\n*************************Visit Again*************************");
		break;
	}
		
	}
  else{
		printf("Plz enter Valid number(1-4)");
	}
}
	return 0;
}
