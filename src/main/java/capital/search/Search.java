package capital.search;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

public class Search implements RequestHandler<Request, String> {

  @Override
  public String handleRequest(Request request, Context context) {

    String url="https://search-testcapital-zekiodzquu4fawrsu7pi6z5hfy.us-west-1.es.amazonaws.com/testcapital/_search";
    if(request.getPlanName()!=null){
      try {
        url+="?q=PLAN_NAME:\""+URLEncoder.encode(request.getPlanName(), "UTF-8")+"\"";
      } catch (UnsupportedEncodingException e) {
        e.printStackTrace();
      }
    }

    if(request.getSponsorName()!=null){
      try {
        url+="?q=SPONSOR_DFE_NAME:\""+URLEncoder.encode(request.getSponsorName(), "UTF-8")+"\"";
      } catch (UnsupportedEncodingException e) {
        e.printStackTrace();
      }

    }
    if(request.getSponsorState()!=null){
      try {
        url+="?q=SPONS_DFE_MAIL_US_STATE:\""+URLEncoder.encode(request.getSponsorState(), "UTF-8")+"\"";
      } catch (UnsupportedEncodingException e) {
        e.printStackTrace();
      }
    }

    StringBuffer response = new StringBuffer();
    JSONObject json = null;
    try {
      URL obj= new URL(url);
      System.out.println(url);
      HttpURLConnection con= (HttpURLConnection) obj.openConnection();
      con.setRequestMethod("GET");
      BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
      String inputLine;
      while((inputLine = in.readLine()) != null){
        response.append(inputLine);
      }
    } catch (Exception e) {
      e.printStackTrace();
    }

    if (response == null) {
      return null;
    }

    return response.toString();
  }
}
