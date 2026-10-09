# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_03:07:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,688 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 03:07:15 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-10 03:06:50 | Panadugama (Nilwala Ganga) | 4.69 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-10 03:05:55 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 03:05:51 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-10 03:05:19 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.019 |  |
| 2026-10-10 03:05:03 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | -0.030 |  |
| 2026-10-10 03:04:42 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-10-10 03:04:41 | Glencourse (Kelani Ganga) | 11.81 | 🟢 Normal | -0.147 |  |
| 2026-10-10 03:04:40 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.499 | 🔺 Rising |
| 2026-10-10 03:04:26 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.057 |  |
| 2026-10-10 03:04:26 | Rathnapura (Kalu Ganga) | 3.47 | 🟢 Normal | -0.109 |  |
| 2026-10-10 03:04:18 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.043 |  |
| 2026-10-10 03:04:09 | Moragaswewa (Deduru Oya) | 2.29 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-10 03:03:57 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-10-10 03:03:34 | Giriulla (Maha Oya) | 4.45 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-10-10 03:03:28 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-10 03:03:16 | Hanwella (Kelani Ganga) | 4.01 | 🟢 Normal | -0.089 |  |
| 2026-10-10 03:02:52 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-10 03:02:40 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-10 03:02:35 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-10 03:02:32 | Peradeniya (Mahaweli Ganga) | 3.63 | 🟢 Normal | -0.238 |  |
| 2026-10-10 03:02:16 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 03:02:14 | Badalgama (Maha Oya) | 4.36 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-10 03:01:56 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-10 03:01:36 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-10 03:01:35 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.031 |  |
| 2026-10-10 03:01:12 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-10 02:34:47 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | -0.238 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 03:04:40 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.499 | 🔺 Rising |
| 2026-10-10 03:03:34 | Giriulla (Maha Oya) | 4.45 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-10-10 03:02:14 | Badalgama (Maha Oya) | 4.36 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-10 03:03:28 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-10 03:04:09 | Moragaswewa (Deduru Oya) | 2.29 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-10 01:47:02 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-10 03:06:50 | Panadugama (Nilwala Ganga) | 4.69 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-10 03:05:51 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-10 03:07:15 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-10 03:01:36 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-10 03:02:52 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-09 18:10:37 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-09 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 03:02:40 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-10 03:05:55 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 02:02:10 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-10 03:02:16 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 03:02:35 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-10 03:01:56 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:04 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-10 03:01:12 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-10 03:03:57 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-10-10 03:05:19 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.019 |  |
| 2026-10-10 02:05:22 | Baddegama (Gin Ganga) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-10-10 02:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.18 | 🟢 Normal | -0.020 |  |
| 2026-10-10 03:04:42 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-10-10 03:05:03 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | -0.030 |  |
| 2026-10-10 03:01:35 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.031 |  |
| 2026-10-10 02:13:20 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.034 |  |
| 2026-10-10 03:04:18 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.043 |  |
| 2026-10-10 03:04:26 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.057 |  |
| 2026-10-10 02:06:57 | Holombuwa (Kelani Ganga) | 1.54 | 🟢 Normal | -0.060 |  |
| 2026-10-10 02:02:07 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.071 |  |
| 2026-10-10 03:03:16 | Hanwella (Kelani Ganga) | 4.01 | 🟢 Normal | -0.089 |  |
| 2026-10-10 03:04:26 | Rathnapura (Kalu Ganga) | 3.47 | 🟢 Normal | -0.109 |  |
| 2026-10-10 03:04:41 | Glencourse (Kelani Ganga) | 11.81 | 🟢 Normal | -0.147 |  |
| 2026-10-10 02:03:55 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.192 |  |
| 2026-10-10 03:02:32 | Peradeniya (Mahaweli Ganga) | 3.63 | 🟢 Normal | -0.238 |  |
| 2026-10-10 02:11:16 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)