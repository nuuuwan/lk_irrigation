# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_03:05:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,701 measurements** from **39** stations.
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
| 2026-10-20 03:05:37 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-10-20 03:05:31 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 03:05:08 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.117 |  |
| 2026-10-20 03:04:49 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | 39.484 | 🔺 Rising |
| 2026-10-20 03:04:34 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-10-20 03:04:18 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | 39.484 | 🔺 Rising |
| 2026-10-20 03:04:01 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.019 |  |
| 2026-10-20 03:03:54 | Ellagawa (Kalu Ganga) | 6.44 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-20 03:03:50 | Panadugama (Nilwala Ganga) | 4.95 | 🟢 Normal | -0.011 |  |
| 2026-10-20 03:03:45 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:03:38 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:03:25 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-20 03:02:41 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-20 03:02:37 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | -0.031 |  |
| 2026-10-20 03:02:32 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.021 |  |
| 2026-10-20 03:02:32 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-20 03:02:31 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:02:22 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-20 03:02:16 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-10-20 03:02:11 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:01:39 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:01:28 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-20 03:00:34 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-20 03:00:21 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:59:49 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:45:21 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-20 02:40:18 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-20 02:31:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.37 | 🟢 Normal | -0.013 |  |
| 2026-10-20 02:29:35 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 03:00:34 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-20 03:04:49 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | 39.484 | 🔺 Rising |
| 2026-10-20 03:05:37 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-10-20 03:02:22 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-20 03:03:54 | Ellagawa (Kalu Ganga) | 6.44 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-20 03:02:41 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-20 03:02:32 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-20 02:12:56 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-20 03:01:28 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-20 03:03:25 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-20 03:05:31 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 02:00:37 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:01:39 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:02:11 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:06:02 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:06:43 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:01:19 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:02:31 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:00:21 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:03:45 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:03:38 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:03:27 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:29:35 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:21:39 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-10-20 02:08:11 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-10-20 03:03:50 | Panadugama (Nilwala Ganga) | 4.95 | 🟢 Normal | -0.011 |  |
| 2026-10-20 02:09:41 | Pitabeddara (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-10-20 02:31:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.37 | 🟢 Normal | -0.013 |  |
| 2026-10-20 03:04:01 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.019 |  |
| 2026-10-20 03:02:32 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.021 |  |
| 2026-10-20 03:04:34 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-10-20 03:02:16 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-10-20 03:02:37 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | -0.031 |  |
| 2026-10-20 00:06:26 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.032 |  |
| 2026-10-19 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.070 |  |
| 2026-10-20 02:03:21 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.106 |  |
| 2026-10-20 03:05:08 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.117 |  |
| 2026-10-20 02:02:50 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.269 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)