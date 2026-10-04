# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_03:19:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,209 measurements** from **39** stations.
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
| 2026-10-05 03:19:10 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | -0.024 |  |
| 2026-10-05 03:11:04 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.900 |  |
| 2026-10-05 03:10:47 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-05 03:10:39 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-05 03:10:38 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-05 03:10:24 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.900 |  |
| 2026-10-05 03:08:11 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -3.429 |  |
| 2026-10-05 03:07:50 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -3.429 |  |
| 2026-10-05 03:07:29 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-05 03:07:04 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.056 |  |
| 2026-10-05 03:06:06 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.070 |  |
| 2026-10-05 03:05:53 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | -0.169 |  |
| 2026-10-05 03:05:18 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:05:18 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.113 |  |
| 2026-10-05 03:04:28 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -396.000 |  |
| 2026-10-05 03:04:27 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -396.000 |  |
| 2026-10-05 03:03:52 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-05 03:03:41 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2026-10-05 03:03:30 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-05 03:03:23 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 03:03:10 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:02:58 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:02:56 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 03:02:56 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:02:52 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-10-05 03:02:42 | Peradeniya (Mahaweli Ganga) | 3.82 | 🟢 Normal | -0.083 |  |
| 2026-10-05 03:02:42 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.015 |  |
| 2026-10-05 03:02:34 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:02:29 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:02:10 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:02:05 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:01:50 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:01:42 | Hanwella (Kelani Ganga) | 4.07 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-05 03:01:28 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:01:17 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-05 03:01:15 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-10-05 03:00:58 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 03:10:39 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-05 02:03:27 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-05 03:01:17 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-05 03:01:42 | Hanwella (Kelani Ganga) | 4.07 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-05 03:10:47 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-05 03:03:30 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-05 03:03:52 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-05 01:09:35 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-05 03:07:29 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-05 03:03:23 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 18:03:37 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 03:02:56 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 03:00:58 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:02:56 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:01:50 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 02:50:59 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-10-04 18:00:18 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:05:18 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:02:05 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:01:28 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:02:58 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:03:10 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:02:34 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-04 18:00:10 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-05 03:02:42 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.015 |  |
| 2026-10-05 03:03:41 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2026-10-04 23:01:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.022 |  |
| 2026-10-05 03:19:10 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | -0.024 |  |
| 2026-10-05 03:02:52 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-10-05 03:01:15 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-10-05 03:07:04 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.056 |  |
| 2026-10-05 03:06:06 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.070 |  |
| 2026-10-05 03:02:42 | Peradeniya (Mahaweli Ganga) | 3.82 | 🟢 Normal | -0.083 |  |
| 2026-10-05 02:10:22 | Glencourse (Kelani Ganga) | 12.70 | 🟢 Normal | -0.101 |  |
| 2026-10-05 03:05:18 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.113 |  |
| 2026-10-05 03:05:53 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | -0.169 |  |
| 2026-10-05 03:11:04 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.900 |  |
| 2026-10-05 03:08:11 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -3.429 |  |
| 2026-10-05 03:04:28 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -396.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)