# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_06:33:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,070 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 06:33:22 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | -0.003 |  |
| 2026-11-07 06:11:47 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:11:46 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:09:25 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.027 |  |
| 2026-11-07 06:08:28 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:07:37 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:07:15 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-11-07 06:07:03 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | -0.095 |  |
| 2026-11-07 06:06:55 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-07 06:06:13 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | -0.171 |  |
| 2026-11-07 06:05:40 | Hanwella (Kelani Ganga) | 4.20 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-11-07 06:05:08 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:05:06 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:04:47 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:04:34 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.127 |  |
| 2026-11-07 06:04:13 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 06:04:11 | Holombuwa (Kelani Ganga) | 1.88 | 🟢 Normal | -0.511 |  |
| 2026-11-07 06:04:01 | Ellagawa (Kalu Ganga) | 6.37 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-07 06:03:47 | Moraketiya (Walawe Ganga) | 2.08 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-07 06:03:05 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:03:01 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-11-07 06:02:58 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-07 06:02:52 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:02:52 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | -0.370 |  |
| 2026-11-07 06:02:47 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.044 |  |
| 2026-11-07 06:02:42 | Giriulla (Maha Oya) | 3.64 | 🟢 Normal | -0.129 |  |
| 2026-11-07 06:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.29 | 🟡 Alert | -0.010 |  |
| 2026-11-07 06:02:28 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.031 |  |
| 2026-11-07 06:02:21 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.986 | 🔺 Rising |
| 2026-11-07 06:02:21 | Badalgama (Maha Oya) | 4.28 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-07 06:02:10 | Glencourse (Kelani Ganga) | 12.56 | 🟢 Normal | -0.163 |  |
| 2026-11-07 06:02:10 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | -0.037 |  |
| 2026-11-07 06:01:37 | Rathnapura (Kalu Ganga) | 3.06 | 🟢 Normal | -0.104 |  |
| 2026-11-07 06:01:12 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.051 |  |
| 2026-11-07 06:00:39 | Magura (Kalu Ganga) | 3.39 | 🟢 Normal | -0.288 |  |
| 2026-11-07 06:00:37 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-11-07 06:00:23 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.021 |  |
| 2026-11-07 06:00:12 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 06:02:58 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-07 06:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.29 | 🟡 Alert | -0.010 |  |
| 2026-11-07 06:02:21 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.986 | 🔺 Rising |
| 2026-11-07 06:05:40 | Hanwella (Kelani Ganga) | 4.20 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-11-07 06:04:01 | Ellagawa (Kalu Ganga) | 6.37 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-07 06:02:21 | Badalgama (Maha Oya) | 4.28 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-07 06:06:55 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-07 06:03:47 | Moraketiya (Walawe Ganga) | 2.08 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-07 06:04:13 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 06:02:52 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:05:08 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:11:47 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:03:05 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:08:28 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:07:37 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:05:06 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:00:12 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:51 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:04:47 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:33:22 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | -0.003 |  |
| 2026-11-07 05:03:13 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-11-07 06:07:15 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-11-07 06:03:01 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-11-07 06:00:37 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-11-07 06:00:23 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.021 |  |
| 2026-11-07 06:09:25 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.027 |  |
| 2026-11-07 06:02:28 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.031 |  |
| 2026-11-07 06:02:10 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | -0.037 |  |
| 2026-11-07 06:02:47 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.044 |  |
| 2026-11-07 06:01:12 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.051 |  |
| 2026-11-07 06:07:03 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | -0.095 |  |
| 2026-11-07 06:01:37 | Rathnapura (Kalu Ganga) | 3.06 | 🟢 Normal | -0.104 |  |
| 2026-11-07 06:04:34 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.127 |  |
| 2026-11-07 06:02:42 | Giriulla (Maha Oya) | 3.64 | 🟢 Normal | -0.129 |  |
| 2026-11-07 06:02:10 | Glencourse (Kelani Ganga) | 12.56 | 🟢 Normal | -0.163 |  |
| 2026-11-07 06:06:13 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | -0.171 |  |
| 2026-11-07 06:00:39 | Magura (Kalu Ganga) | 3.39 | 🟢 Normal | -0.288 |  |
| 2026-11-07 06:02:52 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | -0.370 |  |
| 2026-11-07 06:04:11 | Holombuwa (Kelani Ganga) | 1.88 | 🟢 Normal | -0.511 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)