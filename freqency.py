# -*- coding: utf-8 -*-
"""
Character frequency analysis
"""

import pandas as pd
import re
import collections

#open file
def openfile(file):
    with open(file, 'r') as f:
        mystr = f.read()
    #print(mystr)    
    return mystr

#get characters from .tex file and put in list
def tex_list(mystr):
    
    #start of paragraph = /noindent $###$
    regex = r"noindent \$[0-9]{3}\$"
    #print(mystr)
    m = re.findall(regex, mystr)
    #print(m)
    m.insert(0,0)
    
    paras = re.split(regex, mystr)

    para_dict = dict(zip(m, paras))
    
    #print(paras)
    return para_dict

#make string into list, space as separator
def makelist(mystr):
    charlist = []
    #hold symbol name
    word=""
    
    #strip out enter characters
    mystr1 = mystr.replace('\\noindent', '').replace('$', '')

    ii = 0
    while ii < len(mystr1):
        if mystr1[ii] == "\\" :   #greek letter
            if ii == (len(mystr1)):  #avoid out of bounds error
                break
            else:
                ii+= 1   #need to increment so not checking if backslash is alphs
            while ii< len(mystr1) and mystr1[ii].isalpha() == True:
                word+= mystr1[ii]
                ii+=1

        else:  #all other characters
            word = mystr1[ii]
            ii+=1
        if word != ' ' and word !='\n':
            charlist.append("/"+ word)
            word=""

    return charlist
    #print(charlist)
    
##################################################################
#frequency analysis
def frequency(cipherin):
    #dataframe
    freq_df = pd.DataFrame({"char": cipherin, "count": 1})
    
    df_final = pd.pivot_table(data=freq_df, index=freq_df["char"], aggfunc="sum")
    df_final = df_final.sort_values(by="count", ascending=0)
    
    #total occurrences
    df_total = df_final["count"].sum()
    
    df_final["percent"] = df_final["count"]*100/df_total
    
    #print(df_final)
    #print("\n")
    #print("Sum:", df_total)
    
    
    return(df_final)


    #print duplicate letters and count of each
def findduplicates(cipherin):

    #start with char not in code
    compare="\aa"
    
    #list of single letter duplicates
    duplist = []

    for ii in cipherin:
 
        if ii == compare:
            duplist.append(ii)
        compare = ii
        
    #print("duplicates: ", duplist)
 
    if len(duplist)>0: 
        #to pandas df
        dupdf = pd.DataFrame({"char": duplist})
        
        #dupcount = pd.pivot_table(data = g, aggfunc="count")
        dupdf["count"]=1
        
        df_final = pd.pivot_table(data=dupdf, index=dupdf["char"], aggfunc="sum")
        
        #total occurrences
        df_total = df_final["count"].sum()
        
        df_final["percent"]=df_final["count"]*100/df_total
        
        df_final = df_final.sort_values(by="count", ascending = 0)
        
        #print(df_final)
        
        return df_final

# Space characters are never next to each other. The percent of them is the same. 
    #cipherin = input cipher, spacelist = list of chars that might be spaces.
def notadjacent(cipherin, spacelist):
    
    #hold adj char; 1 or both not space.
    adjacent = []
    
    for item in spacelist:
        for ii in range(0, len(cipherin)-1):
            if cipherin[ii] == item:
                #char are adjacent, one or both are not space.
                if cipherin[ii+1] in spacelist:
                    adjacent.append([cipherin[ii], cipherin[ii+1]])
    #print("adjacent: ",adjacent)
    return( adjacent)


##################################################################################
#map common english letters with the character frequencies
def map_letters(single_list, dup_list, cipher):
    #most frequent english letters, from highest to lowest
    freq_single = [ 'e', 't', 'a', 'o', 'i', 'n', 's', 'h','r', 'd', 'l', 'u']
    freq_double = ['ss', 'ee', 'tt', 'ff', 'll', 'mm','oo']
    
    slic = 6   #arbitrary number of items in list to replace
    
    cipher_single = freq_list.index.tolist()
    cipher_double = dup_list.index.tolist()
    
    single_dict = dict(zip(cipher_single, freq_single))
    double_dict = dict(zip(cipher_double, freq_double))
    
    #print(single_dict, "\n\n", double_dict, "\n\n")
    #print(cipher[:50])
    
    cipher2= cipher
    
    for jj in range(0, len(cipher2)):
        if cipher2[jj] in single_dict:
            new_chara = single_dict[cipher2[jj]]
            cipher2[jj] = new_chara

    #print("\n")

    return cipher2, single_dict, double_dict

#find most common patterns of 3 letters
def patterns(cipher, n):
  
    list1 = []
    
    for ii in range(0, len(cipher) - n-1):
        key1 = ''
        for jj in range(0, n):
            key1 += cipher[ii + jj] + '_'
        list1.append(key1)
        
    df = pd.DataFrame({"pattern": list1, "count": 1})

    try:
        n_df = pd.pivot_table(data=df,  index=df["pattern"], aggfunc="sum")
        n_df = n_df.sort_values(by = "count", ascending = 0)
        ans = n_df[n_df>1].dropna()
    except KeyError:
        print('no multiples')
        ans = 'none'

    #return values that occur more than once
    return ans

