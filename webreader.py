from bs4 import BeautifulSoup




    class PyMon:

    def get_3year_treasury():
        url = "http://www.index.go.kr/strata/jsp/showStblGams3.jsp?stts_cd=288401&amp;idx_cd=2884&amp;freq=Y&amp;period=1998:2016"
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html5lib')
        td_data = soup.select("tr td")

        treasury_3year = {}
        start_year = 1998

        for x in td_data:
            treasury_3year[start_year] = x.text
            start_year += 1

        print(treasury_3year)
        return treasury_3year

    def get_estimated_dividend_yield(code):
        dividend_yield = get_financial_statements(code)
        dividend_yield = sorted(dividend_yield.items())[-1]
        return dividend_yield[1]

    def get_dividend_yield(code):
        url = "http://companyinfo.stock.naver.com/company/c1010001.aspx?cmp_cd=" + code
        html = requests.get(url).text

        soup = BeautifulSoup(html, 'html5lib')
        dt_data = soup.select("td dl dt")

        dividend_yield = dt_data[-2].text
        dividend_yield = dividend_yield.split(' ')[1]
        dividend_yield = dividend_yield[:-1]

        return dividend_yield


if __name__ == "__main__":
    # get_3year_treasury()

    # dividend_yield = get_dividend_yield('058470')
    # print(dividend_yield)

    estimated_dividend_yield = get_estimated_dividend_yield('058470')
    print(estimated_dividend_yield)