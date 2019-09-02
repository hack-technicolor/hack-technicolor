# Further Optimization

## Turning off Power-Saving features

In theory, by turning off all powersaving features, the gateway should be more responsive in every way. To do this

1. Log in via SSH to your gateway
2. Run these commands:

```bash
pwrctl config --cpuspeed 0
pwrctl config --wait off
pwrctl config --ethapd off
pwrctl config --eee off
pwrctl config --autogreeen off
```