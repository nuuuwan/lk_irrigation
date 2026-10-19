# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_01:34:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,640 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 01:34:36 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | 1.348 | 🔺 Rising |
| 2026-10-20 01:27:26 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-20 01:24:11 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:22:19 | Panadugama (Nilwala Ganga) | 4.98 | 🟢 Normal | -0.023 |  |
| 2026-10-20 01:21:57 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.054 |  |
| 2026-10-20 01:21:39 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-10-20 01:17:18 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:14:52 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.039 |  |
| 2026-10-20 01:13:50 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.017 |  |
| 2026-10-20 01:10:15 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-20 01:07:05 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | -0.050 |  |
| 2026-10-20 01:06:31 | Rathnapura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.085 |  |
| 2026-10-20 01:06:12 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:04:33 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-10-20 01:04:31 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.020 |  |
| 2026-10-20 01:04:29 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:04:25 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-10-20 01:04:16 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-10-20 01:03:56 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-10-20 01:02:59 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:02:56 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.011 |  |
| 2026-10-20 01:02:44 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-20 01:02:22 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-20 01:02:14 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:01:45 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-10-20 01:01:30 | Ellagawa (Kalu Ganga) | 6.41 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:01:13 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 1.348 | 🔺 Rising |
| 2026-10-20 01:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.035 |  |
| 2026-10-20 01:00:25 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:00:13 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.033 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 01:34:36 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | 1.348 | 🔺 Rising |
| 2026-10-20 01:02:44 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-20 01:10:15 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-20 01:02:22 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-20 00:01:08 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-20 01:00:25 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:02:14 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:02:59 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:06:02 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:06:43 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:17:18 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:01:30 | Ellagawa (Kalu Ganga) | 6.41 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:24:11 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:12:46 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:06:12 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:04:29 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:03:27 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:21:39 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-10-20 01:04:33 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-10-20 01:27:26 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-20 01:04:25 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-10-20 01:02:56 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.011 |  |
| 2026-10-20 01:13:50 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.017 |  |
| 2026-10-20 01:04:16 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-10-20 01:03:56 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-10-20 00:02:05 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-10-20 01:04:31 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.020 |  |
| 2026-10-20 01:01:45 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-10-20 00:02:37 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-10-20 01:22:19 | Panadugama (Nilwala Ganga) | 4.98 | 🟢 Normal | -0.023 |  |
| 2026-10-20 00:09:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.028 |  |
| 2026-10-20 00:06:26 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.032 |  |
| 2026-10-20 01:00:13 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.033 |  |
| 2026-10-20 01:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.035 |  |
| 2026-10-20 01:14:52 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.039 |  |
| 2026-10-20 01:07:05 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | -0.050 |  |
| 2026-10-20 01:21:57 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.054 |  |
| 2026-10-19 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.070 |  |
| 2026-10-20 01:06:31 | Rathnapura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)