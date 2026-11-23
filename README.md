# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_00:27:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,010 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 00:27:19 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:24:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-24 00:22:04 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-24 00:15:36 | Holombuwa (Kelani Ganga) | 2.60 | 🟢 Normal | -0.009 |  |
| 2026-11-24 00:12:53 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:12:00 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-24 00:11:25 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-24 00:11:25 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-11-24 00:10:40 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-24 00:09:40 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:07:22 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:07:05 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.082 |  |
| 2026-11-24 00:07:00 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-24 00:06:53 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-11-24 00:06:03 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | 30.857 | 🔺 Rising |
| 2026-11-24 00:05:38 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-24 00:05:35 | Urawa (Nilwala Ganga) | 1.66 | 🟢 Normal | 30.857 | 🔺 Rising |
| 2026-11-24 00:04:42 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.108 |  |
| 2026-11-24 00:04:06 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.005 |  |
| 2026-11-24 00:03:32 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.052 |  |
| 2026-11-24 00:03:20 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:03:07 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-24 00:03:01 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-11-24 00:02:54 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | 1.077 | 🔺 Rising |
| 2026-11-24 00:02:37 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:02:36 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:02:28 | Peradeniya (Mahaweli Ganga) | 3.09 | 🟢 Normal | -0.029 |  |
| 2026-11-24 00:02:24 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:02:23 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:02:10 | Giriulla (Maha Oya) | 2.59 | 🟢 Normal | 0.820 | 🔺 Rising |
| 2026-11-24 00:01:56 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:01:49 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:01:19 | Moragaswewa (Deduru Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-11-24 00:01:09 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-24 00:00:17 | Moraketiya (Walawe Ganga) | 2.30 | 🟢 Normal | 0.102 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 00:06:03 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | 30.857 | 🔺 Rising |
| 2026-11-24 00:02:54 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | 1.077 | 🔺 Rising |
| 2026-11-24 00:02:10 | Giriulla (Maha Oya) | 2.59 | 🟢 Normal | 0.820 | 🔺 Rising |
| 2026-11-24 00:06:53 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-11-24 00:11:25 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-11-24 00:00:17 | Moraketiya (Walawe Ganga) | 2.30 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-11-23 23:18:12 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-24 00:03:07 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-24 00:22:04 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-24 00:01:09 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-24 00:11:25 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-24 00:05:38 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-24 00:24:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-24 00:10:40 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-24 00:12:00 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-24 00:04:06 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.005 |  |
| 2026-11-24 00:01:49 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:27:19 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:02:37 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:05:14 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:07:22 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:02:36 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:02:23 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:03:20 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:02:24 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:12:53 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:09:40 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:01:56 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-24 00:15:36 | Holombuwa (Kelani Ganga) | 2.60 | 🟢 Normal | -0.009 |  |
| 2026-11-24 00:07:00 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-24 00:03:01 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-11-23 18:02:13 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-24 00:01:19 | Moragaswewa (Deduru Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 00:02:28 | Peradeniya (Mahaweli Ganga) | 3.09 | 🟢 Normal | -0.029 |  |
| 2026-11-23 18:00:35 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.050 |  |
| 2026-11-24 00:03:32 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.052 |  |
| 2026-11-24 00:07:05 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.082 |  |
| 2026-11-24 00:04:42 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)