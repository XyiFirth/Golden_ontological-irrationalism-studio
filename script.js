const PHI = 1.618;

const ontologyTaxonomy = {
  인간: ["기억", "신체", "관계"],
  장소: ["편의점", "지하철", "골목", "방"],
  사물: ["우산", "영수증", "컵라면", "휴대폰", "문자"],
  감정: ["미련", "불안", "죄책감", "향수", "해방감", "수치심"],
  시간: ["새벽", "목요일", "비", "반복"]
};

const irrationalOperators = [
  "category betrayal",
  "object consciousness",
  "time inversion",
  "sensory crossing",
  "causal collapse",
  "symbolic excess",
  "fragmented memory"
];

const transformations = {
  편의점: ["기억을 보관하는 장기", "새벽이 입원한 병실", "도시가 잠깐 꾸는 꿈"],
  비: ["읽지 않은 문자의 날씨", "하늘에서 떨어지는 미해결 대화", "젖은 시간의 알리바이"],
  문자: ["비가 인간의 언어를 흉내 낸 것", "도착하지 않기 위해 도착한 문장", "작은 검은 우편함에 갇힌 심장"],
  우산: ["접힌 척하는 검은 새", "비를 막는 대신 기억을 접는 도구", "하늘과 인간 사이의 임시 계약서"],
  영수증: ["미래가 과거에게 남긴 유서", "가격 대신 죄책감이 찍힌 흰 혀", "오늘이 자기 자신을 증명하려고 뱉은 종이"],
  컵라면: ["끓는 형태의 위로", "3분 동안만 허락되는 가짜 집", "소금과 열로 만든 작은 심리상담실"],
  휴대폰: ["아직도 과거의 이름을 발음하는 작은 관", "손바닥에 묻힌 검은 신탁", "꺼지지 않는 사적인 신호등"],
  연인: ["목요일마다 재생되는 오류", "사람의 형식을 빌린 반복", "끝났다고 말할수록 시작되는 문법"],
  죄책감: ["안쪽으로 내리는 비", "심장이 만든 그림자", "입 밖으로 나오지 못한 영수증"],
  미련: ["문 닫힌 가게의 불빛", "이미 접힌 우산을 다시 펼치려는 손", "시간이 버리지 못한 작은 열"],
  불안: ["형광등 아래에서 자라는 새", "아직 일어나지 않은 일이 내는 발소리", "문이 열리기 전에 먼저 들어오는 바람"],
  향수: ["오래된 냄새가 입는 옷", "돌아갈 수 없어서 더 정확해지는 지도", "어제의 물컵에 남은 달빛"],
  해방감: ["잠금이 풀린 새벽", "이름표를 떼어낸 바람", "목적지를 버린 발"],
  수치심: ["얼굴 안쪽에 켜진 붉은 전등", "타인의 눈을 빌려 보는 거울", "피부가 혼자 기억하는 문장"]
};

const state = { mutation: 0, lastPayload: null };
const $ = (selector) => document.querySelector(selector);
const $$ = (selector) => [...document.querySelectorAll(selector)];

function hashString(input) {
  let hash = 2166136261;
  for (let i = 0; i < input.length; i += 1) {
    hash ^= input.charCodeAt(i);
    hash += (hash << 1) + (hash << 4) + (hash << 7) + (hash << 8) + (hash << 24);
  }
  return hash >>> 0;
}

function seededRandom(seed) {
  let value = seed || 1;
  return function rand() {
    value = (value * 1664525 + 1013904223) >>> 0;
    return value / 4294967296;
  };
}

function pick(list, rand) {
  return list[Math.floor(rand() * list.length) % list.length];
}

function splitTerms(value) {
  return value.split(/[,.，、/|\n]+/).map((term) => term.trim()).filter(Boolean);
}

function getActiveEmotions() {
  return $$("#emotionChips button.active").map((button) => button.dataset.emotion);
}

