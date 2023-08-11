import "./App.css";
import "survey-core/modern.min.css";
import { Model } from "survey-core";
import { Survey } from "survey-react-ui";
const surveyJson = {
  elements: [
    {
      name: "FirstName",
      title: "Enter your first name:",
      type: "text",
    },
    {
      name: "LastName",
      title: "Enter your last name:",
      type: "text",
    },
    {
      name: "Email",
      title: "Enter your email:",
      inputType: "email",
      type: "text",
    },
    {
      name: "Age",
      title: "Enter your age:",
      type: "text",
      inputType: "number",
      isRequired: true,
      min: 1,
      max: 100,
    },
    {
      name: "Color",
      title: "Select your favorite color:",
      type: "text",
      inputType: "color",
    },
    {
      name: "Date",
      title: "Enter your date of birth:",
      type: "text",
      inputType: "date",
      isRequired: true,
    },
    {
      name: "Date Time Local",
      title: "Enter your date and time:",
      type: "text",
      inputType: "datetime-local",
      isRequired: true,
    },
    {
      name: "Month",
      type: "text",
      inputType: "month",
      title: "Enter your birth month:",
      isRequired: true,
    },
    {
      name: "Time",
      type: "text",
      inputType: "time",
      title: "Enter your birth time:",
      isRequired: true,
    },
    {
      name: "Url",
      type: "text",
      inputType: "url",
      title: "Enter your website:",
    },
    {
      name: "Phone",
      type: "text",
      inputType: "tel",
      title: "Enter your phone number:",
    },
    {
      Name: "Week",
      type: "text",
      inputType: "week",
      title: "Enter your week:",
    },
    {
      Name: "Disabled",
      type: "text",
      inputType: "text",
      title: "Disabled:",
      enableIf: "1 > 2",
    },
  ],
};

function App() {
  const survey = new Model(surveyJson);
  return (
    <>
      <h1>Survey JS</h1>
      <Survey model={survey} />
    </>
  );
}

export default App;
