# CICP_comic_annotation

##環境
pip install django
pip install django-bootstrap-form


##動かす
python manage.py makemigrations -- models.pyの変更を更新  
python manage.py migrate -- データベースの設定を更新  
python manage.py runserver -- サーバを起動

##動作確認
http://127.0.0.1:8000/comic/

##ファイルの説明
気が向いたら書きます  
基本的には「comic/views.py　ページの基本的な動作設定」「comic/models.py　データベースの設定」「comic/forms.py　フォームの設定」をいじる
分からなかったら直接きいてください