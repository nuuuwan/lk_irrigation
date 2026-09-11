# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--12_04:02:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **258,489 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-12 04:02:47 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-12 04:02:05 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-12 04:02:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-12 04:01:40 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-12 04:01:40 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-12 04:01:35 | Manampitiya (Mahaweli Ganga) | -0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-12 04:01:34 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | -0.010 |  |
| 2026-09-12 04:01:20 | Moragaswewa (Deduru Oya) | -0.31 | 🟢 Normal | -0.010 |  |
| 2026-09-12 04:00:46 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-12 04:00:36 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-12 03:29:37 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.007 |  |
| 2026-09-12 03:15:12 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.016 |  |
| 2026-09-12 03:13:49 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-09-12 03:13:43 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-12 03:09:40 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-09-12 04:02:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-12 02:41:56 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-12 04:00:36 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-12 03:03:45 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-12 03:07:34 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-12 03:03:04 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-11 18:03:43 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-11 18:08:01 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-09-12 03:03:18 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-12 02:02:49 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-12 03:11:59 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:02:14 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-12 04:02:05 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-12 03:02:46 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-12 03:07:54 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-12 03:13:43 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-12 03:07:02 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-09-12 03:07:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-12 04:01:40 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-12 04:00:46 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-12 03:02:24 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-12 03:04:33 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 03:04:44 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-12 04:01:35 | Manampitiya (Mahaweli Ganga) | -0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-11 18:02:32 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-12 02:04:00 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-12 01:05:11 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-12 03:01:42 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-12 04:01:40 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-12 03:10:17 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.002 |  |
| 2026-09-12 03:29:37 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.007 |  |
| 2026-09-12 04:01:34 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | -0.010 |  |
| 2026-09-12 04:02:47 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-12 04:01:20 | Moragaswewa (Deduru Oya) | -0.31 | 🟢 Normal | -0.010 |  |
| 2026-09-12 03:15:12 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.016 |  |
| 2026-09-12 03:06:33 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.019 |  |
| 2026-09-12 03:13:49 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-09-12 03:00:58 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.206 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)