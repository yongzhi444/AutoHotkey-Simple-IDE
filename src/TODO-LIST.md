# TODO LIST

编辑器的设计有很多细节的地方，需要做得更加人性化，一个人维护起来难度是有的

我在这里写上我要做的项目，既给自己做个笔记，留个印象，以后完善，也希望对此感兴趣、想加入进来的你能根据这篇文档，与我一同协作，合力完成这个项目（比个心

1，代码智能感知：

代码编辑区是支持HTML-CSS的，我初步的想法是

| 以纯文本插入到编辑区             | 设置监听，随时改变  | 拿走所有代码                                       | 格式化后立即重新放上去                                       |
| -------------------------------- | ------------------- | -------------------------------------------------- | ------------------------------------------------------------ |
| code_text.insertPlainText("xxx") | while True:Sleep xx | code_text.toPlainText()<br />code_text.setText("") | code_text.append("<font color=\"#FF0000\">" + line + "\n\<\/font> ") |

目前代码中的color_it按钮就是为了这个目的做的，但是只是一个小到helloworld一样的功能（尴尬jpg）

2，界面上的文字更加通俗易懂

3,命名规则
