from django.shortcuts import redirect, render
from django.views import generic
from .models import CharactorModel
from django.urls import reverse_lazy

from django_tables2 import SingleTableView
from .tables import CharactorTable

# Create your views here.
def index(request):
    return render(request, 'index.html')
  
class CharactorView(generic.TemplateView):
    table_class = CharactorTable
    template_name = "table.html"
    
    def get(self, request, *args, **kwargs):
        # Modelからすべての情報を取得
        charactor_model_query = CharactorModel.objects
        
        # nameでフィルタ
        name = request.GET.get("name")
        if name == None or name == "":
            # 検索条件が未指定の場合は全件表示
            charactor_objects = charactor_model_query.all()
        else:
            charactor_objects = charactor_model_query.filter(name=name).all()
        
        # Tableデータを生成
        table = CharactorTable(charactor_objects)
        
        # HTMLに出力する内容をセット
        context = {"table": table, 
                   "record_count": charactor_objects.count()} # レコード件数
        
        # HTMLを出力
        return render(request, self.template_name, context)

class CharactorCreate(generic.TemplateView):
    template_name = 'create.html'
    model = CharactorModel
    fields = ('name', 'gender', 'feature')
    success_url = reverse_lazy('list')
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request):
        name = request.POST["name"]
        gender = request.POST["gender"]
        feature = request.POST["feature"]
        image_link = request.POST["image_link"]
        page_link = request.POST["page_link"]
        
        obj = CharactorModel(name=name, gender=gender, feature=feature, image_link=image_link, page_link=page_link)
        obj.save()
        
        return redirect('/list/')