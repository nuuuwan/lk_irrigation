# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_22:02:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,044 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **6** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 22:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.090 |  |
| 2026-11-03 22:02:14 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-03 22:01:47 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-11-03 22:01:40 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-11-03 22:01:34 | Thanamalwila (Kirindi Oya) | 2.56 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-03 22:00:10 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.073 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 21:04:07 | Urawa (Nilwala Ganga) | 2.99 | 🟡 Alert | 0.314 | 🔺 Rising |
| 2026-11-03 21:02:10 | Moraketiya (Walawe Ganga) | 2.65 | 🟢 Normal | 0.967 | 🔺 Rising |
| 2026-11-03 21:07:37 | Kuda Oya (Kirindi Oya) | 2.89 | 🟢 Normal | 0.449 | 🔺 Rising |
| 2026-11-03 22:01:40 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-11-03 21:07:40 | Magura (Kalu Ganga) | 2.59 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-11-03 18:06:38 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-03 21:04:25 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-11-03 21:08:01 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-03 21:06:47 | Panadugama (Nilwala Ganga) | 4.14 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-11-03 18:04:27 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-03 22:00:10 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-03 21:10:51 | Rathnapura (Kalu Ganga) | 2.77 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-03 22:01:34 | Thanamalwila (Kirindi Oya) | 2.56 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-03 22:02:14 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-03 21:05:20 | Norwood (Kelani Ganga) | 1.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-03 21:01:36 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-03 21:01:36 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 21:01:32 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 21:01:06 | Peradeniya (Mahaweli Ganga) | 3.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-03 21:04:00 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-03 21:02:32 | Moragaswewa (Deduru Oya) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-11-03 21:01:20 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 21:07:53 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-03 21:02:55 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 21:01:56 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-03 22:01:47 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-11-03 21:06:56 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-11-03 21:06:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | -0.019 |  |
| 2026-11-03 21:09:04 | Hanwella (Kelani Ganga) | 2.37 | 🟢 Normal | -0.028 |  |
| 2026-11-03 21:02:48 | Wellawaya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.029 |  |
| 2026-11-03 21:03:55 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.042 |  |
| 2026-11-03 21:04:54 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.049 |  |
| 2026-11-03 21:03:41 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.051 |  |
| 2026-11-03 21:02:11 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.070 |  |
| 2026-11-03 21:02:13 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.081 |  |
| 2026-11-03 22:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.090 |  |
| 2026-11-03 21:04:40 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.093 |  |
| 2026-11-03 21:09:10 | Holombuwa (Kelani Ganga) | 1.94 | 🟢 Normal | -0.224 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)