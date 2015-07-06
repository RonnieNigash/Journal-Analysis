#include "Riostream.h"
void histogram() {
	// Read data from ASCII file and create histogram/ntuple combo
	ifstream in;
 	in.open("/users/ronnie/git/Journal-Analysis/data.txt");

	Text_t month;
 	Float_t date, day, words;
	TFile *file = new TFile("histogramTest.root", "CREATE");
	TH1F *histo = new TH1F("histo", "writing distribution", 100, 0, 2);
	TTree *Tree = new TTree("ntuple", "data from file");
					
	Tree->ReadFile(Form("/users/ronnie/git/Journal-Analysis/Daily Journals/data.txt"), "month:date:day:words");
	graph = new TGraph(180, &words, &day);
	// Get the total number of words written and print out to CLI
	Tree->Print();
	Int_t numEntries = (Int_t)(Tree->GetEntries());
	Int_t numWords = 0;
	TBranch *wordsBranch = Tree->GetBranch("words");
	for(Int_t i = 0; i < numEntries; i++) {
		Tree->GetEntry(i, 0);
//		cout << GetValue() << endl;
	}
	// Draw the Tree (words vs. day) on canvas
	Tree->Draw("words:day");
}
