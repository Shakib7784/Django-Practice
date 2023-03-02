//creating function for calling income, food, rent and cloth
function IncomeExpense( amount)
{
    const getamount = document.getElementById(amount).value;
    const finalAmount = parseFloat(getamount);
    return finalAmount;
}
//creating functin for all calculation except savings
function IncomeExpense_Cal ()
{
    const totalExpense = document.getElementById("expense");
    const Balance = document.getElementById("remaining");
    // calling valid message 
    const valid1 = document.getElementById("valid1");
    const valid2 = document.getElementById("valid2");
    const valid3 = document.getElementById("valid3");
    const valid4 = document.getElementById("valid4");
    if(isNaN(IncomeExpense("income")) || IncomeExpense("income")<0)
    {
        valid1.style.display="block";
    }
    else
    {
        valid1.style.display="none";
    }
     if(isNaN(IncomeExpense("food")) || IncomeExpense("food")<0)
    {
        valid2.style.display="block";
    }
    else
    {
        valid2.style.display="none";
    }
    if(isNaN(IncomeExpense("rent")) || IncomeExpense("rent")<0)
    {
        valid3.style.display="block";
    }
    else
    {
        valid3.style.display="none";
    }
     if(isNaN(IncomeExpense("cloth")) || IncomeExpense("cloth")<0)
    {
        valid4.style.display="block";
    }
    else 
    {
        const total = (IncomeExpense("food")+IncomeExpense("rent")+IncomeExpense("cloth"));
        totalExpense.innerText=total;
        //calling higher expense error message
        const higherExpense = document.getElementById("higher_expense");
        if(total>IncomeExpense("income"))
        {
            console.log("expense is higher");
            higherExpense.style.display="block"

        }
        else
        {
            Balance.innerText = IncomeExpense("income")-total;
            higherExpense.style.display="none"
        }
        valid4.style.display="none";
     
    }
    return Balance.innerText;
}
// creating function for savings calculations
function Savings()
{
    const SaveParcent = document.getElementById("input_save").value;
    SaveParcent.value = "";
    //validity check
    const valid5 = document.getElementById("valid5");
    if(isNaN(SaveParcent)|| SaveParcent<0)
    {
        valid5.style.display="block";
    }
    else
    {
    const leftAmount = document.getElementById("left");
    const finalSaveParcent = parseFloat(SaveParcent);
   
    const SavingAmount = document.getElementById("save");
    const SavingAmountFianl = (IncomeExpense("income")*finalSaveParcent)/100;
    SavingAmount.innerText= SavingAmountFianl;
    //checking save amount is greater than remaining amount or not
    const savingMessage = document.getElementById("saving_message");
    if(SavingAmountFianl>IncomeExpense_Cal())
    {
        savingMessage.style.display="block";   
    }
    else
    {
        leftAmount.innerText = (IncomeExpense_Cal()-SavingAmount.innerText);
        savingMessage.style.display="none";
    }
         valid5.style.display="none";
    }
    
}

document.getElementById("calculate").addEventListener("click",function(){
    IncomeExpense_Cal();

})

document.getElementById("savebutton").addEventListener("click",function(){

    Savings();
    
})