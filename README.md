# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_01:03:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,815 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 01:03:03 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-28 01:02:51 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-09-28 01:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | 0.000 |  |
| 2026-09-28 01:02:44 | Kithulgala (Kelani Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-09-28 01:02:38 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 01:01:56 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-28 01:01:27 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | -0.012 |  |
| 2026-09-28 01:01:26 | Ellagawa (Kalu Ganga) | 7.37 | 🟢 Normal | -0.075 |  |
| 2026-09-28 01:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-28 01:00:49 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | -0.010 |  |
| 2026-09-28 01:00:43 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-28 00:27:17 | Baddegama (Gin Ganga) | 4.40 | 🟠 Minor Flood | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 01:01:27 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | -0.012 |  |
| 2026-09-28 00:27:17 | Baddegama (Gin Ganga) | 4.40 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-28 01:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | 0.000 |  |
| 2026-09-28 00:04:33 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-09-28 00:01:42 | Peradeniya (Mahaweli Ganga) | 3.39 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-09-28 00:02:26 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-28 01:02:44 | Kithulgala (Kelani Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | 0.000 |  |
| 2026-09-28 01:00:43 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-28 00:01:13 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 01:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-28 00:11:32 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:01:22 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-28 00:01:43 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-28 01:03:03 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-28 00:00:59 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 01:01:56 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-28 00:03:53 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 01:02:38 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 00:01:52 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-28 00:03:50 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-09-28 00:04:52 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:02:06 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 00:05:01 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-09-28 00:03:20 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-28 00:02:14 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 00:18:51 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | -0.008 |  |
| 2026-09-28 00:11:13 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-09-28 01:00:49 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | -0.010 |  |
| 2026-09-28 00:02:01 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-09-28 00:03:04 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-09-28 00:02:28 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-28 00:01:33 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-09-28 01:02:51 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-09-28 00:08:20 | Hanwella (Kelani Ganga) | 3.55 | 🟢 Normal | -0.027 |  |
| 2026-09-28 00:02:28 | Panadugama (Nilwala Ganga) | 4.92 | 🟢 Normal | -0.046 |  |
| 2026-09-28 00:06:00 | Rathnapura (Kalu Ganga) | 2.67 | 🟢 Normal | -0.050 |  |
| 2026-09-28 01:01:26 | Ellagawa (Kalu Ganga) | 7.37 | 🟢 Normal | -0.075 |  |
| 2026-09-27 18:01:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)