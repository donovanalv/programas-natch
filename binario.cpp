#include <iostream>
using namespace std;
int main(){
	int num;
	cout<< "Dime un numero del 1-9: ";
	cin>>num;
	if(num == 1){
		cout<<"1 ---> 0001";
	}
	else if (num == 2){
		cout<<"2 ---> 0010";
	}
	else if(num == 3){
		cout<<"3 ---> 0011";
	}
	else if(num == 4){
		cout<<"4 ---> 0100";
	}
	else if(num == 5){
		cout<<"5 ---> 0101";
	}
	else if(num == 6){
		cout<<"6 ---> 0110";
	}
	else if(num == 7){
		cout<<"7 ---> 0111";
	}
	else if(num == 8){
		cout<<"8 ---> 1000";
	}
	else if(num == 9){
		cout<<"9 ---> 1001";
	}
	else{
		cout<<"Error";
	}
}
