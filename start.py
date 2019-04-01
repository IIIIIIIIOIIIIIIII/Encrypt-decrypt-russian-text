rus_letts = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',
       'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я',
       '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?', '/', '|', '\\', ',', '.', ':', ';', '"', '{', '}', '[', ']', ' '];

symbols = ['b8$GOT_IT', 'n1)GOT_IT', 'n^5GOT_IT', 'd3.GOT_IT', 'c9*GOT_IT', 'v)8GOT_IT', 'nv4GOT_IT', 'f02GOT_IT', '!7!GOT_IT', 'lf6GOT_IT', 'v#oGOT_IT', 'f#aGOT_IT', '7l)GOT_IT', 'm4$GOT_IT', 'x@3GOT_IT', 'hj!GOT_IT', '0t6GOT_IT', 'gg&GOT_IT', 'm()GOT_IT', 'j6#GOT_IT', 'z)0GOT_IT', 'f2WGOT_IT', 'g^^GOT_IT', 'b5tGOT_IT', 'jk*GOT_IT', 'va&GOT_IT', '7lfGOT_IT', 's3@GOT_IT', 'j%1GOT_IT', 'n)8GOT_IT', 'm%vGOT_IT', '12zGOT_IT', 'f2xGOT_IT',
       'b7$GOT_IT', 'nn0GOT_IT', 'v5#GOT_IT', '^i^GOT_IT', 'b>7GOT_IT', '<o>GOT_IT', 'vIvGOT_IT', 'd#bGOT_IT', 'n4fGOT_IT', 'uk<GOT_IT', 's#aGOT_IT', 'p2@GOT_IT', 'z>oGOT_IT', '$3jGOT_IT', 'z%0GOT_IT', 'alaGOT_IT', '07fGOT_IT', 'nm4GOT_IT', 'f**GOT_IT', 'ho4GOT_IT', 'woeGOT_IT', 'c%aGOT_IT', 't2tGOT_IT', '901GOT_IT', 'bq&GOT_IT', 'h[7GOT_IT', 'z0aGOT_IT', 'd%%GOT_IT', 'h*nGOT_IT', '8!1GOT_IT', 'v()GOT_IT', 's3gGOT_IT', 'v0&GOT_IT',
       'iu2GOT_IT', 'v&4GOT_IT', 'bo(GOT_IT', 'b3pGOT_IT', 'v)(GOT_IT', 'fghGOT_IT', '11%GOT_IT', 'vn^GOT_IT', 'vaGOT_IT', 'b!GOT_IT', 'c00GOT_IT', 'd%*GOT_IT', 'vk!GOT_IT', 'bh%GOT_IT', 'sp(GOT_IT', 'g#0GOT_IT', 'bjiGOT_IT', 'asdGOT_IT', '@@@GOT_IT', 'm*cGOT_IT', 'f)*GOT_IT', 'd#?GOT_IT', 'gh6GOT_IT', 'ghtGOT_IT'];






answer = int(input('''Что вы хотите сделать?
1 - зашифровать текст
2 - расшифровать текст
3 - выйти из программы\n'''));

if answer == 1:    
    text = open('a.txt').readline();
    if text == '':
        print('Пустой файл! Поместите туда текст для шифрования');
        input();
    else:
        text_arr = list(text);
        new_text = [];
        new_phrase = '';

        for i in text_arr:
            for j in rus_letts:
                if i == j:
                    a = rus_letts.index(j);
                    new_text.append(symbols[a]);
        #print(new_text);
        for b in new_text:
            new_phrase += b;
        #print(new_phrase);

        new_f = open('b.txt', 'w');
        new_f.write(new_phrase);
        new_f.close();

        print('Текст зашифрован!');
        input();

elif answer == 2:
    decrypt_text = open('a.txt').readline();
    if decrypt_text == '':
        print('Пустой файл! Поместите туда текст для расшифровки');
        input();
    else:
        text_arr = decrypt_text.split('GOT_IT');
        length = len(text_arr)
        del text_arr[length - 1]
        for y in text_arr:
            text_arr[text_arr.index(y)] += 'GOT_IT'
        
        
        #print(text_arr)
        new_text = [];
        new_phrase = '';

        for i in text_arr:
            for j in symbols:                
                if i == j:
                    a = symbols.index(j)
                    new_text.append(rus_letts[a])

        #print(new_text)

        for b in new_text:
            new_phrase += b

        
        new_f = open('b.txt', 'w');
        new_f.write(new_phrase);
        new_f.close();

        print('Текст расшифрован!');        
        input();
		
					
        
		
		
		
		

                

