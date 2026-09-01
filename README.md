# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_21:27:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **249,264 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **3** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 21:27:51 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:22:37 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.048 |  |
| 2026-09-01 21:18:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.071 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 21:01:10 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-09-01 21:18:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-01 21:02:22 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 21:02:31 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-01 21:05:42 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-01 21:03:08 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-01 21:03:49 | Glencourse (Kelani Ganga) | 9.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 21:08:23 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-01 21:00:37 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:02:24 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:01:48 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:04:59 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:01:16 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:03:31 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:08:23 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:02:56 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:06:20 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:03:58 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:00:44 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:05:04 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:06:40 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:01:00 | Manampitiya (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:27:51 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:00:53 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:02:20 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-01 21:08:55 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-01 21:04:36 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-09-01 18:04:47 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-01 21:02:54 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-09-01 21:02:12 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-09-01 21:01:42 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-09-01 21:03:53 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-09-01 21:03:26 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | -0.029 |  |
| 2026-09-01 21:22:37 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.048 |  |
| 2026-09-01 18:01:28 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.060 |  |
| 2026-09-01 21:03:29 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.090 |  |
| 2026-09-01 21:05:48 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.122 |  |
| 2026-09-01 21:01:06 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.164 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)