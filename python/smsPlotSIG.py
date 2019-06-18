import ROOT as rt
from array import *
from sms import *
from smsPlotABS import *

# class producing the 2D plot with xsec colors
class smsPlotSIG(smsPlotABS):

    def __init__(self, modelname, histo, obsLimits, expLimits, energy, lumi, preliminary, label):
        self.LABEL = label
        self.standardDef(modelname, histo, obsLimits, expLimits, energy, lumi, preliminary)
        # canvas for the plot
        self.ZLIM = 3
        self.c = rt.TCanvas("cCONT_%s" %label,"cCONT_%s" %label,600,600)
        self.histo = histo['histogram']
        # canvas style
        self.setStyle(logz=False)
        self.setStyleCOLZ()

    # define the plot canvas
    def setStyleCOLZ(self):        
        # set z axis
        self.histo.GetZaxis().SetLabelFont(42)
        self.histo.GetZaxis().SetTitleFont(42)
        self.histo.GetZaxis().SetLabelSize(0.035)
        self.histo.GetZaxis().SetTitleSize(0.035)
        self.histo.SetMinimum(-self.ZLIM)
        self.histo.SetMaximum(self.ZLIM)

        for i in range(self.histo.GetNbinsX()):
            for j in range(self.histo.GetNbinsY()):
                if self.histo.GetBinContent(i+1,j+1)<-self.ZLIM:
                    self.histo.SetBinContent(i+1,j+1,-self.ZLIM)

        # define the palette for z axis
        rt.gStyle.SetPalette(rt.kLightTemperature)
        rt.gStyle.SetNumberContours(255)
        
        self.c.cd()
        self.histo.Draw("colz1")

        rt.gPad.Update()
        palette = self.histo.GetListOfFunctions().FindObject("palette")
        palette.SetX1NDC(1.-0.18)
        palette.SetY1NDC(0.14)
        palette.SetX2NDC(1.-0.13)
        palette.SetY2NDC(1.-0.08)
        palette.SetLabelFont(42)
        palette.SetLabelSize(0.035)

    def DrawPaletteLabel(self):
        textCOLZ = rt.TLatex(0.98,0.5,"Signal Significance")
        textCOLZ.SetNDC()
        textCOLZ.SetTextAlign(21)
        textCOLZ.SetTextFont(42)
        textCOLZ.SetTextSize(0.045)
        textCOLZ.SetTextAngle(90)
        textCOLZ.Draw()
        self.c.textCOLZ = textCOLZ
            
    def Draw(self):
        self.emptyHisto.GetXaxis().SetRangeUser(self.model.Xmin, self.model.Xmax)
        self.emptyHisto.GetYaxis().SetRangeUser(self.model.Ymin, self.model.Ymax)
        # self.emptyHisto.GetZaxis().SetRangeUser(self.model.Zmin, self.model.Zmax)
        self.emptyHisto.GetZaxis().SetRangeUser(-self.ZLIM,self.ZLIM)
        self.emptyHisto.Draw()
        self.histo.Draw("COLZ1 SAME")
        self.DrawLines()
        if self.model.boxOn:
            self.DrawCorridor()
        if self.model.diagOn:
            self.DrawDiagonal()
        self.DrawText()
        self.DrawLegend()
        self.DrawPaletteLabel()
        
