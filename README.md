# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_01:30:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **234,598 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 01:30:56 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:18:41 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:16:20 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.008 |  |
| 2026-08-16 01:12:22 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:12:10 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-16 01:07:23 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-08-16 01:06:34 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:06:13 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-08-16 01:05:39 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | -0.042 |  |
| 2026-08-16 01:05:32 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:04:48 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:04:30 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.032 |  |
| 2026-08-16 01:04:24 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:04:22 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-08-16 01:04:22 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.019 |  |
| 2026-08-16 01:04:15 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:03:17 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 01:02:22 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-08-16 01:02:32 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-16 01:01:40 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-16 00:03:42 | Glencourse (Kelani Ganga) | 10.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-16 01:12:10 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-16 01:00:08 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:01:28 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:02:06 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:04:48 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:01:46 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:02:24 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:00:12 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-15 18:11:23 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:30:56 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:04:15 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:05:32 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:12:22 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:53:18 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:04:24 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:03:17 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:04:22 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:18:41 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-08-15 18:01:43 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:06:03 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:01:43 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:01:57 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-16 01:16:20 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.008 |  |
| 2026-08-16 01:07:23 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-08-16 01:06:13 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-08-16 01:02:23 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-08-16 01:02:39 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-08-16 01:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.019 |  |
| 2026-08-16 00:03:18 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-08-16 01:04:22 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-08-16 01:02:06 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.020 |  |
| 2026-08-16 01:01:31 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.030 |  |
| 2026-08-15 18:00:55 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.031 |  |
| 2026-08-16 01:04:30 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.032 |  |
| 2026-08-16 01:05:39 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | -0.042 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)