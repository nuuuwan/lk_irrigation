# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_05:26:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,090 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 05:26:32 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:20:09 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.008 |  |
| 2026-09-27 05:16:44 | Magura (Kalu Ganga) | 3.13 | 🟢 Normal | -0.468 |  |
| 2026-09-27 05:11:50 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -0.028 |  |
| 2026-09-27 05:09:41 | Rathnapura (Kalu Ganga) | 4.02 | 🟢 Normal | -0.094 |  |
| 2026-09-27 05:08:20 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.065 |  |
| 2026-09-27 05:08:20 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.057 |  |
| 2026-09-27 05:07:48 | Thawalama (Gin Ganga) | 2.87 | 🟢 Normal | -0.009 |  |
| 2026-09-27 05:07:45 | Magura (Kalu Ganga) | 3.20 | 🟢 Normal | -0.468 |  |
| 2026-09-27 05:05:59 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:05:50 | Panadugama (Nilwala Ganga) | 5.57 | 🟡 Alert | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 04:29:55 | Baddegama (Gin Ganga) | 4.76 | 🟠 Minor Flood | -0.007 |  |
| 2026-09-27 04:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.79 | 🟠 Minor Flood | -0.014 |  |
| 2026-09-27 05:04:37 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | -0.033 |  |
| 2026-09-27 05:05:50 | Panadugama (Nilwala Ganga) | 5.57 | 🟡 Alert | -0.040 |  |
| 2026-09-27 05:00:42 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:02:21 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:04:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:02:41 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:05:10 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:02:38 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:01:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:05:59 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:03:45 | Putupaula (Kalu Ganga) | 2.87 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:26:32 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:01:32 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:02:54 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.005 |  |
| 2026-09-27 05:20:09 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.008 |  |
| 2026-09-27 05:07:48 | Thawalama (Gin Ganga) | 2.87 | 🟢 Normal | -0.009 |  |
| 2026-09-27 05:05:38 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.009 |  |
| 2026-09-27 05:03:03 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-27 05:02:43 | Dunamale (Aththanagalu Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-09-27 05:01:21 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:02:21 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-27 05:03:54 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.015 |  |
| 2026-09-27 05:11:50 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -0.028 |  |
| 2026-09-27 05:05:42 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.028 |  |
| 2026-09-27 05:01:15 | Ellagawa (Kalu Ganga) | 8.69 | 🟢 Normal | -0.030 |  |
| 2026-09-27 05:04:34 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.038 |  |
| 2026-09-27 05:03:46 | Deraniyagala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.043 |  |
| 2026-09-27 05:08:20 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.057 |  |
| 2026-09-27 05:02:41 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.059 |  |
| 2026-09-27 05:04:18 | Hanwella (Kelani Ganga) | 4.71 | 🟢 Normal | -0.062 |  |
| 2026-09-27 05:08:20 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.065 |  |
| 2026-09-27 05:02:37 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.071 |  |
| 2026-09-27 05:01:47 | Kithulgala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.074 |  |
| 2026-09-26 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.089 |  |
| 2026-09-27 05:09:41 | Rathnapura (Kalu Ganga) | 4.02 | 🟢 Normal | -0.094 |  |
| 2026-09-27 05:02:42 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | -0.146 |  |
| 2026-09-27 05:16:44 | Magura (Kalu Ganga) | 3.13 | 🟢 Normal | -0.468 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)