# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_10:23:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,483 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Peradeniya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 10:23:18 | Putupaula (Kalu Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:17:44 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:11:03 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | -0.038 |  |
| 2026-08-05 10:10:48 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.039 |  |
| 2026-08-05 10:10:35 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:10:24 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:09:37 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:08:31 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:07:48 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-05 10:07:40 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.074 |  |
| 2026-08-05 10:06:46 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.037 |  |
| 2026-08-05 10:06:40 | Kithulgala (Kelani Ganga) | 2.82 | 🟢 Normal | -0.059 |  |
| 2026-08-05 10:06:06 | Peradeniya (Mahaweli Ganga) | 5.00 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-08-05 10:05:53 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-08-05 10:04:58 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:04:54 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-05 10:04:23 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:04:06 | Glencourse (Kelani Ganga) | 12.46 | 🟢 Normal | -0.041 |  |
| 2026-08-05 10:04:00 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:03:53 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:03:53 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:03:48 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | -0.080 |  |
| 2026-08-05 10:03:35 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-08-05 10:03:31 | Rathnapura (Kalu Ganga) | 4.77 | 🟢 Normal | -0.086 |  |
| 2026-08-05 10:03:27 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.33 | 🟢 Normal | -0.069 |  |
| 2026-08-05 10:03:06 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:02:59 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.029 |  |
| 2026-08-05 10:02:55 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:02:38 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:02:31 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:02:19 | Ellagawa (Kalu Ganga) | 8.91 | 🟢 Normal | -0.010 |  |
| 2026-08-05 10:02:19 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | -0.062 |  |
| 2026-08-05 10:01:48 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.020 |  |
| 2026-08-05 10:01:39 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:01:20 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:00:44 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-05 10:00:29 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:00:20 | Nawalapitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.082 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 10:06:06 | Peradeniya (Mahaweli Ganga) | 5.00 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-08-05 10:00:20 | Nawalapitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-08-05 10:07:48 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-05 10:00:44 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-05 10:00:29 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:02:31 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:03:53 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:04:23 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:08:31 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:17:44 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:02:38 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:02:55 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:03:06 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:01:39 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:09:37 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:03:27 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:23:18 | Putupaula (Kalu Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:10:24 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:01:20 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:04:00 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:10:35 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:03:53 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:04:58 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-05 10:04:54 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-05 10:05:53 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-08-05 10:02:19 | Ellagawa (Kalu Ganga) | 8.91 | 🟢 Normal | -0.010 |  |
| 2026-08-05 10:03:35 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-08-05 10:01:48 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.020 |  |
| 2026-08-05 10:02:59 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.029 |  |
| 2026-08-05 10:06:46 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.037 |  |
| 2026-08-05 10:11:03 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | -0.038 |  |
| 2026-08-05 10:10:48 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.039 |  |
| 2026-08-05 10:04:06 | Glencourse (Kelani Ganga) | 12.46 | 🟢 Normal | -0.041 |  |
| 2026-08-05 10:06:40 | Kithulgala (Kelani Ganga) | 2.82 | 🟢 Normal | -0.059 |  |
| 2026-08-05 10:02:19 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | -0.062 |  |
| 2026-08-05 10:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.33 | 🟢 Normal | -0.069 |  |
| 2026-08-05 10:07:40 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.074 |  |
| 2026-08-05 10:03:48 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | -0.080 |  |
| 2026-08-05 10:03:31 | Rathnapura (Kalu Ganga) | 4.77 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)