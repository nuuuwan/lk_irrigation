# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_10:12:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,502 measurements** from **39** stations.
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
| 2026-08-20 10:12:12 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-08-20 10:11:13 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:08:38 | Rathnapura (Kalu Ganga) | 2.90 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-20 10:07:13 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:06:41 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 10:06:28 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-20 10:06:04 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-20 10:05:53 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-20 10:05:50 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-08-20 10:05:48 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-08-20 10:05:28 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.032 |  |
| 2026-08-20 10:05:23 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-20 10:05:08 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:05:05 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:04:22 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:04:01 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-08-20 10:03:46 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-08-20 10:03:32 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:03:31 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:03:23 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:03:09 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-08-20 10:03:01 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-08-20 10:02:37 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-20 10:02:27 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.147 |  |
| 2026-08-20 10:02:20 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-20 10:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-08-20 10:02:14 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:02:11 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:02:07 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:02:03 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-08-20 10:02:02 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:01:26 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:01:21 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:00:44 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 10:00:42 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.030 |  |
| 2026-08-20 10:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-08-20 09:59:41 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 10:12:12 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-08-20 10:03:46 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-08-20 10:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-08-20 10:05:53 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-20 10:08:38 | Rathnapura (Kalu Ganga) | 2.90 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-20 10:02:20 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-20 10:05:23 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-20 10:06:28 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-20 10:06:04 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-20 10:02:37 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-20 10:00:44 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 10:06:41 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 10:02:07 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:02:11 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:02:14 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:04:42 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:02:02 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:04:22 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:03:23 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:09:58 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:59:41 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:05:08 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:03:31 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:07:13 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:03:32 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:05:05 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:11:13 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:01:21 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:01:26 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-20 10:05:48 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-08-20 10:03:01 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-08-20 10:04:01 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-08-20 10:05:50 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-08-20 10:03:09 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-08-20 10:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-08-20 10:00:42 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.030 |  |
| 2026-08-20 10:02:03 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-08-20 10:05:28 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.032 |  |
| 2026-08-20 10:02:27 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)