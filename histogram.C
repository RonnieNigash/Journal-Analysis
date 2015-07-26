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
	graph = new TGraph(200, &words, &day);
	// Get the total number of words written and print out to CLI
	Tree->Print();
	Int_t numEntries = (Int_t)(Tree->GetEntries());
	TBranch *wordsBranch = Tree->GetBranch("words");
	for(Int_t i = 0; i < numEntries; i++) {
		Tree->GetEntry(i, 0);
	}
	// Draw the Tree (words vs. day) on canvas
	Tree->SetEstimate(Tree->GetEntries());
	Tree->Draw("words:day");
	// Have to loop back through drawn tree to get values and count number of words total
	Float_t numWords = 0.0;
	Double_t *array = Tree->GetV1();
	for (Int_t i = 0; i < numEntries; i++) {
		numWords += array[i];
	}
	cout << numWords << endl;
}
