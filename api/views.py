from rest_framework import generics
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
import openai


class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


    def get_answer_from_openai(self, question_text):
        # Отправляем запрос в OpenAI API и получаем ответ
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question_text,
            temperature=0,
            max_tokens=1
        )
        # Извлекаем текст ответа
        answer_text = response.choices[0].text.strip()

        return answer_text

    def perform_create(self, serializer):
        question_text = self.request.data.get('text', '')
        # Отправляем вопрос в OpenAI API и получаем ответ
        answer_text = self.get_answer_from_openai(question_text)
        question = serializer.save(text=question_text)
        Answer.objects.create(question=question, answer=answer_text)
