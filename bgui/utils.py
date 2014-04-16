def scalar(s, maxi, mini):
    #print(s, maxi, mini)
    if s==maxi or maxi==mini:
       return 1.0
    else:
       return((s-mini)/(maxi-mini))

def real(r, maxi, mini):
    return((r*(maxi-mini))+mini)

def clamp(val, mmin, mmax):
    return max(min(val, mmax), mmin)