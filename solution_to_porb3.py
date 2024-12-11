def pie_of_piece():
    cafeteria_contribution_for_pie = 4
    Each_piece_of_pie_splitted = 5 
    total_pie_sold = 60
    total_cafe_contribut = cafeteria_contribution_for_pie * Each_piece_of_pie_splitted

    book_club_contribute = 0
    Each_piece_of_pie_splitted_for_book = 0
    result  = int(total_pie_sold  - total_cafe_contribut)
    result = result / Each_piece_of_pie_splitted
    return f"book contributed: {result}"

result  =  pie_of_piece()
print(result)
