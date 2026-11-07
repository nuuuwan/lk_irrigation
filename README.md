# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_20:02:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,581 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Urawa — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 20:02:30 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-07 20:02:21 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.060 |  |
| 2026-11-07 20:02:10 | Hanwella (Kelani Ganga) | 3.47 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-07 20:01:33 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.064 |  |
| 2026-11-07 20:01:33 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-11-07 20:01:14 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 20:01:04 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-07 20:00:45 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 19:25:17 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-07 19:19:38 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 19:16:38 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 19:10:11 | Urawa (Nilwala Ganga) | 3.55 | 🟡 Alert | 1.090 | 🔺 Rising |
| 2026-11-07 20:02:30 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-07 19:04:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | -0.019 |  |
| 2026-11-07 19:04:06 | Wellawaya (Kirindi Oya) | 2.87 | 🟢 Normal | 0.890 | 🔺 Rising |
| 2026-11-07 19:08:09 | Peradeniya (Mahaweli Ganga) | 3.64 | 🟢 Normal | 0.467 | 🔺 Rising |
| 2026-11-07 20:01:33 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-11-07 19:09:38 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-11-07 19:13:17 | Rathnapura (Kalu Ganga) | 2.78 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-11-07 19:06:33 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-07 20:02:10 | Hanwella (Kelani Ganga) | 3.47 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-07 19:25:17 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-07 19:04:28 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-07 20:01:04 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-07 19:02:00 | Ellagawa (Kalu Ganga) | 6.16 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-07 19:06:53 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-07 19:05:10 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-07 19:09:26 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-07 19:05:21 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 19:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 20:00:45 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 20:01:14 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:03:13 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-07 19:04:10 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-11-07 19:06:36 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 19:19:38 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 19:02:06 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-07 19:01:57 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-07 19:16:38 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.008 |  |
| 2026-11-07 19:02:45 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:01:10 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-07 19:00:14 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-07 19:02:56 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-11-07 19:08:16 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | -0.018 |  |
| 2026-11-07 19:10:12 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.019 |  |
| 2026-11-07 19:03:12 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-11-07 18:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.021 |  |
| 2026-11-07 19:02:12 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -0.057 |  |
| 2026-11-07 20:02:21 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.060 |  |
| 2026-11-07 20:01:33 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)