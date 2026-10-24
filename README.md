# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_11:07:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,607 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 11:07:28 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-24 11:07:20 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.030 |  |
| 2026-10-24 11:06:35 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.075 |  |
| 2026-10-24 11:06:27 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-10-24 11:06:16 | Moragaswewa (Deduru Oya) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:05:29 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.021 |  |
| 2026-10-24 11:05:02 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 11:04:27 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.049 |  |
| 2026-10-24 11:04:09 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-24 11:04:01 | Panadugama (Nilwala Ganga) | 3.97 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-24 11:04:01 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.040 |  |
| 2026-10-24 11:03:51 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.019 |  |
| 2026-10-24 11:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.97 | 🟢 Normal | -0.040 |  |
| 2026-10-24 11:03:38 | Moragaswewa (Deduru Oya) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:03:29 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.030 |  |
| 2026-10-24 11:03:26 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.030 |  |
| 2026-10-24 11:03:10 | Hanwella (Kelani Ganga) | 3.49 | 🟢 Normal | -0.040 |  |
| 2026-10-24 11:03:10 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-24 11:03:05 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:03:04 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:03:01 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-10-24 11:03:01 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-24 11:02:56 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:02:54 | Galgamuwa (Mee Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-24 11:02:49 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-10-24 11:02:30 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:02:09 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.090 |  |
| 2026-10-24 11:01:47 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:01:31 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:01:13 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:00:55 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-24 11:00:49 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.012 |  |
| 2026-10-24 11:00:35 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | 0.382 | 🔺 Rising |
| 2026-10-24 11:00:29 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:26:19 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:26:15 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:26:11 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:26:06 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 11:00:35 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | 0.382 | 🔺 Rising |
| 2026-10-24 11:04:09 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-24 11:00:55 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-24 10:01:40 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-24 11:04:01 | Panadugama (Nilwala Ganga) | 3.97 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-24 11:05:02 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 11:01:47 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:06:16 | Moragaswewa (Deduru Oya) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:01:31 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:02:56 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:09:38 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:00:29 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:01:13 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:03:05 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:00:49 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:26:19 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:01:15 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:03:04 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:02:30 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:06:27 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-10-24 11:03:10 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-24 11:02:49 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-10-24 11:02:54 | Galgamuwa (Mee Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-24 11:07:28 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-24 11:03:01 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-24 11:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.012 |  |
| 2026-10-24 11:03:51 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.019 |  |
| 2026-10-24 11:05:29 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.021 |  |
| 2026-10-24 11:03:26 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.030 |  |
| 2026-10-24 11:03:29 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.030 |  |
| 2026-10-24 11:07:20 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.030 |  |
| 2026-10-24 11:03:01 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-10-24 11:04:01 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.040 |  |
| 2026-10-24 11:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.97 | 🟢 Normal | -0.040 |  |
| 2026-10-24 11:03:10 | Hanwella (Kelani Ganga) | 3.49 | 🟢 Normal | -0.040 |  |
| 2026-10-24 11:04:27 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.049 |  |
| 2026-10-24 10:05:32 | Ellagawa (Kalu Ganga) | 6.37 | 🟢 Normal | -0.053 |  |
| 2026-10-24 11:06:35 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.075 |  |
| 2026-10-24 11:02:09 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)