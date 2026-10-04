# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_21:28:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,001 measurements** from **39** stations.
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
| 2026-10-04 21:28:29 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:12:56 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-10-04 21:10:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.018 |  |
| 2026-10-04 21:08:43 | Holombuwa (Kelani Ganga) | 2.36 | 🟢 Normal | -0.318 |  |
| 2026-10-04 21:08:41 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:08:01 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:07:29 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:06:30 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-04 21:05:51 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-10-04 21:05:18 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-10-04 21:04:50 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.040 |  |
| 2026-10-04 21:04:39 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 21:04:36 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-10-04 21:04:26 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.068 |  |
| 2026-10-04 21:04:20 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-10-04 21:04:20 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.039 |  |
| 2026-10-04 21:03:53 | Glencourse (Kelani Ganga) | 12.57 | 🟢 Normal | 0.359 | 🔺 Rising |
| 2026-10-04 21:03:47 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-04 21:03:40 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-04 21:03:27 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-04 21:03:23 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-04 21:03:12 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-04 21:03:10 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:03:04 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-04 21:03:00 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-04 21:02:52 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-10-04 21:02:47 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.059 |  |
| 2026-10-04 21:02:19 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:02:18 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-10-04 21:02:09 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-04 21:01:55 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:01:44 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.094 |  |
| 2026-10-04 21:01:43 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:01:35 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-04 21:01:17 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.051 |  |
| 2026-10-04 21:00:57 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.162 |  |
| 2026-10-04 21:00:08 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 21:03:53 | Glencourse (Kelani Ganga) | 12.57 | 🟢 Normal | 0.359 | 🔺 Rising |
| 2026-10-04 21:12:56 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-10-04 21:04:20 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-10-04 21:02:52 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-10-04 21:02:09 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-04 21:03:23 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-04 21:04:36 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-10-04 21:02:18 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-10-04 21:03:40 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-04 21:03:00 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-04 21:03:27 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-04 21:06:30 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-04 21:03:47 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-04 21:04:39 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 21:03:04 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-04 21:03:12 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-04 18:03:37 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 21:00:08 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:01:43 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:01:55 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-10-04 18:00:18 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:08:01 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:02:19 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:03:10 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:07:29 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:28:29 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-04 21:05:18 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-10-04 18:00:10 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-04 21:01:35 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-04 21:05:51 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-10-04 21:10:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.018 |  |
| 2026-10-04 21:04:20 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.039 |  |
| 2026-10-04 21:04:50 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.040 |  |
| 2026-10-04 21:01:17 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.051 |  |
| 2026-10-04 21:02:47 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.059 |  |
| 2026-10-04 21:04:26 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.068 |  |
| 2026-10-04 21:01:44 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.094 |  |
| 2026-10-04 21:00:57 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.162 |  |
| 2026-10-04 21:08:43 | Holombuwa (Kelani Ganga) | 2.36 | 🟢 Normal | -0.318 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)