# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_20:03:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,454 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Putupaula — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 20:03:14 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 20:03:08 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-10-29 20:03:06 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | -0.014 |  |
| 2026-10-29 20:02:58 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-29 20:02:50 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-29 20:02:43 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-29 20:02:36 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | 0.000 |  |
| 2026-10-29 20:02:12 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | -0.010 |  |
| 2026-10-29 20:01:56 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-29 20:01:39 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-10-29 20:01:38 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.042 |  |
| 2026-10-29 20:01:38 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-29 20:01:31 | Rathnapura (Kalu Ganga) | 4.29 | 🟢 Normal | -0.052 |  |
| 2026-10-29 20:01:30 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.042 |  |
| 2026-10-29 20:00:39 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.014 |  |
| 2026-10-29 20:00:13 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 19:24:51 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.007 |  |
| 2026-10-29 19:22:40 | Pitabeddara (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-29 19:19:38 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.008 |  |
| 2026-10-29 19:19:24 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | -0.014 |  |
| 2026-10-29 19:16:17 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 19:12:58 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 19:04:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.10 | 🟠 Minor Flood | -0.038 |  |
| 2026-10-29 19:10:45 | Panadugama (Nilwala Ganga) | 5.74 | 🟡 Alert | 0.000 |  |
| 2026-10-29 19:07:15 | Putupaula (Kalu Ganga) | 3.65 | 🟡 Alert | -0.009 |  |
| 2026-10-29 19:05:25 | Baddegama (Gin Ganga) | 3.93 | 🟡 Alert | -0.029 |  |
| 2026-10-29 18:05:01 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-29 20:01:38 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-29 19:03:51 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-29 20:02:50 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-29 20:02:43 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-29 19:22:40 | Pitabeddara (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-29 20:00:13 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 19:11:59 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-29 19:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-10-29 20:01:56 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-29 19:05:45 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-29 19:09:24 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 20:02:36 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | 0.000 |  |
| 2026-10-29 20:03:14 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 19:01:05 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-29 19:04:05 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-29 20:02:58 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-29 19:03:20 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-29 19:24:51 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.007 |  |
| 2026-10-29 19:19:38 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.008 |  |
| 2026-10-29 19:07:47 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.009 |  |
| 2026-10-29 18:06:21 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-10-29 20:02:12 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | -0.010 |  |
| 2026-10-29 20:00:39 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.014 |  |
| 2026-10-29 20:03:06 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | -0.014 |  |
| 2026-10-29 19:01:02 | Magura (Kalu Ganga) | 3.20 | 🟢 Normal | -0.020 |  |
| 2026-10-29 20:03:08 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-10-29 19:11:36 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.026 |  |
| 2026-10-29 20:01:39 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-10-29 20:01:38 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.042 |  |
| 2026-10-29 20:01:30 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.042 |  |
| 2026-10-29 20:01:31 | Rathnapura (Kalu Ganga) | 4.29 | 🟢 Normal | -0.052 |  |
| 2026-10-29 18:01:49 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.059 |  |
| 2026-10-29 19:02:47 | Ellagawa (Kalu Ganga) | 9.71 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)