const cheerio = require('cheerio');
const http = require('http');




let options = {
    host: "www.imooc.com",
    path: "/video/8837",
    Host: "www.imooc.com",
    Connection: "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    Accept: "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    Referer: "http://www.imooc.com/learn/348",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "en-US,en;q=0.8,zh;q=0.6,zh-CN;q=0.4,ja;q=0.2",
    Cookie: "imooc_uuid=d37ad7ca-9551-44f6-8b97-8203f5198188; imooc_isnew_ct=1488116738; PHPSESSID=9q9qovpvn9o7m9aa5ru9b1rsm5; loginstate=1; apsid=U2OGZhMDhkNWFlYTZmNjg2ZTgxNjc0OGVmMDE3ZmUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANDkzMjg3MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABzcGFjZWdvaW5nQGdtYWlsLmNvbQAAAAAAAAAAAAAAAGUyNjQwMWUzZjc1NzVkYzQxNjdjYzhjODUyYWRiMDZlnkPyWJ5D8lg%3DYT; last_login_username=spacegoing%40gmail.com; IMCDNS=0; Hm_lvt_f0cfcccd7b1393990c78efdeebff3968=1489742058,1489840414,1489933649,1492271971; Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968=1492272037; imooc_isnew=2; cvde=58f2436174350-23"
};

function filterChapters(html) {
    let parser = cheerio.load(html);
    let comments_text = [];

    comments = parser('div[class=pl-list-content]').each((i, e) => { comments_text[i] = parser(e).text() });

    comments_text.forEach((v, i, arr) => { console.log(v) });

}

http.get(options, (res) => {
    let html = '';
    res.on('data', (chunck) => html += chunck);
    html = `apfje`;
    res.on('end', () => filterChapters(html));
    console.log(html);
});




