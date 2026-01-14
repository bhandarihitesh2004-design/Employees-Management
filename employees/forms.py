from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id', 'name', 'email', 'phone', 'department', 'role', 'salary', 'date_joined', 'status']
        widgets = {
            'date_joined': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary is not None and salary < 0:
            raise forms.ValidationError('Salary must be non-negative')
        return salary
