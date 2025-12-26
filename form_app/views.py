from django.urls import reverse
from django.db import transaction
import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import StudentSubmission
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime, timedelta


# View for the form submission page (PUBLIC - no login needed)
def form_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        course = request.POST.get('course')
        
        if name and contact and course:
            StudentSubmission.objects.create(
                name=name,
                contact=contact,
                course=course,
                status='pending'
            )
            messages.success(request, 'Submission successful!')
            return redirect('form_app:form_page')
    
    return render(request, 'form_app/index.html')


# Login View
def login_view(request):
    if request.user.is_authenticated:
        return redirect('form_app:management_system')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('form_app:management_system')
    else:
        form = AuthenticationForm()
    
    return render(request, 'form_app/login.html', {'form': form})


# Logout View
def logout_view(request):
    logout(request)
    return redirect('form_app:login_view')


# Management System View with Pagination & Search (PROTECTED)
# 


# Update the management_system view in views.py:

# Update the management_system view:

@login_required
def management_system(request):
    # Get search query from URL parameters
    search_query = request.GET.get('q', '')

    # Get section parameter for pagination
    section = request.GET.get('section', 'dashboard')

     # Get status filter
    status_filter = request.GET.get('status', '')
    
    # Start with all submissions ordered by latest first
    submissions = StudentSubmission.objects.all().order_by('-created_at')

     # Apply status filter if specified
    if status_filter in ['pending', 'processed']:
        submissions = submissions.filter(status=status_filter)
    
    # Apply search filter if query exists
    if search_query:
        submissions = submissions.filter(
            Q(name__icontains=search_query) | 
            Q(course__icontains=search_query) |
            Q(contact__icontains=search_query)
        )
    
    # Pagination - 10 per page
    paginator = Paginator(submissions, 10)
    page_number = request.GET.get('page', 1)
    
    try:
        students = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        students = paginator.page(paginator.num_pages)
    
    
    
     # Counts for statistics
    total_count = StudentSubmission.objects.count()
    pending_count = StudentSubmission.objects.filter(status='pending').count()
    processed_count = StudentSubmission.objects.filter(status='processed').count()  

    
    # ... [keep existing code for search, pagination, etc. until line with new_submissions_count] ...
    
    # REMOVE all the complex notification tracking code
    
    # SIMPLE: Just use pending count for notifications
    # pending_count = StudentSubmission.objects.filter(status='pending').count()
    context = {
        'students': students,
        'search_query': search_query,
        'total_count': total_count,
        'pending_count': pending_count,
        'processed_count': processed_count,
        'new_submissions_count': pending_count,  # Notifications show pending count
        'new_submissions': StudentSubmission.objects.filter(status='pending').order_by('-created_at')[:10],
        'section': section,
        'status_filter': status_filter,  # Add this to context
    }
    
    return render(request, 'form_app/management.html', context)
    
   
   
     
    
   
    
   
        
    
  
    
   
    
   


# Add this new view for marking notifications as read



# Delete Student View (PROTECTED)
@login_required
def delete_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(StudentSubmission, id=student_id)
        student.delete()
        messages.success(request, 'Submission deleted successfully')
        
        # Get current page and search query to stay on same page
        page = request.POST.get('page', 1)
        search_query = request.POST.get('search_query', '')
        
        return redirect(f"{reverse('form_app:management_system')}?section=leads&page={page}&q={search_query}")
    
    return redirect('form_app:management_system')


