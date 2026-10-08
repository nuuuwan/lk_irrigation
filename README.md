# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_21:12:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,593 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Holombuwa — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 21:12:12 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | 0.459 | 🔺 Rising |
| 2026-10-08 21:08:53 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-10-08 21:08:19 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:07:34 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:07:08 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:06:34 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-08 21:06:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-08 21:06:19 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:06:05 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:05:27 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-08 21:05:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-08 21:05:12 | Norwood (Kelani Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 21:04:57 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-10-08 21:04:56 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-10-08 21:04:51 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.032 |  |
| 2026-10-08 21:04:39 | Thawalama (Gin Ganga) | 3.44 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-08 21:04:06 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:03:55 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-08 21:03:54 | Glencourse (Kelani Ganga) | 11.57 | 🟢 Normal | 0.552 | 🔺 Rising |
| 2026-10-08 21:03:35 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:03:34 | Holombuwa (Kelani Ganga) | 4.23 | 🟠 Minor Flood | -0.271 |  |
| 2026-10-08 21:03:12 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.021 |  |
| 2026-10-08 21:02:54 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:02:37 | Giriulla (Maha Oya) | 2.95 | 🟢 Normal | 0.719 | 🔺 Rising |
| 2026-10-08 21:02:34 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-10-08 21:02:30 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:02:30 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-08 21:02:18 | Magura (Kalu Ganga) | 2.59 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-10-08 21:02:10 | Panadugama (Nilwala Ganga) | 4.03 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-10-08 21:02:06 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:02:01 | Peradeniya (Mahaweli Ganga) | 3.27 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-08 21:01:55 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:01:47 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-08 21:01:12 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:01:10 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.065 |  |
| 2026-10-08 21:00:42 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 21:03:34 | Holombuwa (Kelani Ganga) | 4.23 | 🟠 Minor Flood | -0.271 |  |
| 2026-10-08 21:02:37 | Giriulla (Maha Oya) | 2.95 | 🟢 Normal | 0.719 | 🔺 Rising |
| 2026-10-08 21:03:54 | Glencourse (Kelani Ganga) | 11.57 | 🟢 Normal | 0.552 | 🔺 Rising |
| 2026-10-08 21:12:12 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | 0.459 | 🔺 Rising |
| 2026-10-08 21:02:18 | Magura (Kalu Ganga) | 2.59 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-10-08 21:02:10 | Panadugama (Nilwala Ganga) | 4.03 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-10-08 21:02:01 | Peradeniya (Mahaweli Ganga) | 3.27 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-08 21:05:27 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-08 21:04:39 | Thawalama (Gin Ganga) | 3.44 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-08 21:02:30 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-08 21:05:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-08 21:06:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-08 21:06:34 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-08 21:03:55 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-08 21:01:47 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-08 21:00:42 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 21:05:12 | Norwood (Kelani Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:08:19 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:01:55 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:02:06 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:07:01 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:02:30 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:07:08 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:03:35 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:04:06 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:07:34 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:02:54 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:02:32 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:06:05 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:01:12 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:06:19 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 21:04:57 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-10-08 21:02:34 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-10-08 21:03:12 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.021 |  |
| 2026-10-08 21:04:56 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-10-08 21:04:51 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.032 |  |
| 2026-10-08 21:08:53 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-10-08 21:01:10 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)