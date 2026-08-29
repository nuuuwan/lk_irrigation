# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_07:04:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **246,020 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 07:04:42 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:04:32 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 07:04:31 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:04:23 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-08-29 07:04:20 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:04:19 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.217 |  |
| 2026-08-29 07:03:45 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-29 07:03:21 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.131 |  |
| 2026-08-29 07:03:20 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.145 |  |
| 2026-08-29 07:03:19 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:03:10 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-08-29 07:02:55 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 07:02:40 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:02:36 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:02:17 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:02:05 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-08-29 07:02:03 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.050 |  |
| 2026-08-29 07:01:42 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:01:37 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:01:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.090 |  |
| 2026-08-29 07:01:19 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:01:10 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.064 |  |
| 2026-08-29 07:00:54 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-29 07:00:48 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | -0.002 |  |
| 2026-08-29 07:00:17 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-29 06:32:16 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 07:04:23 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-08-29 06:04:24 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-29 07:03:45 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-29 07:00:17 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-29 06:06:42 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-29 06:03:21 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-29 07:00:54 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-29 07:02:55 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 07:04:32 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 07:03:19 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:16:26 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:04:31 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:01:19 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:06:20 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:04:19 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:04:20 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:01:42 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:02:40 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:02:36 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:04:42 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:04:33 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:06:29 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:09:48 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:01:37 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:02:17 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:05:12 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:00:48 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | -0.002 |  |
| 2026-08-29 07:02:05 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-08-29 07:03:10 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-08-29 05:05:43 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-08-29 06:09:13 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.027 |  |
| 2026-08-29 07:02:03 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.050 |  |
| 2026-08-29 07:01:10 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.064 |  |
| 2026-08-29 06:03:32 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.084 |  |
| 2026-08-29 07:01:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.090 |  |
| 2026-08-29 07:03:21 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.131 |  |
| 2026-08-29 07:03:20 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.145 |  |
| 2026-08-29 06:07:12 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.147 |  |
| 2026-08-29 07:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.217 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)