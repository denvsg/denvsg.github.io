#!bash

#for ((i=0;i<10;i++))
#do
#curl https://lmg.jj20.com/up/allimg/1115/032022105050/220320105050-1-1200.jpg > pic.jpg
#curl https://lmg.jj20.com/up/allimg/1115/032022105050/220320105050-2-1200.jpg > pic2.jpg
#done
#line=`curl https://m.jj20.com/bz/hhzw/xhtx/389394_2.html | grep 'info_pic'`
#link=grep 'src="(//.*jpg)"' ${line}
#
#echo line:${line}
#echo link:${link}
str='<div class="info_pic"><a href='389394_3.html'><img src="//lmg.jj20.com/up/allimg/1115/032022105050/220320105050-2-1200.jpg" alt="□□ǣţ□□ͼƬ□□ȫ□□ͼ"/></a></div> '
echo str:$str
link1=`echo $str | grep -o 'lmg.*jpg'`
link2=`echo $str | sed -n 's#.*\(lmg.*jpg\).*#\1#p'`
link3=`echo $str | awk -F"[\"]" '/lmg.*jpg/{print $4}'`

echo link1:$link1
echo link2:$link2
echo link3:$link3
