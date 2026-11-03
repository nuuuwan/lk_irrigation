# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_05:03:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,300 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 05:03:04 | Pitabeddara (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.059 |  |
| 2026-11-04 05:03:03 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-04 05:02:50 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | -0.021 |  |
| 2026-11-04 05:02:50 | Rathnapura (Kalu Ganga) | 3.71 | 🟢 Normal | -0.026 |  |
| 2026-11-04 05:02:42 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-04 05:02:39 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.154 |  |
| 2026-11-04 05:02:33 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.173 |  |
| 2026-11-04 05:02:17 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.206 |  |
| 2026-11-04 05:02:16 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-04 05:02:13 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.029 |  |
| 2026-11-04 05:01:08 | Peradeniya (Mahaweli Ganga) | 3.19 | 🟢 Normal | -0.061 |  |
| 2026-11-04 05:00:40 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-04 05:00:18 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.011 |  |
| 2026-11-04 05:00:17 | Thawalama (Gin Ganga) | 3.24 | 🟢 Normal | -0.210 |  |
| 2026-11-04 05:00:11 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.603 | 🔺 Rising |
| 2026-11-04 04:40:49 | Magura (Kalu Ganga) | 3.65 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-04 04:35:12 | Urawa (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.130 |  |
| 2026-11-04 04:31:06 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-04 04:30:37 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 05:00:11 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.603 | 🔺 Rising |
| 2026-11-04 03:05:20 | Badalgama (Maha Oya) | 3.97 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-11-03 18:06:38 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-04 04:02:23 | Hanwella (Kelani Ganga) | 3.19 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-04 04:40:49 | Magura (Kalu Ganga) | 3.65 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-03 18:04:27 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-04 04:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.10 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-04 04:31:06 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-04 04:06:34 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-04 04:03:30 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-04 04:02:11 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-04 05:02:42 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-04 04:02:34 | Moragaswewa (Deduru Oya) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-11-04 04:07:50 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 05:02:16 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-04 05:03:03 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-04 05:00:40 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-04 05:00:18 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.011 |  |
| 2026-11-04 04:02:42 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.017 |  |
| 2026-11-04 05:02:50 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | -0.021 |  |
| 2026-11-04 05:02:50 | Rathnapura (Kalu Ganga) | 3.71 | 🟢 Normal | -0.026 |  |
| 2026-11-04 05:02:13 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.029 |  |
| 2026-11-04 04:03:36 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | -0.031 |  |
| 2026-11-04 04:30:37 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.031 |  |
| 2026-11-04 04:09:13 | Holombuwa (Kelani Ganga) | 1.41 | 🟢 Normal | -0.037 |  |
| 2026-11-04 04:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.043 |  |
| 2026-11-04 04:04:42 | Manampitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.048 |  |
| 2026-11-04 05:03:04 | Pitabeddara (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.059 |  |
| 2026-11-04 05:01:08 | Peradeniya (Mahaweli Ganga) | 3.19 | 🟢 Normal | -0.061 |  |
| 2026-11-04 04:07:42 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.066 |  |
| 2026-11-04 04:03:11 | Thanamalwila (Kirindi Oya) | 1.71 | 🟢 Normal | -0.070 |  |
| 2026-11-04 04:03:23 | Giriulla (Maha Oya) | 3.65 | 🟢 Normal | -0.072 |  |
| 2026-11-04 04:01:10 | Kuda Oya (Kirindi Oya) | 1.93 | 🟢 Normal | -0.113 |  |
| 2026-11-04 04:35:12 | Urawa (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.130 |  |
| 2026-11-04 05:02:39 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.154 |  |
| 2026-11-04 05:02:33 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.173 |  |
| 2026-11-04 05:02:17 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.206 |  |
| 2026-11-04 05:00:17 | Thawalama (Gin Ganga) | 3.24 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)