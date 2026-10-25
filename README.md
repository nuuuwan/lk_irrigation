# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_09:10:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,423 measurements** from **39** stations.
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
| 2026-10-25 09:10:02 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.133 |  |
| 2026-10-25 09:08:54 | Rathnapura (Kalu Ganga) | 3.71 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-10-25 09:08:21 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-10-25 09:07:58 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | -0.018 |  |
| 2026-10-25 09:07:09 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:06:44 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 09:06:11 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:06:11 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:05:42 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-25 09:05:41 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:05:39 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-25 09:05:27 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-25 09:05:26 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-25 09:05:11 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 09:04:59 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:04:57 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 09:04:26 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.038 |  |
| 2026-10-25 09:04:09 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:03:56 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-25 09:03:43 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-10-25 09:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.02 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-25 09:03:20 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.072 |  |
| 2026-10-25 09:03:04 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-10-25 09:02:54 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-25 09:02:50 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:02:46 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.121 |  |
| 2026-10-25 09:02:45 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:02:39 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-25 09:02:35 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:02:34 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 09:02:20 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 09:02:18 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-10-25 09:02:12 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:01:51 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-10-25 09:01:30 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-25 09:01:11 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.095 |  |
| 2026-10-25 09:01:00 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.051 |  |
| 2026-10-25 09:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 09:08:54 | Rathnapura (Kalu Ganga) | 3.71 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-10-25 09:01:51 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-10-25 09:02:39 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-25 09:05:42 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-25 09:02:54 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-25 09:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.02 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-25 09:05:27 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-25 09:05:39 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-25 09:02:34 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 09:05:11 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 09:05:26 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-25 09:02:20 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 09:04:57 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 09:06:44 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 09:02:50 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:04:59 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:06:11 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:05:41 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:03:44 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:02:12 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:06:11 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:04:09 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:07:09 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:02:45 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:02:35 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-25 09:08:21 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-10-25 09:01:30 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-25 09:03:56 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-25 09:02:18 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-10-25 09:07:58 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | -0.018 |  |
| 2026-10-25 09:03:43 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-10-25 09:03:04 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-10-25 09:04:26 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.038 |  |
| 2026-10-25 09:01:00 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.051 |  |
| 2026-10-25 09:03:20 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.072 |  |
| 2026-10-25 09:01:11 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.095 |  |
| 2026-10-25 09:02:46 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.121 |  |
| 2026-10-25 09:10:02 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)