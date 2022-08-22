#include <fstream>
#include <iostream>
using namespace std;

void create()
{
    // file pointer
    fstream fout;
  
    // opens an existing csv file or creates a new file.
    fout.open("reportcard.csv"); //, ios::out | ios::app);
    cout << "Enter the details of 3 students:"
         << " name maths phy "
    << endl;
  
    int i, phy, chem, math, bio;
    string name;
  
    // Read the input
    for (i = 0; i < 3; i++) {
  
        cin >> name
            >> math
            >> phy;
  
        // Insert the data to file
        fout << name << ", "
             << math << ", "
             << phy
             << "\n";
    }
}