#!bash
set -x

alllink=()
#root_link=$(curl https://m.jj20.com/bz/nxxz/shxz/ |grep 'm.jj20.com')
root_link=$(curl https://www.jj20.com/bz/nxxz/shxz/list_62_cc_11.html | grep 'bz/nxxz/shxz')
echo root_link:${root_link}
c=0
for i in $root_link; do
    if [[ $i =~ "bz/nxxz/shxz/"[0-9]+\.html\"$ ]]; then
        echo $c:$i
        # shellcheck disable=SC2219
        tmp=${i:6}
        alllink[$c]=https://www.jj20.com/${tmp//\"/ }
        let c++
    fi
done

echo ${alllink[*]}

# shellcheck disable=SC2068
file=1
for enery_link in ${alllink[@]}; do
    {
        line=$(curl ${enery_link} | grep 'bigImg')
        echo line:"$line"

        link1=$(echo $line | grep -o 'lmg.*jpg')
        for ((i = 1; i < 10; i++)); do
            {
                let file ++
                link="https://${link1//-1-/-$i-}"
                echo $link
                curl $link > $file$i.jpg
            } &
        done
    }
    #link=grep 'src="(//.*jpg)"' ${line}
done

wait

exit 0

str=$line
echo str:$str
link1=$(echo $str | grep -o 'lmg.*jpg')
link2=$(echo $str | sed -n 's#.*\(lmg.*jpg\).*#\1#p')
link3=$(echo $str | awk -F"[\"]" '/lmg.*jpg/{print $4}')

echo link1:$link1
echo link2:$link2
echo link3:$link3

for ((i = 1; i < 10; i++)); do
    {
        link="https://${link1//-1-/-$i-}"
        echo $link
        curl $link > $i.jpg
    } &
done

wait
