def rect_overlap(rect1, rect2):
    
    if rect1 == rect2: # if both rectangles are same, they are overlapping
        return True, rect1
    
    #get the bottom left and top right coordinates of each rectangle 
    
    rect1_start_len = rect1[0]
    rect1_end_len = rect1[2]
    
    rect2_start_len = rect2[0]
    rect2_end_len = rect2[2]
    
    rect1_start_ht = rect1[1]
    rect1_end_ht = rect1[3]
    
    rect2_start_ht = rect2[1]
    rect2_end_ht = rect2[3]
    
    #initialize overlapping params to False
    len_overlap = False
    ht_overlap = False
    overlap = False
    merged_rect = None
    
    
    #check for x-axis overlap
    if ((rect2_start_len < rect1_end_len and rect2_start_len > rect1_start_len) or #start x-cordinate of 2nd rect within len of 1st rect
        (rect2_end_len > rect1_start_len and rect2_end_len < rect1_end_len) or #end x-cordinate of 2nd rect within len of 1st rect
        (rect1_start_len < rect2_end_len and rect1_start_len > rect2_start_len) or #viceversa 1
        (rect1_end_len > rect2_start_len and rect1_end_len < rect2_end_len) #viceversa 2
        ):
        
        len_overlap = True
    
    #check for y-axis overlap
    if ((rect2_start_ht < rect1_end_ht and rect2_start_ht > rect1_start_ht) or #start y-cordinate of 2nd rect within len of 1st rect
        (rect2_end_ht > rect1_start_ht and rect2_end_ht < rect1_end_ht) or #end y-cordinate of 2nd rect within len of 1st rect
        (rect1_start_ht < rect2_end_ht and rect1_start_ht > rect2_start_ht) or #viceversa 1
        (rect1_end_ht > rect2_start_ht and rect1_end_ht < rect2_end_ht) #viceversa 2
        ):

        ht_overlap = True
    
    #check for rectangle overlap
    if ((len_overlap and ht_overlap) or #both len and height overlap
        (rect1_start_len == rect2_start_len and rect1_end_len == rect2_end_len and ht_overlap) or #equal x-axis len and height overlap
        (rect1_start_ht == rect2_start_ht and rect1_end_ht == rect2_end_ht and len_overlap) #equal y-axis height and length overlap
        ):
        
        overlap = True
        
        #get merged rectangle by finding the bottom left and top right min and max points respectively
        bl_x = min(rect1_start_len, rect2_start_len)
        tr_x = max(rect1_end_len, rect2_end_len)
        bl_y = min(rect1_start_ht, rect2_start_ht)
        tr_y = max(rect1_end_ht, rect2_end_ht)
    
        merged_rect = [bl_x, bl_y, tr_x, tr_y]
    
    return overlap, merged_rect


def merge_rectangles(rect_arr):
    
    final_arr = [] #initialize a final array to be returned
    n = 0 #initialize overlap flag to false
    to_match_rect = rect_arr.pop(0) #first rect will be matched against all rects
    to_be_removed = [] #store all matched rects in a array to remove from the main array
    
    for rect in rect_arr:
        overlap, merged_rect = rect_overlap(to_match_rect, rect) #loop through each rect against first rect and find merged rect
        if overlap:
            n = 1 #even if one rect merges against the first rect,overlap flag = True 
            to_match_rect = merged_rect #store the final merge rect in memory to check later if previous rects in array merge along with this
            to_be_removed.append(rect) #append matched rects to the to be removed array
            
    if to_match_rect not in final_arr: #check if the bigger rectangle is already in the final array. if so we need not append to it                                                           
        final_arr.append(to_match_rect) #else append the rectangle
    
    rect_arr = [x for x in rect_arr if x not in to_be_removed] #remove matched rectangles from original array
    
    if len(rect_arr) > 0: #if there are any elements remaining in rect_array, recursion needs to occur
        if n:            
            rect_arr = [to_match_rect] + rect_arr #if there were overlaps, pass the bigger rect along with the remaining rects

        to_merge = merge_rectangles(rect_arr) #merge remianing rects and append to final array if its not in it
        
        for i in to_merge:
            if i not in final_arr:
                final_arr.append(i)
        
    return final_arr


def main(rect_arr):
    
    prev_len = len(rect_arr)

    while True: #till no further rects merge, keep calling the merge function
        rect_arr = merge_rectangles(rect_arr)
        new_len = len(rect_arr)
        if prev_len == new_len:
            break
        else:
            prev_len = new_len
            
    return rect_arr
       
rect_arr = [[0,4,1,6], [1,3,2,5], [2,2,3,4], [3,1,5,3], [0,0,4,2]] 
print(main(rect_arr))

rect_arr = [[0,0,2,2], [1,1,3,3], [2,2,4,4]]
print(main(rect_arr))

rect_arr = [[0,0,5,5], [2,10,7,12], [6,14,11,19], [8,6,18,16],[9,11,20,25]]
print(main(rect_arr))


rect_arr = [[0,0,4,4], [2,2,4,4], [7,7,10,10], [12,12,14,14],[3,3,5,5]]
print(main(rect_arr))