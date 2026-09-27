# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_16:04:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,504 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 16:04:13 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | -0.070 |  |
| 2026-09-27 16:04:03 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:04:01 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 16:03:56 | Magura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.043 |  |
| 2026-09-27 16:03:53 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:03:35 | Putupaula (Kalu Ganga) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:03:33 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:03:24 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:03:24 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | -0.030 |  |
| 2026-09-27 16:02:54 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:02:45 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:02:32 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-27 16:02:31 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 16:02:14 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-09-27 16:02:09 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.021 |  |
| 2026-09-27 16:02:07 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:01:34 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:01:11 | Weraganthota (Mahaweli Ganga) | -3.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:01:05 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:00:58 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:00:48 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:00:34 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-09-27 16:00:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | -0.094 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 16:02:31 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 15:05:37 | Baddegama (Gin Ganga) | 4.60 | 🟠 Minor Flood | -0.021 |  |
| 2026-09-27 15:03:14 | Panadugama (Nilwala Ganga) | 5.22 | 🟡 Alert | -0.031 |  |
| 2026-09-27 16:00:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | -0.094 |  |
| 2026-09-27 15:08:32 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-27 15:07:02 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-09-27 16:02:32 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-27 16:04:01 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 16:01:11 | Weraganthota (Mahaweli Ganga) | -3.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:00:58 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:02:45 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:02:54 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:01:05 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:02:10 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:05:24 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:00:48 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:01:50 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:03:33 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 16:01:34 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 15:05:16 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | -0.005 |  |
| 2026-09-27 15:07:45 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-09-27 16:04:03 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-09-27 15:04:41 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:02:07 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:03:53 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:03:35 | Putupaula (Kalu Ganga) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-09-27 16:03:24 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-09-27 15:05:04 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-09-27 16:02:14 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-09-27 15:02:29 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.021 |  |
| 2026-09-27 16:02:09 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.021 |  |
| 2026-09-27 16:00:34 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-09-27 16:03:24 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | -0.030 |  |
| 2026-09-27 16:03:56 | Magura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.043 |  |
| 2026-09-27 15:03:04 | Rathnapura (Kalu Ganga) | 3.14 | 🟢 Normal | -0.060 |  |
| 2026-09-27 16:04:13 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | -0.070 |  |
| 2026-09-27 15:02:36 | Ellagawa (Kalu Ganga) | 8.21 | 🟢 Normal | -0.072 |  |
| 2026-09-27 15:04:45 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)