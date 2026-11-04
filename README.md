# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_07:23:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,402 measurements** from **39** stations.
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
| 2026-11-04 07:23:13 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:12:10 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:10:42 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.062 |  |
| 2026-11-04 07:10:25 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:10:17 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-11-04 07:08:51 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.027 |  |
| 2026-11-04 07:07:16 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.047 |  |
| 2026-11-04 07:06:28 | Peradeniya (Mahaweli Ganga) | 3.09 | 🟢 Normal | -0.057 |  |
| 2026-11-04 07:06:25 | Hanwella (Kelani Ganga) | 3.16 | 🟢 Normal | -0.046 |  |
| 2026-11-04 07:05:47 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | -0.203 |  |
| 2026-11-04 07:05:44 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-04 07:05:43 | Horowpothana (Yan Oya) | 2.99 | 🟢 Normal | -0.074 |  |
| 2026-11-04 07:05:33 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -1.878 |  |
| 2026-11-04 07:05:29 | Thanamalwila (Kirindi Oya) | 1.61 | 🟢 Normal | -0.043 |  |
| 2026-11-04 07:04:54 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-04 07:04:52 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | -0.070 |  |
| 2026-11-04 07:04:30 | Panadugama (Nilwala Ganga) | 4.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 07:04:27 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-04 07:04:26 | Galgamuwa (Mee Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:04:19 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-04 07:03:45 | Dunamale (Aththanagalu Oya) | 2.67 | 🟢 Normal | -0.030 |  |
| 2026-11-04 07:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.96 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-11-04 07:03:27 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.087 |  |
| 2026-11-04 07:03:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-04 07:02:59 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:02:50 | Moragaswewa (Deduru Oya) | 4.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 07:02:33 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-11-04 07:02:18 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-04 07:02:06 | Giriulla (Maha Oya) | 3.33 | 🟢 Normal | -0.121 |  |
| 2026-11-04 07:01:54 | Rathnapura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.097 |  |
| 2026-11-04 07:01:51 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:01:46 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | -0.032 |  |
| 2026-11-04 07:01:46 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-04 07:01:45 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | -0.040 |  |
| 2026-11-04 07:01:20 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.043 |  |
| 2026-11-04 07:00:34 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:00:33 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | -0.105 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 07:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.96 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-11-04 07:03:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-04 07:05:44 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-04 07:04:19 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-04 07:04:54 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-04 07:02:18 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-04 07:04:27 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-04 07:04:30 | Panadugama (Nilwala Ganga) | 4.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 07:02:50 | Moragaswewa (Deduru Oya) | 4.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 07:10:25 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:01:46 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:04:26 | Galgamuwa (Mee Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:12:10 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:02:59 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:01:51 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:23:13 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:10:17 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-11-04 07:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-04 07:02:33 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-11-04 07:08:51 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.027 |  |
| 2026-11-04 07:03:45 | Dunamale (Aththanagalu Oya) | 2.67 | 🟢 Normal | -0.030 |  |
| 2026-11-04 07:01:46 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | -0.032 |  |
| 2026-11-04 07:01:45 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | -0.040 |  |
| 2026-11-04 06:01:53 | Pitabeddara (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.041 |  |
| 2026-11-04 07:01:20 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.043 |  |
| 2026-11-04 07:05:29 | Thanamalwila (Kirindi Oya) | 1.61 | 🟢 Normal | -0.043 |  |
| 2026-11-04 07:06:25 | Hanwella (Kelani Ganga) | 3.16 | 🟢 Normal | -0.046 |  |
| 2026-11-04 07:07:16 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.047 |  |
| 2026-11-04 07:06:28 | Peradeniya (Mahaweli Ganga) | 3.09 | 🟢 Normal | -0.057 |  |
| 2026-11-04 07:10:42 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.062 |  |
| 2026-11-04 07:04:52 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | -0.070 |  |
| 2026-11-04 07:05:43 | Horowpothana (Yan Oya) | 2.99 | 🟢 Normal | -0.074 |  |
| 2026-11-04 07:03:27 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.087 |  |
| 2026-11-04 07:01:54 | Rathnapura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.097 |  |
| 2026-11-04 07:00:33 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | -0.105 |  |
| 2026-11-04 07:02:06 | Giriulla (Maha Oya) | 3.33 | 🟢 Normal | -0.121 |  |
| 2026-11-04 07:05:47 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | -0.203 |  |
| 2026-11-04 07:05:33 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -1.878 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)