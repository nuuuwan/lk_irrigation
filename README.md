# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_02:39:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **235,530 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 02:39:10 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-17 02:10:57 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.018 |  |
| 2026-08-17 02:10:33 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-17 02:09:51 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:08:34 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-08-17 02:07:58 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 2.769 | 🔺 Rising |
| 2026-08-17 02:07:45 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 2.769 | 🔺 Rising |
| 2026-08-17 02:07:29 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-08-17 02:06:27 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:05:47 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-17 02:05:07 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-08-17 02:04:03 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:03:59 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:03:38 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-08-17 02:03:34 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 02:07:58 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 2.769 | 🔺 Rising |
| 2026-08-17 01:15:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-08-17 02:10:33 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-17 02:39:10 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-17 02:03:07 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-17 02:03:17 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-17 02:02:03 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-17 02:05:47 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-17 02:01:50 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:01:12 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:00:55 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:01:46 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:01:15 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:01:20 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:02:57 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:01:53 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:03:21 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:09:51 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 01:07:28 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-17 01:30:50 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:02:49 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:02:04 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:03:59 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:03:23 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:10:59 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:04:03 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:02:30 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:06:27 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:02:13 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.005 |  |
| 2026-08-17 02:08:34 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-08-17 02:05:07 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-08-17 02:03:09 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-08-16 18:03:12 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.010 |  |
| 2026-08-17 02:07:29 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-08-17 02:02:10 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-08-17 02:03:34 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.013 |  |
| 2026-08-17 02:10:57 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.018 |  |
| 2026-08-17 02:03:38 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-08-17 01:01:29 | Peradeniya (Mahaweli Ganga) | 3.14 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)