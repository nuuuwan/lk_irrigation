# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_18:15:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,872 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 18:15:21 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:11:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:10:33 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:09:28 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:09:22 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.609 | 🔺 Rising |
| 2026-08-10 18:08:32 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:07:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-10 18:07:12 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:06:56 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:06:32 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:05:08 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:04:47 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:04:23 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.021 |  |
| 2026-08-10 18:03:33 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:03:33 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.070 |  |
| 2026-08-10 18:03:32 | Peradeniya (Mahaweli Ganga) | 3.55 | 🟢 Normal | -0.029 |  |
| 2026-08-10 18:03:24 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.013 |  |
| 2026-08-10 18:03:18 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | -0.049 |  |
| 2026-08-10 18:03:09 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:02:51 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:02:44 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 18:02:37 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:02:33 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.021 |  |
| 2026-08-10 18:02:20 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | -0.011 |  |
| 2026-08-10 18:02:05 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 18:02:01 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.152 |  |
| 2026-08-10 18:02:00 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:01:58 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:01:54 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.035 |  |
| 2026-08-10 18:01:52 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | -0.041 |  |
| 2026-08-10 18:01:43 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:01:41 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.020 |  |
| 2026-08-10 18:01:13 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.069 |  |
| 2026-08-10 18:00:48 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:00:40 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.030 |  |
| 2026-08-10 18:00:33 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.013 |  |
| 2026-08-10 18:00:29 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:00:20 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-08-10 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.020 |  |
| 2026-08-10 17:44:35 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.035 |  |
| 2026-08-10 17:42:25 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 18:09:22 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.609 | 🔺 Rising |
| 2026-08-10 18:07:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-10 18:02:05 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 18:02:44 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 18:00:48 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:08:32 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:11:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:02:51 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:00:29 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:02:17 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:01:43 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:02:00 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:03:33 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:06:32 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:05:08 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:03:09 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:04:47 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:09:28 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:07:12 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:42:25 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:10:33 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:15:21 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:06:56 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 18:00:20 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-08-10 18:02:20 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | -0.011 |  |
| 2026-08-10 18:00:33 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.013 |  |
| 2026-08-10 18:03:24 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.013 |  |
| 2026-08-10 18:01:41 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.020 |  |
| 2026-08-10 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.020 |  |
| 2026-08-10 18:02:33 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.021 |  |
| 2026-08-10 18:04:23 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.021 |  |
| 2026-08-10 18:03:32 | Peradeniya (Mahaweli Ganga) | 3.55 | 🟢 Normal | -0.029 |  |
| 2026-08-10 18:00:40 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.030 |  |
| 2026-08-10 18:01:54 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.035 |  |
| 2026-08-10 18:01:52 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | -0.041 |  |
| 2026-08-10 18:03:18 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | -0.049 |  |
| 2026-08-10 18:01:13 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.069 |  |
| 2026-08-10 18:03:33 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.070 |  |
| 2026-08-10 18:02:01 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)