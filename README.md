# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_07:15:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,868 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 07:15:36 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.008 |  |
| 2026-10-20 07:15:33 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:09:36 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.009 |  |
| 2026-10-20 07:08:47 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:08:23 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.063 |  |
| 2026-10-20 07:07:39 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:06:56 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-10-20 07:06:24 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-20 07:06:20 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:05:35 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 07:05:01 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:04:57 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:04:54 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.124 |  |
| 2026-10-20 07:04:53 | Hanwella (Kelani Ganga) | 3.00 | 🟢 Normal | -0.032 |  |
| 2026-10-20 07:04:51 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 07:04:48 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2026-10-20 07:04:26 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:04:09 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:04:08 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:03:49 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 07:03:46 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-10-20 07:03:00 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.002 |  |
| 2026-10-20 07:03:00 | Ellagawa (Kalu Ganga) | 6.47 | 🟢 Normal | -0.031 |  |
| 2026-10-20 07:02:58 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-10-20 07:02:48 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:02:42 | Panadugama (Nilwala Ganga) | 4.79 | 🟢 Normal | -0.072 |  |
| 2026-10-20 07:02:33 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.020 |  |
| 2026-10-20 07:02:31 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.029 |  |
| 2026-10-20 07:02:29 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-10-20 07:02:26 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 07:02:23 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.137 |  |
| 2026-10-20 07:02:18 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.153 |  |
| 2026-10-20 07:02:06 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | -0.022 |  |
| 2026-10-20 07:01:56 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-20 07:01:27 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.032 |  |
| 2026-10-20 07:01:18 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-10-20 07:00:45 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:00:27 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 07:02:06 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | -0.022 |  |
| 2026-10-20 07:04:48 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2026-10-20 07:02:58 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-10-20 07:02:26 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 07:04:51 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 07:01:56 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-20 07:05:35 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 07:03:49 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 07:04:09 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:00:27 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:06:20 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:15:33 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:00:45 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:07:39 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:04:08 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:04:57 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:02:33 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:04:26 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:05:01 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:08:47 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-20 07:03:00 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.002 |  |
| 2026-10-20 07:15:36 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.008 |  |
| 2026-10-20 07:09:36 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.009 |  |
| 2026-10-20 07:06:56 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-10-20 07:06:24 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-20 07:03:46 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-10-20 07:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.020 |  |
| 2026-10-20 07:02:29 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-10-20 07:02:31 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.029 |  |
| 2026-10-20 07:03:00 | Ellagawa (Kalu Ganga) | 6.47 | 🟢 Normal | -0.031 |  |
| 2026-10-20 07:01:18 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-10-20 07:01:27 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.032 |  |
| 2026-10-20 07:04:53 | Hanwella (Kelani Ganga) | 3.00 | 🟢 Normal | -0.032 |  |
| 2026-10-20 07:08:23 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.063 |  |
| 2026-10-20 07:02:42 | Panadugama (Nilwala Ganga) | 4.79 | 🟢 Normal | -0.072 |  |
| 2026-10-20 07:04:54 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.124 |  |
| 2026-10-20 07:02:23 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.137 |  |
| 2026-10-20 07:02:18 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)