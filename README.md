# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_00:17:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,133 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 00:17:05 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:15:50 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-23 00:12:13 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:09:20 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-11-23 00:09:11 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:08:32 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.019 |  |
| 2026-11-23 00:08:25 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-23 00:07:50 | Urawa (Nilwala Ganga) | 0.83 | 🟢 Normal | -2.880 |  |
| 2026-11-23 00:07:44 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.047 |  |
| 2026-11-23 00:07:25 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | -2.880 |  |
| 2026-11-23 00:07:20 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:07:16 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-23 00:06:14 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:05:26 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | -0.015 |  |
| 2026-11-23 00:05:09 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-23 00:03:51 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-23 00:03:37 | Thawalama (Gin Ganga) | 3.04 | 🟢 Normal | -0.057 |  |
| 2026-11-23 00:03:35 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:02:47 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-23 00:02:39 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-23 00:02:33 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 2.400 | 🔺 Rising |
| 2026-11-23 00:02:30 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.021 |  |
| 2026-11-23 00:02:18 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 2.400 | 🔺 Rising |
| 2026-11-23 00:02:04 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-11-23 00:02:01 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:01:47 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:01:41 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:01:37 | Moragaswewa (Deduru Oya) | 2.53 | 🟢 Normal | -0.249 |  |
| 2026-11-23 00:01:26 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-11-23 00:01:09 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:00:37 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:00:36 | Moraketiya (Walawe Ganga) | 2.75 | 🟢 Normal | -0.051 |  |
| 2026-11-23 00:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-23 00:00:13 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:00:06 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 23:59:25 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 23:56:23 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 00:02:33 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 2.400 | 🔺 Rising |
| 2026-11-23 00:08:25 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-23 00:02:39 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-23 00:02:47 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-23 00:03:51 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-22 18:00:53 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-23 00:07:16 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-23 00:15:50 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-23 00:00:13 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:01:09 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:01:24 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:06:14 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:10 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:00:37 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-22 21:02:08 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:12:13 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:01:41 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:00:06 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:01:47 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:09:11 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:03:35 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:17:05 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:02:00 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:02:01 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-23 00:09:20 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-11-23 00:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-23 00:05:26 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | -0.015 |  |
| 2026-11-23 00:08:32 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.019 |  |
| 2026-11-23 00:01:26 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-11-23 00:05:09 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-22 23:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | -0.020 |  |
| 2026-11-23 00:02:04 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-11-23 00:02:30 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 00:07:44 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.047 |  |
| 2026-11-23 00:00:36 | Moraketiya (Walawe Ganga) | 2.75 | 🟢 Normal | -0.051 |  |
| 2026-11-23 00:03:37 | Thawalama (Gin Ganga) | 3.04 | 🟢 Normal | -0.057 |  |
| 2026-11-23 00:01:37 | Moragaswewa (Deduru Oya) | 2.53 | 🟢 Normal | -0.249 |  |
| 2026-11-23 00:07:50 | Urawa (Nilwala Ganga) | 0.83 | 🟢 Normal | -2.880 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)