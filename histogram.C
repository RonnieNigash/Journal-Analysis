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
	Tree->Print();
	Int_t numEvents = Tree->GetEntries();
	Tree->Draw("words:day");
}
