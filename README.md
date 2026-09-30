# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_23:27:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,455 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 23:27:30 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:26:56 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.008 |  |
| 2026-09-30 23:15:48 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:11:25 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:10:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:09:54 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.028 |  |
| 2026-09-30 23:09:18 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.009 |  |
| 2026-09-30 23:09:10 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-09-30 23:06:41 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:06:11 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-09-30 23:06:07 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-09-30 23:05:54 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:05:48 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.111 |  |
| 2026-09-30 23:05:46 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:05:11 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:04:41 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:04:31 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-09-30 23:04:25 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:03:49 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-30 23:03:46 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-30 23:03:38 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:03:27 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-30 23:03:14 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:03:02 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:02:56 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:02:55 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:02:48 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:02:35 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:02:13 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:02:10 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-09-30 23:01:35 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-30 23:01:34 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.010 |  |
| 2026-09-30 23:01:25 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:01:09 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | -0.011 |  |
| 2026-09-30 23:00:28 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:56:32 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 22:00:37 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-09-30 18:00:36 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-30 23:03:49 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-30 23:03:27 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-30 23:03:46 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-30 22:00:10 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:27:30 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:02:56 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:10:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:03:14 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:27:28 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:05:46 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:04:41 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:02:10 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:02:55 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:03:02 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:02:35 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:00:28 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:11:25 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:05:11 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:06:41 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:02:13 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:15:48 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-30 17:00:54 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:03:38 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:26:56 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.008 |  |
| 2026-09-30 23:09:18 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.009 |  |
| 2026-09-30 23:09:10 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-09-30 23:01:35 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-30 22:01:12 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-09-30 23:01:34 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.010 |  |
| 2026-09-30 23:06:07 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-09-30 22:56:32 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-09-30 23:01:09 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | -0.011 |  |
| 2026-09-30 23:06:11 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-09-30 23:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-09-30 23:09:54 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.028 |  |
| 2026-09-30 23:04:31 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-09-30 23:05:48 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)