#find most common patterns of 3 letters
def threes(cipher):
  
    list1 = []
    
    for ii in range(0, len(cipher) - 2):
        key1 = cipher[ii]+ '_'+ cipher[ii+1] + '_' + cipher[ii+2]
        list1.append(key1)

    df = pd.DataFrame({"threes": list1, "count": 1})

    thr_df = pd.pivot_table(data=df,  index=df["threes"], aggfunc="sum")
    thr_df = thr_df.sort_values(by = "count", ascending = 0)
    print(thr_df)
    return thr_df   

#replace characters with translation guesses. To avoid overwrites
#of english (non-backslash) characters, check for non-backslash in the input file.
def replaceletters(list_orig, replace_dict):
    ii=0
    for chara in list_orig:
        if chara in replace_dict:
            #print(chara, " ", replace_dict[chara])
            list_orig[ii]=replace_dict[chara]

        ii+=1
        
    #print(replace_dict)
    #print(list_orig)
    return(list_orig, replace_dict)

#print to file
def write_file(savepath, *argv):

    with open(savepath, 'a+') as f:
        for arg in argv:
            if type(arg) == pd.core.frame.DataFrame:
                f.write(arg.to_string())
                f.write("\n")
            else:
                try:
                    f.write(arg)
                    f.write("\n")   
                except TypeError:
                    f.write("None")

if __name__=='__main__':
    #path = r'C:\Users\Pizzagirl\Documents\programming\python\pandas\strange_book.tex'
    path = r'C:\Users\Pizzagirl\Documents\programming\python\pandas\book_944.txt'
    #strange_book.tex'
    test = ['/k', '/m', '/m', '/x', '/r', '/5', '/m', '/w', '/k', '/2', '/z']
    #get data from file, read into string
    stringin = openfile(path)
    
    para_dict = tex_list(stringin)
 
    #'/omega', '/m', '/m', '/m', '/5', '/exists', '/m', '/exists', '/gamma', '/k', '/7', '/m', '/exists', '/k', '/exists', '/5', '/gamma', '/epsilon', '/m', '/m', '/k', '/5', '/y', '/k', '/x', '/5', '/Gamma', '/omega', '/x']
    #replace dict: current symbol: new symbol
    replace_letters = {'/m':'s', '/k':'t', '/Sigma':'a', '/gamma':'t', '/omega':'e', '/h': '.', '/Omega': ' ', \
                    '/8': ' ', '/0': ' ', '/u': ' ', '/q': 'y', '/partial': 'h', '/x': 'm'}
    
    #replace characters with guess characters and produce new output (translated) file
    #replacedlist, dict = replaceletters(cipher,replace_dict)
    
    #map_letters(freq_list, dup_list, cipher)
    
    savepath = r"C:\Users\Pizzagirl\Documents\programming\python\pandas\out.txt"
    """
    for para in para_dict:
        
        if para == 0:
            pass
        else:
        
            print(para, "\n")
            
            #make space separated string into a list and add a "/" before each to make all characters not present in english
            cipher = makelist(para_dict[para])
            
            freq_list = frequency(cipher)
        
            #find repeated characters. these can't be spaces.
            dup_list = findduplicates(cipher)
            
            thr_df = threes(cipher)
            
            patt3 = patterns(cipher, 4)
        
            # write stats to output file.
            write_file(savepath, para, str(cipher), "frequencies", freq_list, "duplicates", dup_list, "threes", thr_df, "patterns", patt, "\n")
        
    #'/omega', '/m', '/m', '/m', '/5', '/exists', '/m', '/exists', '/gamma', '/k', '/7', '/m', '/exists', '/k', '/exists', '/5', '/gamma', '/epsilon', '/m', '/m', '/k', '/5', '/y', '/k', '/x', '/5', '/Gamma', '/omega', '/x']
    #replace dict: current symbol: new symbol

    #test space chars by seeing if guesses are adjacent.
    notadjacent(test, ['/m', '/w', '/x', '/r'] )  #['/Omega', '/8', '/0']
    
    #replace most common letters
    #map_letters(freq_list, dup_list, cipher)
    """
    
    replace_dict = {'/3':'e', '/zeta': 't', '/nabla': 't', '/t': 's', '/k': ' ', '/w': ' ', '/7': ' ', '/h': 'a'}
    n= 4
    #spaces: ohm, mu, 8, 0
    for para in para_dict:
        cipher = makelist(para_dict[para])
        
        patt = patterns(cipher, 6)
    
        print(n, " ", patt)
    
        #replace characters with guess characters and produce new output (translated) file
        #replacedlist, dict1 = replaceletters(cipher,replace_dict)
    
        #print(replacedlist)


""" TO DO:  MACHINE LEARNING FOR MOST ENGLISH WORDS, MAKE CLASSES ETC (OOP) """
