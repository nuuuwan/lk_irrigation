# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_06:32:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **245,994 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 06:32:16 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | -0.001 |  |
| 2026-08-29 06:16:26 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:14:14 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:13:21 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:10:59 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-08-29 06:09:48 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:09:36 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:09:13 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.027 |  |
| 2026-08-29 06:09:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-08-29 06:07:39 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:07:12 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.147 |  |
| 2026-08-29 06:06:42 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-29 06:06:32 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.016 |  |
| 2026-08-29 06:06:29 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:06:20 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:05:51 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-29 06:05:29 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | -0.009 |  |
| 2026-08-29 06:05:12 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:05:05 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.067 |  |
| 2026-08-29 06:04:33 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:04:25 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:04:24 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-29 06:04:17 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:04:08 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 06:03:54 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-08-29 06:03:48 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.062 |  |
| 2026-08-29 06:03:32 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.084 |  |
| 2026-08-29 06:03:21 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-29 06:03:05 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 06:02:47 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:02:34 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-29 06:02:30 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:02:28 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.041 |  |
| 2026-08-29 06:02:08 | Hanwella (Kelani Ganga) | 1.71 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-08-29 06:01:37 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:01:35 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-08-29 06:01:29 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-08-29 06:00:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.056 |  |
| 2026-08-29 06:00:06 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 06:09:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-08-29 06:10:59 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-08-29 06:04:24 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-29 06:02:08 | Hanwella (Kelani Ganga) | 1.71 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-08-29 06:06:42 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-29 06:03:21 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-29 06:05:51 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-29 06:04:08 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 06:03:05 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 17:03:05 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 06:16:26 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:02:47 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:06:20 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:07:39 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:14:14 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:09:36 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:00:06 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:02:30 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:01:37 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:04:25 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:04:33 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:06:29 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:09:48 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:05:12 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-29 06:32:16 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | -0.001 |  |
| 2026-08-29 06:05:29 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | -0.009 |  |
| 2026-08-29 06:02:34 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-29 06:01:29 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-08-29 06:03:54 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-08-29 06:06:32 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.016 |  |
| 2026-08-29 06:01:35 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-08-29 05:05:43 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-08-29 06:09:13 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.027 |  |
| 2026-08-29 06:02:28 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.041 |  |
| 2026-08-29 06:00:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.056 |  |
| 2026-08-29 06:03:48 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.062 |  |
| 2026-08-29 06:05:05 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.067 |  |
| 2026-08-29 06:03:32 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.084 |  |
| 2026-08-29 06:07:12 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)