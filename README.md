# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_18:33:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,076 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 18:33:58 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:15:18 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:10:57 | Panadugama (Nilwala Ganga) | 4.81 | 🟢 Normal | -0.011 |  |
| 2026-09-22 18:10:36 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:10:20 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-22 18:08:36 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | -0.019 |  |
| 2026-09-22 18:08:21 | Rathnapura (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:08:12 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.028 |  |
| 2026-09-22 18:07:49 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:07:47 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:07:45 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:06:20 | Rathnapura (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:05:29 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 18:05:10 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:05:04 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 18:04:56 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:04:42 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:04:27 | Hanwella (Kelani Ganga) | 4.56 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:04:23 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:03:45 | Glencourse (Kelani Ganga) | 12.45 | 🟢 Normal | -0.074 |  |
| 2026-09-22 18:03:33 | Nawalapitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-22 18:03:32 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.000 |  |
| 2026-09-22 18:02:59 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-22 18:02:46 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.16 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-22 18:02:19 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:02:16 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-22 18:01:58 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:01:58 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:01:44 | Putupaula (Kalu Ganga) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:01:40 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:01:38 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:01:35 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:01:32 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:01:23 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:01:18 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-09-22 18:01:14 | Ellagawa (Kalu Ganga) | 8.73 | 🟢 Normal | -0.043 |  |
| 2026-09-22 18:01:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:59:55 | Magura (Kalu Ganga) | 4.67 | 🟡 Alert | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 18:05:29 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.16 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-22 18:03:32 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.000 |  |
| 2026-09-22 17:59:55 | Magura (Kalu Ganga) | 4.67 | 🟡 Alert | -0.022 |  |
| 2026-09-22 18:01:18 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-09-22 18:02:16 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-22 18:03:33 | Nawalapitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-22 18:10:20 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-22 18:02:59 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-22 18:05:04 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 18:04:23 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:01:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:01:58 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:01:40 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:01:23 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:07:47 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:04:56 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:15:18 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:04:42 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:33:58 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:01:38 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:07:49 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:10:36 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:07:45 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:08:21 | Rathnapura (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:01:35 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:01:58 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:02:46 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:01:32 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:04:27 | Hanwella (Kelani Ganga) | 4.56 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:02:19 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:01:44 | Putupaula (Kalu Ganga) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:05:10 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:10:57 | Panadugama (Nilwala Ganga) | 4.81 | 🟢 Normal | -0.011 |  |
| 2026-09-22 18:08:36 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | -0.019 |  |
| 2026-09-22 18:08:12 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.028 |  |
| 2026-09-22 18:01:14 | Ellagawa (Kalu Ganga) | 8.73 | 🟢 Normal | -0.043 |  |
| 2026-09-22 18:03:45 | Glencourse (Kelani Ganga) | 12.45 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)