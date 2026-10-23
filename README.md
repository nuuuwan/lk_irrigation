# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_16:06:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,914 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 16:06:27 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-10-23 16:05:25 | Giriulla (Maha Oya) | 2.02 | 🟢 Normal | -0.040 |  |
| 2026-10-23 16:05:01 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.028 |  |
| 2026-10-23 16:04:47 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.028 |  |
| 2026-10-23 16:04:31 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.116 |  |
| 2026-10-23 16:04:26 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-10-23 16:04:07 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | -0.020 |  |
| 2026-10-23 16:04:04 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:03:56 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-23 16:03:50 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.041 |  |
| 2026-10-23 16:03:49 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | -0.049 |  |
| 2026-10-23 16:03:34 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.374 | 🔺 Rising |
| 2026-10-23 16:03:16 | Moragaswewa (Deduru Oya) | 4.54 | 🟢 Normal | -0.060 |  |
| 2026-10-23 16:03:07 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-23 16:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.85 | 🟢 Normal | -0.061 |  |
| 2026-10-23 16:02:42 | Galgamuwa (Mee Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:02:40 | Ellagawa (Kalu Ganga) | 7.40 | 🟢 Normal | -0.041 |  |
| 2026-10-23 16:02:17 | Horowpothana (Yan Oya) | 2.76 | 🟢 Normal | -0.107 |  |
| 2026-10-23 16:02:16 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:02:15 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-10-23 16:02:09 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:02:08 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-23 16:02:02 | Thanthirimale (Malwathu Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:01:53 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:01:39 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:01:31 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.125 |  |
| 2026-10-23 16:01:24 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-10-23 16:01:15 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:01:00 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:00:43 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-10-23 16:00:37 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.050 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 16:03:34 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.374 | 🔺 Rising |
| 2026-10-23 16:00:37 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-23 16:01:53 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:02:42 | Galgamuwa (Mee Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-10-23 15:01:07 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:02:16 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:02:09 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:04:04 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:01:00 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:02:02 | Thanthirimale (Malwathu Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:01:39 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:01:15 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:03:56 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-23 16:02:08 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-23 16:03:07 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-23 16:00:43 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-10-23 15:10:59 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-23 16:04:26 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-10-23 15:03:03 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-10-23 16:02:15 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-10-23 16:04:07 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | -0.020 |  |
| 2026-10-23 16:06:27 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-10-23 15:03:31 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-10-23 16:05:01 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.028 |  |
| 2026-10-23 15:09:07 | Badalgama (Maha Oya) | 3.37 | 🟢 Normal | -0.028 |  |
| 2026-10-23 16:04:47 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.028 |  |
| 2026-10-23 16:05:25 | Giriulla (Maha Oya) | 2.02 | 🟢 Normal | -0.040 |  |
| 2026-10-23 15:05:03 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.041 |  |
| 2026-10-23 16:02:40 | Ellagawa (Kalu Ganga) | 7.40 | 🟢 Normal | -0.041 |  |
| 2026-10-23 16:03:50 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.041 |  |
| 2026-10-23 16:03:49 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | -0.049 |  |
| 2026-10-23 16:01:24 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-10-23 16:03:16 | Moragaswewa (Deduru Oya) | 4.54 | 🟢 Normal | -0.060 |  |
| 2026-10-23 16:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.85 | 🟢 Normal | -0.061 |  |
| 2026-10-23 16:02:17 | Horowpothana (Yan Oya) | 2.76 | 🟢 Normal | -0.107 |  |
| 2026-10-23 15:07:18 | Rathnapura (Kalu Ganga) | 3.28 | 🟢 Normal | -0.112 |  |
| 2026-10-23 16:04:31 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.116 |  |
| 2026-10-23 16:01:31 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.125 |  |
| 2026-10-23 15:09:24 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.167 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)