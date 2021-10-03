
#include<iostream>
#include<string>
using namespace std;

class Book{
private:
	string name;
public:
	Book(string name)
	{
		this->name = name;
	}

	friend void display(Book b);
};
void display(Book k)
{
	cout<<"name is : "<<k.name;
}
int main()
{
	Book s("code");
	display(s);
	// cout<<s.name;
}