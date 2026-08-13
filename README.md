# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_14:13:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **232,407 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-13 14:13:03 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.018 |  |
| 2026-08-13 14:12:13 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-08-13 14:11:19 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:08:29 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-13 14:07:06 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | -0.060 |  |
| 2026-08-13 14:06:46 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:06:37 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:06:16 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:05:38 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-08-13 14:03:52 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 14:03:32 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:03:26 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.061 |  |
| 2026-08-13 14:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:03:14 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-13 14:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.43 | 🟢 Normal | -0.069 |  |
| 2026-08-13 14:03:01 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-08-13 14:02:57 | Hanwella (Kelani Ganga) | 1.71 | 🟢 Normal | -0.020 |  |
| 2026-08-13 14:02:51 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | -0.022 |  |
| 2026-08-13 14:02:34 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:02:30 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:02:25 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 14:02:22 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-08-13 14:02:07 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-08-13 14:02:01 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:01:46 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-08-13 14:01:42 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:01:32 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:01:22 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:01:18 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -36.000 |  |
| 2026-08-13 14:01:17 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -36.000 |  |
| 2026-08-13 14:01:08 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:00:54 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:00:38 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-13 14:00:17 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:00:11 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:00:07 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.021 |  |
| 2026-08-13 13:39:16 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.018 |  |
| 2026-08-13 13:27:13 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-13 14:03:01 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-08-13 14:02:22 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-08-13 14:03:14 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-13 14:00:38 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-13 13:09:11 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-13 14:02:25 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 14:03:52 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 14:02:30 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:11:19 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:02:34 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:01:42 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:01:22 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:03:04 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:00:11 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:02:01 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:01:08 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:06:46 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:06:37 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:00:17 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:03:32 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:00:54 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:06:16 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:01:32 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-13 14:12:13 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-08-13 14:05:38 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-08-13 14:01:46 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-08-13 14:08:29 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-13 13:06:49 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-08-13 13:06:51 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-08-13 14:13:03 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.018 |  |
| 2026-08-13 14:02:57 | Hanwella (Kelani Ganga) | 1.71 | 🟢 Normal | -0.020 |  |
| 2026-08-13 14:02:07 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-08-13 14:00:07 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.021 |  |
| 2026-08-13 14:02:51 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | -0.022 |  |
| 2026-08-13 14:07:06 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | -0.060 |  |
| 2026-08-13 14:03:26 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.061 |  |
| 2026-08-13 14:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.43 | 🟢 Normal | -0.069 |  |
| 2026-08-13 14:01:18 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)