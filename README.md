# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_02:07:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,656 measurements** from **39** stations.
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
| 2026-10-10 02:07:54 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.035 |  |
| 2026-10-10 02:06:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 02:06:57 | Holombuwa (Kelani Ganga) | 1.54 | 🟢 Normal | -0.060 |  |
| 2026-10-10 02:06:29 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-10 02:06:07 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-10-10 02:05:23 | Panadugama (Nilwala Ganga) | 4.62 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-10 02:05:22 | Baddegama (Gin Ganga) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-10-10 02:04:29 | Giriulla (Maha Oya) | 4.28 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-10-10 02:04:10 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-10-10 02:04:08 | Rathnapura (Kalu Ganga) | 3.58 | 🟢 Normal | -0.111 |  |
| 2026-10-10 02:03:55 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.192 |  |
| 2026-10-10 02:03:35 | Dunamale (Aththanagalu Oya) | 3.12 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-10 02:03:28 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.039 |  |
| 2026-10-10 02:03:25 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-10-10 02:03:24 | Glencourse (Kelani Ganga) | 11.96 | 🟢 Normal | -0.183 |  |
| 2026-10-10 02:03:19 | Badalgama (Maha Oya) | 4.28 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-10 02:03:05 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-10 02:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.18 | 🟢 Normal | -0.020 |  |
| 2026-10-10 02:02:22 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 02:02:10 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-10 02:02:08 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-10 02:02:07 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.071 |  |
| 2026-10-10 02:01:59 | Moragaswewa (Deduru Oya) | 2.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 02:01:46 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 02:01:45 | Pitabeddara (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.024 |  |
| 2026-10-10 02:01:40 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-10 02:01:19 | Ellagawa (Kalu Ganga) | 6.88 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-10 02:01:08 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-10 02:01:01 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-10 02:00:46 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-10 01:57:40 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.192 |  |
| 2026-10-10 01:47:02 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.072 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 02:04:29 | Giriulla (Maha Oya) | 4.28 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-10-10 02:02:08 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-10 02:03:35 | Dunamale (Aththanagalu Oya) | 3.12 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-10 02:05:23 | Panadugama (Nilwala Ganga) | 4.62 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-10 02:01:19 | Ellagawa (Kalu Ganga) | 6.88 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-10 02:03:05 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-10 02:03:19 | Badalgama (Maha Oya) | 4.28 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-10 01:47:02 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-10 02:01:01 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 18:10:37 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-10 01:04:59 | Hanwella (Kelani Ganga) | 4.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 02:01:59 | Moragaswewa (Deduru Oya) | 2.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 02:06:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 02:02:22 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 02:02:10 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-10 02:01:46 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 02:01:08 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-10 02:06:29 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:04 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-10 02:01:40 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-10 02:06:07 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-10-10 00:04:01 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-10 02:00:46 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-10 02:05:22 | Baddegama (Gin Ganga) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-10-10 02:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.18 | 🟢 Normal | -0.020 |  |
| 2026-10-10 02:03:25 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-10-10 02:01:45 | Pitabeddara (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.024 |  |
| 2026-10-10 02:04:10 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-10-10 01:02:10 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-10-10 02:07:54 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.035 |  |
| 2026-10-10 02:03:28 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.039 |  |
| 2026-10-10 00:05:45 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.041 |  |
| 2026-10-10 02:06:57 | Holombuwa (Kelani Ganga) | 1.54 | 🟢 Normal | -0.060 |  |
| 2026-10-10 02:02:07 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.071 |  |
| 2026-10-10 02:04:08 | Rathnapura (Kalu Ganga) | 3.58 | 🟢 Normal | -0.111 |  |
| 2026-10-10 01:02:17 | Peradeniya (Mahaweli Ganga) | 3.99 | 🟢 Normal | -0.127 |  |
| 2026-10-10 02:03:24 | Glencourse (Kelani Ganga) | 11.96 | 🟢 Normal | -0.183 |  |
| 2026-10-10 02:03:55 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.192 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)