# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_07:23:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **241,975 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **4** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 07:23:38 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:14:15 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-24 07:14:03 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:11:47 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 07:02:50 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-24 07:01:45 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-24 07:04:44 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-24 07:14:15 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-24 07:06:36 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-24 07:05:18 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-24 07:08:36 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-24 07:01:39 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 07:02:53 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:01:54 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:05:04 | Moragaswewa (Deduru Oya) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:05:58 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:01:59 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:06:14 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:02:35 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:04:26 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:14:03 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:02:21 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:01:42 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:07:53 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:04:31 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:03:45 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:05:38 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:23:38 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:04:02 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:02:01 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 07:02:08 | Thanthirimale (Malwathu Oya) | 0.68 | 🟢 Normal | -0.002 |  |
| 2026-08-24 07:11:47 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.009 |  |
| 2026-08-24 07:03:55 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.009 |  |
| 2026-08-24 07:04:04 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-08-24 07:02:38 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-08-24 07:02:02 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-08-24 06:07:41 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.030 |  |
| 2026-08-24 07:05:37 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.052 |  |
| 2026-08-24 07:00:20 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.080 |  |
| 2026-08-24 07:08:02 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.089 |  |
| 2026-08-24 07:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.118 |  |
| 2026-08-24 07:04:46 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.232 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)