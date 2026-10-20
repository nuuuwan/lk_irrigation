# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_03:06:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,621 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 03:06:19 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-10-21 03:06:02 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.022 |  |
| 2026-10-21 03:05:56 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-10-21 03:05:48 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-10-21 03:05:45 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:05:39 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:05:31 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 03:05:29 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-21 03:05:11 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:04:59 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-21 03:04:24 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-10-21 03:04:11 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-10-21 03:04:10 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.012 |  |
| 2026-10-21 03:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:03:33 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.019 |  |
| 2026-10-21 03:03:27 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.003 |  |
| 2026-10-21 03:03:14 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:03:13 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:03:10 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-21 03:02:52 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:02:21 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-21 03:02:19 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.042 |  |
| 2026-10-21 03:02:11 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 03:02:05 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:01:53 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:01:41 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 03:01:10 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:00:43 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:00:26 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-10-21 02:53:11 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 02:00:49 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | -0.010 |  |
| 2026-10-20 18:02:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-10-21 03:04:11 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-10-21 03:02:21 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-21 03:05:29 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-21 03:05:31 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 03:01:41 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 18:04:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 01:03:55 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 03:02:11 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 03:03:10 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-21 02:12:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-21 03:05:56 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-10-21 02:53:11 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-21 03:04:24 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-21 03:06:19 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-10-21 03:04:59 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-21 03:03:27 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.003 |  |
| 2026-10-21 01:20:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.008 |  |
| 2026-10-21 03:03:14 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:02:52 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:05:11 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:05:45 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:05:39 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:01:53 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:02:05 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:03:13 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:00:43 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-10-21 02:01:25 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:01:10 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:04:10 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.012 |  |
| 2026-10-21 02:21:29 | Panadugama (Nilwala Ganga) | 4.24 | 🟢 Normal | -0.017 |  |
| 2026-10-21 03:03:33 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.019 |  |
| 2026-10-21 03:06:02 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.022 |  |
| 2026-10-21 02:03:47 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.031 |  |
| 2026-10-21 03:02:19 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.042 |  |
| 2026-10-21 02:06:41 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)