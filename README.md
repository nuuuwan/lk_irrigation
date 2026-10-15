# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_01:22:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,034 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 01:22:28 | Thawalama (Gin Ganga) | 3.90 | 🟢 Normal | -0.053 |  |
| 2026-10-16 01:16:19 | Dunamale (Aththanagalu Oya) | 3.81 | 🟡 Alert | 0.000 |  |
| 2026-10-16 01:09:33 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-10-16 01:07:46 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-16 01:07:25 | Pitabeddara (Nilwala Ganga) | 4.58 | 🟡 Alert | -0.063 |  |
| 2026-10-16 01:06:40 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | 0.000 |  |
| 2026-10-16 01:06:35 | Panadugama (Nilwala Ganga) | 6.61 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-10-16 01:05:46 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-16 01:05:40 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 01:05:31 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-16 01:04:56 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-10-16 01:04:43 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-10-16 01:03:20 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-10-16 01:03:14 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-16 01:03:14 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | -0.051 |  |
| 2026-10-16 01:03:10 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 01:03:07 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.021 |  |
| 2026-10-16 01:02:49 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-10-16 01:02:36 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-10-16 01:02:33 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-16 01:02:19 | Baddegama (Gin Ganga) | 2.93 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-16 01:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.84 | 🟡 Alert | -0.010 |  |
| 2026-10-16 01:02:05 | Giriulla (Maha Oya) | 2.26 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-16 01:02:01 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 01:01:59 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 01:01:58 | Ellagawa (Kalu Ganga) | 7.65 | 🟢 Normal | -0.053 |  |
| 2026-10-16 01:01:46 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-16 01:01:17 | Moraketiya (Walawe Ganga) | 3.28 | 🟡 Alert | 0.991 | 🔺 Rising |
| 2026-10-16 01:01:17 | Moragaswewa (Deduru Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-10-16 01:00:06 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 01:06:35 | Panadugama (Nilwala Ganga) | 6.61 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-10-16 01:05:40 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 01:01:17 | Moraketiya (Walawe Ganga) | 3.28 | 🟡 Alert | 0.991 | 🔺 Rising |
| 2026-10-16 01:16:19 | Dunamale (Aththanagalu Oya) | 3.81 | 🟡 Alert | 0.000 |  |
| 2026-10-16 01:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.84 | 🟡 Alert | -0.010 |  |
| 2026-10-16 01:07:25 | Pitabeddara (Nilwala Ganga) | 4.58 | 🟡 Alert | -0.063 |  |
| 2026-10-16 00:06:26 | Urawa (Nilwala Ganga) | 2.50 | 🟡 Alert | -0.115 |  |
| 2026-10-16 01:02:33 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-16 01:01:46 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-15 18:04:44 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-15 23:06:21 | Magura (Kalu Ganga) | 3.92 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-16 01:02:19 | Baddegama (Gin Ganga) | 2.93 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-16 01:07:46 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-16 01:02:05 | Giriulla (Maha Oya) | 2.26 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-16 01:02:01 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 00:04:57 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 18:18:48 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-16 00:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 01:01:59 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 18:02:23 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-16 01:03:14 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-16 01:01:17 | Moragaswewa (Deduru Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-10-16 01:03:10 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 01:06:40 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | 0.000 |  |
| 2026-10-16 01:00:06 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-16 01:05:31 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-16 00:05:02 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 01:09:33 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-10-16 01:05:46 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-16 01:03:20 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-10-16 01:02:36 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-10-16 01:04:56 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-10-16 01:03:07 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.021 |  |
| 2026-10-16 01:02:49 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-10-16 01:04:43 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-10-16 00:04:59 | Putupaula (Kalu Ganga) | 2.48 | 🟢 Normal | -0.044 |  |
| 2026-10-16 01:03:14 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | -0.051 |  |
| 2026-10-16 01:22:28 | Thawalama (Gin Ganga) | 3.90 | 🟢 Normal | -0.053 |  |
| 2026-10-16 01:01:58 | Ellagawa (Kalu Ganga) | 7.65 | 🟢 Normal | -0.053 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)