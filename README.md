# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_19:03:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,586 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 19:03:21 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | 0.470 | 🔺 Rising |
| 2026-10-17 19:03:13 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-10-17 19:02:56 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-17 19:02:54 | Baddegama (Gin Ganga) | 3.25 | 🟢 Normal | -0.030 |  |
| 2026-10-17 19:02:42 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.040 |  |
| 2026-10-17 19:02:12 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-17 19:01:29 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-10-17 19:00:56 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-10-17 19:00:54 | Nawalapitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-17 19:00:08 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 18:07:32 | Panadugama (Nilwala Ganga) | 6.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 18:12:41 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 18:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.57 | 🟡 Alert | -0.030 |  |
| 2026-10-17 18:04:33 | Rathnapura (Kalu Ganga) | 4.30 | 🟢 Normal | 1.482 | 🔺 Rising |
| 2026-10-17 18:06:17 | Deraniyagala (Kelani Ganga) | 2.95 | 🟢 Normal | 0.648 | 🔺 Rising |
| 2026-10-17 19:03:21 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | 0.470 | 🔺 Rising |
| 2026-10-17 18:05:03 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-17 18:05:55 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-10-17 18:04:11 | Pitabeddara (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-17 18:08:39 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-17 17:02:26 | Horowpothana (Yan Oya) | 2.56 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-17 17:04:24 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-17 19:00:54 | Nawalapitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-17 18:11:52 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-17 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-17 18:01:03 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-17 17:02:20 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 19:00:08 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-17 19:03:13 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-10-17 19:02:12 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-17 19:02:56 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-17 19:00:56 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-10-17 18:06:58 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.020 |  |
| 2026-10-17 19:01:29 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-10-17 19:02:54 | Baddegama (Gin Ganga) | 3.25 | 🟢 Normal | -0.030 |  |
| 2026-10-17 18:04:46 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-10-17 18:01:51 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.031 |  |
| 2026-10-17 15:04:20 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | -0.039 |  |
| 2026-10-17 18:01:56 | Thanthirimale (Malwathu Oya) | 2.41 | 🟢 Normal | -0.040 |  |
| 2026-10-17 19:02:42 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.040 |  |
| 2026-10-17 15:01:44 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | -0.045 |  |
| 2026-10-17 18:01:39 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.051 |  |
| 2026-10-17 18:04:12 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | -0.053 |  |
| 2026-10-17 16:01:22 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.054 |  |
| 2026-10-17 18:04:06 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.059 |  |
| 2026-10-17 18:03:26 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | -0.151 |  |
| 2026-10-17 18:06:22 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | -0.771 |  |
| 2026-10-17 18:01:22 | Putupaula (Kalu Ganga) | 2.10 | 🟢 Normal | -1.161 |  |
| 2026-10-17 13:09:01 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -50.400 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)