# Toggle Status View (PROTECTED)
@login_required
def toggle_status(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(StudentSubmission, id=student_id)
        new_status = request.POST.get('new_status')
        
        if new_status in ['pending', 'processed']:
            student.status = new_status
            student.updated_at = timezone.now()
            student.save()
            messages.success(request, f'Status updated to {new_status}')
        
        # Get current page and search query to stay on same page
        page = request.POST.get('page', 1)
        search_query = request.POST.get('search_query', '')
        
        return redirect(f"{reverse('form_app:management_system')}?section=leads&page={page}&q={search_query}")
    
    return redirect('form_app:management_system')


# Edit Student View (PROTECTED)
@login_required
def edit_student(request, student_id):
    student = get_object_or_404(StudentSubmission, id=student_id)
    
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.contact = request.POST.get('contact')
        student.course = request.POST.get('course')
        student.updated_at = timezone.now()
        student.save()
        messages.success(request, f'{student.name} updated successfully')
        
        # Get current page and search query to stay on same page
        page = request.POST.get('page', 1)
        search_query = request.POST.get('search_query', '')
        
        return redirect(f"{reverse('form_app:management_system')}?section=leads&page={page}&q={search_query}")
    
    return render(request, 'form_app/edit_student.html', {'student': student})

















# from django.shortcuts import render, get_object_or_404, redirect
# from .models import StudentSubmission
# from django.contrib import messages
# from django.utils import timezone
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.db.models import Q



# # View for the form submission page
# def form_page(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         contact = request.POST.get('contact')
#         course = request.POST.get('course')
        
#         if name and contact and course:
#             StudentSubmission.objects.create(
#                 name=name,
#                 contact=contact,
#                 course=course,
#                 status='pending'
#             )
#             messages.success(request, 'Submission successful!')
#             return redirect('form_app:form_page')
    
#     return render(request, 'form_app/index.html')


# # Management System View with Pagination & Search
# def management_system(request):
#     # Get search query from URL parameters
#     search_query = request.GET.get('q', '')
    
#     # Start with all submissions ordered by latest first
#     submissions = StudentSubmission.objects.all().order_by('-created_at')
    
#     # Apply search filter if query exists
#     if search_query:
#         submissions = submissions.filter(
#             Q(name__icontains=search_query) | 
#             Q(course__icontains=search_query) |
#             Q(contact__icontains=search_query)
#         )
    
#     # Pagination - 10 per page
#     paginator = Paginator(submissions, 10)
#     page_number = request.GET.get('page', 1)
    
#     try:
#         students = paginator.page(page_number)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page
#         students = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range, deliver last page
#         students = paginator.page(paginator.num_pages)
    
#     # Counts for statistics
#     total_count = StudentSubmission.objects.count()
#     pending_count = StudentSubmission.objects.filter(status='pending').count()
#     processed_count = StudentSubmission.objects.filter(status='processed').count()
    
#     context = {
#         'students': students,
#         'search_query': search_query,
#         'total_count': total_count,
#         'pending_count': pending_count,
#         'processed_count': processed_count,
#     }
    
#     return render(request, 'form_app/management.html', context)


# def delete_student(request, student_id):
#     if request.method == 'POST':
#         student = get_object_or_404(StudentSubmission, id=student_id)
#         student.delete()
#         messages.success(request, 'Submission deleted successfully')
#         return redirect('form_app:management_system')
#     return redirect('form_app:management_system')


# def toggle_status(request, student_id):
#     if request.method == 'POST':
#         student = get_object_or_404(StudentSubmission, id=student_id)
#         new_status = request.POST.get('new_status')
        
#         if new_status in ['pending', 'processed']:
#             student.status = new_status
#             student.updated_at = timezone.now()
#             student.save()
#             messages.success(request, f'Status updated to {new_status}')
        
#         return redirect('form_app:management_system')
#     return redirect('form_app:management_system')


# def edit_student(request, student_id):
#     student = get_object_or_404(StudentSubmission, id=student_id)
    
#     if request.method == 'POST':
#         student.name = request.POST.get('name')
#         student.contact = request.POST.get('contact')
#         student.course = request.POST.get('course')
#         student.updated_at = timezone.now()
#         student.save()
#         messages.success(request, f'{student.name} updated successfully')
#         return redirect('form_app:management_system')
    
#     return render(request, 'form_app/edit_student.html', {'student': student})








# # def management_system(request):
# #     submissions = StudentSubmission.objects.all()
    
# #     # DEBUG: Print to console
# #     print("=" * 50)
# #     print("DEBUG: management_system view called")
# #     print(f"DEBUG: Number of submissions in database: {submissions.count()}")
# #     for sub in submissions:
# #         print(f"DEBUG: - {sub.id}: {sub.name} ({sub.course})")
# #     print("=" * 50)