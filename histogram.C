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
					
	Tree->ReadFile(Form("/users/ronnie/git/Journal-Analysis/data.txt"), "month:date:day:words");
 	Tree->Draw("day:words");
	Tree->Write();
	
}
