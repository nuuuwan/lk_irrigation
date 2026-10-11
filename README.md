# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_22:08:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,314 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 22:08:23 | Magura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-10-11 22:08:12 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | -0.039 |  |
| 2026-10-11 22:07:26 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.021 |  |
| 2026-10-11 22:07:13 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-11 22:06:29 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 22:06:01 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-10-11 22:05:51 | Holombuwa (Kelani Ganga) | 1.94 | 🟢 Normal | -0.149 |  |
| 2026-10-11 22:05:48 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-11 22:05:37 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.021 |  |
| 2026-10-11 22:05:35 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-10-11 22:05:22 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-10-11 22:04:27 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.090 |  |
| 2026-10-11 22:04:01 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-11 22:03:46 | Pitabeddara (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-11 22:03:23 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | -0.010 |  |
| 2026-10-11 22:03:19 | Moragaswewa (Deduru Oya) | 1.85 | 🟢 Normal | -0.059 |  |
| 2026-10-11 22:03:07 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-10-11 22:03:05 | Glencourse (Kelani Ganga) | 12.02 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-10-11 22:02:58 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 22:02:58 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-11 22:02:46 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.031 |  |
| 2026-10-11 22:02:45 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-11 22:02:37 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-11 22:02:36 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.072 |  |
| 2026-10-11 22:02:22 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 22:02:12 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-10-11 22:02:08 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-11 22:02:08 | Ellagawa (Kalu Ganga) | 7.09 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-11 22:01:10 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 22:01:08 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 22:00:35 | Thawalama (Gin Ganga) | 3.61 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-11 22:00:10 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 22:03:07 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-10-11 22:03:05 | Glencourse (Kelani Ganga) | 12.02 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-10-11 22:02:12 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-10-11 22:08:23 | Magura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-10-11 22:00:35 | Thawalama (Gin Ganga) | 3.61 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-11 22:07:13 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-11 22:02:45 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-11 21:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-11 21:03:40 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-11 22:03:46 | Pitabeddara (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-11 22:02:37 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-11 21:07:27 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-11 22:02:08 | Ellagawa (Kalu Ganga) | 7.09 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-11 22:02:08 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-11 21:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-11 22:06:29 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 22:01:10 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 18:00:16 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 22:02:22 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 22:01:08 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:06:55 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 22:00:10 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-11 22:02:58 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 22:02:58 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-11 22:04:01 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-11 22:06:01 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-10-11 22:05:48 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:02:15 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.010 |  |
| 2026-10-11 22:03:23 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | -0.010 |  |
| 2026-10-11 21:02:43 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-10-11 22:07:26 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.021 |  |
| 2026-10-11 22:05:37 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.021 |  |
| 2026-10-11 22:02:46 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.031 |  |
| 2026-10-11 22:08:12 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | -0.039 |  |
| 2026-10-11 22:03:19 | Moragaswewa (Deduru Oya) | 1.85 | 🟢 Normal | -0.059 |  |
| 2026-10-11 22:05:35 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-10-11 22:02:36 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.072 |  |
| 2026-10-11 22:04:27 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.090 |  |
| 2026-10-11 22:05:51 | Holombuwa (Kelani Ganga) | 1.94 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)