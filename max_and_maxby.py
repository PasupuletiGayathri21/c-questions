using System;
using System.Collections.Generic;
using System.Linq;

class Student
{
    public string Name { get; set; }
    public int Marks { get; set; }
    public string Course { get; set; }
}

class Program
{
    static void Main()
    {
        List<Student> students = new List<Student>
        {
            new Student { Name = "Amit", Marks = 78, Course = "CSE" },
            new Student { Name = "Priya", Marks = 92, Course = "CSE" },
            new Student { Name = "Rahul", Marks = 65, Course = "ECE" },
            new Student { Name = "Meera", Marks = 88, Course = "ECE" }
        };

        // Maximum marks
        int x = students.Max(s => s.Marks);

        // Student with maximum marks
        Student y = students.OrderByDescending(s => s.Marks).First();

        Console.WriteLine("Maximum Marks: " + x);
        Console.WriteLine("Student Name: " + y.Name);
        Console.WriteLine("Marks: " + y.Marks);
        Console.WriteLine("Course: " + y.Course);
    }
}