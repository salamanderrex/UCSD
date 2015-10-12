import fileinput
import operator
import string


d = {}
d_p = {}
total_count = 0
for line in fileinput.input("05.txt"):
    columns = line.split(" ")
    if len(columns) >= 2:
        #print columns[0]
        #print columns[0print]
        #print columns[1].rstrip('\n')
        total_count = total_count + int(columns[1])
        d[columns[0]] = int(columns[1].rstrip('\n'))
#print d
#print total_count

for key,value in d.iteritems():
    d_p [key] =  float(value) /  (total_count)
d_p_sort = sorted(d_p.iteritems(),key = operator.itemgetter(1))
#print d_p_sort

# smallest 8
i = 0
print "smallest 8"
for i in range(8):
    print d_p_sort[i]


print "biggest 8"
for i in range(8):
    print d_p_sort[len(d_p_sort) - i- 1]



def get_E(key):
    flag = 0

    for x in range(5):
        #succ list
        for fail_letter in fail_list[str(x)]:
            if fail_letter !='':
                for letter in fail_letter:
                    if letter == key[x]:
                        flag = 1
                        break
        if flag ==1:
            return flag


        #faile list

        for success_letter in success_list[str(x)]:
            if success_letter !='':
                for letter in success_letter:
                    if letter != key [x]:
                        flag =1
                        break
        if flag ==1:
            return flag

    #print flag
    return flag

#if flag == 1 , we do not need to calculate , becuase it is 0



def hangeman(fail_list,success_list):
    MAX_TURN = 1
    predictive_probability_final_list = {}
    for i in range(MAX_TURN):
        print "=========== ROUND " , i ,"============"
        #get P(E|W = w)
        #test success

        #predictive_probability = 0
        for alphaet_l in list(string.ascii_uppercase):
            #print "alphaet is ", alphaet_l
            predictive_probability =0
            #originally, put denominator calculatio in the loop, too slow,
            #move out
            denominator = 0
            for key,value in d_p.iteritems():
                denominator =  denominator + d_p [key] * (1-get_E(key))
            for test_key in d_p:
                #print "test_key is ", test_key

                if get_E(test_key)==0:
                    numerator=  d_p [test_key]
                    posterior_p = numerator / denominator;
                    #print "here"
                else:
                    #zero
                    posterior_p = 0

                #print "posterior_p :", posterior_p;

                #6 letter in a word
                letter_in_word = 0
                predictive_i =0
                for predictive_i in range(5):
                    if alphaet_l == test_key[predictive_i]:
                        letter_in_word = 1
                        break
                predictive_probability =  predictive_probability + letter_in_word * posterior_p
                #print "predictive_probability    " , predictive_probability
            print alphaet_l ,"in word", test_key, "p :", predictive_probability
            predictive_probability_final_list [alphaet_l] = predictive_probability

        success_letters_this_turn = set()
        for x in range(5):
            for letters in success_list[str(x)]:
                for letter in letters:
                    success_letters_this_turn.add(letter)
        #print "success_letters_this_turn : ", success_letters_this_turn
        max_list = sorted(predictive_probability_final_list.iteritems(),key = operator.itemgetter(1))
        #print 'max_list', max_list
        x = 25
        flag = 1
        while(flag):
            max = max_list[x]

            flag = 0
            for letter in success_letters_this_turn:
                if letter == max[0]:
                    flag = 1
                    x = x-1
                    break

        print 'best next guess =================>', max_list[x]
        print "+++++++++ROUND " , i ,"++++++++++++"
        print "\n"





#question b
#once I guess a letter, if it fails, then means it does not apper on any digit
fail_list = { '0' : '', '1' : '' , '2' : '','3' : '','4' : '','5' : ''}
#once success, then we it may on a position or one many position
success_list = { '0' : '', '1' : '' , '2' : '','3' : '','4' : '','5' : ''}

#1)
hangeman(fail_list,success_list)

#2)
fail_list =  { '0' : ['E','O'], '1' : ['E','O'] , '2' : ['E','O'],'3' : ['E','O'],'4' : ['E','O'],'5' : ['E','O']}
success_list = { '0' : '', '1' : '' , '2' : '','3' : '','4' : '','5' : ''}
hangeman(fail_list,success_list)


#3)
fail_list =  { '0' : '', '1' : ['D','I'] , '2' : ['D','I'],'3' : '','4' : ['D','I'],'5' : ''}
success_list = { '0' : 'D', '1' : '' , '2' : '','3' : 'I','4' : '','5' : ''}
hangeman(fail_list,success_list)

#4)
fail_list =  { '0' : ['A','I'], '1' : ['D','I','A'] , '2' : ['D','I','A'],'3' : ['A','D'],'4' : ['D','I','A'],'5' : 'A'}
success_list = { '0' : 'D', '1' : '' , '2' : '','3' : 'I','4' : '','5' : ''}
hangeman(fail_list,success_list)

#5)
fail_list =  { '0' : ['A','I','E','O','S','U'], '1' :['A','I','E','O','S'] , '2' : ['A','I','E','O','S','U'],'3' : ['A','I','E','O','S','U'],'4' : ['A','I','E','O','S','U'],'5' : 'A'}
success_list = { '0' : '', '1' : 'U' , '2' : '','3' : '','4' : '','5' : ''}
hangeman(fail_list,success_list)





