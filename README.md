# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_23:17:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,484 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 23:17:20 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | -0.025 |  |
| 2026-10-30 23:09:23 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-30 23:06:18 | Rathnapura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.019 |  |
| 2026-10-30 23:05:48 | Putupaula (Kalu Ganga) | 3.10 | 🟡 Alert | -0.030 |  |
| 2026-10-30 23:05:29 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:04:45 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.11 | 🟡 Alert | -0.049 |  |
| 2026-10-30 23:04:18 | Ellagawa (Kalu Ganga) | 7.90 | 🟢 Normal | -0.184 |  |
| 2026-10-30 23:04:01 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:03:56 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-30 23:03:55 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-30 23:03:53 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:03:42 | Panadugama (Nilwala Ganga) | 5.07 | 🟡 Alert | -0.033 |  |
| 2026-10-30 23:03:30 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 23:03:19 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-10-30 23:03:18 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.023 |  |
| 2026-10-30 23:03:08 | Padiyathalawa (Maduru Oya) | 1.43 | 🟢 Normal | -0.088 |  |
| 2026-10-30 23:03:02 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.442 | 🔺 Rising |
| 2026-10-30 23:02:53 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 23:02:51 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | -0.012 |  |
| 2026-10-30 23:02:49 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:02:35 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -0.018 |  |
| 2026-10-30 23:02:25 | Nagalagam Street (Kelani Ganga) | 0.29 | 🟢 Normal | -0.016 |  |
| 2026-10-30 23:02:14 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:02:07 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-30 23:02:05 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-10-30 23:01:58 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-10-30 23:01:48 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:01:30 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-10-30 23:01:19 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.014 |  |
| 2026-10-30 23:00:40 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:00:34 | Thalgahagoda (Nilwala Ganga) | 1.77 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 23:00:28 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-10-30 23:00:28 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-10-30 22:59:39 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 23:00:34 | Thalgahagoda (Nilwala Ganga) | 1.77 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 23:05:48 | Putupaula (Kalu Ganga) | 3.10 | 🟡 Alert | -0.030 |  |
| 2026-10-30 23:03:42 | Panadugama (Nilwala Ganga) | 5.07 | 🟡 Alert | -0.033 |  |
| 2026-10-30 23:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.11 | 🟡 Alert | -0.049 |  |
| 2026-10-30 23:03:02 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.442 | 🔺 Rising |
| 2026-10-30 23:03:19 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-10-30 22:01:02 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-30 23:03:56 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-30 23:03:55 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-30 23:02:07 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-30 23:02:53 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 23:03:30 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 23:00:40 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:02:49 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:04:01 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:01:48 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:07 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:03:53 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:02:14 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:21:26 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:04:45 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:05:29 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-30 23:09:23 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-30 23:00:28 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-10-30 23:01:30 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-10-30 23:02:05 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-10-30 23:00:28 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-10-30 23:02:51 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | -0.012 |  |
| 2026-10-30 23:01:19 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.014 |  |
| 2026-10-30 23:02:25 | Nagalagam Street (Kelani Ganga) | 0.29 | 🟢 Normal | -0.016 |  |
| 2026-10-30 23:02:35 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -0.018 |  |
| 2026-10-30 23:06:18 | Rathnapura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.019 |  |
| 2026-10-30 23:01:58 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-10-30 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:00:42 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-30 23:03:18 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.023 |  |
| 2026-10-30 23:17:20 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | -0.025 |  |
| 2026-10-30 23:03:08 | Padiyathalawa (Maduru Oya) | 1.43 | 🟢 Normal | -0.088 |  |
| 2026-10-30 23:04:18 | Ellagawa (Kalu Ganga) | 7.90 | 🟢 Normal | -0.184 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)