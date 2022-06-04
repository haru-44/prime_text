import glob
import os
import re

src_dic = {}
for g in glob.glob('../src/*.py'):
    name = os.path.splitext(os.path.basename(g))[0]
    with open(g, mode='r', encoding='utf-8') as f:
        r = f.read()
        src_dic[name] = r


pre_text = """<html lang="ja">
  <head>
    <title>HTML_TITLE</title>
    <script type="text/x-mathjax-config">
       MathJax.Hub.Config({TeX:{equationNumbers:{autoNumber:"AMS"}}});
    </script>
    <script type="text/javascript" async
        src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML,/www_func/MathJax/MyConfig.js">
    </script>
    <script type="text/javascript" src="https://cdn.rawgit.com/google/code-prettify/master/loader/run_prettify.js?lang=py&skin=sunburst"></script>
  </head>
  <body>
  <strong>このページは、pdfファイル出力用に作成したtexファイルから機械的に変換されています。体裁不良がある場合は<a href="https://github.com/haru-44/prime_text/releases/latest/download/main.pdf">pdfファイル</a>をご覧ください。</strong>
  <hr/>
"""
post_text = '</body></html>'

for file in glob.glob('../tex/*.tex'):
    name = os.path.splitext(os.path.basename(file))[0]
    if name in ['main', 'proof_number', 'proof_group']:
        continue
    with open(file, encoding='utf-8', mode='r') as f:
        text = f.read()
        text = re.sub('\$(.+?)\$', '\(\\1\)', text)

        text = re.sub('\\\\subsubsection{(.+?)}', '<h2>\\1</h2>', text)
        text = re.sub('\\\\IND{(.+?)}{.+?}', '<strong>\\1</strong>', text)
        text = re.sub('\\\\kenten{(.+?)}', '<strong>\\1</strong>', text)
        text = re.sub('\\\\textbf{(.+?)}', '<strong>\\1</strong>', text)
        text = re.sub('\\\\ruby{(.+?)}{.+?}', '\\1', text)

        text = re.sub('\\\\rProp{.+?}', '', text)
        text = re.sub('\\\\rTheo{.+?}', '', text)
        text = re.sub('\\\\rDefi{.+?}', '', text)
        text = re.sub('\\\\rLemm{.+?}', '', text)
        text = re.sub('\\\\rCoro{.+?}', '', text)
        text = re.sub('\\\\rExam{.+?}', '', text)
        text = re.sub('\\\\rAlgo{.+?}', '', text)
        text = re.sub('\\\\cite{.+?}', '', text)
        text = re.sub('\\\\url{(.+?)}', '<a href="\\1">\\1</a>', text)
        text = re.sub('\\\\Notes', '', text)

        text = re.sub('\\\\begin{itemize}', '<ul>', text)
        text = re.sub('\\\\end{itemize}', '</ul>', text)
        text = re.sub('\\\\begin{enumerate}', '<ol>', text)
        text = re.sub('\\\\end{enumerate}', '</ol>', text)
        text = re.sub('\\\\begin{description}', '<ul>', text)
        text = re.sub('\\\\end{description}', '</ul>', text)
        text = re.sub('\\\\item', '<li>', text)

        text = re.sub('\\\\begin{Theo}{.*?}{.*?}',
                      '<div style="padding: 10px; margin-bottom: 10px; border: 1px solid #000000;">(<strong>定理</strong>)', text)
        text = re.sub('\\\\end{Theo}', '</div>', text)
        text = re.sub(
            '\\\\begin{thProof}{.*?}', '<div style="padding: 10px; margin-bottom: 10px; border: 1px solid #000000;">(<strong>証明</strong>)', text)
        text = re.sub('\\\\end{thProof}', '</div>', text)
        text = re.sub('\\\\begin{Prop}{.*?}{.*?}',
                      '<div style="padding: 10px; margin-bottom: 10px; border: 1px solid #000000;">(<strong>命題</strong>)', text)
        text = re.sub('\\\\end{Prop}', '</div>', text)
        text = re.sub(
            '\\\\begin{prProof}{.*?}', '<div style="padding: 10px; margin-bottom: 10px; border: 1px solid #000000;">(<strong>証明</strong>)', text)
        text = re.sub('\\\\end{prProof}', '</div>', text)
        text = re.sub('\\\\begin{Defi}{.*?}{.*?}',
                      '<div style="padding: 10px; margin-bottom: 10px; border: 1px solid #000000;">(<strong>定義</strong>)', text)
        text = re.sub('\\\\end{Defi}', '</div>', text)
        text = re.sub('\\\\begin{Lemm}{.*?}{.*?}',
                      '<div style="padding: 10px; margin-bottom: 10px; border: 1px solid #000000;">(<strong>補題</strong>)', text)
        text = re.sub('\\\\end{Lemm}', '</div>', text)
        text = re.sub(
            '\\\\begin{lmProof}{.*?}', '<div style="padding: 10px; margin-bottom: 10px; border: 1px solid #000000;">(<strong>証明</strong>)', text)
        text = re.sub('\\\\end{lmProof}', '</div>', text)
        text = re.sub('\\\\begin{Coro}{.*?}{.*?}',
                      '<div style="padding: 10px; margin-bottom: 10px; border: 1px solid #000000;">(<strong>系</strong>)', text)
        text = re.sub('\\\\end{Coro}', '</div>', text)
        text = re.sub(
            '\\\\begin{crProof}{.*?}', '<div style="padding: 10px; margin-bottom: 10px; border: 1px solid #000000;">(<strong>証明</strong>)', text)
        text = re.sub('\\\\end{crProof}', '</div>', text)
        text = re.sub('\\\\begin{Conj}{.*?}{.*?}',
                      '<div style="padding: 10px; margin-bottom: 10px; border: 1px solid #000000;">(<strong>予想</strong>)', text)
        text = re.sub('\\\\end{Conj}', '</div>', text)
        text = re.sub('\\\\begin{Exam}{.*?}{.*?}',
                      '<div style="padding: 10px; margin-bottom: 10px; border: 1px solid #000000;">(<strong>例</strong>)', text)
        text = re.sub('\\\\end{Exam}', '</div>', text)
        pattern = re.compile('\\\\Algo{.*?}{(.*?)}{.*?}')
        text = pattern.sub(lambda m: '<pre class="prettyprint">' +
                           src_dic[m.groups(0)[0]] + '</pre>', text)

        lines = text.split('\n')
        text = '<p>'
        tags = -1
        for line in lines:
            if tags == -1:
                for idx, t in enumerate(['<ul>', '<ol>', '<div ', '<pre ']):
                    if t in line:
                        tags = idx
                        text += '</p>'
                        break
            if tags == -1 and line == '':
                text += '</p>\n<p>'
            else:
                text += line + '\n'
            if tags != -1:
                for idx, t in enumerate(['</ul>', '</ol>', '</div>', '</pre>']):
                    if t in line and idx == tags:
                        tags = -1
                        text += '<p>'
                        break
        text += '</p>\n'
        text = text.replace('<p></p>', '')

        text = f'<h1>{name}</h1>\n' + text
        pre_text_ = re.sub('(HTML_TITLE)', name, pre_text)
        text = pre_text_ + text + post_text

    with open(f'../html/{name}.html', mode='w', encoding='utf-8') as f:
        f.write(text)
