# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_11:03:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,105 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 11:03:17 | Rathnapura (Kalu Ganga) | 4.73 | 🟢 Normal | -0.105 |  |
| 2026-10-29 11:03:00 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-10-29 11:02:47 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:02:47 | Ellagawa (Kalu Ganga) | 9.98 | 🟢 Normal | -0.039 |  |
| 2026-10-29 11:02:41 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:02:16 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.040 |  |
| 2026-10-29 11:02:11 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:02:09 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.049 |  |
| 2026-10-29 11:02:04 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.044 |  |
| 2026-10-29 11:01:49 | Putupaula (Kalu Ganga) | 3.71 | 🟡 Alert | -0.010 |  |
| 2026-10-29 11:01:48 | Galgamuwa (Mee Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:01:27 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:01:23 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | -0.011 |  |
| 2026-10-29 11:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:01:03 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | -0.022 |  |
| 2026-10-29 11:00:55 | Magura (Kalu Ganga) | 3.47 | 🟢 Normal | -0.032 |  |
| 2026-10-29 11:00:30 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:00:21 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | -0.032 |  |
| 2026-10-29 11:00:11 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:00:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:29:44 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-29 10:22:47 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 10:17:36 | Rathnapura (Kalu Ganga) | 4.81 | 🟢 Normal | -0.105 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 10:22:47 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 10:08:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.38 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 10:01:07 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-29 11:01:49 | Putupaula (Kalu Ganga) | 3.71 | 🟡 Alert | -0.010 |  |
| 2026-10-29 10:09:30 | Panadugama (Nilwala Ganga) | 5.85 | 🟡 Alert | -0.021 |  |
| 2026-10-29 10:02:35 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-29 10:01:38 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-29 10:00:42 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-29 10:29:44 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-29 11:00:30 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:01:48 | Galgamuwa (Mee Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:02:47 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:00:11 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:02:41 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:02:53 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-29 10:06:49 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:01:27 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:02:11 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:00:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:03:00 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-10-29 10:04:21 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-29 11:01:23 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | -0.011 |  |
| 2026-10-29 10:04:17 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-10-29 10:01:04 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-10-29 11:01:03 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | -0.022 |  |
| 2026-10-29 10:06:08 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-10-29 10:09:29 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-10-29 11:00:55 | Magura (Kalu Ganga) | 3.47 | 🟢 Normal | -0.032 |  |
| 2026-10-29 11:00:21 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | -0.032 |  |
| 2026-10-29 11:02:47 | Ellagawa (Kalu Ganga) | 9.98 | 🟢 Normal | -0.039 |  |
| 2026-10-29 11:02:16 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.040 |  |
| 2026-10-29 10:02:08 | Moragaswewa (Deduru Oya) | 1.32 | 🟢 Normal | -0.040 |  |
| 2026-10-29 10:03:44 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | -0.042 |  |
| 2026-10-29 11:02:04 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.044 |  |
| 2026-10-29 11:02:09 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.049 |  |
| 2026-10-29 10:04:49 | Hanwella (Kelani Ganga) | 3.77 | 🟢 Normal | -0.058 |  |
| 2026-10-29 11:03:17 | Rathnapura (Kalu Ganga) | 4.73 | 🟢 Normal | -0.105 |  |
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

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)