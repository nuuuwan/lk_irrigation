# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_09:13:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,911 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🔴 Nawalapitiya — Major Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 09:13:37 | Magura (Kalu Ganga) | 4.62 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-09-20 09:10:19 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.491 | 🔺 Rising |
| 2026-09-20 09:09:58 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:09:42 | Panadugama (Nilwala Ganga) | 3.70 | 🟢 Normal | 0.352 | 🔺 Rising |
| 2026-09-20 09:08:39 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-09-20 09:08:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.11 | 🟡 Alert | 0.177 | 🔺 Rising |
| 2026-09-20 09:07:07 | Glencourse (Kelani Ganga) | 11.61 | 🟢 Normal | 0.688 | 🔺 Rising |
| 2026-09-20 09:05:54 | Baddegama (Gin Ganga) | 2.74 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-09-20 09:05:30 | Thawalama (Gin Ganga) | 3.86 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-09-20 09:05:27 | Rathnapura (Kalu Ganga) | 4.54 | 🟢 Normal | 1.151 | 🔺 Rising |
| 2026-09-20 09:05:24 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-09-20 09:05:12 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-09-20 09:05:12 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-20 09:04:32 | Hanwella (Kelani Ganga) | 2.12 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-09-20 09:03:58 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:03:51 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:03:50 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-20 09:03:46 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:03:45 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-20 09:03:25 | Deraniyagala (Kelani Ganga) | 2.80 | 🟢 Normal | -0.296 |  |
| 2026-09-20 09:03:20 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 09:03:20 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-09-20 09:03:14 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-20 09:03:14 | Thanthirimale (Malwathu Oya) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 09:03:13 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:03:09 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-20 09:03:03 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-09-20 09:02:40 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 09:02:29 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:02:20 | Nawalapitiya (Mahaweli Ganga) | 6.00 | 🔴 Major Flood | 0.000 |  |
| 2026-09-20 09:02:12 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:02:12 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 09:02:02 | Kithulgala (Kelani Ganga) | 2.68 | 🟢 Normal | -0.271 |  |
| 2026-09-20 09:01:49 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:01:30 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:01:27 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.674 | 🔺 Rising |
| 2026-09-20 09:01:15 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:01:03 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 09:00:22 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 09:02:20 | Nawalapitiya (Mahaweli Ganga) | 6.00 | 🔴 Major Flood | 0.000 |  |
| 2026-09-20 09:08:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.11 | 🟡 Alert | 0.177 | 🔺 Rising |
| 2026-09-20 09:13:37 | Magura (Kalu Ganga) | 4.62 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-09-20 09:05:27 | Rathnapura (Kalu Ganga) | 4.54 | 🟢 Normal | 1.151 | 🔺 Rising |
| 2026-09-20 09:07:07 | Glencourse (Kelani Ganga) | 11.61 | 🟢 Normal | 0.688 | 🔺 Rising |
| 2026-09-20 09:01:27 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.674 | 🔺 Rising |
| 2026-09-20 09:10:19 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.491 | 🔺 Rising |
| 2026-09-20 09:09:42 | Panadugama (Nilwala Ganga) | 3.70 | 🟢 Normal | 0.352 | 🔺 Rising |
| 2026-09-20 09:05:30 | Thawalama (Gin Ganga) | 3.86 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-09-20 09:03:03 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-09-20 09:05:24 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-09-20 09:03:20 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-09-20 09:05:12 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-09-20 09:05:54 | Baddegama (Gin Ganga) | 2.74 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-09-20 09:08:39 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-09-20 09:04:32 | Hanwella (Kelani Ganga) | 2.12 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-09-20 09:03:45 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-20 09:05:12 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-20 09:01:03 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 09:03:14 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-20 09:02:40 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 09:03:14 | Thanthirimale (Malwathu Oya) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 09:03:09 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-20 09:02:12 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 09:03:20 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 09:01:30 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:03:46 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:01:49 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:03:58 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:01:15 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:03:51 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:09:58 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:03:13 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:02:12 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:02:29 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 09:03:50 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-20 09:00:22 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-09-20 09:02:02 | Kithulgala (Kelani Ganga) | 2.68 | 🟢 Normal | -0.271 |  |
| 2026-09-20 09:03:25 | Deraniyagala (Kelani Ganga) | 2.80 | 🟢 Normal | -0.296 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)