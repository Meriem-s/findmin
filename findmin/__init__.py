
def monotonic(a):
    """Check if the first few elements of an array are strictly monotonically decreasing,        
    while the remaining ones are strictly monotonically increasing. 

    Parameters
    ----------
    a : Array of elements

    Returns
    -------
    boolean
            Return True if the array is monotonic, else return False
    """
    #check corner cases
    if a==[] or len(a)==1 or len(a)==2 or len(a)==3:
        return False
    
    #Get first decreasing elements 
    j = 0
    dec=True 
    while j <= len(a)-1 and dec == True:
        if a[j] < a[j+1]:
            dec = False
        j+=1

    if j==1: return False
    
    return (all(a[i] > a[i + 1] for i in range(0,j-1)) and
            all(a[i] < a[i + 1] for i in range(j, len(a)-1)))


def findmin(a):
    """Find the minimum inside of an array of elements
    using as few comparisons as possible

    Parameters
    ----------
    a : array of elements
    """

    #to decrease the time complexity, I am using a binary search method
    if monotonic(a)== False:
        raise ValueError("Wrong Array format")
    low = 0
    high = len(a) - 1
    while low <high:
        mid = ( high + low ) // 2
        
        if a [mid] < a[mid+1]:
            #update low and high
            high = mid
            
        else:
            low = mid + 1                  
    return a[low]

