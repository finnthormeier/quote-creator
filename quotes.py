###########################

#SCRAPE?
scrape = "no"
#DEFINE CANVAS FILE NAME
canvas_file = "reminders_canvas.png" #needs to be 1080x1080px
#DEFINE FONT FILE NAME
font_file = "Georgia.ttf"
#DEFINE FONT COLOR
font_color = "white"
#DEFINE QUOTE PLACEMENT
quote_width = 1000  #standard=1000
quote_hight = 1200  #600 standard=480
quote_pos_ver = 1350 #950 #centered=1080 #Quote Position (vertical)

###########################

import csv
import os
import time
from selenium import webdriver
from PIL import Image, ImageFont, ImageDraw

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

book_name = input('What is the name of the book? ')        

if scrape == 'yes':
    book_id = int(input('What is the Goodreads ID of the book you want to create? '))

    chrome_driver = '/anaconda3/lib/python3.7/site-packages/selenium/chromedriver'
    driver = webdriver.Chrome(chrome_driver)

    print('Fetching quotes now...')

    with open(f'{book_id}.csv', 'w') as csvfile:
        
        quotes_csv = csv.writer(csvfile)       

        for page in range(1,4):

            driver.get(f"https://www.goodreads.com/work/quotes/{book_id}?page={page}")

            time.sleep(5)

            quotes = driver.find_elements_by_class_name("quoteText")

            for quote in quotes:
                x = 0
                quote_full = ''
                for character in quote.text:
                    if character == '“' or character == '”':
                        x += 1
                    if x < 2:
                        quote_full += character
                    else:
                        pass
                
                quotes_csv.writerow([quote_full[1:]])
                #print(quote_full[1:])
                #print('\n')
                
    print('Done fetching the quotes.')

else:
    book_id = input('What is the name of the csv file? (excluding the ".csv") ')

createFolder(f'./{book_name}/')
print(f'Created new folder called {book_name}')

print('Creating quote posts now...')

