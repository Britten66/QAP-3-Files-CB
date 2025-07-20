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

const LAWN = 0.95;

const LAWN_RATE = 0.07;

const FERT_RATE = 0.05;



// Tax Rate Here

const HST_RATE = 0.15;

const ENV_TAX_RATE = 0.014;



// Grabbing inputs from customer 

  let custName = "Chris"; // prompt("Enter The Membership Number: ". "99999");

  let stAdd = "123 Main St"; // prompt("Enter The Membership Number: ". "99999");

  let city = "St. John's"; //prompt("Enter The Membership Number: ". "99999");

  let phone = "123456789"; //parsefloat prompt("")
  
  let custSqFt = 2000 //prompt("Enter The Membership Number: ". "99999");

   if (custSqFt > 0) {

     let borderSqFt = custSqFt * BORDER_PERCENT;

     let borderCharge = borderSqFt * BORDER_RATE

     let lawnSwFt = custSqFt * LAWN;

     let lawnCharge = custSqFt * LAWN_RATE;

     let fertCharge = custSqFt * FERT_RATE;

     let servTotal = borderCharge + lawnCharge + fertCharge;

      let hst = servTotal * HST_RATE;  

     let envFee = servTotal * ENV_TAX_RATE;

     let grandTotal = servTotal + hst + envFee;



    // Output Table Seciton Start

    document.writeln("<table class = 'invoicetable'>");
    // Header Here
    document.writeln("<tr>")
    document.writeln("<tr class = 'headerVert'>")
    document.writeln("<td colspan= '2' class='invoiceVert'>Mo's Lawncare Services - Customer Invoice</td>");
    document.writeln("</tr>");

    // Customer Detail
    document.writeln("<tr>")
    document.writeln("<td colspan = '2'>")
    document.writeln("Customer Details: <br/>");
    document.writeln(custName + "<br/>");
    document.writeln(stAdd + "<br/>");
    document.writeln(city + " " + phone + "<br/>")
    document.writeln("Property size (in sw ft): " + custSqFt + " SqFt");
    document.writeln("</td>");
    document.writeln("</tr>");

    
    // border cost
    document.writeln("<tr><td> Border Cost:</td><td>$" + borderCharge.toFixed(2) + "</td></tr>");
    

    // Moving Cost Here
    document.writeln("<tr><td> Mowing Cost:</td><td>$" + lawnCharge.toFixed(2) + "</td></tr>");
    // Fertilizer Cost 
    document.writeln("<tr><td> Fertilizer Cost:</td><td>$" + fertCharge.toFixed(2) + "</td></tr>");   
    
        // Empty Row 
    document.writeln("<tr>");
    document.writeln("<tr><td colspan='2' class='blankrow' >&nbsp;</td></tr>");
    
    

    //Total Charge
    document.writeln("<tr><td> Total Cost:</td><td>$" + servTotal.toFixed(2) + "</td></tr>");   

    // Empty Row 
    document.writeln("<tr>");
    document.writeln("<td colspan='2' class='blankrow' >&nbsp;</td>");
    document.writeln("</tr>");
    // HST Here
    document.writeln("<tr><td> Sales Tax (HST):</td><td>$" + hst.toFixed(2) + "</td></tr>");   


    // Enviromental fee
    document.writeln("<tr><td>Enviromental Cost:</td><td>$" + envFee.toFixed(2) + "</td></tr>");   

    // Empty Row 

    document.writeln("<tr><td colspan='2' class='blankrow' >&nbsp;</td></tr>");
    
    // Invoice total Here
    document.writeln("<tr><td>Invoice Total:</td><td>$" + grandTotal.toFixed(2) + "</td></tr>");   


    //Footer 
    document.writeln("<tr>");
    document.writeln("<td colspan = '2' class='footer'>Turning Lawns Into Landscapes  </td>")
    document.writeln("</tr>");


     }else{
      alert("Please Enter a valid Square Footage Greater Than 0")
    }
  



 

