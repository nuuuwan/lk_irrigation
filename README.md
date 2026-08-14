# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_09:11:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **233,099 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 09:11:35 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.009 |  |
| 2026-08-14 09:08:33 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:08:08 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-08-14 09:06:52 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-08-14 09:06:39 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-14 09:06:16 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-14 09:05:54 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:05:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | -0.106 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 09:06:39 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-14 09:06:16 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-14 09:03:20 | Peradeniya (Mahaweli Ganga) | 3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-14 09:02:00 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:00:21 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:00:33 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:03:20 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:02:43 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:02:09 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:04:04 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:05:54 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:02:49 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:01:56 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:00:55 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:02:58 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:02:37 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:02:35 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:03:51 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:08:33 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:02:11 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:02:04 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:04:32 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-14 09:11:35 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.009 |  |
| 2026-08-14 09:08:08 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-08-14 09:06:52 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-08-14 09:01:10 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | -0.010 |  |
| 2026-08-14 09:04:30 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-08-14 09:05:00 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.014 |  |
| 2026-08-14 09:02:44 | Nagalagam Street (Kelani Ganga) | 0.08 | 🟢 Normal | -0.015 |  |
| 2026-08-14 09:02:09 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.020 |  |
| 2026-08-14 09:03:55 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-08-14 09:03:30 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-08-14 09:02:48 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.030 |  |
| 2026-08-14 09:00:12 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.031 |  |
| 2026-08-14 09:01:07 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.040 |  |
| 2026-08-14 09:04:26 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.102 |  |
| 2026-08-14 09:05:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | -0.106 |  |
| 2026-08-14 09:03:30 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.225 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)