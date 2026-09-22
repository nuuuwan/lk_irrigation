# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_21:05:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,170 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 21:05:37 | Peradeniya (Mahaweli Ganga) | 3.48 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-22 21:04:56 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-22 21:04:35 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.021 |  |
| 2026-09-22 21:04:33 | Hanwella (Kelani Ganga) | 4.51 | 🟢 Normal | -0.021 |  |
| 2026-09-22 21:04:21 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-09-22 21:04:11 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:03:33 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:03:09 | Nawalapitiya (Mahaweli Ganga) | 2.39 | 🟢 Normal | -0.113 |  |
| 2026-09-22 21:02:59 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:02:28 | Magura (Kalu Ganga) | 4.58 | 🟡 Alert | -0.029 |  |
| 2026-09-22 21:02:27 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:02:17 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:02:14 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-22 21:02:06 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.15 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-22 21:01:25 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:01:17 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-09-22 21:01:13 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:00:34 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:00:23 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 20:08:59 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 21:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.15 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-22 20:01:02 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.000 |  |
| 2026-09-22 21:02:28 | Magura (Kalu Ganga) | 4.58 | 🟡 Alert | -0.029 |  |
| 2026-09-22 21:05:37 | Peradeniya (Mahaweli Ganga) | 3.48 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-22 21:04:56 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-22 20:11:11 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-22 21:02:14 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-22 20:05:58 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:00:23 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:02:17 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:01:25 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:04:56 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:04:11 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:02:27 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:02:06 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:03:33 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:07:44 | Putupaula (Kalu Ganga) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:00:34 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:01:13 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:02:59 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-22 21:04:21 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:02:46 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-22 20:04:19 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-22 20:04:52 | Glencourse (Kelani Ganga) | 12.40 | 🟢 Normal | -0.010 |  |
| 2026-09-22 21:01:17 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-09-22 20:04:33 | Deraniyagala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-09-22 20:05:26 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-09-22 21:04:33 | Hanwella (Kelani Ganga) | 4.51 | 🟢 Normal | -0.021 |  |
| 2026-09-22 21:04:35 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.021 |  |
| 2026-09-22 20:08:39 | Panadugama (Nilwala Ganga) | 4.77 | 🟢 Normal | -0.022 |  |
| 2026-09-22 20:07:45 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | -0.028 |  |
| 2026-09-22 20:05:45 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.029 |  |
| 2026-09-22 20:00:36 | Thawalama (Gin Ganga) | 2.73 | 🟢 Normal | -0.029 |  |
| 2026-09-22 20:03:11 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | -0.033 |  |
| 2026-09-22 20:03:14 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.054 |  |
| 2026-09-22 21:03:09 | Nawalapitiya (Mahaweli Ganga) | 2.39 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)