'''
# xpath中 elements = wd.find_elements(By.XPATH, "//div//p")
1、根据属性选择
    //*[@id='west']
    //select[@class='single_choice']
2、按次序选择
    //div/p[2]
    倒数第几个元素：//p[last()-1]
3、范围选择
    选取option类型第1到2个子元素
        //option[position()<=2]
    选择class属性为multi_choice的后3个子元素
        //*[@class='multi_choice']/*[position()>=last()-2]
4、组选择
    比如，要选所有的option元素 和所有的 h4 元素，可以使用
        //option | //h4
    等同于CSS选择器
        option , h4
5、选择父节点
    某个元素的父节点用 /.. 表示

'''