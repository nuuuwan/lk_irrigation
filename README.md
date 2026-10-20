# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_02:06:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,587 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 02:06:41 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.082 |  |
| 2026-10-21 02:06:28 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.023 |  |
| 2026-10-21 02:06:20 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-21 02:06:10 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.043 |  |
| 2026-10-21 02:05:41 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-21 02:05:13 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-10-21 02:04:40 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.021 |  |
| 2026-10-21 02:04:39 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-10-21 02:03:55 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-10-21 02:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-10-21 02:03:47 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.031 |  |
| 2026-10-21 02:03:44 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.015 |  |
| 2026-10-21 02:03:35 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-21 02:03:23 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-21 02:03:14 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-21 02:02:58 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-10-21 02:02:39 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-21 02:02:17 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-10-21 02:02:06 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-21 02:01:49 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-21 02:01:25 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-21 02:01:18 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.061 |  |
| 2026-10-21 02:01:17 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-21 02:01:17 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-10-21 02:01:17 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | -0.040 |  |
| 2026-10-21 02:00:49 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | -0.010 |  |
| 2026-10-21 01:52:17 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.043 |  |
| 2026-10-21 01:24:12 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 02:00:49 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | -0.010 |  |
| 2026-10-20 18:02:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-10-21 01:01:54 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-21 02:03:14 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-21 01:09:01 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 18:04:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 01:02:35 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 02:05:41 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:03:55 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 02:03:35 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:01:02 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-21 02:02:39 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-21 02:01:49 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:01:29 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-10-21 02:06:20 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:09:28 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:03:38 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-21 02:02:06 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:20:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.008 |  |
| 2026-10-21 02:03:23 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-21 02:02:17 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-10-21 02:03:55 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-10-21 02:01:17 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-10-21 02:05:13 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-10-21 02:01:25 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-21 02:01:17 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-21 02:03:44 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.015 |  |
| 2026-10-21 02:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-10-21 02:02:58 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-10-21 02:04:40 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.021 |  |
| 2026-10-21 02:06:28 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.023 |  |
| 2026-10-21 00:04:07 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.027 |  |
| 2026-10-21 02:04:39 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-10-21 02:03:47 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.031 |  |
| 2026-10-21 02:01:17 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | -0.040 |  |
| 2026-10-21 02:06:10 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.043 |  |
| 2026-10-21 02:01:18 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.061 |  |
| 2026-10-21 02:06:41 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)