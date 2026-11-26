# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_09:20:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,057 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 09:20:20 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | -0.023 |  |
| 2026-11-26 09:20:13 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.132 |  |
| 2026-11-26 09:18:51 | Moragaswewa (Deduru Oya) | 4.22 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-26 09:12:56 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.012 |  |
| 2026-11-26 09:11:00 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.072 |  |
| 2026-11-26 09:09:58 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.019 |  |
| 2026-11-26 09:08:38 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.044 |  |
| 2026-11-26 09:08:05 | Badalgama (Maha Oya) | 4.37 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:07:55 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-11-26 09:07:54 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.052 |  |
| 2026-11-26 09:07:39 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | -0.151 |  |
| 2026-11-26 09:06:41 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.483 |  |
| 2026-11-26 09:05:59 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:05:58 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.070 |  |
| 2026-11-26 09:05:34 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | -0.054 |  |
| 2026-11-26 09:05:27 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | -0.059 |  |
| 2026-11-26 09:05:15 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:05:11 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.060 |  |
| 2026-11-26 09:04:48 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.035 |  |
| 2026-11-26 09:04:48 | Galgamuwa (Mee Oya) | 1.28 | 🟢 Normal | -36.000 |  |
| 2026-11-26 09:04:47 | Galgamuwa (Mee Oya) | 1.29 | 🟢 Normal | -36.000 |  |
| 2026-11-26 09:04:34 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-11-26 09:04:10 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:03:54 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:03:47 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | 0.000 |  |
| 2026-11-26 09:03:44 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-26 09:03:33 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-11-26 09:03:27 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.11 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-11-26 09:03:01 | Giriulla (Maha Oya) | 3.30 | 🟢 Normal | -0.120 |  |
| 2026-11-26 09:02:58 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | -0.080 |  |
| 2026-11-26 09:02:56 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-11-26 09:02:46 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:02:37 | Thanamalwila (Kirindi Oya) | 1.71 | 🟢 Normal | -0.030 |  |
| 2026-11-26 09:02:13 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 09:01:25 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-11-26 09:01:21 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:01:07 | Manampitiya (Mahaweli Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:00:23 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.063 |  |
| 2026-11-26 09:00:09 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 09:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.11 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-11-26 09:03:47 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | 0.000 |  |
| 2026-11-26 09:18:51 | Moragaswewa (Deduru Oya) | 4.22 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-26 09:03:44 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-26 09:02:13 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 09:05:15 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:05:59 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:03:27 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:01:21 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:04:10 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:08:05 | Badalgama (Maha Oya) | 4.37 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:01:07 | Manampitiya (Mahaweli Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:03:54 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:03:33 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-11-26 09:07:55 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-11-26 09:01:25 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-11-26 09:12:56 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.012 |  |
| 2026-11-26 09:09:58 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.019 |  |
| 2026-11-26 09:04:34 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-11-26 09:02:56 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-26 09:20:20 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | -0.023 |  |
| 2026-11-26 09:02:37 | Thanamalwila (Kirindi Oya) | 1.71 | 🟢 Normal | -0.030 |  |
| 2026-11-26 09:00:09 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.031 |  |
| 2026-11-26 09:04:48 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.035 |  |
| 2026-11-26 09:08:38 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.044 |  |
| 2026-11-26 09:07:54 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.052 |  |
| 2026-11-26 09:05:34 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | -0.054 |  |
| 2026-11-26 09:05:27 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | -0.059 |  |
| 2026-11-26 09:05:11 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.060 |  |
| 2026-11-26 09:00:23 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.063 |  |
| 2026-11-26 09:05:58 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.070 |  |
| 2026-11-26 09:11:00 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.072 |  |
| 2026-11-26 09:02:58 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | -0.080 |  |
| 2026-11-26 09:03:01 | Giriulla (Maha Oya) | 3.30 | 🟢 Normal | -0.120 |  |
| 2026-11-26 09:20:13 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.132 |  |
| 2026-11-26 09:07:39 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | -0.151 |  |
| 2026-11-26 09:06:41 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.483 |  |
| 2026-11-26 09:04:48 | Galgamuwa (Mee Oya) | 1.28 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)