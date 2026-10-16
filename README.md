# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_16:08:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,608 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 16:08:14 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-16 16:07:36 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | -0.029 |  |
| 2026-10-16 16:07:17 | Magura (Kalu Ganga) | 3.23 | 🟢 Normal | -0.019 |  |
| 2026-10-16 16:07:10 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-16 16:05:42 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.029 |  |
| 2026-10-16 16:05:10 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.054 |  |
| 2026-10-16 16:04:41 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.019 |  |
| 2026-10-16 16:04:40 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-16 16:04:40 | Ellagawa (Kalu Ganga) | 7.36 | 🟢 Normal | -0.020 |  |
| 2026-10-16 16:04:21 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | -0.049 |  |
| 2026-10-16 16:03:51 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.078 |  |
| 2026-10-16 16:03:40 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-10-16 16:03:37 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-16 16:03:35 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 16:03:31 | Galgamuwa (Mee Oya) | 2.06 | 🟢 Normal | -0.021 |  |
| 2026-10-16 16:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.95 | 🟡 Alert | 0.000 |  |
| 2026-10-16 16:03:07 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-16 16:02:50 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 16:02:48 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-16 16:02:31 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-16 16:02:27 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-10-16 16:02:21 | Moragaswewa (Deduru Oya) | 2.30 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-16 16:02:20 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-10-16 16:02:09 | Pitabeddara (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-16 16:02:02 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-16 16:02:00 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-10-16 16:01:42 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-16 16:01:41 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-16 16:01:30 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-16 16:01:23 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 16:01:22 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 16:01:05 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 16:02:50 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 15:06:31 | Panadugama (Nilwala Ganga) | 6.52 | 🟠 Minor Flood | -0.051 |  |
| 2026-10-16 16:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.95 | 🟡 Alert | 0.000 |  |
| 2026-10-16 15:05:36 | Dunamale (Aththanagalu Oya) | 3.34 | 🟡 Alert | -0.039 |  |
| 2026-10-16 16:02:31 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-16 16:03:37 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-16 16:02:00 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-10-16 16:02:09 | Pitabeddara (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-16 15:06:11 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-16 16:01:30 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-16 16:03:07 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-16 16:02:21 | Moragaswewa (Deduru Oya) | 2.30 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-16 16:01:22 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 16:04:40 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-16 15:06:01 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-16 16:01:23 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 16:03:35 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 16:01:05 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 16:02:48 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-16 16:08:14 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-16 16:03:40 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-10-16 16:01:42 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-16 16:02:02 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-16 15:04:35 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-10-16 16:07:10 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-16 16:01:41 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-16 16:02:20 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-10-16 16:02:27 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-10-16 15:03:10 | Urawa (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-10-16 16:04:41 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.019 |  |
| 2026-10-16 16:07:17 | Magura (Kalu Ganga) | 3.23 | 🟢 Normal | -0.019 |  |
| 2026-10-16 16:04:40 | Ellagawa (Kalu Ganga) | 7.36 | 🟢 Normal | -0.020 |  |
| 2026-10-16 16:03:31 | Galgamuwa (Mee Oya) | 2.06 | 🟢 Normal | -0.021 |  |
| 2026-10-16 16:05:42 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.029 |  |
| 2026-10-16 16:07:36 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | -0.029 |  |
| 2026-10-16 16:04:21 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | -0.049 |  |
| 2026-10-16 16:05:10 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.054 |  |
| 2026-10-16 16:03:51 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.078 |  |
| 2026-10-16 15:07:27 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)