# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_19:09:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,216 measurements** from **39** stations.
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
| 2026-10-01 19:09:50 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-10-01 19:08:14 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.044 |  |
| 2026-10-01 19:07:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | -0.046 |  |
| 2026-10-01 19:07:43 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:06:47 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-10-01 19:06:20 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.019 |  |
| 2026-10-01 19:06:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.093 |  |
| 2026-10-01 19:05:13 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:05:08 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:05:03 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:04:24 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:04:23 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 19:04:10 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-01 19:03:49 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-10-01 19:03:39 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.530 | 🔺 Rising |
| 2026-10-01 19:03:16 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-01 19:02:32 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:02:28 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:02:21 | Kithulgala (Kelani Ganga) | 2.98 | 🟢 Normal | 0.899 | 🔺 Rising |
| 2026-10-01 19:02:20 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-10-01 19:02:19 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.060 |  |
| 2026-10-01 19:01:42 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:01:38 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:01:35 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | -0.021 |  |
| 2026-10-01 19:01:21 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-10-01 19:01:18 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-01 19:01:15 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:01:15 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-01 19:00:28 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 19:00:20 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-10-01 18:59:22 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 19:02:21 | Kithulgala (Kelani Ganga) | 2.98 | 🟢 Normal | 0.899 | 🔺 Rising |
| 2026-10-01 19:03:39 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.530 | 🔺 Rising |
| 2026-10-01 19:01:21 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-10-01 19:09:50 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-10-01 19:01:18 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-01 19:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-01 19:04:23 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 18:03:51 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-01 18:18:41 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-01 19:04:10 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-01 19:00:28 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 19:02:32 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:01:15 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:01:47 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:01:52 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:05:13 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:01:42 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:09:37 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:05:03 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:01:15 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:05:08 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:07:43 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:04:24 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:00:58 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:02:28 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:01:38 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-01 19:06:47 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-10-01 18:05:18 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-10-01 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-01 19:00:20 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-10-01 19:03:16 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-01 19:06:20 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.019 |  |
| 2026-10-01 19:03:49 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-10-01 19:02:20 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-10-01 19:01:35 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | -0.021 |  |
| 2026-10-01 19:08:14 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.044 |  |
| 2026-10-01 19:07:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | -0.046 |  |
| 2026-10-01 19:02:19 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.060 |  |
| 2026-10-01 19:06:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)