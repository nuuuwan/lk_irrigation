# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_17:18:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,961 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 17:18:37 | Moragaswewa (Deduru Oya) | 4.47 | 🟢 Normal | -0.056 |  |
| 2026-10-23 17:15:50 | Panadugama (Nilwala Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 17:11:51 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | -0.095 |  |
| 2026-10-23 17:09:45 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.382 | 🔺 Rising |
| 2026-10-23 17:09:34 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | -0.019 |  |
| 2026-10-23 17:09:05 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-23 17:08:27 | Panadugama (Nilwala Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 17:07:05 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 17:07:00 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-10-23 17:06:55 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.028 |  |
| 2026-10-23 17:06:50 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.030 |  |
| 2026-10-23 17:06:26 | Glencourse (Kelani Ganga) | 11.28 | 🟢 Normal | -0.058 |  |
| 2026-10-23 17:06:05 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.085 |  |
| 2026-10-23 17:05:18 | Rathnapura (Kalu Ganga) | 3.12 | 🟢 Normal | -0.126 |  |
| 2026-10-23 17:05:07 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 17:04:54 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-10-23 17:04:46 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-23 17:04:32 | Putupaula (Kalu Ganga) | 1.99 | 🟢 Normal | -0.040 |  |
| 2026-10-23 17:04:26 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-23 17:04:26 | Siyambalanduwa (Heda Oya) | 1.68 | 🟢 Normal | 0.720 | 🔺 Rising |
| 2026-10-23 17:03:59 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-23 17:03:22 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-10-23 17:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.79 | 🟢 Normal | -0.060 |  |
| 2026-10-23 17:03:18 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-23 17:03:08 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.021 |  |
| 2026-10-23 17:03:02 | Galgamuwa (Mee Oya) | 2.53 | 🟢 Normal | -0.050 |  |
| 2026-10-23 17:02:52 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | -0.051 |  |
| 2026-10-23 17:02:45 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.014 |  |
| 2026-10-23 17:02:42 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | -0.060 |  |
| 2026-10-23 17:02:36 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-23 17:02:11 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-10-23 17:02:01 | Thanthirimale (Malwathu Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-10-23 17:01:39 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-23 17:01:30 | Weraganthota (Mahaweli Ganga) | 3.12 | 🟢 Normal | 6.162 | 🔺 Rising |
| 2026-10-23 17:01:23 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-10-23 17:00:49 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | -0.045 |  |
| 2026-10-23 17:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-23 17:00:13 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 17:01:30 | Weraganthota (Mahaweli Ganga) | 3.12 | 🟢 Normal | 6.162 | 🔺 Rising |
| 2026-10-23 17:04:26 | Siyambalanduwa (Heda Oya) | 1.68 | 🟢 Normal | 0.720 | 🔺 Rising |
| 2026-10-23 17:09:45 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.382 | 🔺 Rising |
| 2026-10-23 17:09:05 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-23 17:05:07 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 17:04:46 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-23 17:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-23 17:01:39 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-23 17:04:26 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-23 17:02:36 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-23 17:15:50 | Panadugama (Nilwala Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 17:07:05 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 17:02:01 | Thanthirimale (Malwathu Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:13:53 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-10-23 16:15:36 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-10-23 17:03:59 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-23 17:03:18 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-23 17:07:00 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-10-23 17:01:23 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-10-23 17:02:45 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.014 |  |
| 2026-10-23 17:09:34 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | -0.019 |  |
| 2026-10-23 17:04:54 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-10-23 17:02:11 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-10-23 17:03:22 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-10-23 17:03:08 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.021 |  |
| 2026-10-23 17:00:13 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.023 |  |
| 2026-10-23 17:06:55 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.028 |  |
| 2026-10-23 17:06:50 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.030 |  |
| 2026-10-23 17:04:32 | Putupaula (Kalu Ganga) | 1.99 | 🟢 Normal | -0.040 |  |
| 2026-10-23 17:00:49 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | -0.045 |  |
| 2026-10-23 17:03:02 | Galgamuwa (Mee Oya) | 2.53 | 🟢 Normal | -0.050 |  |
| 2026-10-23 17:02:52 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | -0.051 |  |
| 2026-10-23 17:18:37 | Moragaswewa (Deduru Oya) | 4.47 | 🟢 Normal | -0.056 |  |
| 2026-10-23 17:06:26 | Glencourse (Kelani Ganga) | 11.28 | 🟢 Normal | -0.058 |  |
| 2026-10-23 17:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.79 | 🟢 Normal | -0.060 |  |
| 2026-10-23 17:02:42 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | -0.060 |  |
| 2026-10-23 17:06:05 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.085 |  |
| 2026-10-23 17:11:51 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | -0.095 |  |
| 2026-10-23 17:05:18 | Rathnapura (Kalu Ganga) | 3.12 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)