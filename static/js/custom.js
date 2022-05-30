function validate()
{
     var username=document.getElementById('name').value;
     var subject=document.getElementById('subject').value;
     var email=document.getElementById('email').value;
     var atposition=email.indexOf('@');
     var dotposition=email.indexOf('.');
     
     if(username == "")
     {
          alert("Please enter name");
     }else if(!isNaN(username))
     {
          alert("Please enter only alphabets");
     }else if(email == "")
     {
          alert("Please enter email");
     }else if(atposition<1 || dotposition<atposition+2|| dotposition+2>=email.length)
     {
          alert("Please enter valid email");
     }else if(subject == "")
     {
          alert("Please enter subject");
     }else if(!isNaN(subject))
     {
          alert("Please enter only alphabets");
     }else
     {
      document.getElementById('contactus_form').submit();
     }
}
function validateregister()
{
           var fname=document.getElementById('fname').value;
           var lname=document.getElementById('lname').value;
           var password=document.getElementById('password').value;
           var email=document.getElementById('email').value;
           var mobile=document.getElementById('mobile_no').value;
           
           var atposition=email.indexOf('@');
           var dotposition=email.indexOf('.');
           
           if(fname == "")
           {
                         alert("Please enter username");
           }else if(!isNaN(fname))
           {
                         alert("Please enter only alphabets");
           }else if(lname == "")
           {
                         alert("Please enter password");
           }else if(!isNaN(lname))
           {
                         alert("Please enter only alphabets");
           }
           else if(password == "")
           {
                         alert("Please enter password");
           }
           else if(email == "")
           {
                         alert("Please enter email");
           }else if(atposition<1 || dotposition<atposition+2|| dotposition+2>=email.length)
          {
                         alert("Please enter valid email");
          }else if(mobile == "")
          {
                         alert("Please enter mobile no");
          }else if(isNaN(mobile))
          {
                         alert("Please enter valid mobile number");
          }else
          {
               document.getElementById('signup_form').submit();
          }
}
function adminloginvalidate()
{
           var username=document.getElementById('username').value;
           
            if(username == "")
           {
                         alert("Please enter username");
           }else if(!isNaN(username))
           {
                         alert("Please enter only alphabets");
           }
           else
          {
               document.getElementById('adminlogin_form').submit();
          }
}

function userloginvalidate()
{
          var email=document.getElementById('email').value;
          
          var atposition=email.indexOf('@');
          var dotposition=email.indexOf('.');
          if(email == "")
           {
                         alert("Please enter email");
           }else if(atposition<1 || dotposition<atposition+2|| dotposition+2>=email.length)
          {
                         alert("Please enter valid email");
          }
          else
          {
               document.getElementById('userlogin_form').submit();
          }
              
}