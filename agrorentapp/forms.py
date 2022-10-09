from faulthandler import disable
from django import forms
from agrorentapp.models import Tool

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ('tool_photo' ,'tool_type', 'location','tool_spec_1','tool_spec_2','tool_info','rent_price')
        types = [(day, day) for day in ['Tractor','Sprayer','Cutter','Other']]
        widgets = {
            'tool_photo': forms.FileInput(attrs={'onchange':'loadFile(event)','class':'form-control form-control-lg','id':'image','alt':'Chose Image','value':'','name':'image', 'accept':'image/png, image/jpeg , image/jpg'}),
            'location' : forms.TextInput(attrs={'class':'form-control form-control-sm mb-3','required':'required','placeholder':'Add location','id':'location','aria-label':".form-control-sm example"}),
            'tool_type' : forms.Select(attrs={'class':'form-select form-select-sm mb-3','required':'required','placeholder':'Select from list','id':'tool_type','aria-label':".form-select-sm example"},choices=types),
            'tool_spec_1' : forms.TextInput(attrs={'class':'form-control form-control-sm mb-3','required':'required','placeholder':'Specification 1 ,hp , wires','id':'line1','aria-label':".form-control-sm example"}),
            'tool_spec_2' : forms.TextInput(attrs={'class':'form-control form-control-sm mb-3','required':'required','placeholder':'Specification 2 , power , engine','id':'line2','aria-label':".form-control-sm example"}),
            'tool_info' : forms.Textarea(attrs={'class':'form-control','required':'required','id':'tool_desc'}),
            'rent_price' : forms.NumberInput(attrs={'class':'form-control form-control-sm mb-3','required':'required','placeholder':'Booking Price i.e 800rs/day','id':'rent_price','aria-label':".form-control-sm example"}),
        }
        