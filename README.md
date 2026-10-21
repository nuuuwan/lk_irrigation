# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_18:09:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,208 measurements** from **39** stations.
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
| 2026-10-21 18:09:49 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | 5.838 | 🔺 Rising |
| 2026-10-21 18:09:12 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | 5.838 | 🔺 Rising |
| 2026-10-21 18:07:53 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-21 18:06:57 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-10-21 18:04:38 | Pitabeddara (Nilwala Ganga) | 1.88 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-10-21 18:04:36 | Glencourse (Kelani Ganga) | 10.54 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-21 18:04:16 | Deraniyagala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.735 | 🔺 Rising |
| 2026-10-21 18:03:42 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.031 |  |
| 2026-10-21 18:03:31 | Thaldena (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.222 |  |
| 2026-10-21 18:03:29 | Wellawaya (Kirindi Oya) | 2.43 | 🟢 Normal | -0.922 |  |
| 2026-10-21 18:03:29 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-21 18:03:28 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-21 18:03:28 | Yaka Wewa (Ma Oya) | 1.50 | 🟢 Normal | 0.835 | 🔺 Rising |
| 2026-10-21 18:03:23 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 18:03:16 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-21 18:03:12 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-21 18:03:09 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-21 18:03:02 | Nawalapitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.640 | 🔺 Rising |
| 2026-10-21 18:03:01 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-21 18:02:55 | Peradeniya (Mahaweli Ganga) | 3.99 | 🟢 Normal | 0.539 | 🔺 Rising |
| 2026-10-21 18:02:53 | Nakkala (Kumbukkan Oya) | 2.10 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-10-21 18:02:51 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-21 18:02:20 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | -0.022 |  |
| 2026-10-21 18:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.101 |  |
| 2026-10-21 18:02:13 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 18:02:09 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 18:02:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-10-21 18:02:02 | Kithulgala (Kelani Ganga) | 2.78 | 🟢 Normal | 0.627 | 🔺 Rising |
| 2026-10-21 18:01:56 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-21 18:01:39 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 18:01:26 | Galgamuwa (Mee Oya) | 1.81 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-21 18:01:19 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-21 18:01:17 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-21 18:01:17 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-21 18:00:59 | Moraketiya (Walawe Ganga) | 1.24 | 🟢 Normal | -0.053 |  |
| 2026-10-21 18:00:58 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-21 18:00:47 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-10-21 18:00:34 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.056 |  |
| 2026-10-21 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.070 |  |
| 2026-10-21 17:30:56 | Wellawaya (Kirindi Oya) | 2.93 | 🟢 Normal | -0.922 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 18:09:49 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | 5.838 | 🔺 Rising |
| 2026-10-21 18:03:28 | Yaka Wewa (Ma Oya) | 1.50 | 🟢 Normal | 0.835 | 🔺 Rising |
| 2026-10-21 18:04:16 | Deraniyagala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.735 | 🔺 Rising |
| 2026-10-21 18:03:02 | Nawalapitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.640 | 🔺 Rising |
| 2026-10-21 18:02:02 | Kithulgala (Kelani Ganga) | 2.78 | 🟢 Normal | 0.627 | 🔺 Rising |
| 2026-10-21 18:02:55 | Peradeniya (Mahaweli Ganga) | 3.99 | 🟢 Normal | 0.539 | 🔺 Rising |
| 2026-10-21 18:04:38 | Pitabeddara (Nilwala Ganga) | 1.88 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-10-21 18:02:53 | Nakkala (Kumbukkan Oya) | 2.10 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-10-21 18:01:26 | Galgamuwa (Mee Oya) | 1.81 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-21 18:03:29 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-21 18:01:17 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-21 18:03:28 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-21 18:00:58 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-21 18:04:36 | Glencourse (Kelani Ganga) | 10.54 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-21 17:01:25 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-21 18:01:56 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-21 18:03:09 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-21 18:01:39 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 18:01:19 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-21 18:02:13 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 18:03:01 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-21 18:07:53 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-21 18:02:09 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 18:01:17 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-21 18:02:51 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-21 18:03:23 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 18:03:12 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-21 18:06:57 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-10-21 18:03:16 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-21 18:00:47 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-10-21 18:02:20 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | -0.022 |  |
| 2026-10-21 18:02:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-10-21 18:03:42 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.031 |  |
| 2026-10-21 18:00:59 | Moraketiya (Walawe Ganga) | 1.24 | 🟢 Normal | -0.053 |  |
| 2026-10-21 18:00:34 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.056 |  |
| 2026-10-21 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.070 |  |
| 2026-10-21 18:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.101 |  |
| 2026-10-21 18:03:31 | Thaldena (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.222 |  |
| 2026-10-21 18:03:29 | Wellawaya (Kirindi Oya) | 2.43 | 🟢 Normal | -0.922 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)