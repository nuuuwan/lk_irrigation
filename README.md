# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_17:03:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,750 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 17:03:01 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 17:02:50 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:02:50 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-11-14 17:02:33 | Hanwella (Kelani Ganga) | 2.74 | 🟢 Normal | -0.010 |  |
| 2026-11-14 17:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.17 | 🟢 Normal | -0.100 |  |
| 2026-11-14 17:02:26 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-11-14 17:02:25 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 17:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:02:11 | Thanamalwila (Kirindi Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-11-14 17:02:04 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:01:38 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:01:33 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:00:52 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-14 17:00:08 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-14 16:42:58 | Urawa (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.006 |  |
| 2026-11-14 16:21:33 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 16:21:33 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 16:01:46 | Panadugama (Nilwala Ganga) | 5.31 | 🟡 Alert | -0.031 |  |
| 2026-11-14 17:00:52 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-14 17:02:25 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 17:03:01 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 16:02:58 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:02:04 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:03:56 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:01:01 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:01:38 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:02:30 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:01:38 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:04:01 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:02:37 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:04:49 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:00:36 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:01:33 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-14 17:02:50 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:42:58 | Urawa (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.006 |  |
| 2026-11-14 16:08:20 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.009 |  |
| 2026-11-14 16:03:53 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-11-14 17:02:33 | Hanwella (Kelani Ganga) | 2.74 | 🟢 Normal | -0.010 |  |
| 2026-11-14 16:00:55 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-11-14 17:00:08 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-14 17:02:11 | Thanamalwila (Kirindi Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-11-14 16:05:05 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-11-14 16:08:11 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.019 |  |
| 2026-11-14 16:05:11 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.019 |  |
| 2026-11-14 17:02:26 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-11-14 17:02:50 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-11-14 16:13:40 | Baddegama (Gin Ganga) | 3.38 | 🟢 Normal | -0.027 |  |
| 2026-11-14 16:01:49 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.029 |  |
| 2026-11-14 16:04:21 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.032 |  |
| 2026-11-14 16:09:37 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.036 |  |
| 2026-11-14 16:05:02 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.038 |  |
| 2026-11-14 16:03:11 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-11-14 16:07:30 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.050 |  |
| 2026-11-14 17:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.17 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)