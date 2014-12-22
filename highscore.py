import shelve

name = "highscore.shlf"

def set_newscore(player, score):
    # open the self
    shelf = shelve.open(name)
    try:
        # get saved score
        saved = shelf[player]
        if score > saved:
            # update dict with new score
            shelf[player] = score
        else:
            # return the previous score since higher
            score = saved        
            
    except:
        # score doesn't exist, create new
        shelf[player] = score
                
    shelf.close()
    return score
    
    
