# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_08:12:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **227,674 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 08:12:41 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-08-08 08:12:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | -43.571 |  |
| 2026-08-08 08:12:16 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-08 08:11:12 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-08 08:09:02 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:08:26 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:07:39 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.018 |  |
| 2026-08-08 08:06:55 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-08-08 08:06:45 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-08 08:06:44 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-08-08 08:06:27 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-08 08:06:26 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:05:21 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-08 08:05:06 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.019 |  |
| 2026-08-08 08:05:01 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-08 08:04:39 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-08-08 08:04:24 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-08 08:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 8.78 | 🔴 Major Flood | -43.571 |  |
| 2026-08-08 08:03:42 | Hanwella (Kelani Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-08-08 08:03:36 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-08-08 08:03:29 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:03:10 | Peradeniya (Mahaweli Ganga) | 3.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 08:03:08 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-08 08:03:03 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 08:02:40 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-08 08:02:36 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:02:23 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 08:02:20 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:02:18 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:02:01 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:01:57 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-08 08:01:56 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:01:48 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | -0.040 |  |
| 2026-08-08 08:01:32 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:01:31 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:01:27 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:01:26 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.021 |  |
| 2026-08-08 08:00:29 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:00:11 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:41:34 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.071 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 08:06:55 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-08-08 08:05:21 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-08 08:03:36 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-08-08 08:02:40 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-08 08:11:12 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-08 08:12:16 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-08 08:03:08 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-08 08:03:10 | Peradeniya (Mahaweli Ganga) | 3.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 08:02:23 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 08:01:57 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-08 08:03:03 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 08:06:45 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-08 08:06:27 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-08 08:09:02 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:02:20 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:00:11 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:01:27 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:01:56 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:03:29 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:02:01 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:08:26 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:01:32 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:02:36 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:02:18 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:06:26 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 06:01:41 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:01:31 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:00:29 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 08:06:44 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-08-08 08:12:41 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-08-08 08:04:39 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-08-08 08:03:42 | Hanwella (Kelani Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-08-08 08:04:24 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-08 08:05:01 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-08 08:07:39 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.018 |  |
| 2026-08-08 08:05:06 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.019 |  |
| 2026-08-08 08:01:26 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.021 |  |
| 2026-08-08 08:01:48 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | -0.040 |  |
| 2026-08-08 08:12:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | -43.571 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)