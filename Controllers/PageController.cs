using Microsoft.AspNetCore.Mvc;

namespace Demo.Controllers;

public class PageController : Controller
{
    public IActionResult Home()
    {
        ViewData["Title"] = "Home";
        return View("/Views/Page/Index.cshtml");
    }

    public IActionResult Jobs()
    {
        ViewData["Title"] = "Jobs";
        return View();
    }

    public IActionResult Companies()
    {
        ViewData["Title"] = "Companies";
        return View();
    }

    public IActionResult Contact()
    {
        ViewData["Title"] = "Contact";
        return View();
    }
}