function classifyTerm(term, emotions) {
  if (ontologyTaxonomy.감정.includes(term) || emotions.includes(term)) return "감정";
  if (["새벽", "목요일", "비", "밤", "낮", "아침", "반복"].some((token) => term.includes(token))) return "시간";
  if (["편의점", "지하철", "골목", "방", "도시", "거리"].some((token) => term.includes(token))) return "장소";
  if (["연인", "가족", "타인", "나", "너", "대화", "관계"].some((token) => term.includes(token))) return "인간/관계";
  return "사물";
}

function collectPayload() {
  const scene = $("#scene").value.trim();
  const objects = splitTerms($("#objects").value);
  const relation = $("#relation").value.trim();
  const time = $("#time").value.trim();
  const emotions = getActiveEmotions();
  const mode = $("#mode").value;
  const ratio = Number($("#ratio").value);
  const terms = [...splitTerms(scene), ...objects, relation, time, ...emotions].filter(Boolean);
  return { scene, objects, relation, time, emotions, mode, ratio, terms };
}

function ontologyMap(payload) {
  return payload.terms.map((term) => ({ term, category: classifyTerm(term, payload.emotions) }));
}

function transformTerm(term, rand) {
  const directKey = Object.keys(transformations).find((key) => term.includes(key));
  if (directKey) return pick(transformations[directKey], rand);
  const fallback = [
    `${term}의 그림자가 먼저 도착한 장소`,
    `${term}이 자기 이름을 잊어버린 상태`,
    `${term}을(를) 흉내 내는 오래된 감각`,
    `닫힌 눈꺼풀 뒤에서 반복되는 ${term}`
  ];
  return pick(fallback, rand);
}

function buildDreamDictionary(payload, rand) {
  const uniqueTerms = [...new Set(payload.terms)].slice(0, 12);
  return uniqueTerms.map((term) => ({
    term,
    category: classifyTerm(term, payload.emotions),
    dream: transformTerm(term, rand),
    operator: pick(irrationalOperators, rand)
  }));
}

function weights(ratio) {
  const ontology = 1 / (1 + ratio);
  const irrational = ratio / (1 + ratio);
  return {
    ontology: Math.round(ontology * 1000) / 10,
    irrational: Math.round(irrational * 1000) / 10
  };
}

function generatePoem(payload, dictionary, rand) {
  const anchor = payload.scene || "이 장면";
  const primaryEmotion = payload.emotions[0] || "이상한 평온";
  const secondaryEmotion = payload.emotions[1] || "낯선 감각";
  const a = pick(dictionary, rand);
  const b = pick(dictionary, rand);
  const c = pick(dictionary, rand);
  const object = payload.objects[0] || a.term;
  return `${payload.time}.\n${anchor}은(는) 아직 분류되지 않은 표정으로 켜져 있었다.\n\n온톨로지는 말했다. ${a.term}은(는) ${a.category}에 속한다고.\n그러나 비합리 AI는 그것을 ${a.dream}(으)로 다시 등록했다.\n\n나는 ${object}을(를) 만졌고,\n그 표면에서 ${primaryEmotion}의 냄새가 났다.\n${b.term}은(는) ${b.dream}처럼 내 앞에 누워 있었고,\n${c.term}은(는) ${c.operator}의 방식으로 조용히 원인을 잃어버렸다.\n\n합리는 세계를 설명하려고 선을 그었지만,\n비합리는 그 선 위에 젖은 새를 앉혔다.\n그래서 이 작품은 이해되는 대신,\n${secondaryEmotion}처럼 오래 남는다.`;
}

