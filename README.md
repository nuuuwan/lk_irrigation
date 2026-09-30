# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_11:08:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,998 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 11:08:12 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:07:57 | Panadugama (Nilwala Ganga) | 3.43 | 🟢 Normal | -0.019 |  |
| 2026-09-30 11:07:38 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:06:32 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.204 |  |
| 2026-09-30 11:06:17 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:06:05 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:05:43 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.019 |  |
| 2026-09-30 11:05:35 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | -0.040 |  |
| 2026-09-30 11:05:11 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:04:50 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.049 |  |
| 2026-09-30 11:04:46 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-09-30 11:04:37 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-30 11:04:16 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.012 |  |
| 2026-09-30 11:03:52 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.011 |  |
| 2026-09-30 11:03:51 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 11:03:43 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-09-30 11:03:24 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.060 |  |
| 2026-09-30 11:03:22 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:03:18 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 11:02:58 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-09-30 11:02:55 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:02:50 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:02:49 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.112 |  |
| 2026-09-30 11:02:40 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.12 | 🟢 Normal | -0.021 |  |
| 2026-09-30 11:02:11 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 11:02:07 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | -0.021 |  |
| 2026-09-30 11:01:51 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.141 |  |
| 2026-09-30 11:01:45 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:01:41 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:01:27 | Nagalagam Street (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:01:14 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:00:56 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.042 |  |
| 2026-09-30 11:00:38 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-09-30 11:00:35 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 11:03:18 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 11:03:51 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 11:02:11 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 10:07:09 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:02:50 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:00:35 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:02:55 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:06:05 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-30 10:05:59 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-09-30 10:03:42 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:01:27 | Nagalagam Street (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:01:14 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:02:40 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:01:41 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:08:12 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:03:22 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:01:45 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:05:11 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-30 11:06:17 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 10:14:23 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.009 |  |
| 2026-09-30 11:04:46 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-09-30 11:04:37 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-30 10:03:26 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-09-30 11:00:38 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-09-30 11:03:43 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-09-30 11:03:52 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.011 |  |
| 2026-09-30 11:04:16 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.012 |  |
| 2026-09-30 11:07:57 | Panadugama (Nilwala Ganga) | 3.43 | 🟢 Normal | -0.019 |  |
| 2026-09-30 11:05:43 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.019 |  |
| 2026-09-30 11:02:58 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-09-30 11:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.12 | 🟢 Normal | -0.021 |  |
| 2026-09-30 11:02:07 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | -0.021 |  |
| 2026-09-30 11:05:35 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | -0.040 |  |
| 2026-09-30 11:00:56 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.042 |  |
| 2026-09-30 11:04:50 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.049 |  |
| 2026-09-30 11:03:24 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.060 |  |
| 2026-09-30 11:02:49 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.112 |  |
| 2026-09-30 11:01:51 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.141 |  |
| 2026-09-30 11:06:32 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)