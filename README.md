# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_21:22:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **278,090 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **4** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 21:22:38 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.018 |  |
| 2026-10-03 21:19:42 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.052 |  |
| 2026-10-03 21:19:37 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-03 21:10:13 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 21:04:37 | Peradeniya (Mahaweli Ganga) | 3.38 | 🟢 Normal | 0.551 | 🔺 Rising |
| 2026-10-03 21:04:10 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-10-03 21:05:24 | Glencourse (Kelani Ganga) | 12.24 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-10-03 21:03:06 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-03 21:06:55 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-03 21:02:46 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-03 21:02:01 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-03 21:02:05 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 21:01:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 21:01:22 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:03:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-03 21:03:48 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-10-03 21:07:02 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-03 21:06:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 21:04:44 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-03 21:10:13 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-03 21:04:26 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-03 21:05:44 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:02:29 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-03 21:19:37 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-03 21:06:51 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-03 21:01:15 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-03 21:01:51 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-10-03 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-03 21:04:50 | Manampitiya (Mahaweli Ganga) | -0.39 | 🟢 Normal | -0.010 |  |
| 2026-10-03 21:02:24 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-10-03 21:02:49 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.011 |  |
| 2026-10-03 21:22:38 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.018 |  |
| 2026-10-03 21:04:42 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-10-03 21:03:01 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-10-03 21:08:22 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.021 |  |
| 2026-10-03 21:03:02 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.022 |  |
| 2026-10-03 21:04:22 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.031 |  |
| 2026-10-03 21:01:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.035 |  |
| 2026-10-03 21:02:02 | Ellagawa (Kalu Ganga) | 5.81 | 🟢 Normal | -0.041 |  |
| 2026-10-03 21:19:42 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.052 |  |
| 2026-10-03 21:02:57 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.060 |  |
| 2026-10-03 21:07:50 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.081 |  |
| 2026-10-03 21:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)