qPathOrdered = OrderedDict([
        
    ('S_raw','inputFiles/sanger.total.aftertrim.removeCT.min500bp.fasta'),
    ('S_ass','inputFiles/SangerAssembledAndNonAssembled.min500bp.withoutCandT.fasta'),


    ('PB_raw','inputFiles/PB.Cell1and2.raw.fasta'),
    ('PB_ass','inputFiles/PacBio.Correct.C1.fasta'),

    ('MI_raw','inputFiles/LejlaControl.2D.min500bp.fasta'),
    ('MI_demux'   , 'output/LejlaControl.2D.min500bp.afterBC.fasta'),
    ('MI_corr1'   , 'output/LejlaControl.2D.min500bp.afterNC1.fasta'),
    ('MI_corr2'   , 'output/LejlaControl.2D.min500bp.afterNC2.fasta'), 

    ('MIpc_raw', 'inputFiles/poreCamp.2D.min500.fasta'), 
    ('MIpc_demux' , 'output/poreCamp.2D.min500.afterBC.fasta'),  
    ('MIpc_corr1' , 'output/poreCamp.2D.min500.afterNC1.fasta'), 
    ('MIpc_corr2' , 'output/poreCamp.2D.min500.afterNC2.fasta')
        
      
    
    ])

annotationPathOrdered = OrderedDict([
        
    ('S_raw','output/annotation/sanger.total.aftertrim.removeCT.min500bp.fasta.annotated.csv'), 
    ('S_ass','output/annotation/SangerAssembledAndNonAssembled.min500bp.withoutCandT.fasta.annotated.csv'),


    ('PB_raw','output/annotation/PB.Cell1and2.raw.fasta.annotated.csv'), 
    ('PB_ass','output/annotation/PacBio.Correct.C1.fasta.annotated.csv'),

    ('MI_raw','output/annotation/LejlaControl.2D.min500bp/LejlaControl.2D.min500bp.annotated.csv'), 
    ('MI_demux'   , 'output/annotation/LejlaControl.2D.min500bp/LejlaControl.2D.min500bp.afterBC.annotated.csv'), 
    ('MI_corr1'   , 'output/annotation/LejlaControl.2D.min500bp/LejlaControl.2D.min500bp.afterNC1.annotated.csv'), 
    ('MI_corr2'   , 'output/annotation/LejlaControl.2D.min500bp/LejlaControl.2D.min500bp.afterNC2.annotated.csv'), 

    ('MIpc_raw', 'output/annotation/poreCamp.2D.min500/poreCamp.2D.min500.annotated.csv'), 
    ('MIpc_demux' , 'output/annotation/poreCamp.2D.min500/poreCamp.2D.min500.afterBC.annotated.csv'),  
    ('MIpc_corr1' , 'output/annotation/poreCamp.2D.min500/poreCamp.2D.min500.afterNC1.annotated.csv'),  
    ('MIpc_corr2' , 'output/annotation/poreCamp.2D.min500/poreCamp.2D.min500.afterNC2.annotated.csv'), 


    
    ])


readLabels = OrderedDict([
        
    ('S_raw','Sanger raw'),
    ('S_ass','Sanger assembled'),


    ('PB_raw','PacBio raw'), 
    ('PB_ass','PacBio assembled'),


    ('MIpc_raw', 'nanopore lib. B:\n2D reads'), 
    ('MIpc_demux' , 'nanopore lib. B:\nafter debarcoding'),
    ('MIpc_corr1' , 'nanopore lib. B:\nafter nanocorrect round 1'), 
    ('MIpc_corr2' , 'nanopore lib. B:\nafter nanocorrect round 2'), 

    ('MI_raw','nanopore lib. A: 2D reads'), 
    ('MI_demux'   , 'nanopore lib. A:\nafter debarcoding'),
    ('MI_corr1'   , 'nanopore lib. A:\nafter nanocorrect round 1'), 
    ('MI_corr2'   , 'nanopore lib. A:\nafter nanocorrect round 2')  

    
    ])

readLabelsSample = OrderedDict([
        
    ('S_raw','Sanger'), 
    ('S_ass','Sanger'),


    ('PB_raw','PacBio'), 
    ('PB_ass','PacBio'),


    ('MIpc_raw'   , 'nanopore lib. B'),
    ('MIpc_demux' , 'nanopore lib. B'), 
    ('MIpc_corr1' , 'nanopore lib. B'), 
    ('MIpc_corr2' , 'nanopore lib. B'), 
    
    ('MI_raw'     , 'nanopore lib. A'),
    ('MI_demux'   , 'nanopore lib. A'),
    ('MI_corr1'   , 'nanopore lib. A'), 
    ('MI_corr2'   , 'nanopore lib. A')

    
    ])

readLabelsWorkflow = OrderedDict([
        
    ('S_raw','raw'), 
    ('S_ass','assembled'),


    ('PB_raw','raw'), 
    ('PB_ass','assembled'),


    ('MIpc_raw', 'raw 2D'), 
    ('MIpc_demux' , 'after debarcoding'),
    ('MIpc_corr1' , 'after nanocorrect round 1'), 
    ('MIpc_corr2' , 'after nanocorrect round 2'),

    ('MI_raw','raw 2D'), 
    ('MI_demux'   , 'after debarcoding'),
    ('MI_corr1'   , 'after nanocorrect round 1'), 
    ('MI_corr2'   , 'after nanocorrect round 2') 
    
    ])

colorSet = {'MI': '#4daf4a',
        'PB': '#377eb8',
        'MIpc':'#ff7f00',
        'S':'#984ea3'}
