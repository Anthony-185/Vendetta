""" ___________________________________________________________________________
                                  :MMMMMM                                     
                                MMMMMMMMMMMZ                                  
                               MMMMMMMMMMMMMM                                 
  =                           MMMMMMMMMMMMMMM:                           ?    
  7MMM+                       MMMMMMMMMMMMMMMM                        MMMM    
   MM MMMM                   MMMMMMMMMMMMMMMNMM                   OMMM7MM8    
   MM?   MMMM?             MMMMMMMMMMMMMMMMMMMMMM              MMMM    MM     
   ~MM      8M           MM $MMMMMMMMMMMMMM MMM  MN           MM      MMM     
    MMD      M         MM   MMMMMMMMMMMMMMMM MMM   M8         M       MM      
     MM      MM      MM    MMMMMMMMMMN:MMMMMM$MMD    M       MM      MMI      
      MM      MM$  8M      MMMMMMMMMMMMMIMMM M:MM     ?M    MM      MM8       
       MM:      MMM       ZMMMMMMMMMMMMMMM    MMM       OMMM       MM~        
         MO       MM      NMMMMMMMMMMMMMMMM  MMMM       +M=       MM          
          MM       OM     $MMMMDMMMMMMMMMMMMMM MM      MM       MM            
            MM       MM  MMMMMMMMMMMMMMMMMM MMM MM   DM       DM:             
             ~MI      :MOMMMMM MMMMMMMMMMMMMMMMMMMM MM       MM               
               MM       MMMMMM MMMMMMMMMMMMMMMMMMMMM       MM                 
               MMMM     ?MMMMM MMMMMMMMMMMMMMMMMMMM      =MMMD                
              =MMMMM=   :MMMMM:MMMMMMMMMMMMMMMMMMMM     MMMMMM                
              MMMM  MM   MMMMMM MMMMMMMMMMMMMMMMMMM   MM  MMMM                
              MMMM    MM MMMMMMM 8MMMMMMMMMMMMMMMMM :MI   MMMM                
              MMMM     NMMMMMMMMM MMMMMMMMMMMMMMMMMMM     MMMM                
              MMMM       MMMMMMMMMMMMMMMMMMMMMMMMMM       MMMM                
              MMMM        MMMMMMMMMMMMMMMMMMMMMMMM        MMMM                
              MMMM        MMMMMMMMMMMMMMMMMMMMMMMM         MMM                
               MM+       MMMMMMMMMMMMMMMMMMMMMMMMMM        MM                 
              NMM        MMMMMMMMMMMMMMMMMMMMMMMMMM        MMM                
             MMM          MMDMMMMMMMMMMMMMMMMMOMMM          MMM8              
           MMM           DMMMM  MMMMMMMMMMMM  MMMM            MMM             
          ~MM          MMMMMMMMM IMMMMMMMM: MMMMMMMMM          MMM            
          MMM          MMMMZMMMMMMMMMMMMMMMMMMMM MMMM          MMM            
          MMM        MMM~MMMI MMMMMMMMMMMMMMMM  MMMMMMN        MMM            
          MMMM     MMMMMNMMNMM  MMMMMMMMMMMM  IM MM MMMMI     MMMM            
          MMMMM  :MMMMMM MMMIM M            M M MMMZMMMMMM   MMMMM            
            MMMMMMMMMMMMM~MM?MM              MMMMMMMMMMMMMMMMMMMI             
             MMMMMMMMMMMM?MMM              =~ IMMMNMMMMMMMMMMMM               
            MMMMMMMMMMMM     MMMM  Z    M =MMMM    $MMMMMMMMMMMM              
          MMMMMMMMMMMMM       MMMMMM    MMMNMM       MMMMMMMMMMMMM            
        DMMMMMMMMMMMMM        MMMMM     MMMMMM        MMMMMMMMMMMMMM          
      :MMMMMMMMMMMIMMMM      MMMMMMM   :MMMMMM:      MMMMMMMMMMMMMMMMM        
    OMMMMMMMMMMM    MMMM7     MMMM        MMMM      MMMM    MMMMMMMMMMMM      
   MMMM$MMMMMM8      MMMMM          M  M          MMMMM       MMMMMM7MMMMN    
   MMMMMMMMMM         ?MMMM         M  M         MMMMM         MMMMMMMMMM     
   =MMMM MMM            MMMM=       M  M        MMMM            MMMMMMMMM     
    MMMMMMM              MMMMM      M  M      8MMMM              MM~MMMM      
    OMMMM~                =MMMM    MM  MMD   MMMMM                MMMMMM      
     MMMM                   MMMMMMMMM  MMMMMMMMM                   MMMM       
     ZMN                     MMMMMMMM  IMMMMMMM                      MM       
                              :MMMMM    MMMMMM                                
                                ZZZZ    ZZZZ                                  
____________________________________________________________________________"""
# Vendetta module, create a tkinter interface, wrap the functions
#     count the calls,
import tkinter
import time