function generateExhibitionText(payload, dictionary) {
  const w = weights(payload.ratio);
  const motifs = dictionary.slice(0, 5).map((item) => `${item.term} → ${item.dream}`).join("\n");
  return `《Ontology of Dreams: ${payload.scene || "Untitled"}》\n\n이 작품은 세계를 이해하려는 충동과 세계를 다시 감각하려는 충동 사이에서 발생한다.\n작품의 생성 규칙은 Ontology 1 : Irrationality ${payload.ratio.toFixed(3)}이며,\n이는 약 ${w.ontology}%의 구조와 ${w.irrational}%의 의미 이탈로 구성된다.\n\n온톨로지는 입력된 장면을 사람, 장소, 사물, 감정, 시간으로 분류한다.\n비합리 AI는 그 분류를 보존하지 않고 감염시킨다.\n장소는 장기가 되고, 사물은 기억이 되며, 감정은 날씨처럼 행동한다.\n\n주요 변환:\n${motifs}\n\n이 작업은 완전한 논리도 완전한 노이즈도 지향하지 않는다.\n그 사이, 즉 의미가 무너지기 직전의 비율에서 관객은 해석하고 싶지만 완전히 소유할 수 없는 이미지를 마주한다.`;
}

function generateConcept(payload, dictionary, rand) {
  const titleSeed = pick(dictionary, rand);
  const operators = [...new Set(dictionary.map((item) => item.operator))].slice(0, 4);
  const scenes = dictionary.slice(0, 4).map((item, index) => `${index + 1}. ${item.category}로 분류된 ${item.term}이(가) ${item.dream}(으)로 변형된다.`).join("\n");
  return `작품명: ${titleSeed.dream}\n\n형식: 인터랙티브 웹 설치 / 생성형 텍스트 / 온톨로지 그래프\n핵심 비율: 1 : ${payload.ratio.toFixed(3)}\n정서 앵커: ${payload.emotions.join(", ") || "미정"}\n\n시놉시스:\n관객은 하나의 현실 조각을 입력한다. 시스템은 그것을 먼저 합리적으로 분류한다.\n그 후 분류된 개념들은 황금비적 광기에 의해 서로의 범주를 침범한다.\n그래프는 지식 지도처럼 시작하지만, 시간이 지날수록 꿈의 지도처럼 변형된다.\n\n장면 구성:\n${scenes}\n\n사용된 비합리 연산:\n${operators.map((op) => `- ${op}`).join("\n")}\n\n관객 경험:\n관객은 자신이 입력한 장면이 이해 가능한 구조에서 출발해 이해 불가능하지만 감정적으로 정확한 이미지로 변형되는 과정을 본다.`;
}

function generateImagePrompt(payload, dictionary) {
  const motifs = dictionary.slice(0, 6).map((item) => item.dream).join(", ");
  const emotion = payload.emotions.join(", ") || "ambiguous nostalgia";
  return `A surreal ontological art installation based on ${payload.scene}.\nGolden ratio composition, 38.2% rational knowledge graph structure and 61.8% irrational dream logic.\nVisible ontology nodes transforming into symbolic objects: ${motifs}.\nAtmosphere of ${emotion}.\nFragmented memory, stream of consciousness, category violation, object consciousness, poetic darkness, cinematic lighting, conceptual AI art, museum installation, readable graph lines melting into dream symbols.`;
}

function generateOutput(payload, dictionary, rand) {
  switch (payload.mode) {
    case "exhibition": return generateExhibitionText(payload, dictionary, rand);
    case "concept": return generateConcept(payload, dictionary, rand);
    case "imagePrompt": return generateImagePrompt(payload, dictionary, rand);
    case "poem":
    default: return generatePoem(payload, dictionary, rand);
  }
}

function drawGraph(dictionary, ratio) {
  const svg = $("#graph");
  svg.innerHTML = "";
  const leftX = 155;
  const rightX = 555;
  const items = dictionary.slice(0, 7);
  const step = 420 / (items.length + 1);
  const root = svgNode("g", {});
  const center = svgNode("g", { class: "node root" });
  center.appendChild(svgNode("circle", { cx: 360, cy: 210, r: 45 }));
  center.appendChild(svgText(360, 206, "O + φI"));
  center.appendChild(svgText(360, 226, `1:${ratio.toFixed(3)}`, "mini"));
  root.appendChild(center);
  items.forEach((item, index) => {
    const y = step * (index + 1);
    const driftY = y + Math.sin(index + ratio) * 22;
    root.appendChild(svgNode("path", { class: "edge", d: `M${leftX + 58},${y} C${280},${y} ${300},210 ${318},210` }));
    root.appendChild(svgNode("path", { class: "edge drift", d: `M${402},210 C${455},${210 + (driftY - 210) / 2} ${480},${driftY} ${rightX - 62},${driftY}` }));
    const left = svgNode("g", { class: "node" });
    left.appendChild(svgNode("circle", { cx: leftX, cy: y, r: 44 }));
    left.appendChild(svgText(leftX, y - 6, truncate(item.term, 9)));
    left.appendChild(svgText(leftX, y + 13, item.category, "mini"));
    root.appendChild(left);
    const right = svgNode("g", { class: "node dream" });
    right.appendChild(svgNode("circle", { cx: rightX, cy: driftY, r: 54 }));
    right.appendChild(svgText(rightX, driftY - 7, truncate(item.dream, 11)));
    right.appendChild(svgText(rightX, driftY + 14, item.operator, "mini"));
    root.appendChild(right);
  });
  svg.appendChild(root);
}

