# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_12:04:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,959 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 12:04:24 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:04:07 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-31 12:03:55 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.01 | 🟡 Alert | -0.069 |  |
| 2026-10-31 12:03:45 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:03:30 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-31 12:03:28 | Putupaula (Kalu Ganga) | 2.26 | 🟢 Normal | -0.090 |  |
| 2026-10-31 12:03:23 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -0.031 |  |
| 2026-10-31 12:03:12 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-10-31 12:03:11 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.030 |  |
| 2026-10-31 12:03:11 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-10-31 12:03:01 | Galgamuwa (Mee Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:02:42 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-31 12:02:21 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.031 |  |
| 2026-10-31 12:02:11 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.021 |  |
| 2026-10-31 12:01:59 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:01:58 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-10-31 12:01:56 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:01:49 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-10-31 12:01:36 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-10-31 12:01:20 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-31 12:01:17 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-10-31 12:01:13 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-31 12:01:10 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.021 |  |
| 2026-10-31 12:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:01:07 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.031 |  |
| 2026-10-31 12:01:02 | Thalgahagoda (Nilwala Ganga) | 1.64 | 🟡 Alert | -0.020 |  |
| 2026-10-31 12:00:56 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-10-31 12:00:53 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-10-31 12:00:15 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 12:01:02 | Thalgahagoda (Nilwala Ganga) | 1.64 | 🟡 Alert | -0.020 |  |
| 2026-10-31 12:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.01 | 🟡 Alert | -0.069 |  |
| 2026-10-31 12:02:42 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-31 12:04:07 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-31 12:01:13 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-31 12:03:30 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-31 12:01:59 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:01:56 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:03:01 | Galgamuwa (Mee Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:03:45 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:06:49 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:04:24 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:03:55 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:06:03 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-31 12:01:58 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-10-31 11:02:19 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-10-31 12:03:12 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-10-31 12:01:49 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-10-31 12:01:17 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-10-31 12:01:20 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-31 12:00:56 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-10-31 12:00:15 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.014 |  |
| 2026-10-31 12:01:36 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-10-31 12:03:11 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-10-31 12:00:53 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-10-31 12:02:11 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.021 |  |
| 2026-10-31 12:01:10 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.021 |  |
| 2026-10-31 11:18:14 | Panadugama (Nilwala Ganga) | 4.75 | 🟢 Normal | -0.025 |  |
| 2026-10-31 11:00:46 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-10-31 12:03:11 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.030 |  |
| 2026-10-31 12:02:21 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.031 |  |
| 2026-10-31 11:06:22 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.031 |  |
| 2026-10-31 12:01:07 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.031 |  |
| 2026-10-31 12:03:23 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -0.031 |  |
| 2026-10-31 11:03:08 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -0.036 |  |
| 2026-10-31 11:04:16 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-10-31 11:01:47 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | -0.062 |  |
| 2026-10-31 12:03:28 | Putupaula (Kalu Ganga) | 2.26 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)