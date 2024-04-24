using Microsoft.AspNetCore.Mvc;
using System;

namespace HoraApi.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class DateTimeController : ControllerBase
    {
        [HttpGet(Name = "GetDateTime")]
        public IActionResult GetDateTime()
        {
            var currentDateTime = DateTime.Now;
            return Ok(currentDateTime);
        }
    }
}
