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



    // Output Table Seciton Starts 


    document.writeln("<br/>");
    document.writeln("<table style = 'width: 400px; border-collapse: collapse; font-family: sans-serif; border: 1px solid black;'>");

    // Header Here
    document.writeln("<tr style='background-color: #f6c600; color: black;'> ");
    document.writeln("<td colspan= '2' style='padding: 10px; font-weight: bold;'>Mo's Lawncare Services - Customer Invoice</td>");
    document.writeln("</tr>");

    // Customer Detail Block
    document.writeln("<tr><td colspan = '2' style = ' padding: 10px;'>")
    document.writeln("Customer Details: <br/>");
    document.writeln(custName + "<br/>");
    document.writeln(stAdd + "<br/>");
    document.writeln(city + " " + phone + "<br/>")
    document.writeln("Property size (in sw ft): " + custSqFt + " SqFt");
    document.writeln("</td></tr>")

     // Cost Row
    // border cost
    document.writeln("<tr><td style = ' border: 1px solid black; padding: 6px; '> Border Cost </td>");
    document.writeln("<td style ='border: 1px solid black; text align: right; padding: 6px;'>" + cur2Format.format(borderCharge) + "</td></tr>");

    // Moving Cost Here
    document.writeln("<tr><td style = ' border: 1px solid black; padding: 6px; '> Moving Cost </td>");
    document.writeln("<td style = 'border: 1px solid black; text-align: right; padding: 6px; '>" + cur2Format.format(lawnCharge) + "</td></tr>");

    // Fertilizer Cost 
    document.writeln("<tr><td style = ' border: 1px solid black; padding: 6px; '>Fertilizer Cost</td>");
    document.writeln("<td style = 'border: 1px solid black; text-align: right; padding: 6px; '>" + cur2Format.format(fertCharge) + "</td></tr>");

    //Total Charge
    document.writeln("<tr><td style = ' border: 1px solid black; padding: 6px; '> Total Cost </td>");
    document.writeln("<td style = 'border: 1px solid black; text-align: right; padding: 6px; '>" + cur2Format.format(servTotal) + "</td></tr>");

    // HST Here
    document.writeln("<tr><td style = ' border: 1px solid black; padding: 6px; '> Sales Tax (HST) </td>");
    document.writeln("<td style = 'border: 1px solid black; text-align: right; padding: 6px; '>" + cur2Format.format(hst) + "</td></tr>");

    // Enviromental fee
    document.writeln("<tr><td style = ' border: 1px solid black; padding: 6px; '> Enviromental Tax </td>");
    document.writeln("<td style = 'border: 1px solid black; text-align: right; padding: 6px; '>" + cur2Format.format(envFee) + "</td></tr>");

    // Invoice total Here

    document.writeln("<tr><td style = ' border: 1px solid black; padding: 6px; font-weight: bold;'> Invoice Total </td>");
    document.writeln("<td style = 'border: 1px solid black;  text-align: right; padding: 6px; font-weight: bold; '>" + cur2Format.format(grandTotal) + "</td></tr>");

    //Footer 
    document.writeln("<tr style='background-color: #f6c600; color: black; font-weight bold;'> ");
    document.writeln("<td colspan = '2' style = 'text-align: center; padding: 10px; font-weight bold; '>Turning Lawns Into Landscapes  </td>")
    document.writeln("</tr>");


     }else{
      alert("Please Enter a valid Swuare FDFootage Greater Than 0")
    }
  



