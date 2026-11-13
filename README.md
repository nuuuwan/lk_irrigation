# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_10:03:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,585 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 10:03:09 | Ellagawa (Kalu Ganga) | 7.99 | 🟢 Normal | -0.019 |  |
| 2026-11-13 10:03:00 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-13 10:02:56 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 10:02:49 | Rathnapura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.104 |  |
| 2026-11-13 10:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.07 | 🟡 Alert | -0.010 |  |
| 2026-11-13 10:02:30 | Moraketiya (Walawe Ganga) | 3.80 | 🟡 Alert | 0.665 | 🔺 Rising |
| 2026-11-13 10:02:30 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.022 |  |
| 2026-11-13 10:02:29 | Manampitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-13 10:02:20 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-13 10:02:17 | Thanamalwila (Kirindi Oya) | 2.15 | 🟢 Normal | -0.100 |  |
| 2026-11-13 10:02:07 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 10:02:04 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-11-13 10:01:51 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-13 10:01:51 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-11-13 10:01:36 | Weraganthota (Mahaweli Ganga) | -1.64 | 🟢 Normal | -0.020 |  |
| 2026-11-13 10:01:07 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-13 10:00:14 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 09:08:21 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 08:20:05 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 09:06:37 | Panadugama (Nilwala Ganga) | 6.31 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-13 10:02:30 | Moraketiya (Walawe Ganga) | 3.80 | 🟡 Alert | 0.665 | 🔺 Rising |
| 2026-11-13 10:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.07 | 🟡 Alert | -0.010 |  |
| 2026-11-13 09:01:59 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | -0.074 |  |
| 2026-11-13 10:02:29 | Manampitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-13 08:09:02 | Horowpothana (Yan Oya) | 2.59 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-13 10:02:07 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 10:02:56 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 10:01:51 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-13 09:05:26 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-13 10:03:00 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-13 10:01:07 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-13 09:06:45 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-11-13 09:00:29 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-13 09:01:12 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-11-13 08:23:48 | Urawa (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-11-13 10:01:51 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-11-13 10:02:20 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-13 10:02:04 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-11-13 10:00:14 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.017 |  |
| 2026-11-13 09:04:46 | Nakkala (Kumbukkan Oya) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-11-13 10:03:09 | Ellagawa (Kalu Ganga) | 7.99 | 🟢 Normal | -0.019 |  |
| 2026-11-13 09:03:07 | Moragaswewa (Deduru Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-13 10:01:36 | Weraganthota (Mahaweli Ganga) | -1.64 | 🟢 Normal | -0.020 |  |
| 2026-11-13 09:02:56 | Kuda Oya (Kirindi Oya) | 2.41 | 🟢 Normal | -0.020 |  |
| 2026-11-13 09:08:56 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | -0.020 |  |
| 2026-11-13 09:01:49 | Thaldena (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-11-13 10:02:30 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.022 |  |
| 2026-11-13 09:06:05 | Badalgama (Maha Oya) | 3.49 | 🟢 Normal | -0.031 |  |
| 2026-11-13 09:02:51 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | -0.040 |  |
| 2026-11-13 09:03:13 | Hanwella (Kelani Ganga) | 3.84 | 🟢 Normal | -0.040 |  |
| 2026-11-13 09:03:26 | Giriulla (Maha Oya) | 2.19 | 🟢 Normal | -0.043 |  |
| 2026-11-13 09:04:52 | Pitabeddara (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.083 |  |
| 2026-11-13 10:02:17 | Thanamalwila (Kirindi Oya) | 2.15 | 🟢 Normal | -0.100 |  |
| 2026-11-13 09:02:05 | Thawalama (Gin Ganga) | 2.74 | 🟢 Normal | -0.102 |  |
| 2026-11-13 09:14:29 | Magura (Kalu Ganga) | 3.79 | 🟢 Normal | -0.103 |  |
| 2026-11-13 10:02:49 | Rathnapura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)