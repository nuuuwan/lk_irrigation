# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_13:20:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,298 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Putupaula — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 13:20:42 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | 0.008 | 🔺 Rising |
| 2026-10-28 13:18:29 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 13:16:20 | Magura (Kalu Ganga) | 4.07 | 🟡 Alert | -0.036 |  |
| 2026-10-28 13:11:19 | Urawa (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.621 | 🔺 Rising |
| 2026-10-28 13:10:07 | Panadugama (Nilwala Ganga) | 5.86 | 🟡 Alert | 0.036 | 🔺 Rising |
| 2026-10-28 13:09:39 | Horowpothana (Yan Oya) | 2.77 | 🟢 Normal | -0.109 |  |
| 2026-10-28 13:08:06 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-28 13:07:38 | Thawalama (Gin Ganga) | 3.41 | 🟢 Normal | 0.319 | 🔺 Rising |
| 2026-10-28 13:07:34 | Glencourse (Kelani Ganga) | 11.66 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-28 13:07:33 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 13:07:24 | Galgamuwa (Mee Oya) | 2.38 | 🟢 Normal | -0.018 |  |
| 2026-10-28 13:06:58 | Hanwella (Kelani Ganga) | 4.35 | 🟢 Normal | -0.039 |  |
| 2026-10-28 13:06:23 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-28 13:05:51 | Putupaula (Kalu Ganga) | 3.66 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-28 13:05:33 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 13:05:05 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-28 13:04:51 | Rathnapura (Kalu Ganga) | 6.21 | 🟡 Alert | -0.060 |  |
| 2026-10-28 13:04:38 | Dunamale (Aththanagalu Oya) | 3.62 | 🟡 Alert | -0.029 |  |
| 2026-10-28 13:04:35 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-28 13:04:06 | Ellagawa (Kalu Ganga) | 10.43 | 🟡 Alert | 0.000 |  |
| 2026-10-28 13:04:05 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.048 |  |
| 2026-10-28 13:04:04 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-28 13:03:55 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 13:03:52 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | -0.040 |  |
| 2026-10-28 13:03:43 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-10-28 13:03:27 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | -0.029 |  |
| 2026-10-28 13:03:07 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | -0.026 |  |
| 2026-10-28 13:03:02 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.019 |  |
| 2026-10-28 13:02:12 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-28 13:02:11 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-28 13:02:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.75 | 🟠 Minor Flood | -0.021 |  |
| 2026-10-28 13:01:56 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-10-28 13:01:42 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-10-28 13:01:18 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-28 13:01:08 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-28 13:01:00 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | -0.129 |  |
| 2026-10-28 13:00:57 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-28 13:00:46 | Moragaswewa (Deduru Oya) | 3.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-28 13:00:25 | Pitabeddara (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 13:20:42 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | 0.008 | 🔺 Rising |
| 2026-10-28 13:07:33 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 13:02:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.75 | 🟠 Minor Flood | -0.021 |  |
| 2026-10-28 13:10:07 | Panadugama (Nilwala Ganga) | 5.86 | 🟡 Alert | 0.036 | 🔺 Rising |
| 2026-10-28 13:05:51 | Putupaula (Kalu Ganga) | 3.66 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-28 13:04:06 | Ellagawa (Kalu Ganga) | 10.43 | 🟡 Alert | 0.000 |  |
| 2026-10-28 13:04:38 | Dunamale (Aththanagalu Oya) | 3.62 | 🟡 Alert | -0.029 |  |
| 2026-10-28 13:16:20 | Magura (Kalu Ganga) | 4.07 | 🟡 Alert | -0.036 |  |
| 2026-10-28 13:04:51 | Rathnapura (Kalu Ganga) | 6.21 | 🟡 Alert | -0.060 |  |
| 2026-10-28 13:11:19 | Urawa (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.621 | 🔺 Rising |
| 2026-10-28 13:07:38 | Thawalama (Gin Ganga) | 3.41 | 🟢 Normal | 0.319 | 🔺 Rising |
| 2026-10-28 13:01:08 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-28 13:05:05 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-28 13:00:25 | Pitabeddara (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-28 13:07:34 | Glencourse (Kelani Ganga) | 11.66 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-28 13:00:46 | Moragaswewa (Deduru Oya) | 3.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-28 13:03:55 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 13:05:33 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 13:06:23 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-28 13:01:18 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-28 13:04:35 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-28 13:18:29 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 13:02:12 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-28 13:00:57 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-28 13:04:04 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-28 13:08:06 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-28 13:01:56 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-10-28 13:02:11 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-28 13:03:43 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-10-28 13:07:24 | Galgamuwa (Mee Oya) | 2.38 | 🟢 Normal | -0.018 |  |
| 2026-10-28 13:03:02 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.019 |  |
| 2026-10-28 13:01:42 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-10-28 13:03:07 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | -0.026 |  |
| 2026-10-28 13:03:27 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | -0.029 |  |
| 2026-10-28 13:06:58 | Hanwella (Kelani Ganga) | 4.35 | 🟢 Normal | -0.039 |  |
| 2026-10-28 13:03:52 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | -0.040 |  |
| 2026-10-28 13:04:05 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.048 |  |
| 2026-10-28 13:09:39 | Horowpothana (Yan Oya) | 2.77 | 🟢 Normal | -0.109 |  |
| 2026-10-28 13:01:00 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)