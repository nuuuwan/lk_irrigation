# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_08:10:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,566 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 08:10:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | -0.009 |  |
| 2026-10-13 08:09:48 | Rathnapura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.138 |  |
| 2026-10-13 08:08:24 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | -0.030 |  |
| 2026-10-13 08:07:49 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-13 08:07:19 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-10-13 08:06:46 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-10-13 08:06:11 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-13 08:05:40 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.051 |  |
| 2026-10-13 08:05:36 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:05:14 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.019 |  |
| 2026-10-13 08:04:47 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-10-13 08:04:32 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:04:22 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:04:17 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:04:17 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-13 08:03:56 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-13 08:03:41 | Pitabeddara (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.068 |  |
| 2026-10-13 08:03:40 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:03:38 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.029 |  |
| 2026-10-13 08:03:37 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | -0.050 |  |
| 2026-10-13 08:03:27 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.029 |  |
| 2026-10-13 08:03:24 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:03:19 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.122 |  |
| 2026-10-13 08:03:01 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 08:02:58 | Panadugama (Nilwala Ganga) | 6.21 | 🟠 Minor Flood | -0.077 |  |
| 2026-10-13 08:02:44 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.029 |  |
| 2026-10-13 08:02:34 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.044 |  |
| 2026-10-13 08:02:09 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:02:06 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:01:41 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.051 |  |
| 2026-10-13 08:01:37 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.042 |  |
| 2026-10-13 08:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-13 08:00:56 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-13 08:00:56 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | -0.030 |  |
| 2026-10-13 08:00:53 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:00:10 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.048 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 08:02:58 | Panadugama (Nilwala Ganga) | 6.21 | 🟠 Minor Flood | -0.077 |  |
| 2026-10-13 08:04:47 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-10-13 08:10:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | -0.009 |  |
| 2026-10-13 08:03:56 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-13 08:07:49 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-13 08:00:56 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-13 07:10:15 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-13 08:06:11 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-13 08:03:01 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 08:02:09 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:04:17 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:04:32 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:05:36 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:03:40 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:04:22 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:00:53 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:02:06 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:03:24 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-10-13 08:07:19 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-10-13 08:06:46 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-10-13 08:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-13 08:04:17 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-13 08:05:14 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.019 |  |
| 2026-10-13 07:10:55 | Magura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.026 |  |
| 2026-10-13 08:03:27 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.029 |  |
| 2026-10-13 08:02:44 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.029 |  |
| 2026-10-13 08:03:38 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.029 |  |
| 2026-10-13 08:08:24 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | -0.030 |  |
| 2026-10-13 08:00:56 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | -0.030 |  |
| 2026-10-13 08:01:37 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.042 |  |
| 2026-10-13 08:02:34 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.044 |  |
| 2026-10-13 08:00:10 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.048 |  |
| 2026-10-13 08:03:37 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | -0.050 |  |
| 2026-10-13 08:01:41 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.051 |  |
| 2026-10-13 08:05:40 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.051 |  |
| 2026-10-13 08:03:41 | Pitabeddara (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.068 |  |
| 2026-10-13 08:03:19 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.122 |  |
| 2026-10-13 08:09:48 | Rathnapura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.138 |  |
| 2026-10-13 07:10:40 | Urawa (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.236 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)