function svgNode(name, attrs) {
  const element = document.createElementNS("http://www.w3.org/2000/svg", name);
  Object.entries(attrs).forEach(([key, value]) => element.setAttribute(key, value));
  return element;
}

function svgText(x, y, value, className = "") {
  const text = svgNode("text", { x, y, class: className });
  text.textContent = value;
  return text;
}

function truncate(value, max) {
  return value.length > max ? `${value.slice(0, max)}…` : value;
}

function renderOperators(dictionary) {
  const operators = [...new Set(dictionary.map((item) => item.operator))].slice(0, 7);
  $("#operators").innerHTML = operators.map((operator) => `<span>${operator}</span>`).join("");
}

function renderDecoder(dictionary) {
  $("#decoderList").innerHTML = dictionary.slice(0, 7).map((item) => `<li><b>${escapeHtml(item.term)}</b> — ${escapeHtml(item.dream)}</li>`).join("");
}

function escapeHtml(value) {
  return String(value).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;").replaceAll("'", "&#039;");
}

function renderWeights(ratio) {
  const w = weights(ratio);
  $("#ontologyWeight").textContent = `${w.ontology}%`;
  $("#irrationalWeight").textContent = `${w.irrational}%`;
  $("#ratioLabel").textContent = `Ontology 1 : Irrationality ${ratio.toFixed(3)}`;
}

function runGeneration() {
  const payload = collectPayload();
  const seed = hashString(JSON.stringify(payload) + state.mutation);
  const rand = seededRandom(seed);
  const dictionary = buildDreamDictionary(payload, rand);
  const output = generateOutput(payload, dictionary, rand);
  state.lastPayload = { ...payload, ontology: ontologyMap(payload), dreamDictionary: dictionary, output };
  renderWeights(payload.ratio);
  drawGraph(dictionary, payload.ratio);
  renderOperators(dictionary);
  renderDecoder(dictionary);
  $("#output").textContent = output;
}

function showToast(message) {
  const toast = $("#toast");
  toast.textContent = message;
  toast.classList.add("show");
  window.setTimeout(() => toast.classList.remove("show"), 1600);
}

function copyOutput() {
  const text = $("#output").textContent;
  navigator.clipboard.writeText(text).then(() => showToast("Copied")).catch(() => showToast("Copy failed"));
}

function downloadJSON() {
  if (!state.lastPayload) return;
  const blob = new Blob([JSON.stringify(state.lastPayload, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = "ontological-irrationalism-output.json";
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
  showToast("Exported JSON");
}

function wireEvents() {
  $("#studioForm").addEventListener("submit", (event) => { event.preventDefault(); runGeneration(); });
  $("#ratio").addEventListener("input", (event) => { renderWeights(Number(event.target.value)); });
  $("#mutateBtn").addEventListener("click", () => { state.mutation += 1; runGeneration(); });
  $("#copyBtn").addEventListener("click", copyOutput);
  $("#downloadBtn").addEventListener("click", downloadJSON);
  $$("#emotionChips button").forEach((button) => { button.addEventListener("click", () => button.classList.toggle("active")); });
}

wireEvents();
runGeneration();
