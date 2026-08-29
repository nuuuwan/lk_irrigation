# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_03:03:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **246,763 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 03:03:19 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-08-30 03:03:12 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:02:56 | Hanwella (Kelani Ganga) | 1.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-30 03:02:42 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-30 03:02:29 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:02:19 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:01:43 | Giriulla (Maha Oya) | 0.16 | 🟢 Normal | -0.835 |  |
| 2026-08-30 03:01:38 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:01:33 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:01:24 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-30 03:01:23 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:01:17 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-30 03:01:08 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-08-30 02:59:47 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 02:35:10 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:23:59 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:22:51 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:17:11 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.035 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 02:02:52 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-08-30 02:05:45 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-30 03:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-30 02:17:11 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-30 03:01:17 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-30 03:02:56 | Hanwella (Kelani Ganga) | 1.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-30 01:01:25 | Glencourse (Kelani Ganga) | 9.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-30 02:59:47 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 03:01:23 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:13:02 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:02:26 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-29 18:02:54 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:02:19 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:02:29 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:01:12 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:05:44 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:03:12 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:01:33 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:01:38 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:02:42 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:07:35 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:35:10 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:23:59 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-08-29 18:00:49 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:10:05 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:02:13 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:11:30 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | -0.005 |  |
| 2026-08-30 01:35:01 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.007 |  |
| 2026-08-30 02:03:49 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-08-30 03:03:19 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-08-30 03:01:24 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-30 03:01:08 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-08-30 00:01:49 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-08-30 01:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-08-30 02:13:44 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | -0.027 |  |
| 2026-08-29 18:01:39 | Weraganthota (Mahaweli Ganga) | -3.51 | 🟢 Normal | -0.030 |  |
| 2026-08-30 02:02:18 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.109 |  |
| 2026-08-30 01:32:33 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.110 |  |
| 2026-08-30 03:01:43 | Giriulla (Maha Oya) | 0.16 | 🟢 Normal | -0.835 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)