# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_12:10:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,259 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Ellagawa — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 12:10:20 | Magura (Kalu Ganga) | 4.11 | 🟡 Alert | -0.065 |  |
| 2026-10-28 12:10:14 | Putupaula (Kalu Ganga) | 3.65 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-10-28 12:09:16 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.362 | 🔺 Rising |
| 2026-10-28 12:07:45 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.009 |  |
| 2026-10-28 12:07:31 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 12:06:42 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.029 |  |
| 2026-10-28 12:05:45 | Nagalagam Street (Kelani Ganga) | 0.72 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-28 12:05:37 | Hanwella (Kelani Ganga) | 4.39 | 🟢 Normal | -0.030 |  |
| 2026-10-28 12:05:36 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:05:25 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 12:05:17 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.77 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 12:04:42 | Rathnapura (Kalu Ganga) | 6.27 | 🟡 Alert | -0.068 |  |
| 2026-10-28 12:04:39 | Urawa (Nilwala Ganga) | 1.65 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-10-28 12:04:19 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.030 |  |
| 2026-10-28 12:03:52 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.040 |  |
| 2026-10-28 12:03:51 | Ellagawa (Kalu Ganga) | 10.43 | 🟡 Alert | 0.000 |  |
| 2026-10-28 12:03:50 | Panadugama (Nilwala Ganga) | 5.82 | 🟡 Alert | -0.020 |  |
| 2026-10-28 12:03:49 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | -0.088 |  |
| 2026-10-28 12:03:16 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:03:15 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 12:02:59 | Glencourse (Kelani Ganga) | 11.63 | 🟢 Normal | -0.021 |  |
| 2026-10-28 12:02:56 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:02:51 | Dunamale (Aththanagalu Oya) | 3.65 | 🟡 Alert | -0.118 |  |
| 2026-10-28 12:02:32 | Galgamuwa (Mee Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:02:18 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | -0.021 |  |
| 2026-10-28 12:02:11 | Moragaswewa (Deduru Oya) | 3.07 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-28 12:02:09 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:01:51 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:01:39 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-10-28 12:01:39 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.032 |  |
| 2026-10-28 12:01:36 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:01:28 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.011 |  |
| 2026-10-28 12:01:21 | Thanthirimale (Malwathu Oya) | 2.17 | 🟢 Normal | -0.071 |  |
| 2026-10-28 12:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:01:12 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:01:04 | Pitabeddara (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-28 12:00:41 | Weraganthota (Mahaweli Ganga) | -2.53 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 12:07:31 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 12:05:25 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 12:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.77 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 12:10:14 | Putupaula (Kalu Ganga) | 3.65 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-10-28 12:03:51 | Ellagawa (Kalu Ganga) | 10.43 | 🟡 Alert | 0.000 |  |
| 2026-10-28 12:03:50 | Panadugama (Nilwala Ganga) | 5.82 | 🟡 Alert | -0.020 |  |
| 2026-10-28 12:10:20 | Magura (Kalu Ganga) | 4.11 | 🟡 Alert | -0.065 |  |
| 2026-10-28 12:04:42 | Rathnapura (Kalu Ganga) | 6.27 | 🟡 Alert | -0.068 |  |
| 2026-10-28 12:02:51 | Dunamale (Aththanagalu Oya) | 3.65 | 🟡 Alert | -0.118 |  |
| 2026-10-28 12:09:16 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.362 | 🔺 Rising |
| 2026-10-28 12:04:39 | Urawa (Nilwala Ganga) | 1.65 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-10-28 12:05:45 | Nagalagam Street (Kelani Ganga) | 0.72 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-28 12:01:04 | Pitabeddara (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-28 12:02:11 | Moragaswewa (Deduru Oya) | 3.07 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-28 12:03:15 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 12:01:12 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:01:36 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:02:32 | Galgamuwa (Mee Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:05:17 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:03:16 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:07:36 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:01:51 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:02:56 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:05:36 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:02:09 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-28 12:07:45 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.009 |  |
| 2026-10-28 12:00:41 | Weraganthota (Mahaweli Ganga) | -2.53 | 🟢 Normal | -0.010 |  |
| 2026-10-28 12:01:28 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.011 |  |
| 2026-10-28 12:01:39 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-10-28 12:02:18 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | -0.021 |  |
| 2026-10-28 12:02:59 | Glencourse (Kelani Ganga) | 11.63 | 🟢 Normal | -0.021 |  |
| 2026-10-28 12:06:42 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.029 |  |
| 2026-10-28 12:05:37 | Hanwella (Kelani Ganga) | 4.39 | 🟢 Normal | -0.030 |  |
| 2026-10-28 12:04:19 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.030 |  |
| 2026-10-28 12:01:39 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.032 |  |
| 2026-10-28 12:03:52 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.040 |  |
| 2026-10-28 12:01:21 | Thanthirimale (Malwathu Oya) | 2.17 | 🟢 Normal | -0.071 |  |
| 2026-10-28 12:03:49 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)