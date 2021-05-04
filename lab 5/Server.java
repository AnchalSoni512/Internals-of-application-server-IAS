import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class Server_ extends HttpServlet
{
  private String s;
  public void init()
  {

  }
  public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException,IOException
  {
    response.setContentType("text/html");
    PrintWriter var=response.getWriter();
    var.println("<h2> Hello World to <h2>");
    var.println("<h2> Name:  "+request.getParameter("lname")+"</h2>");
    var.println("<h2> Host:  " + request.getServerName()+"</h2>");
    var.println("<h2> Port:  " + request.getServerPort()+"</h2>");

  }
  public void doPost(HttpServletRequest req, HttpServletResponse res) throws ServletException,IOException
  {
    doGet(req,res);
  }

  public void destroy()
  {}

}
