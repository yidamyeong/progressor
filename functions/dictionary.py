country_capital = {'대한민국':'서울',
                   '영국':'런던',
                   '미국':'워싱턴',
                   '일본':'도쿄'}
capital_country = {capital: country for country, capital in country_capital.items()}
print(capital_country)  # {'서울': '대한민국', '런던': '영국', '워싱턴': '미국', '도쿄': '일본'}

country = ['Sweden', 'Saudi', 'USA', 'Korea', 'Swiss']
print({w[0] : w for w in country})
# {'S':'Swiss', 'U':'USA', 'K':'Korea'}
