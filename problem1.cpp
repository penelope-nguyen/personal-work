#include <iostream>
using namespace std; 

// Given a list of array size n, replace each element in the with the product of all other elements in the array.  
// Constraints are that division must not be used and the algorithm must have O(n). 
// My solution is 3n + c = O(n). 

int main() { 
	
	int size; 
	int * fixedArray;
	int * previousProducts; 
	int * nextProducts;  
	int lastPos = size - 1;
	int firstPos = 0;
	int secondPos = firstPos + 1;
	int secondToLastPos = lastPos - 1;
	cout << "How many numbers would you like in the array? ";
	cin >> size;

	cout << "Please enter your numbers: \n";
	for (int i = 0; i < size; i++) {
		cin >> fixedArray[i];
	}

	cout << endl;

	fixedArray = new int[size];
	previousProducts = new int[size]; 
	nextProducts = new int[size];

	previousProducts[firstPos] = 1;
	nextProducts[lastPos] = 1;

	for (int forward = secondPos; forward <= lastPos; forward++) {
		previousProducts[forward] = fixedArray[forward - 1] * previousProducts[forward - 1];
	}

	for (int backward = secondToLastPos; backward >= firstPos; backward--) {
		nextProducts[backward] = fixedArray[backward +1] * nextProducts[backward + 1];
	}

	cout << "The results are: " << endl;

	for (int pos = 0; pos < size; k++) {
		fixedArray[pos] = previousProducts[pos] * nextProducts[pos];
		cout << fixedArray[pos] << " ";
	}

	cout << endl;

	// This is a preliminary implementation of the code, with a fixed array size. 

	/*

	int fixedArray[5] = { 3, -1, -3, 2, -1};
	int goingForward[5];
	goingForward[0] = 1; // set the first element equal to 1 
	int  goingBackwards[5];
	goingBackwards[4] = 1; // set last element to 1 
	for (int i = 1; i <= 4; i++) {
		goingForward[i] = fixedArray[i - 1] * goingForward[i - 1];
	}

	for (int j = 3; j >= 0; j--) {
		goingBackwards[j] = fixedArray[j + 1] * goingBackwards[j + 1]; 
	}

	for (int i = 0; i < 5; i++) {
		fixedArray[i] = goingForward[i] * goingBackwards[i];
		cout << fixedArray[i] << " ";
	}

	*/ 
	
	system("pause");
	return 0;
}