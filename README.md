# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_23:02:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,798 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Holombuwa — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 23:02:40 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-06 23:02:36 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-06 23:02:20 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 23:02:19 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-06 23:02:15 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-06 23:02:14 | Moragaswewa (Deduru Oya) | 2.08 | 🟢 Normal | -0.172 |  |
| 2026-11-06 23:01:40 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 1.189 | 🔺 Rising |
| 2026-11-06 23:01:26 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-11-06 23:01:24 | Nawalapitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.177 |  |
| 2026-11-06 23:00:47 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-11-06 22:26:39 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.014 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 22:08:38 | Holombuwa (Kelani Ganga) | 4.75 | 🟠 Minor Flood | 0.081 | 🔺 Rising |
| 2026-11-06 22:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-11-06 23:01:40 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 1.189 | 🔺 Rising |
| 2026-11-06 22:00:30 | Peradeniya (Mahaweli Ganga) | 3.72 | 🟢 Normal | 0.592 | 🔺 Rising |
| 2026-11-06 22:08:44 | Giriulla (Maha Oya) | 2.62 | 🟢 Normal | 0.441 | 🔺 Rising |
| 2026-11-06 22:05:37 | Rathnapura (Kalu Ganga) | 3.33 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-11-06 22:09:39 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-11-06 22:09:55 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-11-06 22:03:00 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-06 22:05:23 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-11-06 23:01:26 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-11-06 22:02:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-11-06 18:00:25 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-06 22:08:24 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-06 22:02:58 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-06 23:02:15 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-06 22:03:07 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-06 22:08:37 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-06 22:14:43 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-06 23:02:20 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 22:04:56 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 22:06:12 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-06 22:26:39 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-06 21:03:07 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 22:02:03 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 23:02:19 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:05:00 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-06 22:06:22 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-11-06 22:05:44 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-11-06 23:02:40 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-06 23:02:36 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:51 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-06 22:04:39 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-06 22:02:07 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-06 22:06:03 | Thawalama (Gin Ganga) | 2.75 | 🟢 Normal | -0.009 |  |
| 2026-11-06 22:05:57 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-06 23:00:47 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-11-06 23:02:14 | Moragaswewa (Deduru Oya) | 2.08 | 🟢 Normal | -0.172 |  |
| 2026-11-06 23:01:24 | Nawalapitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.177 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)