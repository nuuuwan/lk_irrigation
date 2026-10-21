# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_12:15:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,974 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 12:15:23 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.036 |  |
| 2026-10-21 12:13:01 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-21 12:12:22 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-21 12:07:29 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:06:20 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:06:04 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-10-21 12:05:08 | Galgamuwa (Mee Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:05:07 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:04:52 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:04:46 | Panadugama (Nilwala Ganga) | 4.00 | 🟢 Normal | -0.014 |  |
| 2026-10-21 12:04:40 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:04:12 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:04:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.99 | 🟢 Normal | -0.029 |  |
| 2026-10-21 12:03:53 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:03:18 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.098 |  |
| 2026-10-21 12:03:17 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-10-21 12:03:10 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | -0.038 |  |
| 2026-10-21 12:03:06 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-21 12:03:04 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-10-21 12:03:04 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:02:52 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:02:44 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:02:39 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-21 12:02:31 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-21 12:02:18 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:02:14 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 12:02:12 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-21 12:02:09 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.020 |  |
| 2026-10-21 12:02:03 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:01:54 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:01:38 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 12:01:34 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-21 12:01:22 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-21 12:01:20 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 12:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-21 12:01:11 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 12:00:41 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:00:34 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.041 |  |
| 2026-10-21 12:00:24 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:00:12 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.082 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 12:00:12 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-21 12:02:39 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-21 12:02:12 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-21 12:03:06 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-21 12:12:22 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-21 12:02:31 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-21 12:01:38 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 12:01:20 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 12:01:11 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 12:02:14 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 12:13:01 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-21 12:01:54 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:05:08 | Galgamuwa (Mee Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:02:18 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:05:07 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:04:40 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:02:52 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:06:20 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:03:53 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:00:41 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:04:52 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:02:44 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:07:29 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:03:04 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:04:12 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:00:24 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 12:01:34 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-21 12:03:04 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-10-21 12:03:17 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-10-21 12:01:22 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-21 12:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-21 12:04:46 | Panadugama (Nilwala Ganga) | 4.00 | 🟢 Normal | -0.014 |  |
| 2026-10-21 12:06:04 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-10-21 12:02:09 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.020 |  |
| 2026-10-21 12:04:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.99 | 🟢 Normal | -0.029 |  |
| 2026-10-21 12:15:23 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.036 |  |
| 2026-10-21 12:03:10 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | -0.038 |  |
| 2026-10-21 12:00:34 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.041 |  |
| 2026-10-21 12:03:18 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)