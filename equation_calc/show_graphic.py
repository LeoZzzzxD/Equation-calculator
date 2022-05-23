import matplotlib.pyplot as plt

def fig(*args):

      Fig = plt.figure(figsize=(1, 2))
      a = Fig.add_subplot(111)
      a.scatter(args[0], args[1], s=7, label="func", color=args[2], linewidth=2)
      if (args[4] < args[0][-1]) and (args[4] > args[0][0]):
         a.scatter(args[4], args[5](args[4]), color="blue")
      if args[3]:
         a.legend(fontsize=8, loc='upper left')
      
      return Fig

   

