# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_02:26:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,169 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 02:26:53 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.088 |  |
| 2026-10-05 02:22:58 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.044 |  |
| 2026-10-05 02:11:16 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.099 |  |
| 2026-10-05 02:10:22 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-05 02:10:22 | Glencourse (Kelani Ganga) | 12.70 | 🟢 Normal | -0.101 |  |
| 2026-10-05 02:09:51 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-05 02:07:16 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-05 02:07:14 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-05 02:06:17 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.101 |  |
| 2026-10-05 02:05:49 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-05 02:05:29 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-05 02:05:13 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-05 02:04:57 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 02:04:56 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | -1.337 |  |
| 2026-10-05 02:03:42 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-10-05 02:03:27 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-05 02:03:20 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-05 02:03:09 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-05 02:02:34 | Giriulla (Maha Oya) | 1.99 | 🟢 Normal | -0.060 |  |
| 2026-10-05 02:02:30 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.148 |  |
| 2026-10-05 02:02:29 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.030 |  |
| 2026-10-05 02:02:11 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.073 |  |
| 2026-10-05 02:01:56 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-10-05 02:01:55 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 02:01:43 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-10-05 02:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-10-05 02:01:35 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-10-05 02:00:18 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-05 01:59:33 | Peradeniya (Mahaweli Ganga) | 4.02 | 🟢 Normal | -1.337 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 02:07:16 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-05 02:01:56 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-10-05 02:03:27 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-05 02:03:20 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-05 02:05:49 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-05 01:05:45 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-05 02:05:13 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-05 01:09:35 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-05 01:13:45 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-05 01:02:42 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 18:03:37 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 02:03:42 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-10-05 02:10:22 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-05 02:03:09 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-05 02:01:55 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 01:00:49 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-10-04 18:00:18 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-05 02:05:29 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-05 01:01:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 02:04:57 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:02:31 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 18:00:10 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-05 02:00:18 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-05 02:01:43 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-10-05 00:12:50 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.017 |  |
| 2026-10-05 02:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-10-05 02:01:35 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-10-04 23:01:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.022 |  |
| 2026-10-05 02:02:29 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.030 |  |
| 2026-10-05 02:22:58 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.044 |  |
| 2026-10-05 02:02:34 | Giriulla (Maha Oya) | 1.99 | 🟢 Normal | -0.060 |  |
| 2026-10-05 02:02:11 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.073 |  |
| 2026-10-05 02:26:53 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.088 |  |
| 2026-10-05 02:11:16 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.099 |  |
| 2026-10-05 02:10:22 | Glencourse (Kelani Ganga) | 12.70 | 🟢 Normal | -0.101 |  |
| 2026-10-05 02:06:17 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.101 |  |
| 2026-10-05 02:02:30 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.148 |  |
| 2026-10-05 02:04:56 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | -1.337 |  |
| 2026-10-05 01:20:36 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -576.000 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)