import FWCore.ParameterSet.Config as cms

hgcaltbdigisplotter = cms.EDAnalyzer("DigiPlotter",
                                     pedestalsHighGain=cms.untracked.string("CondObjects/data/Ped_HighGain_OneLayer_1.txt"),
                                     pedestalsLowGain=cms.untracked.string("CondObjects/data/Ped_LowGain_OneLayer_1.txt")
                                     )
hgcaltbdigisplotter_new = cms.EDAnalyzer("DigiPlotter_New")
hgcaltbdigisplotter_ped = cms.EDAnalyzer("DigiPlotter_Ped")
