import "survey-core/modern.min.css";
import { Model } from "survey-core";
import { Survey } from "survey-react-ui";
const surveyJson = {
  elements: [
    {
      name: "Date Time Local",
      title: "Enter your local date and time:",
      type: "text",
      inputType: "datetime-local",
      isRequired: true,
    },
  ],
};

export default function DateTimeLocal() {
  const survey = new Model(surveyJson);
  return (
    <>
      <h1>Datetime Local</h1>
      <Survey model={survey} />
    </>
  );
}
