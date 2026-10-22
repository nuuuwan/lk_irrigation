# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_14:20:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,945 measurements** from **39** stations.
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
| 2026-10-22 14:20:02 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-10-22 14:19:39 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | -0.046 |  |
| 2026-10-22 14:14:07 | Moragaswewa (Deduru Oya) | 4.33 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:13:23 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 14:12:46 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:10:37 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 14:09:59 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 14:09:14 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-10-22 14:07:54 | Glencourse (Kelani Ganga) | 12.15 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-22 14:07:39 | Badalgama (Maha Oya) | 3.67 | 🟢 Normal | -0.030 |  |
| 2026-10-22 14:07:30 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.019 |  |
| 2026-10-22 14:06:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.51 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-22 14:06:33 | Hanwella (Kelani Ganga) | 4.33 | 🟢 Normal | -0.060 |  |
| 2026-10-22 14:06:30 | Ellagawa (Kalu Ganga) | 7.59 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-22 14:06:18 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:06:03 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.063 |  |
| 2026-10-22 14:06:02 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:05:54 | Putupaula (Kalu Ganga) | 1.51 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-22 14:05:48 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:05:29 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.029 |  |
| 2026-10-22 14:05:27 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.020 |  |
| 2026-10-22 14:05:04 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.092 |  |
| 2026-10-22 14:04:47 | Moragaswewa (Deduru Oya) | 4.33 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:04:35 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-22 14:04:30 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.058 |  |
| 2026-10-22 14:04:26 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 14:03:55 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.019 |  |
| 2026-10-22 14:03:43 | Rathnapura (Kalu Ganga) | 4.24 | 🟢 Normal | -0.131 |  |
| 2026-10-22 14:03:24 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:02:59 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-22 14:02:26 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-22 14:02:11 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:02:09 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-22 14:01:44 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:01:24 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:01:21 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:01:20 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-22 14:00:45 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-10-22 14:00:38 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.062 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 14:20:02 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-10-22 14:04:35 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-22 14:05:54 | Putupaula (Kalu Ganga) | 1.51 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-22 14:07:54 | Glencourse (Kelani Ganga) | 12.15 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-22 14:06:30 | Ellagawa (Kalu Ganga) | 7.59 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-22 14:06:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.51 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-22 13:21:06 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-22 14:02:26 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-22 14:04:26 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 14:10:37 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 14:09:59 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 14:13:23 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 14:01:44 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:01:21 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:14:07 | Moragaswewa (Deduru Oya) | 4.33 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:03:24 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:06:18 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:02:59 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:05:48 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:12:46 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:02:11 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:06:02 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-10-22 14:01:20 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-22 14:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-22 14:02:09 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-22 14:09:14 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-10-22 14:03:55 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.019 |  |
| 2026-10-22 14:07:30 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.019 |  |
| 2026-10-22 14:05:27 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.020 |  |
| 2026-10-22 14:00:45 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-10-22 14:05:29 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.029 |  |
| 2026-10-22 14:07:39 | Badalgama (Maha Oya) | 3.67 | 🟢 Normal | -0.030 |  |
| 2026-10-22 14:19:39 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | -0.046 |  |
| 2026-10-22 14:04:30 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.058 |  |
| 2026-10-22 14:06:33 | Hanwella (Kelani Ganga) | 4.33 | 🟢 Normal | -0.060 |  |
| 2026-10-22 14:00:38 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.062 |  |
| 2026-10-22 14:06:03 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.063 |  |
| 2026-10-22 14:05:04 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.092 |  |
| 2026-10-22 14:03:43 | Rathnapura (Kalu Ganga) | 4.24 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)