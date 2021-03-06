#include "stdafx.h"
#include <vector>
#include <iostream>

template <typename T>
void displayVector(std::vector<T> vec)
{
	std::cout << "[";
	for (std::vector<int>::iterator it = vec.begin(); it != vec.end(); ++it)
	{
		std::cout << *it << " ";
	}
	std::cout << "]\n";
}

template <typename T>
void sort(std::vector<T> &toSort) {
	int lastToCheck = toSort.size() - 1;
	while (lastToCheck >= 0)
	{
		for (int i = 0; i < lastToCheck; i++) 
		{
			if (toSort[i] > toSort[i + 1])
			{
				T temp = toSort[i];
				toSort[i] = toSort[i + 1];
				toSort[i + 1] = temp;
			}
		}
		lastToCheck--;
	}
}

void test1()
{
	std::vector<int> testVector = std::vector<int>();
	testVector.push_back(4);
	testVector.push_back(1);
	sort(testVector);
	displayVector(testVector);
}

void test2()
{
	std::vector<int> testVector = std::vector<int>();
	testVector.push_back(4);
	testVector.push_back(1);
	testVector.push_back(2);
	testVector.push_back(9);
	testVector.push_back(7);
	testVector.push_back(2);
	testVector.push_back(4);
	testVector.push_back(1);
	sort(testVector);
	displayVector(testVector);
}

void test3()
{
	std::vector<int> testVector = std::vector<int>();
	testVector.push_back(4);
	sort(testVector);
	displayVector(testVector);
}

void test4()
{
	std::vector<int> testVector = std::vector<int>();
	sort(testVector);
	displayVector(testVector);
}

int main()
{
	test1();
	test2();
	test3();
	test4();
	char c;
	std::cin >> c;
    return 0;
}

