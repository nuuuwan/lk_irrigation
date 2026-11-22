# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_11:28:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,649 measurements** from **39** stations.
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
| 2026-11-22 11:28:23 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:13:46 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.027 |  |
| 2026-11-22 11:12:39 | Panadugama (Nilwala Ganga) | 4.58 | 🟢 Normal | -0.021 |  |
| 2026-11-22 11:10:39 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.026 |  |
| 2026-11-22 11:10:00 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | -0.056 |  |
| 2026-11-22 11:09:26 | Rathnapura (Kalu Ganga) | 2.72 | 🟢 Normal | -0.146 |  |
| 2026-11-22 11:08:58 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | -0.035 |  |
| 2026-11-22 11:07:53 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.063 |  |
| 2026-11-22 11:07:22 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-22 11:07:18 | Moragaswewa (Deduru Oya) | 3.35 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-11-22 11:07:13 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 11:06:17 | Peradeniya (Mahaweli Ganga) | 2.43 | 🟢 Normal | -0.091 |  |
| 2026-11-22 11:05:54 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.040 |  |
| 2026-11-22 11:04:22 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-22 11:04:18 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-11-22 11:04:13 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-11-22 11:04:03 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:03:36 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-11-22 11:03:32 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 11:03:32 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:03:12 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.010 |  |
| 2026-11-22 11:02:57 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.030 |  |
| 2026-11-22 11:02:48 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-22 11:02:47 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-22 11:02:35 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-22 11:02:31 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:02:19 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:02:11 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-11-22 11:02:09 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.065 |  |
| 2026-11-22 11:01:54 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:01:43 | Manampitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-22 11:01:31 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-22 11:01:19 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:01:17 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.022 |  |
| 2026-11-22 11:01:15 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | -0.041 |  |
| 2026-11-22 11:00:55 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-11-22 11:00:45 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 11:07:18 | Moragaswewa (Deduru Oya) | 3.35 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-11-22 11:02:47 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-22 11:01:43 | Manampitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-22 11:04:22 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-22 11:01:31 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-22 11:07:22 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-22 11:07:13 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 11:03:32 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 11:00:45 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:01:19 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:02:31 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:00:08 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:01:54 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:02:19 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:04:03 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:28:23 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:03:32 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 11:02:35 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-22 11:03:12 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.010 |  |
| 2026-11-22 11:02:48 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-22 11:04:13 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-11-22 11:00:55 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-11-22 11:04:18 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-11-22 11:02:11 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-11-22 11:12:39 | Panadugama (Nilwala Ganga) | 4.58 | 🟢 Normal | -0.021 |  |
| 2026-11-22 11:01:17 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.022 |  |
| 2026-11-22 11:10:39 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.026 |  |
| 2026-11-22 11:13:46 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.027 |  |
| 2026-11-22 11:03:36 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-11-22 11:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.030 |  |
| 2026-11-22 11:08:58 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | -0.035 |  |
| 2026-11-22 11:05:54 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.040 |  |
| 2026-11-22 11:01:15 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | -0.041 |  |
| 2026-11-22 11:10:00 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | -0.056 |  |
| 2026-11-22 11:07:53 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.063 |  |
| 2026-11-22 11:02:09 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.065 |  |
| 2026-11-22 11:06:17 | Peradeniya (Mahaweli Ganga) | 2.43 | 🟢 Normal | -0.091 |  |
| 2026-11-22 11:09:26 | Rathnapura (Kalu Ganga) | 2.72 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)