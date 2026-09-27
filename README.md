# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_06:09:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,128 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 06:09:05 | Baddegama (Gin Ganga) | 4.73 | 🟠 Minor Flood | -0.018 |  |
| 2026-09-27 06:07:57 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.032 |  |
| 2026-09-27 06:07:56 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.092 |  |
| 2026-09-27 06:07:23 | Hanwella (Kelani Ganga) | 4.65 | 🟢 Normal | -0.057 |  |
| 2026-09-27 06:07:22 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.019 |  |
| 2026-09-27 06:05:02 | Magura (Kalu Ganga) | 3.05 | 🟢 Normal | -0.099 |  |
| 2026-09-27 06:04:32 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | -0.010 |  |
| 2026-09-27 06:04:31 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.001 |  |
| 2026-09-27 06:04:28 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-09-27 06:04:21 | Kithulgala (Kelani Ganga) | 2.50 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-09-27 06:04:07 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 06:04:02 | Panadugama (Nilwala Ganga) | 5.53 | 🟡 Alert | -0.041 |  |
| 2026-09-27 06:03:58 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 06:03:56 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 06:03:41 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.087 |  |
| 2026-09-27 06:03:21 | Ellagawa (Kalu Ganga) | 8.66 | 🟢 Normal | -0.029 |  |
| 2026-09-27 06:03:14 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-27 06:02:49 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-09-27 06:02:36 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 06:02:00 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 06:09:05 | Baddegama (Gin Ganga) | 4.73 | 🟠 Minor Flood | -0.018 |  |
| 2026-09-27 06:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | -0.448 |  |
| 2026-09-27 06:04:02 | Panadugama (Nilwala Ganga) | 5.53 | 🟡 Alert | -0.041 |  |
| 2026-09-27 06:04:21 | Kithulgala (Kelani Ganga) | 2.50 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-09-27 06:02:11 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-27 06:04:07 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 06:04:31 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.001 |  |
| 2026-09-27 06:01:24 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 06:00:39 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 06:02:22 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 06:03:56 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:05:10 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 06:02:49 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-09-27 06:03:58 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 06:02:19 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 06:03:14 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-27 06:02:09 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-09-27 06:04:32 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:02:21 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-27 06:01:41 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-09-27 06:02:23 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.011 |  |
| 2026-09-27 06:01:34 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.017 |  |
| 2026-09-27 06:07:22 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.019 |  |
| 2026-09-27 06:04:28 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-09-27 06:01:50 | Dunamale (Aththanagalu Oya) | 2.37 | 🟢 Normal | -0.020 |  |
| 2026-09-27 06:01:34 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-09-27 06:01:13 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.021 |  |
| 2026-09-27 06:01:29 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.021 |  |
| 2026-09-27 06:02:36 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.028 |  |
| 2026-09-27 06:03:21 | Ellagawa (Kalu Ganga) | 8.66 | 🟢 Normal | -0.029 |  |
| 2026-09-27 06:07:57 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.032 |  |
| 2026-09-27 06:02:22 | Thawalama (Gin Ganga) | 2.83 | 🟢 Normal | -0.044 |  |
| 2026-09-27 06:07:23 | Hanwella (Kelani Ganga) | 4.65 | 🟢 Normal | -0.057 |  |
| 2026-09-27 06:00:40 | Glencourse (Kelani Ganga) | 12.23 | 🟢 Normal | -0.072 |  |
| 2026-09-27 06:03:41 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.087 |  |
| 2026-09-27 06:07:56 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.092 |  |
| 2026-09-27 06:05:02 | Magura (Kalu Ganga) | 3.05 | 🟢 Normal | -0.099 |  |
| 2026-09-27 06:01:08 | Rathnapura (Kalu Ganga) | 3.93 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)