# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_05:04:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,685 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 05:04:09 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-21 05:03:51 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.057 |  |
| 2026-10-21 05:03:16 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-10-21 05:03:15 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-10-21 05:02:51 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.021 |  |
| 2026-10-21 05:02:15 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-21 05:02:14 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-21 05:02:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-10-21 05:01:59 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-21 05:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-10-21 05:01:55 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-10-21 05:01:45 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-21 05:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-21 05:01:41 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.020 |  |
| 2026-10-21 05:01:06 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.149 |  |
| 2026-10-21 05:00:48 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-10-21 05:00:30 | Thalgahagoda (Nilwala Ganga) | 1.47 | 🟡 Alert | -0.005 |  |
| 2026-10-21 05:00:08 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.050 |  |
| 2026-10-21 04:58:31 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.005 |  |
| 2026-10-21 04:52:20 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | -0.011 |  |
| 2026-10-21 04:45:33 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:32:22 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-21 04:28:06 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 05:00:30 | Thalgahagoda (Nilwala Ganga) | 1.47 | 🟡 Alert | -0.005 |  |
| 2026-10-20 18:02:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-10-21 05:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-21 04:05:53 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-21 04:04:26 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-21 05:01:59 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-21 04:02:37 | Dunamale (Aththanagalu Oya) | 1.89 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-21 04:32:22 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-20 18:04:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 04:02:19 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:03:56 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:03:59 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:28:06 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-21 05:04:09 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:06:20 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-21 05:00:48 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:45:33 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:58:31 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.005 |  |
| 2026-10-21 04:13:47 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-10-21 05:01:45 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:02:48 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:00:48 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-10-21 05:02:14 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:02:01 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-10-21 05:02:15 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-21 05:03:16 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:00:22 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:52:20 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | -0.011 |  |
| 2026-10-21 05:01:41 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.020 |  |
| 2026-10-21 05:02:51 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.021 |  |
| 2026-10-21 05:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-10-21 04:16:21 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.026 |  |
| 2026-10-21 05:03:15 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-10-21 05:01:55 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-10-21 05:02:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-10-21 05:00:08 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.050 |  |
| 2026-10-21 05:03:51 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.057 |  |
| 2026-10-21 05:01:06 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)