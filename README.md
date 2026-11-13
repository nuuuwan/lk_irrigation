# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_16:21:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,844 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 16:21:11 | Panadugama (Nilwala Ganga) | 6.15 | 🟠 Minor Flood | -0.016 |  |
| 2026-11-13 16:20:29 | Pitabeddara (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.032 |  |
| 2026-11-13 16:17:37 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.077 |  |
| 2026-11-13 16:15:29 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | -0.024 |  |
| 2026-11-13 16:15:06 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-11-13 16:12:31 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | -0.060 |  |
| 2026-11-13 16:10:29 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | -0.018 |  |
| 2026-11-13 16:09:10 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.053 |  |
| 2026-11-13 16:08:30 | Peradeniya (Mahaweli Ganga) | 3.68 | 🟢 Normal | -0.136 |  |
| 2026-11-13 16:08:12 | Putupaula (Kalu Ganga) | 2.28 | 🟢 Normal | -0.018 |  |
| 2026-11-13 16:07:34 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.019 |  |
| 2026-11-13 16:07:14 | Moraketiya (Walawe Ganga) | 3.73 | 🟡 Alert | -0.018 |  |
| 2026-11-13 16:06:04 | Baddegama (Gin Ganga) | 4.09 | 🟠 Minor Flood | -0.025 |  |
| 2026-11-13 16:05:52 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-11-13 16:05:33 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-11-13 16:05:09 | Rathnapura (Kalu Ganga) | 3.32 | 🟢 Normal | -0.080 |  |
| 2026-11-13 16:05:05 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-13 16:04:19 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-11-13 16:04:01 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-13 16:03:49 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-13 16:03:37 | Hanwella (Kelani Ganga) | 3.48 | 🟢 Normal | -0.051 |  |
| 2026-11-13 16:03:36 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 16:01:48 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 16:21:11 | Panadugama (Nilwala Ganga) | 6.15 | 🟠 Minor Flood | -0.016 |  |
| 2026-11-13 16:06:04 | Baddegama (Gin Ganga) | 4.09 | 🟠 Minor Flood | -0.025 |  |
| 2026-11-13 16:07:14 | Moraketiya (Walawe Ganga) | 3.73 | 🟡 Alert | -0.018 |  |
| 2026-11-13 16:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.91 | 🟡 Alert | -0.030 |  |
| 2026-11-13 16:04:01 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-13 16:00:23 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-13 16:03:27 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-13 16:01:38 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-13 16:01:31 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-13 16:01:35 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-13 16:05:05 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-13 16:04:19 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-11-13 16:03:49 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-13 16:10:29 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | -0.018 |  |
| 2026-11-13 16:08:12 | Putupaula (Kalu Ganga) | 2.28 | 🟢 Normal | -0.018 |  |
| 2026-11-13 16:15:06 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-11-13 16:07:34 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.019 |  |
| 2026-11-13 16:02:40 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-11-13 16:05:33 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-11-13 16:05:52 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-11-13 16:01:28 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-11-13 16:03:36 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.020 |  |
| 2026-11-13 16:02:42 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-11-13 16:01:52 | Kuda Oya (Kirindi Oya) | 2.31 | 🟢 Normal | -0.023 |  |
| 2026-11-13 16:15:29 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | -0.024 |  |
| 2026-11-13 16:02:35 | Thanamalwila (Kirindi Oya) | 2.07 | 🟢 Normal | -0.030 |  |
| 2026-11-13 16:20:29 | Pitabeddara (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.032 |  |
| 2026-11-13 16:02:29 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -0.040 |  |
| 2026-11-13 16:03:37 | Hanwella (Kelani Ganga) | 3.48 | 🟢 Normal | -0.051 |  |
| 2026-11-13 16:01:02 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.051 |  |
| 2026-11-13 16:09:10 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.053 |  |
| 2026-11-13 16:01:28 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.054 |  |
| 2026-11-13 16:12:31 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | -0.060 |  |
| 2026-11-13 16:01:09 | Ellagawa (Kalu Ganga) | 7.69 | 🟢 Normal | -0.070 |  |
| 2026-11-13 16:17:37 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.077 |  |
| 2026-11-13 16:05:09 | Rathnapura (Kalu Ganga) | 3.32 | 🟢 Normal | -0.080 |  |
| 2026-11-13 16:01:17 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | -0.133 |  |
| 2026-11-13 16:08:30 | Peradeniya (Mahaweli Ganga) | 3.68 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)