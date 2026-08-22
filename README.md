# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_10:20:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **240,296 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 10:20:26 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.008 |  |
| 2026-08-22 10:19:57 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:14:36 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-08-22 10:11:09 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:10:25 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.044 |  |
| 2026-08-22 10:09:42 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-08-22 10:09:34 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.045 |  |
| 2026-08-22 10:09:01 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-08-22 10:07:57 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-22 10:07:13 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:06:24 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 10:09:42 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-08-22 10:07:57 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-22 10:00:25 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:04:16 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:00:09 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:02:03 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:00:52 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:01:02 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:04:17 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:03:10 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:01:13 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:11:09 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:01:12 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:02:52 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:02:56 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:02:15 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:07:13 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:04:44 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:03:38 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:19:57 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:06:24 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:02:53 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:20:26 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.008 |  |
| 2026-08-22 10:14:36 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-08-22 10:03:10 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-08-22 10:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | -0.010 |  |
| 2026-08-22 10:05:18 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-08-22 10:03:04 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-08-22 10:01:14 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-08-22 10:09:01 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-08-22 10:01:25 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.020 |  |
| 2026-08-22 10:02:27 | Ellagawa (Kalu Ganga) | 5.89 | 🟢 Normal | -0.020 |  |
| 2026-08-22 10:03:22 | Hanwella (Kelani Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-08-22 10:02:49 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.022 |  |
| 2026-08-22 10:00:40 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.031 |  |
| 2026-08-22 10:10:25 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.044 |  |
| 2026-08-22 10:09:34 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.045 |  |
| 2026-08-22 10:01:37 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.049 |  |
| 2026-08-22 10:05:16 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)