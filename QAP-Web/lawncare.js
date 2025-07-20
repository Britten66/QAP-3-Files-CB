


// Desc: Mo's Lawncare Service Invoice Calculator 
// Author: Christopher Britten
// Dates: 07/15/2025



var $ = function (id) {
  return document.getElementById(id);
};


// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per2Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});


// Define program constants.

const BORDER_PERCENT = 0.04;

const BORDER_RATE = 0.35;

const LAWN_PERC = 0.95;

const LAWN_RATE = 0.07;

const FERT_RATE = 0.05;



// Tax Rate Here

const HST_RATE = 0.15;

const ENV_TAX_RATE = 0.014;



// Grabbing inputs from customer 

  let custName =  prompt("Enter The Customer Name: ");

  let custLast =  prompt("Enter The Customer Last Name: ");

  let stAdd =  prompt("Enter Street Address: ");

  let city = prompt("Enter The City: ");

  let phone = prompt("Enter The Customer Phone Number (9999999)")

  let formatttedPhone = phone.slice(0,3) + "-" + phone.slice(3,6) + "-" + phone.slice(6,11);
  
  let custSqFt = parseFloat(prompt("Enter The Square Footage: "));

   if (custSqFt > 0) {

     let borderSqFt = custSqFt * BORDER_PERCENT;

     let borderCharge = borderSqFt * BORDER_RATE

     let lawnSqFt = custSqFt * LAWN_PERC;

     let lawnCharge = lawnSqFt * LAWN_RATE;

     let fertCharge = custSqFt * FERT_RATE;

     let servTotal = borderCharge + lawnCharge + fertCharge;

     let hst = servTotal * HST_RATE;  

     let envFee = servTotal * ENV_TAX_RATE;

     let grandTotal = servTotal + hst + envFee;



    // Output Table Seciton Start

    document.writeln("<table class = 'invoicetable'>");
    // Header Here
    
    document.writeln("<tr class = 'headerVert'>")
    document.writeln("<td colspan= '2'>Mo's Lawncare Services - Customer Invoice</td>");
    document.writeln("</tr>");


    // formatting to line up everything 
    document.writeln("<tr>")
    document.writeln("<td colspan = '2' class = 'left-align'>");
    
    document.writeln("<br/> Customer Details: </br></br>");

    


    // Customer Detail
    document.writeln("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + custName +" " +custLast + "<br/>")
    document.writeln("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + stAdd + "<br/>")
    document.writeln("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + city + ",  " + formatttedPhone + "<br/></br>")

    document.writeln("Property Size (In Sq Ft): " + custSqFt +" Sqft" + "<br/></br>")
    
   
    
    


    document.writeln("</td>");
    document.writeln("</tr>");

    
    // border cost
    document.writeln("<tr><td> Border Cost:</td><td class ='right-align'>" + cur2Format.format(borderCharge) + "</td></tr>");
    

    // Moving Cost Here
    document.writeln("<tr><td> Mowing Cost:</td><td class ='right-align'>" + cur2Format.format(lawnCharge) + "</td></tr>");
    // Fertilizer Cost 
    document.writeln("<tr><td> Fertilizer Cost:</td><td class ='right-align'>" + cur2Format.format(fertCharge) + "</td></tr>");   
    
        // Empty Row 
    document.writeln("<tr>");
    document.writeln("<td class='blankline' >&nbsp;</td>");
    document.writeln("</tr>");
    

    //Total Charge
    document.writeln("<tr><td> Total Cost:</td><td class ='right-align'>" + cur2Format.format(servTotal) + "</td></tr>");   

    // Empty Row 
    document.writeln("<tr>");
    document.writeln("<td class='blankline'>&nbsp;</td>");
    document.writeln("</tr>");


    // HST Here
    document.writeln("<tr><td> Sales Tax (HST):</td><td class ='right-align'>" + cur2Format.format(hst) + "</td></tr>");   


    // Enviromental fee
    document.writeln("<tr><td>Enviromental Cost:</td><td class ='right-align'>" + cur2Format.format(envFee) + "</td></tr>");   

    // Empty line
    document.writeln("<tr>");
    document.writeln("<td class='blankline' >&nbsp;</td>");
    document.writeln("</tr>");



    // Invoice total Here
    document.writeln("<tr><td>Invoice Total:</td><td class ='right-align'>" + cur2Format.format(grandTotal) + "</td></tr>");   


    //Footer 
    document.writeln("<tr>");
    document.writeln("<td colspan = '2' class='footer' >Turning Lawns Into Landscapes  </td>")
    document.writeln("</tr>");


     }else{
      alert("Please Enter a valid Square Footage Greater Than 0")
    }
  



 