with open(f'{book_id}.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    quotes = []
    for row in csv_reader:
        quotes.append(row)
        #line_count += 1
        #if line_count > 10:
            #break
            
quote_nr = 1
error_nr = 0

for [quote] in quotes:
    
    canvas = Image.open(canvas_file)

    font_size = 80
    font = ImageFont.truetype(font_file,font_size)
    
    quote_words = quote.rsplit()

    length = -22 # because a space (" ") is 22 pixels long
    wordcount = 0
    break_lines = []

    for word in quote_words:
        w,h = font.getsize(word+' ')
        length += w
        if length >= quote_width:
            break_lines.append(wordcount)
            length = w-22
        else:
            pass
        wordcount += 1

    width,height = font.getsize('randomword')

    if (height * (len(break_lines) + 1)) > quote_hight:

        font_size = 70
        font = ImageFont.truetype(font_file,font_size)

        quote_words = quote.rsplit()

        length = -22 # because a space is 22 pixels long
        wordcount = 0
        break_lines = []

        for word in quote_words:
            w,h = font.getsize(word+' ')
            length += w
            if length >= quote_width:
                break_lines.append(wordcount)
                length = w-22
            else:
                pass
            wordcount += 1

        width,height = font.getsize('randomword')

        if (height * (len(break_lines) + 1)) > quote_hight:

            font_size = 60
            font = ImageFont.truetype(font_file,font_size)

            quote_words = quote.rsplit()

            length = -22 # because a space is 22 pixels long
            wordcount = 0
            break_lines = []

            for word in quote_words:
                w,h = font.getsize(word+' ')
                length += w
                if length >= quote_width:
                    break_lines.append(wordcount)
                    length = w-22
                else:
                    pass
                wordcount += 1

            width,height = font.getsize('randomword')

            if (height * (len(break_lines) + 1)) > quote_hight:

                font_size = 50
                font = ImageFont.truetype(font_file,font_size)

                quote_words = quote.rsplit()

                length = -22 # because a space is 22 pixels long
                wordcount = 0
                break_lines = []

                for word in quote_words:
                    w,h = font.getsize(word+' ')
                    length += w
                    if length >= quote_width:
                        break_lines.append(wordcount)
                        length = w-22
                    else:
                        pass
                    wordcount += 1

                width,height = font.getsize('randomword')

                if (height * (len(break_lines) + 1)) > quote_hight:

                    font_size = 40
                    font = ImageFont.truetype(font_file,font_size)

                    quote_words = quote.rsplit()

                    length = -22 # because a space is 22 pixels long
                    wordcount = 0
                    break_lines = []

                    for word in quote_words:
                        w,h = font.getsize(word+' ')
                        length += w
                        if length >= quote_width:
                            break_lines.append(wordcount)
                            length = w-22
                        else:
                            pass
                        wordcount += 1

                    width,height = font.getsize('randomword')

                    if (height * (len(break_lines) + 1)) > quote_hight:

                        font_size = 30
                        font = ImageFont.truetype(font_file,font_size)

                        quote_words = quote.rsplit()

                        length = -22 # because a space is 22 pixels long
                        wordcount = 0
                        break_lines = []

                        for word in quote_words:
                            w,h = font.getsize(word+' ')
                            length += w
                            if length >= quote_width:
                                break_lines.append(wordcount)
                                length = w-22
                            else:
                                pass
                            wordcount += 1

                        width,height = font.getsize('randomword')

                        if (height * (len(break_lines) + 1)) > quote_hight:

                            print(f'Quote Nr. {quote_nr} is too long')
                            
                            quote_nr += 1

                            error_nr += 1

                        else:

                            quote_full = ''
                            counter = 0

                            for word in quote_words:
                                counter += 1
                                if counter in break_lines:
                                    quote_full = quote_full + word + '\n'
                                else:
                                    quote_full = quote_full + word + ' '

                            w,h = font.getsize_multiline(quote_full)
                            draw = ImageDraw.Draw(canvas)
                            draw.text(((1080-w)/2,(quote_pos_ver-h)/2),quote_full,font=font,fill=font_color)

                            #if quote_nr < 30:
                                #canvas.show()
                            
                            canvas.save(f'./{book_name}/{book_name}_Quote_{quote_nr}.png')
                    
                            quote_nr += 1

                    else:

                        quote_full = ''
                        counter = 0

                        for word in quote_words:
                            counter += 1
                            if counter in break_lines:
                                quote_full = quote_full + word + '\n'
                            else:
                                quote_full = quote_full + word + ' '

                        w,h = font.getsize_multiline(quote_full)
                        draw = ImageDraw.Draw(canvas)
                        draw.text(((1080-w)/2,(quote_pos_ver-h)/2),quote_full,font=font,fill=font_color)

                        #if quote_nr < 30:
                            #canvas.show()
                        
                        canvas.save(f'./{book_name}/{book_name}_Quote_{quote_nr}.png')
                
                        quote_nr += 1        

                else:

                    quote_full = ''
                    counter = 0

                    for word in quote_words:
                        counter += 1
                        if counter in break_lines:
                            quote_full = quote_full + word + '\n'
                        else:
                            quote_full = quote_full + word + ' '

                    w,h = font.getsize_multiline(quote_full)
                    draw = ImageDraw.Draw(canvas)
                    draw.text(((1080-w)/2,(quote_pos_ver-h)/2),quote_full,font=font,fill=font_color)

                    #if quote_nr < 30:
                        #canvas.show()
                    
                    canvas.save(f'./{book_name}/{book_name}_Quote_{quote_nr}.png')
            
                    quote_nr += 1

            else:

                quote_full = ''
                counter = 0

                for word in quote_words:
                    counter += 1
                    if counter in break_lines:
                        quote_full = quote_full + word + '\n'
                    else:
                        quote_full = quote_full + word + ' '

                w,h = font.getsize_multiline(quote_full)
                draw = ImageDraw.Draw(canvas)
                draw.text(((1080-w)/2,(quote_pos_ver-h)/2),quote_full,font=font,fill=font_color)

                #if quote_nr < 30:
                    #canvas.show()
                
                canvas.save(f'./{book_name}/{book_name}_Quote_{quote_nr}.png')
        
                quote_nr += 1

        else:

            quote_full = ''
            counter = 0

            for word in quote_words:
                counter += 1
                if counter in break_lines:
                    quote_full = quote_full + word + '\n'
                else:
                    quote_full = quote_full + word + ' '

            w,h = font.getsize_multiline(quote_full)
            draw = ImageDraw.Draw(canvas)
            draw.text(((1080-w)/2,(quote_pos_ver-h)/2),quote_full,font=font,fill=font_color)

            #if quote_nr < 30:
                #canvas.show()
            
            canvas.save(f'./{book_name}/{book_name}_Quote_{quote_nr}.png')
        
            quote_nr += 1

    else:

        quote_full = ''
        counter = 0

        for word in quote_words:
            counter += 1
            if counter in break_lines:
                quote_full = quote_full + word + '\n'
            else:
                quote_full = quote_full + word + ' '

        w,h = font.getsize_multiline(quote_full)
        draw = ImageDraw.Draw(canvas)
        draw.text(((1080-w)/2,(quote_pos_ver-h)/2),quote_full,font=font,fill=font_color)

        #if quote_nr < 30:
            #canvas.show()
        
        canvas.save(f'./{book_name}/{book_name}_Quote_{quote_nr}.png')
        
        quote_nr += 1

quotes_created = quote_nr - error_nr - 1

print(f'--------------------\nDone. {quotes_created} out of {quote_nr - 1} Quotes were created.')