$latex = 'platex -synctex=1 --src-specials %O %S';
$bibtex = 'pbibtex %O %B';
$dvipdf = 'dvipdfmx %O -o %D %S';
$makeindex = 'mendex -r -c -g -s ./misc/line.ist -p any %O %S';
$max_repeat = 10;
