from array import *

class sms():

    def __init__(self, modelname):
        if modelname.startswith("T1tttt") : self.T1tttt()
        if modelname.startswith("T1bbbb") : self.T1bbbb()
        if modelname.startswith("T1qqqq") : self.T1qqqq()
        if modelname.startswith("T5qqqqWW") : self.T5qqqqWW()
        if modelname.startswith("T5qqqqVV") : self.T5qqqqVV()
        if modelname.startswith("T2tt") : self.T2tt()
        if modelname.startswith("T2bb") : self.T2bb()
        if modelname.startswith("T2bW") : self.T2bW()
        if modelname.startswith("T2bt") : self.T2bt()
        if modelname.startswith("T2cc") : self.T2cc()
        if modelname.startswith("T2qq") : self.T2qq()
        if modelname.startswith("rpvMonoPhi") : self.rpvMonoPhi()
        if modelname.startswith("T2-4bd") : self.T24bd()
        if modelname.startswith("Axial1p0") : self.Axial1p0()
        if modelname.startswith("Axial0p25") : self.Axial0p25()
        if modelname.startswith("Vector1p0") : self.Vector1p0()
        if modelname.startswith("Vector0p25") : self.Vector0p25()


    def T1tttt(self):
        # model name
        self.modelname = "T1tttt"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow t #bar{t} #tilde{#chi}^{0}_{1}";
        self.label2= "";
        # scan range to plot
        self.Xmin = 600.
        self.Xmax = 2600.
        self.Ymin = 0.
        self.Ymax = 2000.
        self.Zmin = 0.0001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{g}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False
        self.exp2sigma = True
        
    def T1bbbb(self):
        # model name
        self.modelname = "T1bbbb"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow b #bar{b} #tilde{#chi}^{0}_{1}";
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 800.
        self.Xmax = 2600.
        self.Ymin = 0.
        self.Ymax = 2200.
        self.Zmin = 0.0001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{g}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False
        self.exp2sigma = True

    def T1qqqq(self):
        # model name
        self.modelname = "T1qqqq"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow q #bar{q} #tilde{#chi}^{0}_{1}";
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600.
        self.Xmax = 2600.
        self.Ymin = 0.
        self.Ymax = 2000.
        self.Zmin = 0.0001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{g}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False
        self.exp2sigma = True

    def T5qqqqWW(self):
        # model name
        self.modelname = "T5qqqqWW"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        chargino_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{#pm}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{g} #tilde{g},  #tilde{g} #rightarrow q #bar{q}' "+ chargino_s +",  "+chargino_s+" #rightarrow W^{#pm} "+lsp_s;
        self.label2= "m_{{#kern[0.2]{{{0}}}}} = 0.5(m_{{#kern[0.2]{{#tilde{{g}}}}}} + m_{{#kern[0.1]{{{1}}}}}#kern[0.4]{{)}}".format(chargino_s, lsp_s);
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600.
        self.Xmax = 2400.
        self.Ymin = 0.
        self.Ymax = 2000.
        self.Zmin = 0.0001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False
        self.exp2sigma = True

    def T5qqqqVV(self):
        # model name
        self.modelname = "T5qqqqWW"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        lsp2_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-0.9]{#scale[0.85]{_{2}}}"
        chargino_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{#pm}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= r"pp #rightarrow #tilde{{g}} #tilde{{g}},  #scale[0.85]{{BR(#tilde{{g}} #rightarrow q #bar{{q}}' {0} ) = 2/3, BR(#tilde{{g}} #rightarrow q #bar{{q}} {1} ) = 1/3}}".format(chargino_s, lsp2_s)
        self.label2= r"{0} #rightarrow W^{{#pm}} {1}\\{2} #rightarrow Z {1}\\m_{{#kern[0.1]{{{0},{2}}}}} = 0.5(m_{{#kern[0.1]{{#tilde{{g}}}}}} + m_{{#kern[0.1]{{{1}}}}}#kern[0.4]{{)}}".format(chargino_s, lsp_s, lsp2_s)
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600.
        self.Xmax = 2400.
        self.Ymin = 0.
        self.Ymax = 2000.
        self.Zmin = 0.0001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False
        self.exp2sigma = True

    def T2tt(self):
        # model name
        self.modelname = "T2tt"
        # decay chain
        self.label= "pp #rightarrow #tilde{t} #tilde{t}, #tilde{t} #rightarrow t #tilde{#chi}^{0}_{1}";
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 150.
        self.Xmax = 1300.
        self.Ymin = 0.
        self.Ymax = 1000.
        self.Zmin = 0.0001
        self.Zmax = 100.
        # produce sparticle
        self.sParticle = "m_{#tilde{t}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False

    def T2bb(self):
        # model name
        self.modelname = "T2bb"
        # decay chain
        self.label= "pp #rightarrow #tilde{b} #tilde{b}, #tilde{b} #rightarrow b #tilde{#chi}^{0}_{1}";
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 300.
        self.Xmax = 1400.
        self.Ymin = 0.
        self.Ymax = 1100.
        self.Zmin = 0.0001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{b}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False
        self.exp2sigma = True

    def T2bW(self):
        # model name
        self.modelname = "T2bW"
        # decay chain
        self.label= "pp #rightarrow #tilde{t} #tilde{t},  #tilde{t} #rightarrow b #tilde{#chi}^{\pm}_{1},  #tilde{#chi}^{\pm}_{1} #rightarrow W^{#pm} #tilde{#chi}^{0}_{1}";
        self.label2= r"m_{#tilde{#chi}^{\pm}_{1}} = (m_{#tilde{t}} + m_{#tilde{#chi}^{0}_{1}})/2";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 300.
        self.Xmax = 1200.
        self.Ymin = 0.
        self.Ymax = 800.
        self.Zmin = 0.0001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{t}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False

    def T2bt(self):
        # model name
        self.modelname = "T2bt"
        # decay chain
        self.label= "pp #rightarrow #tilde{t} #tilde{t}, #tilde{t} #rightarrow b #tilde{#chi}^{\pm}_{1} #rightarrow b W^{#pm} #tilde{#chi}^{0}_{1} or #tilde{t} #rightarrow t #tilde{#chi}^{0}_{1}";
        self.label2= r"m_{#tilde{#chi}^{\pm}_{1}} #minus m_{#tilde{#chi}^{0}_{1}} = 5 GeV\\BR(#tilde{t} #rightarrow t #tilde{#chi}^{0}_{1}) = 50%";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 300.
        self.Xmax = 1400.
        self.Ymin = 0.
        self.Ymax = 860.
        self.Zmin = 0.0001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{t}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False

    def T2qq(self):
        # model name
        self.modelname = "T2qq"
        # decay chain
        self.label= "pp #rightarrow #tilde{q} #tilde{q}, #tilde{q} #rightarrow q #tilde{#chi}^{0}_{1}";
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 550.
        self.Xmax = 2000.
        self.Ymin = 0.
        self.Ymax = 1600.
        self.Zmin = 0.0001
        self.Zmax = 4.
        # produce sparticle
        self.sParticle = "m_{#tilde{q}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False

    def T2cc(self):
        # model name
        self.modelname = "T2cc"
        # decay chain
        self.label= "pp #rightarrow #tilde{t} #tilde{t}, #tilde{t} #rightarrow c #tilde{#chi}^{0}_{1}";
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 200.
        self.Xmax = 800.
        self.Ymin = 0.
        self.Ymax = 1000.
        self.Zmin = 0.001
        self.Zmax = 10.
        # produce sparticle
        self.sParticle = "m_{#tilde{t}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False
        self.exp2sigma = True

    def rpvMonoPhi(self):
        # model name
        self.modelname = "rpvMonoPhi"
        # decay chain
        self.label= "pp #rightarrow #phi #rightarrow q#psi"
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 800.
        self.Xmax = 2000.
        self.Ymin = 0.
        self.Ymax = 2600.
        self.Zmin = 0.001
        self.Zmax = 10.
        # produce sparticle
        self.sParticle = "m_{#phi} [GeV]"
        # LSP
        self.LSP = "m_{#psi} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.boxOn = False
        self.exp2sigma = False

    def T24bd(self):
        # model name
        self.modelname = "T2-4bd"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{t} #tilde{t}, #tilde{t} #rightarrow b f f' "+lsp_s;
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 100.
        self.Xmax = 600.
        self.Ymin = 0.
        self.Ymax = 750.
        self.Zmin = 0.5
        self.Zmax = 100.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{t}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False

    def Axial1p0(self):
        # model name
        self.modelname = "Axial1p0"
        # decay chain
        self.label= "Axial 1p0";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 100.
        self.Xmax = 2000.
        self.Ymin = 0.
        self.Ymax = 500.
        self.Zmin = 0.001
        self.Zmax = 5.
        # produce sparticle
        self.sParticle = "m_{med} [GeV]"
        # LSP
        self.LSP = "m_{DM} [GeV]"
        # turn off diagonal lines
        self.diagOn = False

    def Axial0p25(self):
        # model name
        self.modelname = "Axial0p25"
        # decay chain
        self.label= "Axial 0p25";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 100.
        self.Xmax = 2000.
        self.Ymin = 0.
        self.Ymax = 500.
        self.Zmin = 0.001
        self.Zmax = 5.
        # produce sparticle
        self.sParticle = "m_{med} [GeV]"
        # LSP
        self.LSP = "m_{DM} [GeV]"
        # turn off diagonal lines
        self.diagOn = False

    def Vector1p0(self):
        # model name
        self.modelname = "Vector1p0"
        # decay chain
        self.label= "Vector 1p0";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 100.
        self.Xmax = 2000.
        self.Ymin = 0.
        self.Ymax = 500.
        self.Zmin = 0.001
        self.Zmax = 5.
        # produce sparticle
        self.sParticle = "m_{med} [GeV]"
        # LSP
        self.LSP = "m_{DM} [GeV]"
        # turn off diagonal lines
        self.diagOn = False


    def Vector0p25(self):
        # model name
        self.modelname = "Vector1p0"
        # decay chain
        self.label= "Vector 1p0";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 100.
        self.Xmax = 2000.
        self.Ymin = 0.
        self.Ymax = 500.
        self.Zmin = 0.001
        self.Zmax = 5.
        # produce sparticle
        self.sParticle = "m_{med} [GeV]"
        # LSP
        self.LSP = "m_{DM} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
