# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_10:25:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,501 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 10:25:45 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.007 |  |
| 2026-11-14 10:24:38 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 10:24:15 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.023 |  |
| 2026-11-14 10:19:39 | Panadugama (Nilwala Ganga) | 5.50 | 🟡 Alert | -0.031 |  |
| 2026-11-14 10:19:13 | Magura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.008 |  |
| 2026-11-14 10:15:16 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | -0.044 |  |
| 2026-11-14 10:11:17 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:08:12 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:07:17 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.009 |  |
| 2026-11-14 10:06:07 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:05:41 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:05:28 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-14 10:05:23 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:05:10 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.022 |  |
| 2026-11-14 10:04:51 | Putupaula (Kalu Ganga) | 1.69 | 🟢 Normal | -0.058 |  |
| 2026-11-14 10:04:31 | Holombuwa (Kelani Ganga) | 1.99 | 🟢 Normal | 1.005 | 🔺 Rising |
| 2026-11-14 10:04:30 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | -0.020 |  |
| 2026-11-14 10:04:19 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | -0.031 |  |
| 2026-11-14 10:04:04 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:04:03 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:04:01 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-11-14 10:03:22 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:03:12 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:03:12 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.011 |  |
| 2026-11-14 10:02:59 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | -0.030 |  |
| 2026-11-14 10:02:58 | Kuda Oya (Kirindi Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.88 | 🟢 Normal | -0.106 |  |
| 2026-11-14 10:02:25 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:02:15 | Ellagawa (Kalu Ganga) | 6.29 | 🟢 Normal | -0.074 |  |
| 2026-11-14 10:01:47 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | -0.019 |  |
| 2026-11-14 10:01:47 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 10:01:43 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:01:42 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:01:35 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:01:07 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:01:02 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:00:50 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:00:36 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 10:24:38 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 10:19:39 | Panadugama (Nilwala Ganga) | 5.50 | 🟡 Alert | -0.031 |  |
| 2026-11-14 10:15:16 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | -0.044 |  |
| 2026-11-14 10:04:31 | Holombuwa (Kelani Ganga) | 1.99 | 🟢 Normal | 1.005 | 🔺 Rising |
| 2026-11-14 10:04:01 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-11-14 10:05:28 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-14 10:01:47 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 10:01:43 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:00:50 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:01:02 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:08:12 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:04:03 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:03:12 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:04:04 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:01:07 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:05:41 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:01:35 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:06:07 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:11:17 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:25:45 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.007 |  |
| 2026-11-14 10:19:13 | Magura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.008 |  |
| 2026-11-14 10:07:17 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.009 |  |
| 2026-11-14 10:01:42 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:00:36 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:02:58 | Kuda Oya (Kirindi Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:02:25 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:05:23 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:03:22 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:03:12 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.011 |  |
| 2026-11-14 10:01:47 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | -0.019 |  |
| 2026-11-14 10:04:30 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | -0.020 |  |
| 2026-11-14 10:05:10 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.022 |  |
| 2026-11-14 10:24:15 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.023 |  |
| 2026-11-14 10:02:59 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | -0.030 |  |
| 2026-11-14 10:04:19 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | -0.031 |  |
| 2026-11-14 10:04:51 | Putupaula (Kalu Ganga) | 1.69 | 🟢 Normal | -0.058 |  |
| 2026-11-14 10:02:15 | Ellagawa (Kalu Ganga) | 6.29 | 🟢 Normal | -0.074 |  |
| 2026-11-14 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.88 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)