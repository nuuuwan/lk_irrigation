# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_12:09:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **236,783 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **0** measurements in the last **1 hour**.*

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-18 12:02:52 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-08-18 12:04:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-18 12:03:19 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-18 12:05:30 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-18 12:01:04 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-18 12:01:21 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:01:47 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:04:57 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:02:42 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:02:51 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:09:09 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:02:22 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:03:24 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:01:14 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:02:36 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:07:22 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:02:59 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:05:01 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:04:26 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:03:55 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:07:09 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:00:48 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:01:42 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:03:11 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-18 12:03:12 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-08-18 12:07:02 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-08-18 12:00:15 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.010 |  |
| 2026-08-18 12:03:14 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-08-18 12:02:00 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-08-18 12:05:33 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.015 |  |
| 2026-08-18 12:03:27 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-08-18 12:03:42 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-08-18 12:03:00 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-08-18 12:01:29 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.021 |  |
| 2026-08-18 12:03:39 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | -0.030 |  |
| 2026-08-18 12:03:20 | Hanwella (Kelani Ganga) | 1.61 | 🟢 Normal | -0.030 |  |
| 2026-08-18 12:06:40 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.033 |  |
| 2026-08-18 12:06:20 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.040 |  |
| 2026-08-18 12:03:19 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)