
$(function () {

  const AI_NAME   = "Nexus";
  const USER_NAME = "You";


  const AI_RESPONSES = [
    "That's a great question! Let me break it down for you. The concept involves several interconnected ideas that build upon each other. First, we need to understand the foundational principles, then we can explore how they apply to your specific scenario.",
    "I'd be happy to help with that! Here's what I know about this topic:\n\n**Key Points:**\n- The core idea is built around simplicity and effectiveness\n- There are multiple approaches you can take depending on your needs\n- Best practices suggest starting with the fundamentals\n\nWould you like me to go deeper on any of these points?",
    "Interesting! This is a topic that many people find challenging at first, but once you grasp the core idea, everything else falls into place. Let me give you a clear, step-by-step explanation.",
    "Great choice! Here's a quick `code snippet` to get you started:\n\n```\nfunction example(input) {\n  // Process your input\n  return input.trim().toLowerCase();\n}\n```\n\nThis is a clean, reusable pattern. Let me know if you need me to customize it for your use case.",
    "Absolutely! I can help you brainstorm that. Here are some creative directions you might consider — each has its own strengths and would appeal to different audiences. The best choice depends on your target users and the overall vision you have in mind.",
    "That's a fascinating perspective. From what I know, the research on this suggests that the most effective approach combines both theoretical understanding and practical application. The key is consistency and iteration.",
    "Of course! Let me summarize the most important aspects clearly and concisely so you can get a good overview quickly, and then we can dive deeper into any area that interests you most.",
    "Here's a structured way to think about this problem. I'd recommend starting with a clear definition of your goal, then working backwards to identify what steps are needed. This approach tends to reduce complexity and make progress feel more manageable.",
    "Great question! There are a few different ways to approach this depending on your context. The simplest method works well for most cases, but if you have specific constraints, we might want to explore a more tailored solution.",
    "That makes a lot of sense. To directly answer your question — yes, that approach is valid and commonly used. However, keep in mind that there are a few edge cases worth being aware of, especially as you scale or introduce more complexity.",
  ];


  let messageCount   = 0;  // tracks how many messages have been sent
  let isDarkMode     = false;
  let isAiTyping     = false;

  function getCurrentTime() {
    const now  = new Date();
    let hours  = now.getHours();
    const mins = String(now.getMinutes()).padStart(2, "0");
    const ampm = hours >= 12 ? "PM" : "AM";
    hours = hours % 12 || 12;
    return `${hours}:${mins} ${ampm}`;
  }


  function formatMessage(text) {
    // Escape HTML first
    let safe = $("<div>").text(text).html();

    // Code blocks (```)
    safe = safe.replace(/```([\s\S]*?)```/g, "<pre><code>$1</code></pre>");

    // Inline code
    safe = safe.replace(/`([^`\n]+)`/g, "<code>$1</code>");

    // Bold **text**
    safe = safe.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");

    // Italic *text*
    safe = safe.replace(/\*(.+?)\*/g, "<em>$1</em>");

    // Bullet list items (lines starting with - or •)
    safe = safe.replace(/(^|\n)([-•] .+)/g, "$1$2");

    // Line breaks
    safe = safe.replace(/\n/g, "<br>");

    return safe;
  }

  function addMessage(text, sender) {
    const isUser    = sender === "user";
    const msgClass  = isUser ? "user-message" : "ai-message";
    const avatarCls = isUser ? "user-avatar-msg" : "ai-avatar";
    const avatarIcon = isUser
      ? '<i class="fa-solid fa-user"></i>'
      : '<i class="fa-solid fa-wand-magic-sparkles"></i>';
    const name     = isUser ? USER_NAME : AI_NAME;
    const time     = getCurrentTime();
    const content  = isUser
      ? $("<div>").text(text).html()  
      : formatMessage(text);          

    const $msg = $(`
      <div class="message ${msgClass}">
        <div class="message-avatar ${avatarCls}">
          ${avatarIcon}
        </div>
        <div class="message-content">
          <div class="message-header">
            <span class="message-sender">${name}</span>
            <span class="message-time">${time}</span>
          </div>
          <div class="message-bubble">${content}</div>
        </div>
      </div>
    `);


    $msg.insertBefore($("#typingIndicator"));

    messageCount++;
    scrollToBottom();


    if (messageCount === 1) {
      hideWelcomeScreen();
    }
  }


  function hideWelcomeScreen() {
    $("#welcomeScreen").fadeOut(300, function () {
      $(this).remove();
    });
  }


  function scrollToBottom() {
    const $wrapper = $("#messagesWrapper");
    $wrapper.animate({ scrollTop: $wrapper[0].scrollHeight }, 300);
  }


  function showTyping() {
    isAiTyping = true;
    $("#typingIndicator").show();
    scrollToBottom();
  }

  function hideTyping() {
    isAiTyping = false;
    $("#typingIndicator").hide();
  }


  function getRandomResponse() {
    const idx = Math.floor(Math.random() * AI_RESPONSES.length);
    return AI_RESPONSES[idx];
  }


  function sendMessage() {
    const $input = $("#messageInput");
    const text   = $input.val().trim();

    if (!text || isAiTyping) return;


    addMessage(text, "user");


    $input.val("").trigger("input");

    const delay = 1000 + Math.random() * 1000;
    showTyping();

    setTimeout(function () {
      hideTyping();
      addMessage(getRandomResponse(), "ai");
    }, delay);
  }

  const $input  = $("#messageInput");
  const $sendBtn = $("#sendBtn");


  $input.on("input", function () {
    const hasText = $(this).val().trim().length > 0;
    $sendBtn.prop("disabled", !hasText);

    this.style.height = "auto";
    this.style.height = Math.min(this.scrollHeight, 180) + "px";
  });


  $input.on("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      if (!$sendBtn.prop("disabled")) {
        sendMessage();
      }
    }
  });


  $sendBtn.on("click", function () {
    sendMessage();
    $input.focus();
  });


  $(document).on("click", ".suggestion-card", function () {
    const prompt = $(this).data("prompt");
    $input.val(prompt).trigger("input").focus();
    sendMessage();
  });

  $("#hamburgerBtn").on("click", function () {
    openSidebar();
  });

  $("#sidebarCloseBtn").on("click", function () {
    closeSidebar();
  });

  $("#sidebarOverlay").on("click", function () {
    closeSidebar();
  });

  function openSidebar() {
    $("#sidebar").addClass("open");
    $("#sidebarOverlay").addClass("active");
    $("body").css("overflow", "hidden");
  }

  function closeSidebar() {
    $("#sidebar").removeClass("open");
    $("#sidebarOverlay").removeClass("active");
    $("body").css("overflow", "");
  }


  $("#newChatBtn").on("click", function () {

    if (messageCount > 0) {
      const firstMsg = $(".user-message .message-bubble").first().text();
      const truncated = firstMsg.length > 32
        ? firstMsg.substring(0, 32) + "…"
        : firstMsg;

      const $newItem = $(`
        <li class="history-item">
          <i class="fa-regular fa-message"></i>
          <span>${truncated || "Previous chat"}</span>
        </li>
      `);

      $(".history-item.active").removeClass("active");
      $newItem.prependTo("#chatHistoryList");
    }


    messageCount = 0;
    isAiTyping   = false;
    hideTyping();
    $(".message").remove();

    const $welcome = $(`
      <div class="welcome-screen" id="welcomeScreen">
        <div class="welcome-inner">
          <div class="welcome-logo">
            <div class="welcome-icon-ring">
              <i class="fa-solid fa-wand-magic-sparkles"></i>
            </div>
          </div>
          <h1 class="welcome-title">What can I help with?</h1>
          <p class="welcome-subtitle">Ask me anything — I'm ready to assist, explain, create, or brainstorm.</p>
          <div class="suggestion-grid" id="suggestionGrid">
            <button class="suggestion-card" data-prompt="Explain how neural networks work in simple terms">
              <div class="card-icon"><i class="fa-solid fa-brain"></i></div>
              <div class="card-body-content"><h6>Explain concepts</h6><p>Break down complex topics in simple, clear language</p></div>
            </button>
            <button class="suggestion-card" data-prompt="Write a Python function to sort a list of dictionaries by a specific key">
              <div class="card-icon"><i class="fa-solid fa-code"></i></div>
              <div class="card-body-content"><h6>Write code</h6><p>Get help writing, reviewing, or debugging code</p></div>
            </button>
            <button class="suggestion-card" data-prompt="Help me brainstorm creative names for a tech startup that builds AI tools">
              <div class="card-icon"><i class="fa-solid fa-lightbulb"></i></div>
              <div class="card-body-content"><h6>Brainstorm ideas</h6><p>Generate creative ideas for projects, names, content</p></div>
            </button>
            <button class="suggestion-card" data-prompt="Summarize the key points about how the internet works">
              <div class="card-icon"><i class="fa-solid fa-file-lines"></i></div>
              <div class="card-body-content"><h6>Summarize topics</h6><p>Get clear summaries of articles, topics, or documents</p></div>
            </button>
          </div>
        </div>
      </div>
    `);

    $welcome.insertBefore("#typingIndicator");

    $(".history-item.active").removeClass("active");
    $(".history-item").first().addClass("active");

    $input.val("").trigger("input").focus();
    closeSidebar();
  });


  $("#themeToggleBtn").on("click", function () {
    isDarkMode = !isDarkMode;

    if (isDarkMode) {
      $("html").attr("data-theme", "dark");
      $("#themeIcon").removeClass("fa-moon").addClass("fa-sun");
      $("#themeLabel").text("Light Mode");
    } else {
      $("html").removeAttr("data-theme");
      $("#themeIcon").removeClass("fa-sun").addClass("fa-moon");
      $("#themeLabel").text("Dark Mode");
    }
  });


  $("#exportChatBtn").on("click", function () {
    if (messageCount === 0) {
      alert("No messages to export yet!");
      return;
    }

    let chatContent = "NexusChat — Exported Conversation\n";
    chatContent += "Date: " + new Date().toLocaleString() + "\n";
    chatContent += "=".repeat(50) + "\n\n";

    $(".message").each(function () {
      const sender = $(this).find(".message-sender").text();
      const time   = $(this).find(".message-time").text();
      const text   = $(this).find(".message-bubble").text();
      chatContent += `[${time}] ${sender}:\n${text}\n\n`;
    });


    const blob = new Blob([chatContent], { type: "text/plain;charset=utf-8" });
    const url  = URL.createObjectURL(blob);
    const $a   = $("<a>").attr({ href: url, download: "NexusChat_export.txt" });

    $("body").append($a);
    $a[0].click();
    $a.remove();
    URL.revokeObjectURL(url);
  });

  $input.focus();

  console.log("✅ NexusChat initialized successfully.");
});