class Vendetta:

    deja = False
    
    def __init__(self):
        
        if Vendetta.deja:
            print('already initied')
            return
        
        Vendetta.saved_print = print # <----------------------- saving print()
        
        self.tk = tkinter.Tk()
        self.frame = tkinter.Frame(
            self.tk,
            bg = 'cyan')
        self.frame.grid(row = 0, column = 0)
        self.canvas = tkinter.Canvas(
            self.frame,
            width = 400,
            height = 300,
            bg = 'black')
        self.canvas.grid(row = 0, column = 0)
        self.label = tkinter.Label(
            self.frame,
            bg = 'black',
            anchor = 'nw',
            font = ("Terminal", -12),
            justify = 'left',
            fg = 'cyan',
            width = 80,
            wraplength = 400)
        self.label.grid(row = 1, column = 0)
        
        list_x, list_y = [x for x in range(40, 360, 10)], [290] * 32
        coord = []
        for x, y in zip(list_x, list_y): coord.extend([x ,y])
        self.time_line = self.canvas.create_line(
            coord, fill = 'cyan')
        
        self.eta = time.time()
        self.logged_function = {}
        self.check_statement = []
        Vendetta.deja = True

    @staticmethod
    def saved_print():
        ''' copy of print function'''
        ... # <--------------------------------- define if Vendetta is initied
    
    def check(self, statement, *, get = False):
        ''' home-made assert improved '''
        try:
            result = eval(statement)
        except Exception as error:
            result = error
            print('<!> V.check', error, ':', statement)
        else:
            if result is False:
                print('<.> V.check warning :', statement, 'is', result)
            elif get:
                return result
        finally:
            self.check_statement.append((statement, result))

    def write(self, msg):
        ''' to redirect print in Vendetta
        
        print overwrite, stdout in tkinter Label
        ---> V.label['text']'''
        to_print = self.label['text']
        if len(msg) > 80:
            i = 0
            for index, character in enumerate(msg):
                if character == '\n': i = 0 ; continue
                i += 1
                if i > 80: msg = msg[:index] + '\n' + msg[index:] ; i = 0
        if msg == '\n':
            to_print += msg
            if to_print.count('\n') >= 20:
                to_print = to_print[to_print.find('\n') + 1:]
        elif '\n' in msg:
            to_print = to_print.split('\n') + msg.split('\n')
            to_print = '\n'.join(to_print[-20:])
        else:
            to_print += msg
        assert to_print.count('\n') < 21, AssertionError('Vendetta write')
        self.label['text'] = to_print
        if '\n' in msg: self.tk.update() # <- update tk only if new line
        
    def work(self):
        current = time.time()
        elapse_time = int((current - self.eta) * 32)
        if elapse_time > 32:
            coord = self.canvas.coords(V.time_line)
            coord[1::2] = [290] * len(coord[1::2])
            self.canvas.coords(V.time_line, coord)
            self.eta = current
        elif elapse_time < 1:
            pass
        else:
            coord = self.canvas.coords(V.time_line).copy()
            coord_y = coord[1::2]
            coord_y = [290] * (elapse_time - 1)\
                    + [270]\
                    + coord_y[:-elapse_time]
            coord[1::2] = coord_y
            self.canvas.coords(V.time_line, coord)
            self.eta = current
        self.tk.update()

    def for_vendetta(self, func):
        ''' wrapper for log function '''
        def function_wrapped(*args, **kvargs):
            ''' log the function call
            
            log with args and kwargs
            and have a called counter'''
            log = self.logged_function
            name = func.__name__
            if name not in log:
                log[name] = {'call': 0}
            log[name]['last'] = {
                'args': (args),
                'kvargs': (kvargs),
                'result': func(*args, **kvargs)}
            log[name]['call'] += 1
            return log[name]['last']['result']
        return function_wrapped

