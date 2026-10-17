# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_17:08:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,542 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kithulgala — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 17:08:26 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.028 |  |
| 2026-10-17 17:08:22 | Baddegama (Gin Ganga) | 3.31 | 🟢 Normal | -0.033 |  |
| 2026-10-17 17:07:31 | Thawalama (Gin Ganga) | 2.53 | 🟢 Normal | -0.064 |  |
| 2026-10-17 17:07:18 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 17:07:03 | Rathnapura (Kalu Ganga) | 2.88 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-10-17 17:05:39 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.020 |  |
| 2026-10-17 17:05:39 | Kithulgala (Kelani Ganga) | 3.07 | 🟡 Alert | 0.839 | 🔺 Rising |
| 2026-10-17 17:05:22 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-10-17 17:05:18 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-17 17:05:06 | Urawa (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-10-17 17:05:03 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | -0.058 |  |
| 2026-10-17 17:04:33 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.531 | 🔺 Rising |
| 2026-10-17 17:04:28 | Dunamale (Aththanagalu Oya) | 2.85 | 🟢 Normal | -0.039 |  |
| 2026-10-17 17:04:24 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-17 17:04:14 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-10-17 17:04:14 | Deraniyagala (Kelani Ganga) | 2.28 | 🟢 Normal | 1.504 | 🔺 Rising |
| 2026-10-17 17:03:50 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | -0.063 |  |
| 2026-10-17 17:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.60 | 🟡 Alert | -108.000 |  |
| 2026-10-17 17:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.63 | 🟡 Alert | -108.000 |  |
| 2026-10-17 17:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.63 | 🟡 Alert | -108.000 |  |
| 2026-10-17 17:03:18 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | -0.061 |  |
| 2026-10-17 17:03:18 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-10-17 17:02:26 | Horowpothana (Yan Oya) | 2.56 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-17 17:02:20 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 17:02:17 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -36.000 |  |
| 2026-10-17 17:02:15 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | -36.000 |  |
| 2026-10-17 17:02:12 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -36.000 |  |
| 2026-10-17 17:02:10 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -36.000 |  |
| 2026-10-17 17:02:10 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-10-17 17:01:57 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-17 17:01:45 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.012 |  |
| 2026-10-17 17:01:41 | Thanthirimale (Malwathu Oya) | 2.45 | 🟢 Normal | -0.041 |  |
| 2026-10-17 17:01:22 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-10-17 17:00:30 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-17 17:00:18 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-17 17:00:09 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-17 17:00:07 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 17:00:07 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 17:08:26 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.028 |  |
| 2026-10-17 17:05:39 | Kithulgala (Kelani Ganga) | 3.07 | 🟡 Alert | 0.839 | 🔺 Rising |
| 2026-10-17 17:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.60 | 🟡 Alert | -108.000 |  |
| 2026-10-17 17:04:14 | Deraniyagala (Kelani Ganga) | 2.28 | 🟢 Normal | 1.504 | 🔺 Rising |
| 2026-10-17 17:04:33 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.531 | 🔺 Rising |
| 2026-10-17 17:05:06 | Urawa (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-10-17 17:02:10 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-10-17 17:07:03 | Rathnapura (Kalu Ganga) | 2.88 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-10-17 17:05:22 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-10-17 17:02:26 | Horowpothana (Yan Oya) | 2.56 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-17 17:04:24 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-17 17:07:18 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 17:00:18 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-17 17:02:20 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 16:02:02 | Pitabeddara (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-10-17 17:00:30 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-17 17:05:18 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-17 16:04:10 | Putupaula (Kalu Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-10-17 17:01:57 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-17 17:00:09 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-17 17:01:45 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.012 |  |
| 2026-10-17 17:04:14 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-10-17 17:05:39 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.020 |  |
| 2026-10-17 17:01:22 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-10-17 17:03:18 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-10-17 17:08:22 | Baddegama (Gin Ganga) | 3.31 | 🟢 Normal | -0.033 |  |
| 2026-10-17 15:04:20 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | -0.039 |  |
| 2026-10-17 17:04:28 | Dunamale (Aththanagalu Oya) | 2.85 | 🟢 Normal | -0.039 |  |
| 2026-10-17 16:05:41 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.040 |  |
| 2026-10-17 17:01:41 | Thanthirimale (Malwathu Oya) | 2.45 | 🟢 Normal | -0.041 |  |
| 2026-10-17 15:01:44 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | -0.045 |  |
| 2026-10-17 16:01:22 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.054 |  |
| 2026-10-17 17:05:03 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | -0.058 |  |
| 2026-10-17 17:03:18 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | -0.061 |  |
| 2026-10-17 17:03:50 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | -0.063 |  |
| 2026-10-17 17:07:31 | Thawalama (Gin Ganga) | 2.53 | 🟢 Normal | -0.064 |  |
| 2026-10-17 17:02:17 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -36.000 |  |
| 2026-10-17 13:09:01 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -50.400 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)