# Can AI design circuit boards yet?

URL: https://eebench.org/blog/can-ai-design-circuit-boards-yet/

Score: 316

---

Can AI design circuit boards yet?
OpenAI showed GPT-6 Astra working in KiCad. We have been building a way to measure
          whether the circuits that come out of these models are any good.
September 4, 2026
8 min read
We got pretty excited yesterday when OpenAI put a demo of
GPT-6 Astra working on a circuit board in KiCad
on the front page of its
          launch post. It is cool to see electronics show up in a major model release like this.
We are obviously still some distance from asking an AI to build an entire phone in one prompt. The demo does
          raise a question we have been thinking about for a while, though: how do we measure whether the electronics an
          AI produces are actually any good?
The models know a surprising amount about electronics
Our experience has been that current models know much more about electronics than their output in
          conventional design tools tends to show. They have read textbooks, datasheets, application notes and a lot of
          code.
You can have an agent operate a graphical CAD tool, but it spends a lot of time clicking around and keeping
          track of what is on screen. A lot of its context consists of coordinates, menus and application state.
EEBench uses
atopile
instead. The circuit
          lives in declarative code, so the agent can work directly on components, connections and electrical
          constraints. It can change the design, build it, run a simulation and inspect what failed without leaving the
          project.
This has worked much better for us than asking a model to draw lines in a GUI. It also means the benchmark
          can spend less time testing computer use and more time testing electronics.
A small part of the starter design for one public EEBench task, in ato v2
.
ELEC
:
@STD
::
Import
{
.
project
&=
"electronics"
.
org
&=
"atopile"
}
.
Submission
:
@type
{
.
vin
:
ELEC
::
ElectricPower
.
vhold
:
ELEC
::
ElectricPower
.
vhold.lv
~
.
vin.lv
.
c_bank
:
ELEC
::
Capacitor
{
.
capacitance
&=
22uF
+/-
20%
.
max_voltage
&=
10V
..
25V
.
temperature_coefficient
&=
"X5R"
.
package
&=
"0805"
}
.
vhold.hv
~>
.
c_bank
~>
.
vhold.lv
}
The real world is messy
One of the public tasks is based on a residential energy meter. When its 5 V supply disappears, the circuit
          has to keep the processor alive for another 20 ms so it can save the accumulated reading. The protected rail
          must stay above the processor's 3.0 V brownout threshold during that window.
Most models intuitively jump to the right base conclusion: add a capacitor.
A real capacitor makes the task more interesting. A ceramic part may provide much less than its advertised
          capacitance once it has voltage across it. Parts have tolerances. Adding more capacitance costs more, takes up
          space and makes the rail slower to recharge when the power returns. A design that works with nominal values
          can fail with the parts that arrive.
EEBench cuts the input power in simulation and measures what happens. It checks the voltage throughout the
          outage, the effective capacitance at the operating point, the recovery after power returns and the limits on
          package, dielectric, voltage rating and cost.
One real failure
A submitted design used 22 ÂµF nominally. At 4.7 V
          bias, the grader found only 11.4 ÂµF of effective capacitance, far below the 545 ÂµF requirement. The source
          built successfully; the circuit still failed the job.
Saved ngspice output from that submission. The protected rail falls below the 3 V requirement
            after 0.85 ms.
Failed power-loss hold-up simulation
The protected rail starts near 4.55 volts and falls below the required 3 volt
              threshold after 0.85 milliseconds, long before the required 20 milliseconds.
0
5
10
15
20 ms
0
1
2
3
4
5 V
3 V minimum
fails at 0.85 ms
The meter is one of the easier tasks. In a harder analog task, the agent may have to synthesize a
          multiple-feedback low-pass filter around an op-amp, solve the resistor and capacitor ratios for the required
          poles, and keep its gain, cutoff frequency and Q inside their limits after every component is pushed to a
          worst-case tolerance corner. The harness rebuilds the SPICE deck for those corners, runs the AC and transient
          captures, binds measurements to named probes, and records each result against its lower and upper
          specification limits.
But getting the equations right is only part of electronics engineering. EEBench uses real manufacturer
          parts, with specifications extracted from their datasheets and carried into the SPICE model. The agent has to
          find a combination that works across those tolerance corners while also choosing parts that exist, can be
          ordered and are reasonably priced for the product. That trade-off between electrical performance, cost and
          supply is much closer to designing real hardware than picking ideal values from a textbook.
This is the part we find most interesting, because it is what electrical engineering eventually boils down
          to, just like every other engineering discipline: trade-offs.
How the grading works
EEBench checks are fully deterministic. It builds the submitted design, constructs the circuit
          graph and bill of materials, and runs a set of SPICE simulations and design checks. Each requirement produces
          a measurement with a limit.
For the energy-meter task, the harness measures the protected rail while the input drops out and returns.
          Other tasks measure gain, thresholds, ripple, transient response and behavior at component-tolerance corners.
          The technical score is combined with cost efficiency against a reference bill of materials. Cost only helps
          once the circuit works.
This is similar to giving a coding agent a compiler and tests, except the tests are measuring voltages and
          component behavior..
EEBench V1 covers analog and digital design through simulation. It does not yet tell us whether a model can
          lay out, manufacture and bring up a complete product. We want to add those parts later. The current benchmark
          concentrates on the requirements, design and verification loop because that is where we can already grade
          useful engineering work objectively. The full
methodology and sample result
            explorer
are public.
What we are seeing on the leaderboard
The September 1 results are encouraging. Claude Opus 5 scored 61.6% across the 13 tasks in EEBench V1. Grok
          4.6 came second at 57.1%, just ahead of Claude Fable 5.1 at 56.4%. A few months ago we would not have expected
          models to do this well.
1
Claude Opus 5
61.6%
2
Grok 4.6
57.1%
3
Claude Fable 5.1
56.4%
4
Claude Fable 5
54.3%
5
Claude Opus 4.8 Max
51.4%
See the full leaderboard and run details
There was another result we were especially happy to see: xAI included EEBench in the
Grok 4.6 model
            card
. It appears in the section on âengineering acceleration,â alongside evaluations for 3D modeling and
          parametric CAD. Their published run put Grok 4.6 at 60.0% with xhigh reasoning effort. Seeing a frontier lab
          use EEBench to describe a new model's engineering ability makes us think this is becoming a category people
          care about.
Anthropic's models have consistently done well in this environment. Grok's rise is also interesting. In its
Grok 4.6 launch post
, xAI says the
          model received high-quality engineering data and RL training in domain-specific environments including
          computer-aided design. Its EEBench result fits that story.
The OpenAI models we have tested so far sit further down the table. GPT-5.5 scored 42.3%, while GPT-5.6 Sol
          scored 39.4%. We do not have a GPT-6 Astra result yet. After seeing it work on a board in KiCad, we would
          really like to find out how it ha