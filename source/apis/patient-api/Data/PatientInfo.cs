using static Bogus.DataSets.Name;

namespace Kmpt.WorkExperience.PatientApi;

public record PatientInfo
{
    public string NhsNumber { get; set; } 
    public string FirstName { get; set; } 
    public string LastName { get; set; } 
    public string Email { get; set; } 
    public Gender Gender { get; set; }
}