<!-- components/NewsSection.vue -->
<template>
  <section>
    <header>
      <h1>인공지능이 영향을 미칠 직업들</h1>
    </header>

    <article>
      <h2>인공지능의 급속한 발전, 우리의 직업은 안전한가?</h2>
      <p>
        인공지능(AI)은 기술 혁신의 중심에 있으며, 그 영향력은 이미 다양한 산업에 걸쳐 확산되고 있습니다.
        특히 <span class="highlight">자동화와 머신러닝</span> 기술은 업무 효율성을 극대화하고 있지만,
        동시에 일부 직업의 변화 또는 사라짐을 예고하고 있습니다. 그렇다면, AI가 가장 큰 영향을 미칠 직업들은 무엇일까요?
      </p>

      <h2>AI의 영향을 받을 직업군</h2>
      <p>
        많은 전문가들은 AI가 주로 반복적이고 정형화된 작업을 수행하는 직업에 큰 영향을 미칠 것이라 예측하고 있습니다.
        아래는 그 중 일부 주요 직업들입니다:
      </p>
      <div class="job-impact">
        <ul>
          <li><strong>제조업 근로자:</strong> 이미 로봇 자동화가 공장에서 많은 업무를 대체하고 있으며, AI가 더 정교한 작업을 수행할 수 있게 되면 이 추세는 가속화될 것입니다.</li>
          <li><strong>콜센터 상담원:</strong> AI 챗봇과 음성 인식 기술이 발전함에 따라, 고객 문의 응대 업무는 점점 자동화되고 있습니다.</li>
          <li><strong>은행원 및 회계사:</strong> 금융 데이터 분석 및 반복적인 회계 업무는 AI의 주력 분야 중 하나로, 자동화 도입이 늘어나고 있습니다.</li>
          <li><strong>운송업 종사자:</strong> 자율 주행 기술이 상용화되면 택시 운전사, 트럭 운전사 등 운송업 종사자들이 직격탄을 맞을 수 있습니다.</li>
        </ul>
      </div>

      <h2>미래를 준비하는 자세</h2>
      <p>
        그러나 모든 직업이 위험에 처한 것은 아닙니다. AI의 발전에도 불구하고, 창의성, 문제 해결 능력, 감성 지능을 필요로 하는
        직업은 여전히 인간의 역할이 중요할 것입니다. AI와의 공존을 위해 우리는 지속적으로 <span class="highlight">새로운 기술을 배우고 적응</span>하는 능력을 키워야 합니다.
      </p>
    </article>

    <footer>
      <p>Copyright &copy; 2024 미래 직업 탐구. All rights reserved.</p>
    </footer>
  </section>
</template>

<script>
export default {

}
</script>

<style scoped>
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  color: #333;
  line-height: 1.6;
  margin: 0;
  padding: 20px;
}

header {
  background-color: #008cba;
  color: white;
  padding: 10px 0;
  text-align: center;
}

header h1 {
  margin: 0;
  font-size: 2.5rem;
}

article {
  background-color: white;
  padding: 20px;
  margin: 20px auto;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  max-width: 800px;
}

h2 {
  color: #008cba;
  margin-bottom: 10px;
}

.highlight {
  background-color: #ffffcc;
  padding: 0 5px;
}

p {
  margin-bottom: 15px;
}

.job-impact {
  padding-left: 20px;
  margin-bottom: 10px;
}

.job-impact ul {
  list-style-type: disc;
  margin: 0;
}

footer {
  text-align: center;
  margin-top: 20px;
  font-size: 0.9rem;
  color: #777;
}
</style>