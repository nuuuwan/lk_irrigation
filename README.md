# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_01:04:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,930 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 01:04:10 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-10-17 01:04:02 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 01:04:00 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.060 |  |
| 2026-10-17 01:03:59 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.106 |  |
| 2026-10-17 01:03:57 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-17 01:03:52 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.029 |  |
| 2026-10-17 01:03:38 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-10-17 01:03:23 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.108 |  |
| 2026-10-17 01:03:21 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-17 01:02:52 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-17 01:02:45 | Moragaswewa (Deduru Oya) | 1.90 | 🟢 Normal | -0.061 |  |
| 2026-10-17 01:02:34 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-17 01:01:57 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-17 01:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.89 | 🟡 Alert | -0.010 |  |
| 2026-10-17 01:01:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-17 01:01:17 | Peradeniya (Mahaweli Ganga) | 3.29 | 🟢 Normal | -0.010 |  |
| 2026-10-17 01:01:08 | Ellagawa (Kalu Ganga) | 7.39 | 🟢 Normal | 0.000 |  |
| 2026-10-17 01:00:55 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-17 01:00:14 | Moraketiya (Walawe Ganga) | 1.51 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-17 01:00:12 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-10-17 00:16:52 | Panadugama (Nilwala Ganga) | 6.35 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 00:16:52 | Panadugama (Nilwala Ganga) | 6.35 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 00:13:11 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 01:03:38 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-10-17 01:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.89 | 🟡 Alert | -0.010 |  |
| 2026-10-17 01:01:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-17 00:02:47 | Magura (Kalu Ganga) | 3.93 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-17 01:03:21 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-17 01:02:34 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-17 00:15:33 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-17 01:01:57 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-16 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-17 01:02:52 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-17 00:01:15 | Rathnapura (Kalu Ganga) | 4.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-17 01:00:14 | Moraketiya (Walawe Ganga) | 1.51 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-16 18:01:05 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-17 01:04:02 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 00:04:33 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 01:01:08 | Ellagawa (Kalu Ganga) | 7.39 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:14:02 | Baddegama (Gin Ganga) | 3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-17 01:03:57 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:03:23 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:03:32 | Urawa (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:07:52 | Putupaula (Kalu Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-10-17 00:06:19 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-17 01:00:12 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-10-17 01:01:17 | Peradeniya (Mahaweli Ganga) | 3.29 | 🟢 Normal | -0.010 |  |
| 2026-10-17 00:06:16 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.020 |  |
| 2026-10-17 01:00:55 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-16 18:02:38 | Galgamuwa (Mee Oya) | 2.02 | 🟢 Normal | -0.023 |  |
| 2026-10-17 01:03:52 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.029 |  |
| 2026-10-17 01:04:10 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-10-17 00:05:39 | Thawalama (Gin Ganga) | 3.45 | 🟢 Normal | -0.041 |  |
| 2026-10-17 00:09:16 | Pitabeddara (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.044 |  |
| 2026-10-17 01:04:00 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.060 |  |
| 2026-10-17 01:02:45 | Moragaswewa (Deduru Oya) | 1.90 | 🟢 Normal | -0.061 |  |
| 2026-10-17 00:08:08 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.097 |  |
| 2026-10-17 01:03:59 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.106 |  |
| 2026-10-17 01:03:23 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.108 |  |
| 2026-10-17 00:06:55 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)