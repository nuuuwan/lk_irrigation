# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_04:48:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **234,700 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 04:48:54 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.006 |  |
| 2026-08-16 04:37:30 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.013 |  |
| 2026-08-16 04:29:45 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:26:05 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:25:35 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:17:40 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:15:18 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:15:08 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-16 04:14:50 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:07:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -0.018 |  |
| 2026-08-16 04:07:17 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-08-16 04:06:26 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:05:44 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:05:25 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-16 04:05:02 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-08-16 04:04:39 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:04:23 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:04:22 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-08-16 04:04:06 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-16 04:04:02 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-08-16 04:03:35 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:03:22 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-16 04:03:07 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:02:56 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-16 04:02:32 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.019 |  |
| 2026-08-16 04:02:26 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:02:26 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 04:04:22 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-08-16 04:04:06 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-16 04:04:02 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-08-16 04:02:56 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-16 04:03:22 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-16 04:05:25 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-16 04:15:08 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-16 04:03:07 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-08-16 03:00:39 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:02:26 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:03:35 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:05:44 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:17:40 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-15 18:11:23 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:06:26 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:02:06 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:26:05 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:04:23 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:29:45 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:14:50 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:04:39 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:15:18 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-15 18:01:43 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:25:35 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-16 03:04:18 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:01:12 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 04:48:54 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.006 |  |
| 2026-08-16 03:05:40 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-08-16 04:07:17 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-08-16 04:01:44 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-08-16 04:02:10 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-08-16 04:05:02 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-08-16 04:37:30 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.013 |  |
| 2026-08-16 04:07:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -0.018 |  |
| 2026-08-16 04:02:32 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.019 |  |
| 2026-08-15 18:00:55 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.031 |  |
| 2026-08-16 04:02:26 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | -0.032 |  |
| 2026-08-16 04:01:13 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.032 |  |
| 2026-08-16 04:01:46 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.199 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)