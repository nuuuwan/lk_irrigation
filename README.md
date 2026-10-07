# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_01:06:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,828 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 01:06:10 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-10-08 01:04:24 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-10-08 01:04:19 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-08 01:03:59 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-08 01:03:46 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-08 01:03:36 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-08 01:03:23 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.050 |  |
| 2026-10-08 01:03:03 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 01:03:00 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.021 |  |
| 2026-10-08 01:02:52 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-08 01:02:41 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 01:02:37 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-08 01:02:36 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 01:02:35 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-08 01:02:34 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-10-08 01:02:21 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-08 01:02:10 | Peradeniya (Mahaweli Ganga) | 3.46 | 🟢 Normal | -0.070 |  |
| 2026-10-08 01:02:08 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 01:02:07 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-08 01:02:00 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-08 01:01:48 | Nakkala (Kumbukkan Oya) | 0.00 | 🟢 Normal | -0.659 |  |
| 2026-10-08 01:01:08 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-08 01:01:07 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 01:00:21 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-08 00:59:53 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 00:04:02 | Magura (Kalu Ganga) | 3.61 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-10-08 01:02:37 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-08 01:03:36 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-08 01:04:19 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-08 01:02:52 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-08 01:01:08 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-08 01:03:59 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-08 01:02:07 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-08 01:02:08 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-07 18:03:09 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-08 01:02:41 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 00:59:53 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 01:02:00 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:05:45 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-08 01:00:21 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:03:15 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-08 01:02:36 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 01:02:35 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-08 00:05:38 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-10-08 01:01:07 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 00:01:16 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:09:53 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-08 01:03:03 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 01:03:46 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-08 00:03:50 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.005 |  |
| 2026-10-08 00:02:30 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-10-08 01:02:21 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-08 01:02:34 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-10-08 01:06:10 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-10-08 00:16:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | -0.016 |  |
| 2026-10-08 00:11:02 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.018 |  |
| 2026-10-08 01:04:24 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-10-08 01:03:00 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.021 |  |
| 2026-10-08 00:08:56 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.048 |  |
| 2026-10-08 01:03:23 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.050 |  |
| 2026-10-08 01:02:10 | Peradeniya (Mahaweli Ganga) | 3.46 | 🟢 Normal | -0.070 |  |
| 2026-10-08 00:10:28 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | -0.107 |  |
| 2026-10-08 00:07:59 | Holombuwa (Kelani Ganga) | 2.62 | 🟢 Normal | -0.457 |  |
| 2026-10-08 01:01:48 | Nakkala (Kumbukkan Oya) | 0.00 | 🟢 Normal | -0.659 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)