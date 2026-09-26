# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_22:06:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,837 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 22:06:46 | Baddegama (Gin Ganga) | 4.80 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 22:06:31 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-26 22:05:58 | Glencourse (Kelani Ganga) | 12.71 | 🟢 Normal | -0.097 |  |
| 2026-09-26 22:05:52 | Thawalama (Gin Ganga) | 3.05 | 🟢 Normal | -0.049 |  |
| 2026-09-26 22:04:49 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | -0.019 |  |
| 2026-09-26 22:04:34 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-09-26 22:04:17 | Hanwella (Kelani Ganga) | 5.13 | 🟢 Normal | -0.060 |  |
| 2026-09-26 22:04:12 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:03:56 | Nawalapitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | -0.019 |  |
| 2026-09-26 22:03:18 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:02:36 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:02:36 | Kithulgala (Kelani Ganga) | 2.63 | 🟢 Normal | -0.021 |  |
| 2026-09-26 22:02:35 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:02:15 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-09-26 22:02:14 | Peradeniya (Mahaweli Ganga) | 3.49 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-09-26 22:02:13 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:02:08 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-26 22:02:07 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-09-26 22:01:35 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:01:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.85 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 22:01:24 | Ellagawa (Kalu Ganga) | 8.85 | 🟢 Normal | -0.010 |  |
| 2026-09-26 22:01:18 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:01:17 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:01:11 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:01:05 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-26 22:00:52 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 21:04:52 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 22:01:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.85 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 22:06:46 | Baddegama (Gin Ganga) | 4.80 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 21:03:40 | Panadugama (Nilwala Ganga) | 5.80 | 🟡 Alert | -0.020 |  |
| 2026-09-26 22:02:14 | Peradeniya (Mahaweli Ganga) | 3.49 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-09-26 22:06:31 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-26 22:02:08 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-26 22:01:05 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-26 22:01:18 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:02:13 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 21:04:33 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:00:52 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:05:10 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-26 21:14:00 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:02:35 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-26 21:01:37 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:04:12 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:03:18 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:01:35 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:02:36 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:01:11 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-26 22:01:17 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 21:11:52 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | -0.009 |  |
| 2026-09-26 22:02:07 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-09-26 21:04:23 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-09-26 22:01:24 | Ellagawa (Kalu Ganga) | 8.85 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:02:21 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-26 22:04:49 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | -0.019 |  |
| 2026-09-26 22:03:56 | Nawalapitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | -0.019 |  |
| 2026-09-26 22:02:15 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-09-26 22:04:34 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-09-26 22:02:36 | Kithulgala (Kelani Ganga) | 2.63 | 🟢 Normal | -0.021 |  |
| 2026-09-26 21:05:19 | Magura (Kalu Ganga) | 3.51 | 🟢 Normal | -0.034 |  |
| 2026-09-26 22:05:52 | Thawalama (Gin Ganga) | 3.05 | 🟢 Normal | -0.049 |  |
| 2026-09-26 22:04:17 | Hanwella (Kelani Ganga) | 5.13 | 🟢 Normal | -0.060 |  |
| 2026-09-26 21:08:29 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.068 |  |
| 2026-09-26 21:05:45 | Rathnapura (Kalu Ganga) | 4.69 | 🟢 Normal | -0.072 |  |
| 2026-09-26 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.089 |  |
| 2026-09-26 22:05:58 | Glencourse (Kelani Ganga) | 12.71 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)