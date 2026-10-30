# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_20:03:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,357 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 20:03:00 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-30 20:03:00 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 20:02:58 | Padiyathalawa (Maduru Oya) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-10-30 20:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-30 20:02:40 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 20:02:39 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-30 20:02:38 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-30 20:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | -0.040 |  |
| 2026-10-30 20:02:37 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-30 20:02:32 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-10-30 20:02:15 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-30 20:02:15 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-30 20:02:11 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-10-30 20:02:09 | Rathnapura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.030 |  |
| 2026-10-30 20:02:08 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-30 20:01:16 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | -0.042 |  |
| 2026-10-30 20:00:18 | Pitabeddara (Nilwala Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-10-30 19:31:09 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 19:31:09 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 19:02:46 | Putupaula (Kalu Ganga) | 3.18 | 🟡 Alert | -0.010 |  |
| 2026-10-30 19:12:09 | Panadugama (Nilwala Ganga) | 5.16 | 🟡 Alert | -0.018 |  |
| 2026-10-30 20:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | -0.040 |  |
| 2026-10-30 19:02:29 | Peradeniya (Mahaweli Ganga) | 3.04 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-30 19:02:43 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-30 20:02:37 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-30 19:06:43 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-30 19:00:10 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-30 20:02:38 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-30 19:14:44 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-30 19:03:20 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 20:02:15 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-30 20:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-30 20:03:00 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 19:08:27 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:07 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-30 20:02:39 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-30 19:05:20 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.000 |  |
| 2026-10-30 19:12:10 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 20:02:40 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 20:03:00 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-30 20:02:08 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-30 19:06:49 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-30 19:08:50 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-10-30 19:03:44 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-30 20:02:11 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-10-30 20:02:15 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-30 20:00:18 | Pitabeddara (Nilwala Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-10-30 19:05:18 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.011 |  |
| 2026-10-30 20:02:32 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-10-30 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.021 |  |
| 2026-10-30 19:00:32 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:00:42 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-30 20:02:09 | Rathnapura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.030 |  |
| 2026-10-30 20:01:16 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | -0.042 |  |
| 2026-10-30 20:02:58 | Padiyathalawa (Maduru Oya) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-10-30 19:05:37 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.082 |  |
| 2026-10-30 19:03:32 | Ellagawa (Kalu Ganga) | 8.32 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)