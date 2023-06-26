using Bogus;
using Kmpt.WorkExperience.PatientApi;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.

app.UseSwagger();
app.UseSwaggerUI();

app.MapGet("/patients", (int count) =>
{
    var patients = new Faker<PatientInfo>()
        .RuleFor(u => u.Gender, f => f.PickRandom<Bogus.DataSets.Name.Gender>())
        .RuleFor(u => u.Email, (f, u) => f.Internet.Email(u.FirstName, u.LastName))
        .RuleFor(u => u.FirstName, (f, u) => f.Name.FirstName(u.Gender))
        .RuleFor(u => u.LastName, (f, u) => f.Name.LastName(u.Gender))
        .RuleFor(u => u.NhsNumber, f => f.Random.ReplaceNumbers("### ### ####"));
    return patients.Generate(count);
});

app.Run();
