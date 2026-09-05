# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_21:02:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **252,833 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-05 21:02:56 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:45 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-05 21:02:40 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:25 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-05 21:02:21 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:17 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-09-05 21:02:09 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:07 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:01:46 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-09-05 21:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 21:01:23 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:01:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:01:06 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:00:49 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:00:09 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-05 20:15:07 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 24.592 | 🔺 Rising |
| 2026-09-05 21:02:17 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-09-05 21:01:46 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-09-05 20:03:12 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-09-05 21:02:45 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-05 20:06:12 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-05 21:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 21:01:23 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:40 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:07 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:01:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:09 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:00:09 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:05:48 | Galgamuwa (Mee Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:00:22 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-05 20:13:00 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-05 20:01:07 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-05 20:08:39 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:01:06 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-05 20:03:39 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:21 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 20:05:10 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-05 20:05:05 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:13:48 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 20:03:26 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:00:49 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:56 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-05 20:02:15 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-05 20:15:01 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.008 |  |
| 2026-09-05 20:06:39 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.010 |  |
| 2026-09-05 21:02:25 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-05 20:04:04 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-09-05 20:03:21 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.024 |  |
| 2026-09-05 20:04:21 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.030 |  |
| 2026-09-05 20:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.038 |  |
| 2026-09-05 18:09:31 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.049 |  |
| 2026-09-05 20:03:57 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.059 |  |
| 2026-09-05 20:04:43 | Glencourse (Kelani Ganga) | 8.96 | 🟢 Normal | -0.104 |  |
| 2026-09-05 20:05:01 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)