import ROOT as rt
from array import *
from sms import *
from color import *
from math import atan, pi
import CMS_lumi
class smsPlotABS(object):
    # modelname is the sms name (see sms.py)
    # histo is the 2D xsec map
    # obsLimits is a list of opbserved limits [NOMINAL, +1SIGMA, -1SIGMA]
    # expLimits is a list of expected limits [NOMINAL, +1SIGMA, -1SIGMA]
    # label is a label referring to the analysis (e.g. RA1, RA2, RA2b, etc)

    def __init__(self, modelname, histo, obsLimits, expLimits, energy, lumi, preliminary, label):
        self.standardDef(modelname, histo, obsLimits, expLimits, energy, lumi, preliminary)
        self.LABEL = label
        self.c = rt.TCanvas("cABS_%s" %label,"cABS_%s" %label,300,300)
        self.histo = histo

    def standardDef(self, modelname, histo, obsLimits, expLimits, energy, lumi, preliminary):
        # which SMS?
        self.model = sms(modelname)
        self.OBS = obsLimits
        self.EXP = expLimits
        self.lumi = lumi
        self.energy = energy
        self.preliminary = preliminary
        # create the reference empty histo
        self.emptyhisto = self.emptyHistogramFromModel()

    def emptyHistogramFromModel(self):
        self.emptyHisto = rt.TH2D("emptyHisto"+self.LABEL, "", 1, self.model.Xmin, self.model.Xmax, 
                                  1, self.model.Ymin, self.model.Ymax)
        
    # define the plot canvas
    def setStyle(self, logz=True):
        # canvas style
        rt.gStyle.SetOptStat(0)
        rt.gStyle.SetOptTitle(0)        

        self.c.SetLogz(logz)
        self.c.SetTickx(1)
        self.c.SetTicky(1)

        self.c.SetRightMargin(0.19)
        self.c.SetTopMargin(0.08)
        self.c.SetLeftMargin(0.14)
        self.c.SetBottomMargin(0.14)

        # set x axis
        self.emptyHisto.GetXaxis().SetLabelFont(42)
        self.emptyHisto.GetXaxis().SetLabelSize(0.032)
        self.emptyHisto.GetXaxis().SetLabelOffset(0.01)
        self.emptyHisto.GetXaxis().SetTitleFont(42)
        self.emptyHisto.GetXaxis().SetTitleSize(0.045)
        self.emptyHisto.GetXaxis().SetTitleOffset(1.2)
        self.emptyHisto.GetXaxis().SetTitle(self.model.sParticle)
        #self.emptyHisto.GetXaxis().CenterTitle(True)

        # set y axis
        self.emptyHisto.GetYaxis().SetLabelFont(42)
        self.emptyHisto.GetYaxis().SetLabelSize(0.032)
        self.emptyHisto.GetYaxis().SetTitleFont(42)
        self.emptyHisto.GetYaxis().SetTitleSize(0.045)
        self.emptyHisto.GetYaxis().SetTitleOffset(1.48)
        self.emptyHisto.GetYaxis().SetTitle(self.model.LSP)
        #self.emptyHisto.GetYaxis().CenterTitle(True)
                
    def DrawText(self):
        #redraw axes
        self.c.RedrawAxis()
        # white background
        graphWhite = rt.TGraph(5)
        graphWhite.SetName("white")
        graphWhite.SetTitle("white")
        graphWhite.SetFillColor(rt.kWhite)
        graphWhite.SetFillStyle(1001)
        graphWhite.SetLineColor(rt.kBlack)
        graphWhite.SetLineStyle(1)
        graphWhite.SetLineWidth(3)
        graphWhite.SetPoint(0,self.model.Xmin, self.model.Ymax)
        graphWhite.SetPoint(1,self.model.Xmax, self.model.Ymax)

        # if(self.model.label2 == ""):
        #     graphWhite.SetPoint(2,self.model.Xmax, self.model.Ymax*0.75)
        #     graphWhite.SetPoint(3,self.model.Xmin, self.model.Ymax*0.75)
        # else:
        #     graphWhite.SetPoint(2,self.model.Xmax, self.model.Ymax*0.69)
        #     graphWhite.SetPoint(3,self.model.Xmin, self.model.Ymax*0.69)
        graphWhite.SetPoint(2,self.model.Xmax, self.model.Ymax*0.75)
        graphWhite.SetPoint(3,self.model.Xmin, self.model.Ymax*0.75)

        graphWhite.SetPoint(4,self.model.Xmin, self.model.Ymax)
        graphWhite.Draw("FSAME")
        graphWhite.Draw("LSAME")
        self.c.graphWhite = graphWhite
       	CMS_lumi.writeExtraText = 0
	CMS_lumi.extraText = self.preliminary
	CMS_lumi.lumi_13TeV = self.lumi+" fb^{-1}"

	CMS_lumi.lumi_sqrtS = self.energy+" TeV"  
	iPos=0
	CMS_lumi.CMS_lumi(self.c,4, iPos)
        # CMS LABEL
        textCMS = rt.TLatex(0.25,0.96,"  %s " %(self.preliminary))
        textCMS.SetNDC()
        textCMS.SetTextAlign(13)
        textCMS.SetTextFont(52)
        textCMS.SetTextSize(0.038)
        textCMS.Draw()
        self.c.textCMS = textCMS
        exclusion_text = "Approx. NNLO+NNLL exclusion"
        if "rpvMonoPhi" in self.model.modelname:
            exclusion_text = "    LO exclusion"
        # MODEL LABEL
        if(self.model.label2 == ""):
            textModelLabel= rt.TLatex(0.15,0.90,"%s  %s" %(self.model.label,exclusion_text))
            textModelLabel.SetNDC()
            textModelLabel.SetTextAlign(13)
            textModelLabel.SetTextFont(42)
            textModelLabel.SetTextSize(0.030 if "rpvMonoPhi" not in self.model.modelname else 0.037)
            textModelLabel.Draw()
            self.c.textModelLabel = textModelLabel
        else:
            textModelLabel= rt.TLatex(0.15,0.910,"%s" %self.model.label)
            textModelLabel.SetNDC()
            textModelLabel.SetTextAlign(13)
            textModelLabel.SetTextFont(42)
            textModelLabel.SetTextSize(0.032)
            textModelLabel.Draw()
            self.c.textModelLabel = textModelLabel
            textModelLabel2= rt.TLatex(0.15,0.860,exclusion_text)
            textModelLabel2.SetNDC()
            textModelLabel2.SetTextAlign(13)
            textModelLabel2.SetTextFont(42)
            textModelLabel2.SetTextSize(0.032)
            textModelLabel2.Draw()
            self.c.textModelLabel2 = textModelLabel2
            self.c.otherLabels = []
            for i,text in enumerate(self.model.label2.split(r"\\")):
                tl = rt.TLatex(0.58, 0.855-i*0.044, text)
                tl.SetNDC()
                tl.SetTextAlign(13)
                tl.SetTextFont(42)
                tl.SetTextSize(0.027)
                tl.Draw()
                self.c.otherLabels.append(tl)

            self.c.SaveAs("~/public_html/test.pdf")

        # NLO NLL XSEC
        textNLONLL= rt.TLatex(0.16,0.32,"NLO-NLL exclusion")
        textNLONLL.SetNDC()
        textNLONLL.SetTextAlign(13)
        textNLONLL.SetTextFont(42)
        textNLONLL.SetTextSize(0.04)
        textNLONLL.Draw()
        #self.c.textNLONLL = textNLONLL

    def Save(self,label):
        # save the output
        self.c.SaveAs("%s.pdf" %label)
        
    def DrawLegend(self):
        if(self.model.label2 == ""):
            offset = 0
        else:
            # offset = -100
            offset = -20 if "T5qqqq" in self.model.modelname else -10
        xRange = self.model.Xmax-self.model.Xmin
        yRange = self.model.Ymax-self.model.Ymin
        
        LObs = rt.TGraph(2)
        LObs.SetName("LObs")
        LObs.SetTitle("LObs")
        LObs.SetLineColor(color(self.OBS['colorLine']))
        LObs.SetLineStyle(1)
        LObs.SetLineWidth(4)
        LObs.SetMarkerStyle(20)
        LObs.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-1.35*yRange/100*10+offset)
        LObs.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-1.35*yRange/100*10+offset)

        LObsP = rt.TGraph(2)
        LObsP.SetName("LObsP")
        LObsP.SetTitle("LObsP")
        LObsP.SetLineColor(color(self.OBS['colorLine']))
        LObsP.SetLineStyle(1)
        LObsP.SetLineWidth(2)
        LObsP.SetMarkerStyle(20)
        LObsP.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-1.20*yRange/100*10+offset)
        LObsP.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-1.20*yRange/100*10+offset)

        LObsM = rt.TGraph(2)
        LObsM.SetName("LObsM")
        LObsM.SetTitle("LObsM")
        LObsM.SetLineColor(color(self.OBS['colorLine']))
        LObsM.SetLineStyle(1)
        LObsM.SetLineWidth(2)
        LObsM.SetMarkerStyle(20)
        LObsM.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-1.50*yRange/100*10+offset)
        LObsM.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-1.50*yRange/100*10+offset)

        textObs = rt.TLatex(self.model.Xmin+11*xRange/100, self.model.Ymax-1.50*yRange/100*10+offset, 
                            "Observed #pm 1 #sigma_{theory}")
        textObs.SetTextFont(42)
        textObs.SetTextSize(0.040 if self.model.label2=="" else 0.035)
        textObs.Draw()
        self.c.textObs = textObs

        do2sigma = "exp2sigma" in self.model.__dict__ and self.model.exp2sigma
        dy = 0.09 if do2sigma else 0.136

        LExpP = rt.TGraph(2)
        LExpP.SetName("LExpP")
        LExpP.SetTitle("LExpP")
        LExpP.SetLineColor(color(self.EXP['colorLine']))
        LExpP.SetLineStyle(7)
        LExpP.SetLineWidth(2)  
        LExpP.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-(2.0-1.1*dy)*yRange/100*10+offset)
        LExpP.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-(2.0-1.1*dy)*yRange/100*10+offset)

        LExp = rt.TGraph(2)
        LExp.SetName("LExp")
        LExp.SetTitle("LExp")
        LExp.SetLineColor(color(self.EXP['colorLine']))
        LExp.SetLineStyle(7)
        LExp.SetLineWidth(4)
        LExp.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-2.00*yRange/100*10+offset)
        LExp.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-2.00*yRange/100*10+offset)
        
        LExpM = rt.TGraph(2)
        LExpM.SetName("LExpM")
        LExpM.SetTitle("LExpM")
        LExpM.SetLineColor(color(self.EXP['colorLine']))
        LExpM.SetLineStyle(7)
        LExpM.SetLineWidth(2)  
        LExpM.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-(2.0+1.1*dy)*yRange/100*10+offset)
        LExpM.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-(2.0+1.1*dy)*yRange/100*10+offset)

        if do2sigma:
            LExpP2 = rt.TGraph(2)
            LExpP2.SetName("LExpP2")
            LExpP2.SetTitle("LExpP2")
            LExpP2.SetLineColor(color(self.EXP['colorLine']))
            LExpP2.SetLineStyle(3)
            LExpP2.SetLineWidth(2)  
            LExpP2.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-(2.0-2*dy)*yRange/100*10+offset)
            LExpP2.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-(2.0-2*dy)*yRange/100*10+offset)

            LExpM2 = rt.TGraph(2)
            LExpM2.SetName("LExpM2")
            LExpM2.SetTitle("LExpM2")
            LExpM2.SetLineColor(color(self.EXP['colorLine']))
            LExpM2.SetLineStyle(3)
            LExpM2.SetLineWidth(2)  
            LExpM2.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-(2.0+2*dy)*yRange/100*10+offset)
            LExpM2.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-(2.0+2*dy)*yRange/100*10+offset)
            
        textExp = rt.TLatex(self.model.Xmin+11*xRange/100, self.model.Ymax-2.15*yRange/100*10+offset, 
                            "Expected #pm {0} #sigma_{{experiment}}".format("1" if not do2sigma else "1, 2"))
        textExp.SetTextFont(42)
        textExp.SetTextSize(0.040 if self.model.label2=="" else 0.035)
        textExp.Draw()
        self.c.textExp = textExp

        LObs.Draw("LSAME")
        LObsM.Draw("LSAME")
        LObsP.Draw("LSAME")
        LExp.Draw("LSAME")
        LExpM.Draw("LSAME")
        LExpP.Draw("LSAME")
        if do2sigma:
            LExpP2.Draw("LSAME")
            LExpM2.Draw("LSAME")
        
        self.c.LObs = LObs
        self.c.LObsM = LObsM
        self.c.LObsP = LObsP
        self.c.LExp = LExp
        self.c.LExpM = LExpM
        self.c.LExpP = LExpP
        if do2sigma:
            self.c.LExpP2 = LExpP2
            self.c.LExpM2 = LExpM2

    def DrawDiagonal(self):
        diagonal = rt.TGraph(2, array('d',[self.model.Xmin,self.model.Xmax]), array('d',[self.model.Xmin-175,self.model.Xmax-175]))
        diagonal.SetName("diagonal")
        diagonal.SetFillColor(rt.kWhite)
        diagonal.SetLineColor(rt.kGray+1)
        diagonal.SetLineStyle(2)
        diagonal.SetLineWidth(2)
        diagonal.Draw("FSAME")
        diagonal.Draw("LSAME")
        self.c.diagonal = diagonal
        mt_text = rt.TLatex(0.5*(self.model.Xmin+self.model.Xmax), 0.5*(self.model.Xmin+self.model.Xmax)-175+0.5,
                            "m_{#tilde{t}} = m_{t} + m_{#tilde{#chi}_{1}^{0}}")
        mt_text.SetTextAlign(11)
        mt_text.SetTextColor(rt.kGray+2)
        mt_text.SetTextFont(62)
        mt_text.SetTextSize(0.030)
        canvasx = 1.0 - self.c.GetRightMargin() - self.c.GetLeftMargin()
        canvasy = 1.0 - self.c.GetBottomMargin() - self.c.GetTopMargin()
        gevperpixx = (self.model.Xmax-self.model.Xmin) / canvasx
        gevperpixy = (self.model.Ymax-self.model.Ymin) / canvasy
        angle = atan(gevperpixx / gevperpixy) * 180 / pi
        mt_text.SetTextAngle(angle)
        mt_text.Draw()
        self.c.mt_text = mt_text
        
    def DrawLines(self):
        # observed
        self.OBS['nominal'].SetLineColor(color(self.OBS['colorLine']))
        self.OBS['nominal'].SetLineStyle(1)
        self.OBS['nominal'].SetLineWidth(4)
        # observed + 1sigma
        self.OBS['plus'].SetLineColor(color(self.OBS['colorLine']))
        self.OBS['plus'].SetLineStyle(1)
        self.OBS['plus'].SetLineWidth(2)        
        # observed - 1sigma
        self.OBS['minus'].SetLineColor(color(self.OBS['colorLine']))
        self.OBS['minus'].SetLineStyle(1)
        self.OBS['minus'].SetLineWidth(2)        
        # expected + 1sigma
        self.EXP['plus'].SetLineColor(color(self.EXP['colorLine']))
        self.EXP['plus'].SetLineStyle(7)
        self.EXP['plus'].SetLineWidth(2)                
        # expected
        self.EXP['nominal'].SetLineColor(color(self.EXP['colorLine']))
        self.EXP['nominal'].SetLineStyle(7)
        self.EXP['nominal'].SetLineWidth(4)        
        # expected - 1sigma
        self.EXP['minus'].SetLineColor(color(self.EXP['colorLine']))
        self.EXP['minus'].SetLineStyle(7)
        self.EXP['minus'].SetLineWidth(2)                        

        do2sigma = "exp2sigma" in self.model.__dict__ and self.model.exp2sigma
        if do2sigma:
            self.EXP['plus2'].SetLineColor(color(self.EXP['colorLine']))
            self.EXP['plus2'].SetLineStyle(3)
            self.EXP['plus2'].SetLineWidth(2)
            self.EXP['minus2'].SetLineColor(color(self.EXP['colorLine']))
            self.EXP['minus2'].SetLineStyle(3)
            self.EXP['minus2'].SetLineWidth(2)

        # DRAW LINES
        self.EXP['nominal'].Draw("LSAME")
        self.EXP['plus'].Draw("LSAME")
        self.EXP['minus'].Draw("LSAME")
        if do2sigma:
            self.EXP['plus2'].Draw("LSAME")
            self.EXP['minus2'].Draw("LSAME")
        self.OBS['nominal'].Draw("LSAME")
        self.OBS['plus'].Draw("LSAME")
        self.OBS['minus'].Draw("LSAME")        

    def DrawCorridor(self):
        ## Moriond Recommendation for T2tt.
        ## Blank out the diagonal delimited by these four points: 
        ## (262.5,112.5) (287.5,87.5) (200,0) (150,0) 

        ## lower left corner
        x1 = self.model.Xmin ## = 150
        y1 = self.model.Ymin ## = 0  

        ## lower right corner
        x2 = self.model.Xmin+50. ## = 200
        y2 = self.model.Ymin     ## = 0  
        
        ## upper right corner
        x3 = self.model.Xmin+137.5 ## = 287.5
        y3 = self.model.Ymin+87.5  ## = 87.5

        ## upper left corner
        x4 = self.model.Xmin+112.5 ## = 262.5
        y4 = self.model.Ymin+112.5 ## = 112.5

        whitebox = rt.TGraph(4, array('d',[x1,x2,x3,x4]), array('d',[y1,y2,y3,y4]))

        whitebox.SetName("whitebox")
        whitebox.SetFillColor(rt.kWhite)
        whitebox.Draw("FSAME")
        self.c.whitebox = whitebox
