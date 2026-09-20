# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_21:02:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,348 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Holombuwa — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thawalama — Alert; 🟡 Baddegama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 21:02:50 | Giriulla (Maha Oya) | 3.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-20 21:02:44 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:02:20 | Dunamale (Aththanagalu Oya) | 3.26 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-09-20 21:01:52 | Nawalapitiya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.284 |  |
| 2026-09-20 21:01:27 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-09-20 21:01:24 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-09-20 21:01:22 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:00:39 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 21:00:24 | Magura (Kalu Ganga) | 5.56 | 🟡 Alert | 0.000 |  |
| 2026-09-20 20:59:39 | Magura (Kalu Ganga) | 5.56 | 🟡 Alert | 0.000 |  |
| 2026-09-20 20:43:02 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 20:06:48 | Panadugama (Nilwala Ganga) | 6.09 | 🟠 Minor Flood | 0.051 | 🔺 Rising |
| 2026-09-20 20:08:56 | Holombuwa (Kelani Ganga) | 3.16 | 🟡 Alert | 0.177 | 🔺 Rising |
| 2026-09-20 20:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-09-20 20:05:39 | Thawalama (Gin Ganga) | 5.45 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-09-20 20:09:08 | Baddegama (Gin Ganga) | 3.59 | 🟡 Alert | 0.028 | 🔺 Rising |
| 2026-09-20 20:04:56 | Glencourse (Kelani Ganga) | 15.57 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-20 21:00:24 | Magura (Kalu Ganga) | 5.56 | 🟡 Alert | 0.000 |  |
| 2026-09-20 20:09:47 | Rathnapura (Kalu Ganga) | 6.63 | 🟡 Alert | -0.057 |  |
| 2026-09-20 20:02:52 | Norwood (Kelani Ganga) | 1.81 | 🟡 Alert | -0.080 |  |
| 2026-09-20 20:02:59 | Peradeniya (Mahaweli Ganga) | 5.48 | 🟡 Alert | -0.297 |  |
| 2026-09-20 20:06:22 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | 0.494 | 🔺 Rising |
| 2026-09-20 20:02:53 | Hanwella (Kelani Ganga) | 6.42 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-09-20 20:03:31 | Ellagawa (Kalu Ganga) | 8.37 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-09-20 20:05:10 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-09-20 21:02:20 | Dunamale (Aththanagalu Oya) | 3.26 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-09-20 20:08:17 | Putupaula (Kalu Ganga) | 2.12 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-20 18:03:01 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 21:02:50 | Giriulla (Maha Oya) | 3.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-20 18:02:11 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 20:02:40 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 21:00:39 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 20:07:55 | Thalgahagoda (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-20 21:02:44 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 20:43:02 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 20:09:38 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:01:22 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-20 20:02:14 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 20:09:35 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-20 20:04:56 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 20:01:43 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:01:27 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-09-20 18:00:17 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-20 21:01:24 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-09-20 20:06:37 | Urawa (Nilwala Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2026-09-20 20:03:08 | Pitabeddara (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.039 |  |
| 2026-09-20 20:04:16 | Kithulgala (Kelani Ganga) | 2.67 | 🟢 Normal | -0.133 |  |
| 2026-09-20 21:01:52 | Nawalapitiya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.284 |  |
| 2026-09-20 20:03:52 | Deraniyagala (Kelani Ganga) | 2.81 | 🟢 Normal | -0.401 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)