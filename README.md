# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_17:06:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,644 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 17:06:12 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:05:41 | Panadugama (Nilwala Ganga) | 6.46 | 🟠 Minor Flood | -0.035 |  |
| 2026-10-16 17:05:19 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | -0.010 |  |
| 2026-10-16 17:05:13 | Magura (Kalu Ganga) | 3.21 | 🟢 Normal | -0.021 |  |
| 2026-10-16 17:05:00 | Moragaswewa (Deduru Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-10-16 17:04:52 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:04:47 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:04:39 | Baddegama (Gin Ganga) | 3.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 17:04:21 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:04:15 | Putupaula (Kalu Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:04:03 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | -0.050 |  |
| 2026-10-16 17:04:01 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 17:03:50 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-16 17:03:42 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | -0.020 |  |
| 2026-10-16 17:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | -0.010 |  |
| 2026-10-16 17:03:24 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:03:14 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:03:09 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 17:03:07 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 17:02:58 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 17:02:54 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-10-16 17:02:45 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.059 |  |
| 2026-10-16 17:02:09 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-16 17:01:59 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:01:54 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-16 17:01:51 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 17:01:18 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | -0.023 |  |
| 2026-10-16 17:00:47 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.062 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 16:02:50 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 17:05:41 | Panadugama (Nilwala Ganga) | 6.46 | 🟠 Minor Flood | -0.035 |  |
| 2026-10-16 17:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | -0.010 |  |
| 2026-10-16 17:02:54 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-10-16 16:09:11 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-10-16 16:02:00 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-10-16 17:03:50 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-16 17:02:09 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-16 16:02:09 | Pitabeddara (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-16 17:01:54 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-16 17:03:09 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 17:02:58 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 17:03:07 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 17:01:51 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 16:01:05 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 17:04:39 | Baddegama (Gin Ganga) | 3.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 17:04:01 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 16:11:31 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:04:47 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:04:21 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:04:52 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:03:24 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:04:15 | Putupaula (Kalu Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:06:12 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:03:14 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-16 16:13:53 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:01:59 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-16 17:05:00 | Moragaswewa (Deduru Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-10-16 17:05:19 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | -0.010 |  |
| 2026-10-16 16:16:24 | Urawa (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.016 |  |
| 2026-10-16 17:03:42 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | -0.020 |  |
| 2026-10-16 17:05:13 | Magura (Kalu Ganga) | 3.21 | 🟢 Normal | -0.021 |  |
| 2026-10-16 16:03:31 | Galgamuwa (Mee Oya) | 2.06 | 🟢 Normal | -0.021 |  |
| 2026-10-16 17:01:18 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | -0.023 |  |
| 2026-10-16 16:07:36 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | -0.029 |  |
| 2026-10-16 17:04:03 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | -0.050 |  |
| 2026-10-16 17:02:45 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.059 |  |
| 2026-10-16 17:00:47 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.062 |  |
| 2026-10-16 16:03:51 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)