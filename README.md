# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_21:33:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,909 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Peradeniya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **1** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 21:33:11 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 21:03:59 | Peradeniya (Mahaweli Ganga) | 5.90 | 🟡 Alert | -0.335 |  |
| 2026-08-05 21:03:03 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-05 21:03:17 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-05 21:08:34 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 21:07:09 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-05 21:06:15 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:11:01 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 21:02:11 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-08-05 21:04:17 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 21:09:07 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-08-05 21:06:22 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 21:00:32 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-05 21:03:25 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-05 21:01:30 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-05 21:03:43 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 21:33:11 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:09:25 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-05 21:02:22 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-05 21:01:25 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 21:05:55 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 21:04:14 | Putupaula (Kalu Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-08-05 21:06:04 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-08-05 21:02:31 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-08-05 21:01:24 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-08-05 21:02:50 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-08-05 21:03:38 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.011 |  |
| 2026-08-05 21:01:36 | Nawalapitiya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.020 |  |
| 2026-08-05 20:02:42 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-08-05 21:04:28 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-08-05 21:05:15 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.022 |  |
| 2026-08-05 21:02:41 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.023 |  |
| 2026-08-05 21:03:24 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.029 |  |
| 2026-08-05 21:02:11 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.032 |  |
| 2026-08-05 20:10:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.045 |  |
| 2026-08-05 21:04:10 | Glencourse (Kelani Ganga) | 11.87 | 🟢 Normal | -0.059 |  |
| 2026-08-05 21:02:48 | Hanwella (Kelani Ganga) | 3.94 | 🟢 Normal | -0.061 |  |
| 2026-08-05 21:05:46 | Rathnapura (Kalu Ganga) | 3.63 | 🟢 Normal | -0.118 |  |
| 2026-08-05 21:02:06 | Kithulgala (Kelani Ganga) | 2.50 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)