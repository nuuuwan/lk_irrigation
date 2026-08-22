# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_01:41:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **240,867 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-23 01:41:33 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.006 |  |
| 2026-08-23 01:27:42 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.025 |  |
| 2026-08-23 01:09:42 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-08-23 01:07:47 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:07:11 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-08-23 01:07:07 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:06:51 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.040 |  |
| 2026-08-23 01:06:13 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.024 |  |
| 2026-08-23 01:06:07 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-08-23 01:05:21 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-23 01:01:41 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-23 01:03:52 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-23 01:04:04 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-22 18:00:58 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:00:42 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:00:44 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:00:50 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:03:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:01:24 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-22 23:00:33 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:07:20 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:02:38 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:02:01 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:07:47 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-23 00:05:03 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-23 00:00:50 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-23 00:51:03 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-23 00:07:51 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-23 00:03:39 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:01:56 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:03:43 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:07:07 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:01:58 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:41:33 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.006 |  |
| 2026-08-23 01:03:29 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-08-23 01:06:07 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-08-23 01:03:08 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-08-23 01:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-08-23 01:05:21 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-08-23 01:09:42 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-08-23 01:07:11 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-08-23 01:06:13 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.024 |  |
| 2026-08-23 01:27:42 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.025 |  |
| 2026-08-22 22:10:54 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.034 |  |
| 2026-08-23 01:04:17 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | -0.040 |  |
| 2026-08-23 01:06:51 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.040 |  |
| 2026-08-23 01:01:11 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.064 |  |
| 2026-08-23 01:02:35 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)