# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_07:04:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,472 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 07:04:37 | Ellagawa (Kalu Ganga) | 6.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 07:04:25 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.116 |  |
| 2026-11-03 07:04:21 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.059 |  |
| 2026-11-03 07:04:08 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-11-03 07:03:57 | Galgamuwa (Mee Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-03 07:03:56 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 07:03:36 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 07:03:26 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.051 |  |
| 2026-11-03 07:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-11-03 07:03:12 | Moraketiya (Walawe Ganga) | 1.47 | 🟢 Normal | -0.186 |  |
| 2026-11-03 07:02:39 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.085 |  |
| 2026-11-03 07:02:23 | Nakkala (Kumbukkan Oya) | 1.41 | 🟢 Normal | -0.107 |  |
| 2026-11-03 07:02:10 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-03 07:02:07 | Wellawaya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.052 |  |
| 2026-11-03 07:01:59 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.215 |  |
| 2026-11-03 07:01:49 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 07:01:24 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-03 07:00:54 | Weraganthota (Mahaweli Ganga) | -2.21 | 🟢 Normal | -0.138 |  |
| 2026-11-03 07:00:52 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-11-03 07:00:42 | Moragaswewa (Deduru Oya) | 3.61 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-03 07:00:34 | Kuda Oya (Kirindi Oya) | 2.08 | 🟢 Normal | -0.121 |  |
| 2026-11-03 06:36:53 | Galgamuwa (Mee Oya) | 1.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 06:03:35 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | 0.772 | 🔺 Rising |
| 2026-11-03 06:03:25 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-11-03 07:00:52 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-11-03 07:00:42 | Moragaswewa (Deduru Oya) | 3.61 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-03 07:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-11-03 06:11:47 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-11-03 07:01:24 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-03 07:03:56 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 07:04:37 | Ellagawa (Kalu Ganga) | 6.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 06:07:06 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-03 07:03:36 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 07:01:49 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 07:03:57 | Galgamuwa (Mee Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:02:23 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-03 07:02:10 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:01:41 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-03 06:01:35 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-03 07:04:08 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-11-03 06:09:18 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.022 |  |
| 2026-11-03 06:01:20 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.032 |  |
| 2026-11-03 06:03:48 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | -0.034 |  |
| 2026-11-03 06:03:10 | Giriulla (Maha Oya) | 3.08 | 🟢 Normal | -0.040 |  |
| 2026-11-03 06:06:57 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.043 |  |
| 2026-11-03 07:03:26 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.051 |  |
| 2026-11-03 07:02:07 | Wellawaya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.052 |  |
| 2026-11-03 07:04:21 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.059 |  |
| 2026-11-03 06:09:05 | Horowpothana (Yan Oya) | 3.16 | 🟢 Normal | -0.081 |  |
| 2026-11-03 07:02:39 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.085 |  |
| 2026-11-03 07:02:23 | Nakkala (Kumbukkan Oya) | 1.41 | 🟢 Normal | -0.107 |  |
| 2026-11-03 06:00:11 | Rathnapura (Kalu Ganga) | 3.38 | 🟢 Normal | -0.113 |  |
| 2026-11-03 07:04:25 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.116 |  |
| 2026-11-03 07:00:34 | Kuda Oya (Kirindi Oya) | 2.08 | 🟢 Normal | -0.121 |  |
| 2026-11-03 07:00:54 | Weraganthota (Mahaweli Ganga) | -2.21 | 🟢 Normal | -0.138 |  |
| 2026-11-03 06:05:14 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | -0.150 |  |
| 2026-11-03 06:06:10 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.181 |  |
| 2026-11-03 07:03:12 | Moraketiya (Walawe Ganga) | 1.47 | 🟢 Normal | -0.186 |  |
| 2026-11-03 07:01:59 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.215 |  |
| 2026-11-03 06:01:25 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.217 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)