V = Vendetta()

def print(*args, **kvargs):
    kvargs.update({'file': V})
    Vendetta.saved_print(*args, **kvargs)

for i in range(1, 7 + 1) : print( i * '_', i)
print('End of Vendetta')
V.check('1==1')
V.check('1==0')
V.check('1//0')print( ('*' + '_' * 9) * 16)
print([i for i in range(117)])

# _____________________________________________________________________________
#   image generated by http://www.glassgiant.com/ascii/ (and custom by me)
# _____________________________________________________________________________
#                            . .               =                               
#                              $               . .  .                          
#                           .  .N            .N. .                             
#                       .  .. M O.           .7 8     ,                        
#                        N.M. N ..           . .D. D.D.                        
#                      N M.N.:NI             ..NN..N,N I                       
#                  .   D.,NMMNMMN            .MNNMMNN~ D   ,                   
#                   D  .NMMNMNMNM             N,MMNNDNM   M                    
#                    N   N~MMNN..             . MNNM,D.  N                     
#                     D .DNNMNMN.             .MMNNNND..N                      
#                    .MM8NNNMNNM.             .MDNNNNN$MN                      
#                    .=NNMNMMMMM              .MMNNNMMNM~                      
#                     NMMMNMMMNMN:           +MMMMNNNMNNN                      
#                     DMMNNNNNNNMM.         .MMMMMMMMMMND                      
#                      MMMNMMMMMMMM         NMMMMMNMNMMN                       
#                     NNMMMMMMNNNMN         MMMMMMMNNMNNN                      
#                    DMMMMNNMMMMMNN         MNNMMMMMMMNNNO                     
#                    :NNDMMMMMMNDM.         .DNMMMMMMMDMN=                     
#                    .MMNNMMNMMN.              NMMNNMNMMM                      
#                    .MNMMM.MMM.   .MMM..       MMM.MNNMD                      
#                     MNMN:NMM.  NMMDNNNMM.     .MMM=MNNM                      
#                   DD.NMMMMMN     .MNMMMNMN     MMMMMDM NN                    
#                  .ND DNMNMNM     ,MMMMMMON    .NNMMMMN MD                    
#                      .MNNNMNMMD   NMMMMMM.  8MMMMMMNN.                       
#                      . NDNDNNN.D. . ..     O NMMNMMM                         
#                        .8DNDDN.M,         .M NMMNMM.                         
#                        17  17 .17.  7 .11117 .111117                          
#                        17  17 .117. 7 .117   .17                              
#                        17  17 .7 17.7 .  117 .17                              
#                        111117 .7  117 .11117 .111117                          
#                   .       7.NDD.           .DDN.D      .                     
#                    7       =MNN+ .        .:N:DZ       ?                     
#                    .,..    ~DZ.DO  .   .  DD..N.     ?~                      
#                    . 8  ...?.  D DD .. .NDDN.: O. .. ~..                     
#                          N   ND?N.D8N~8DDDDNDO ..D ..,                       
#                        .,I $. DN.DD7D.DDDNNDD. 7.+:                          
#                         D..8 .8DD.DDDD.8ND8.N  8 .8.                         
#                         ..,..Z .D,,ZD8DZ:.8.  D+=                            
#                             :+..=.?...$?:8.7.,~                              
#                               .DDD? .,..?D8D                                 
#                                 $88DDDDD88                                   
#                                    OD8D8
# _____________________________________________________________________________