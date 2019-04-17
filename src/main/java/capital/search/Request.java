package capital.search;

public class Request {

  private String planName;

  private String sponsorName;

  private String sponsorState;

  public void setPlanName(String planName) {
    this.planName = planName;
  }

  public String getPlanName() {
    return this.planName;
  }

  public void setSponsorName(String sponsorName) {
    this.sponsorName = sponsorName;
  }

  public String getSponsorName() {
    return this.sponsorName;
  }

  public void setSponsorState(String sponsorState) {
    this.sponsorState = sponsorState;
  }

  public String getSponsorState() {
    return this.sponsorState;
  }
}
