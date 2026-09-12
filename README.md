# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--12_06:32:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **258,592 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **45** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-12 06:32:41 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.002 |  |
| 2026-09-12 06:25:25 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:13:02 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.171 |  |
| 2026-09-12 06:12:37 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:10:43 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:10:34 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:10:26 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:10:14 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-09-12 06:10:00 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.174 |  |
| 2026-09-12 06:08:57 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-12 06:08:32 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:07:55 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.045 |  |
| 2026-09-12 06:07:12 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:06:50 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:05:27 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:05:26 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:04:52 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:04:19 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-12 06:04:14 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:04:08 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:04:08 | Moragaswewa (Deduru Oya) | -0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:03:45 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:03:43 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.030 |  |
| 2026-09-12 06:03:24 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | -0.048 |  |
| 2026-09-12 06:03:22 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:02:53 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:02:37 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:02:20 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:02:12 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-12 06:02:03 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-12 06:01:52 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:01:38 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.042 |  |
| 2026-09-12 06:01:32 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-09-12 06:01:22 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:01:16 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-12 06:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-09-12 06:01:04 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.043 |  |
| 2026-09-12 06:00:56 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-12 06:00:34 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:00:31 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-12 05:55:32 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.171 |  |
| 2026-09-12 05:51:59 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-12 05:51:09 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-12 05:50:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.227 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-12 06:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-09-12 06:02:03 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-12 06:08:57 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-12 06:01:16 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-12 06:02:12 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-12 06:04:19 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-12 06:32:41 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.002 |  |
| 2026-09-12 06:01:52 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:03:22 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:04:08 | Moragaswewa (Deduru Oya) | -0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:00:34 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:03:45 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:00:31 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:10:34 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:05:27 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:02:53 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:08:32 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:06:50 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:12:37 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:04:52 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:02:37 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:04:08 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:07:12 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:10:43 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-11 18:02:32 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:25:25 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:04:14 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:01:22 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-12 06:10:14 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-09-12 06:00:56 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-12 06:01:32 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-09-12 06:03:43 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.030 |  |
| 2026-09-12 06:01:38 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.042 |  |
| 2026-09-12 06:01:04 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.043 |  |
| 2026-09-12 06:07:55 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.045 |  |
| 2026-09-12 06:03:24 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | -0.048 |  |
| 2026-09-12 06:13:02 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.171 |  |
| 2026-09-12 06:10:00 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.174 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)