# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_11:25:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,544 measurements** from **39** stations.
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
| 2026-08-20 11:25:19 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.015 |  |
| 2026-08-20 11:19:29 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.049 |  |
| 2026-08-20 11:11:33 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:11:27 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.046 |  |
| 2026-08-20 11:09:50 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.027 |  |
| 2026-08-20 11:09:12 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-20 11:07:35 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-08-20 11:07:09 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 10:12:12 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-08-20 11:04:03 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-08-20 11:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-20 11:03:47 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-20 11:03:15 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-20 11:09:12 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-20 11:05:20 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-20 11:05:00 | Rathnapura (Kalu Ganga) | 2.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-20 11:03:39 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-20 11:01:13 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 11:02:42 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:01:43 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:01:22 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:05:14 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:01:43 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:01:25 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:03:28 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:00:18 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:07:09 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:11:33 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:03:16 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:03:55 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:04:39 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:00:50 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:01:54 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:01:08 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:03:32 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-20 11:07:35 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-08-20 11:03:09 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-08-20 11:25:19 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.015 |  |
| 2026-08-20 11:01:01 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.020 |  |
| 2026-08-20 11:09:50 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.027 |  |
| 2026-08-20 11:01:47 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.036 |  |
| 2026-08-20 11:05:19 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.039 |  |
| 2026-08-20 11:11:27 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.046 |  |
| 2026-08-20 11:19:29 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.049 |  |
| 2026-08-20 11:02:56 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.090 |  |
| 2026-08-20 11:04:19 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)