# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_20:33:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,074 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 20:33:32 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | -0.018 |  |
| 2026-10-23 20:21:15 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:11:42 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.035 |  |
| 2026-10-23 20:08:37 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:08:23 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-10-23 20:06:44 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-23 20:06:09 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | -0.227 |  |
| 2026-10-23 20:06:03 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:05:59 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:05:42 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-10-23 20:04:52 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.029 |  |
| 2026-10-23 20:04:34 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:04:26 | Glencourse (Kelani Ganga) | 11.14 | 🟢 Normal | -0.041 |  |
| 2026-10-23 20:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.68 | 🟢 Normal | -0.019 |  |
| 2026-10-23 20:04:04 | Putupaula (Kalu Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-10-23 20:03:45 | Badalgama (Maha Oya) | 3.22 | 🟢 Normal | -0.021 |  |
| 2026-10-23 20:03:45 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-23 20:02:50 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.063 |  |
| 2026-10-23 20:02:40 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:02:28 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.040 |  |
| 2026-10-23 20:02:14 | Hanwella (Kelani Ganga) | 3.68 | 🟢 Normal | -0.050 |  |
| 2026-10-23 20:02:13 | Ellagawa (Kalu Ganga) | 7.19 | 🟢 Normal | -0.011 |  |
| 2026-10-23 20:02:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:02:05 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.021 |  |
| 2026-10-23 20:01:59 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.069 |  |
| 2026-10-23 20:01:50 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.074 |  |
| 2026-10-23 20:01:44 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:01:33 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-23 20:01:32 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.234 |  |
| 2026-10-23 20:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-23 20:01:21 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.072 |  |
| 2026-10-23 20:01:12 | Moragaswewa (Deduru Oya) | 4.28 | 🟢 Normal | -0.072 |  |
| 2026-10-23 20:00:38 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-10-23 20:00:37 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-10-23 20:00:22 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:00:13 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 20:05:42 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-10-23 20:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-23 20:06:44 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-23 20:08:37 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:02:40 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:01:44 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:06:03 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:02:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:00:22 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:04:34 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:05:59 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:21:15 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-23 20:03:45 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-23 20:01:33 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-23 18:01:50 | Thanthirimale (Malwathu Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-10-23 20:00:13 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-23 20:04:04 | Putupaula (Kalu Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-10-23 20:02:13 | Ellagawa (Kalu Ganga) | 7.19 | 🟢 Normal | -0.011 |  |
| 2026-10-23 20:00:38 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-10-23 20:33:32 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | -0.018 |  |
| 2026-10-23 20:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.68 | 🟢 Normal | -0.019 |  |
| 2026-10-23 20:08:23 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-10-23 20:00:37 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-10-23 20:02:05 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.021 |  |
| 2026-10-23 20:03:45 | Badalgama (Maha Oya) | 3.22 | 🟢 Normal | -0.021 |  |
| 2026-10-23 20:04:52 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.029 |  |
| 2026-10-23 20:11:42 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.035 |  |
| 2026-10-23 20:02:28 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.040 |  |
| 2026-10-23 20:04:26 | Glencourse (Kelani Ganga) | 11.14 | 🟢 Normal | -0.041 |  |
| 2026-10-23 18:05:52 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | -0.048 |  |
| 2026-10-23 20:02:14 | Hanwella (Kelani Ganga) | 3.68 | 🟢 Normal | -0.050 |  |
| 2026-10-23 20:02:50 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.063 |  |
| 2026-10-23 20:01:59 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.069 |  |
| 2026-10-23 20:01:12 | Moragaswewa (Deduru Oya) | 4.28 | 🟢 Normal | -0.072 |  |
| 2026-10-23 20:01:21 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.072 |  |
| 2026-10-23 20:01:50 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.074 |  |
| 2026-10-23 20:06:09 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | -0.227 |  |
| 2026-10-23 20:01:32 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.234 |  |
| 2026-10-23 18:03:29 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -6.108 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)