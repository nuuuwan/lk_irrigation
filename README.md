# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_10:29:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,085 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 10:29:44 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-29 10:22:47 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 10:17:36 | Rathnapura (Kalu Ganga) | 4.81 | 🟢 Normal | -0.058 |  |
| 2026-10-29 10:09:30 | Panadugama (Nilwala Ganga) | 5.85 | 🟡 Alert | -0.021 |  |
| 2026-10-29 10:09:29 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-10-29 10:08:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.38 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 10:07:58 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | -0.009 |  |
| 2026-10-29 10:06:49 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:06:20 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.018 |  |
| 2026-10-29 10:06:08 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-10-29 10:05:53 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.009 |  |
| 2026-10-29 10:05:47 | Galgamuwa (Mee Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:05:44 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:04:49 | Hanwella (Kelani Ganga) | 3.77 | 🟢 Normal | -0.058 |  |
| 2026-10-29 10:04:21 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-29 10:04:17 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-10-29 10:04:10 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.048 |  |
| 2026-10-29 10:04:03 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-29 10:03:50 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:03:44 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | -0.042 |  |
| 2026-10-29 10:03:14 | Putupaula (Kalu Ganga) | 3.72 | 🟡 Alert | -0.010 |  |
| 2026-10-29 10:02:59 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:02:53 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:02:35 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-29 10:02:18 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:02:17 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-10-29 10:02:08 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 10:02:08 | Moragaswewa (Deduru Oya) | 1.32 | 🟢 Normal | -0.040 |  |
| 2026-10-29 10:02:01 | Ellagawa (Kalu Ganga) | 10.02 | 🟡 Alert | -0.040 |  |
| 2026-10-29 10:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-10-29 10:01:38 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-29 10:01:18 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:01:12 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.082 |  |
| 2026-10-29 10:01:07 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-29 10:01:04 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-10-29 10:00:56 | Pitabeddara (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.110 |  |
| 2026-10-29 10:00:42 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-29 10:00:25 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:00:07 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-10-29 09:58:45 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 10:22:47 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 10:08:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.38 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 10:01:07 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-29 10:03:14 | Putupaula (Kalu Ganga) | 3.72 | 🟡 Alert | -0.010 |  |
| 2026-10-29 10:09:30 | Panadugama (Nilwala Ganga) | 5.85 | 🟡 Alert | -0.021 |  |
| 2026-10-29 10:02:01 | Ellagawa (Kalu Ganga) | 10.02 | 🟡 Alert | -0.040 |  |
| 2026-10-29 10:02:35 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-29 10:04:03 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-29 10:01:38 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-29 10:00:42 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-29 10:29:44 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-29 10:02:08 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 10:02:18 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:05:47 | Galgamuwa (Mee Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:05:44 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:02:59 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:02:53 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:06:49 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:03:50 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:01:18 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:00:25 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:07:58 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | -0.009 |  |
| 2026-10-29 10:05:53 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.009 |  |
| 2026-10-29 10:02:17 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-10-29 10:04:21 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-29 10:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-10-29 10:00:07 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-10-29 10:04:17 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-10-29 10:06:20 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.018 |  |
| 2026-10-29 10:01:04 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-10-29 10:06:08 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-10-29 10:09:29 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-10-29 10:02:08 | Moragaswewa (Deduru Oya) | 1.32 | 🟢 Normal | -0.040 |  |
| 2026-10-29 10:03:44 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | -0.042 |  |
| 2026-10-29 10:04:10 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.048 |  |
| 2026-10-29 10:17:36 | Rathnapura (Kalu Ganga) | 4.81 | 🟢 Normal | -0.058 |  |
| 2026-10-29 10:04:49 | Hanwella (Kelani Ganga) | 3.77 | 🟢 Normal | -0.058 |  |
| 2026-10-29 10:01:12 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.082 |  |
| 2026-10-29 10:00:56 | Pitabeddara (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)