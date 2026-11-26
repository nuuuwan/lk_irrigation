# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_21:03:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,497 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Holombuwa — Alert; 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 21:03:17 | Giriulla (Maha Oya) | 3.62 | 🟢 Normal | 0.740 | 🔺 Rising |
| 2026-11-26 21:03:13 | Siyambalanduwa (Heda Oya) | 1.68 | 🟢 Normal | -0.212 |  |
| 2026-11-26 21:03:09 | Putupaula (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-26 21:03:00 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.069 |  |
| 2026-11-26 21:03:00 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.041 |  |
| 2026-11-26 21:03:00 | Moragaswewa (Deduru Oya) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:02:38 | Moraketiya (Walawe Ganga) | 4.47 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-11-26 21:02:21 | Hanwella (Kelani Ganga) | 3.34 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-26 21:02:03 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 21:01:56 | Nakkala (Kumbukkan Oya) | 2.10 | 🟢 Normal | 0.735 | 🔺 Rising |
| 2026-11-26 21:01:38 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:01:18 | Dunamale (Aththanagalu Oya) | 3.50 | 🟡 Alert | 0.073 | 🔺 Rising |
| 2026-11-26 21:01:09 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.041 |  |
| 2026-11-26 21:00:46 | Padiyathalawa (Maduru Oya) | 3.80 | 🟢 Normal | -0.152 |  |
| 2026-11-26 21:00:43 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:00:40 | Wellawaya (Kirindi Oya) | 2.00 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-26 20:24:04 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-26 20:19:46 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 20:19:13 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.069 |  |
| 2026-11-26 20:17:04 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | 0.740 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 20:03:05 | Magura (Kalu Ganga) | 4.55 | 🟡 Alert | 0.271 | 🔺 Rising |
| 2026-11-26 20:06:32 | Holombuwa (Kelani Ganga) | 3.20 | 🟡 Alert | 0.185 | 🔺 Rising |
| 2026-11-26 21:01:18 | Dunamale (Aththanagalu Oya) | 3.50 | 🟡 Alert | 0.073 | 🔺 Rising |
| 2026-11-26 21:02:38 | Moraketiya (Walawe Ganga) | 4.47 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-11-26 19:15:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | 0.016 | 🔺 Rising |
| 2026-11-26 20:02:29 | Kuda Oya (Kirindi Oya) | 2.65 | 🟢 Normal | 0.799 | 🔺 Rising |
| 2026-11-26 21:03:17 | Giriulla (Maha Oya) | 3.62 | 🟢 Normal | 0.740 | 🔺 Rising |
| 2026-11-26 21:01:56 | Nakkala (Kumbukkan Oya) | 2.10 | 🟢 Normal | 0.735 | 🔺 Rising |
| 2026-11-26 20:12:32 | Rathnapura (Kalu Ganga) | 3.54 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-11-26 20:05:13 | Thaldena (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-11-26 20:05:17 | Pitabeddara (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-26 20:02:49 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-26 21:00:40 | Wellawaya (Kirindi Oya) | 2.00 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-26 21:02:21 | Hanwella (Kelani Ganga) | 3.34 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-26 21:02:03 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 20:04:44 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-26 18:00:24 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 20:07:31 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 21:03:00 | Moragaswewa (Deduru Oya) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:01:38 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:00:43 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:02:07 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-26 20:04:14 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-26 20:24:04 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:03:09 | Putupaula (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-26 20:08:31 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-11-26 20:05:05 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | -0.011 |  |
| 2026-11-26 20:14:10 | Panadugama (Nilwala Ganga) | 3.58 | 🟢 Normal | -0.017 |  |
| 2026-11-26 20:03:10 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-11-26 18:01:55 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-11-26 21:03:00 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.041 |  |
| 2026-11-26 21:01:09 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.041 |  |
| 2026-11-26 20:04:41 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.043 |  |
| 2026-11-26 20:02:50 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |
| 2026-11-26 21:03:00 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.069 |  |
| 2026-11-26 20:14:39 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.070 |  |
| 2026-11-26 20:01:09 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.085 |  |
| 2026-11-26 21:00:46 | Padiyathalawa (Maduru Oya) | 3.80 | 🟢 Normal | -0.152 |  |
| 2026-11-26 21:03:13 | Siyambalanduwa (Heda Oya) | 1.68 | 🟢 Normal | -0.212 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)