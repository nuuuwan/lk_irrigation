# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_16:14:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **278,812 measurements** from **39** stations.
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
| 2026-10-04 16:14:51 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-10-04 16:11:25 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.036 |  |
| 2026-10-04 16:11:03 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | -0.009 |  |
| 2026-10-04 16:10:29 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.059 |  |
| 2026-10-04 16:08:56 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:08:16 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-04 16:07:24 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:07:05 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-04 16:06:24 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-10-04 16:06:00 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-04 16:05:16 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | -0.070 |  |
| 2026-10-04 16:05:06 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.029 |  |
| 2026-10-04 16:04:18 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-10-04 16:04:04 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-10-04 16:04:03 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-04 16:04:01 | Glencourse (Kelani Ganga) | 10.58 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-04 16:03:54 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-04 16:03:53 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-10-04 16:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.032 |  |
| 2026-10-04 16:03:35 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-10-04 16:03:32 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -0.050 |  |
| 2026-10-04 16:03:30 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-04 16:03:16 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:03:04 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:03:02 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.050 |  |
| 2026-10-04 16:02:45 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-04 16:02:44 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-10-04 16:02:32 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-10-04 16:02:28 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.029 |  |
| 2026-10-04 16:02:22 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | -0.011 |  |
| 2026-10-04 16:02:19 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-04 16:01:51 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:01:48 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:01:31 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-10-04 16:01:18 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:01:00 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:00:57 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:00:19 | Weraganthota (Mahaweli Ganga) | -3.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 16:04:04 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-10-04 16:06:00 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-04 16:07:05 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-04 16:03:54 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-04 16:04:01 | Glencourse (Kelani Ganga) | 10.58 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-04 16:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-04 16:08:16 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-04 16:07:24 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:00:19 | Weraganthota (Mahaweli Ganga) | -3.51 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:01:00 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:01:48 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:03:04 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:08:56 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:02:19 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:01:51 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:03:16 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:01:18 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:00:57 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 16:11:03 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | -0.009 |  |
| 2026-10-04 16:14:51 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-10-04 16:03:53 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-10-04 16:04:03 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-04 16:06:24 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-10-04 16:03:30 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-04 16:03:35 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-10-04 16:02:45 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-04 16:02:22 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | -0.011 |  |
| 2026-10-04 16:04:18 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-10-04 16:01:31 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-10-04 16:05:06 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.029 |  |
| 2026-10-04 16:02:28 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.029 |  |
| 2026-10-04 16:02:32 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-10-04 16:02:44 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-10-04 16:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.032 |  |
| 2026-10-04 16:11:25 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.036 |  |
| 2026-10-04 16:03:32 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -0.050 |  |
| 2026-10-04 16:03:02 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.050 |  |
| 2026-10-04 16:10:29 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.059 |  |
| 2026-10-04 16:05:16 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)