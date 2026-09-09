# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_17:23:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **256,349 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 17:23:39 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.016 |  |
| 2026-09-09 17:16:01 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:15:06 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-09 17:13:08 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:11:53 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.028 |  |
| 2026-09-09 17:10:39 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:09:25 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | -0.067 |  |
| 2026-09-09 17:07:59 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.076 |  |
| 2026-09-09 17:07:50 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 17:07:40 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.029 |  |
| 2026-09-09 17:07:15 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.139 |  |
| 2026-09-09 17:06:36 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.028 |  |
| 2026-09-09 17:05:04 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:04:20 | Ellagawa (Kalu Ganga) | 4.84 | 🟢 Normal | -0.010 |  |
| 2026-09-09 17:03:58 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | -0.016 |  |
| 2026-09-09 17:03:55 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.019 |  |
| 2026-09-09 17:03:55 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:03:52 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:03:40 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:03:38 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.021 |  |
| 2026-09-09 17:03:33 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:03:23 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 17:03:05 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:03:03 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:52 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 17:02:49 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | -0.116 |  |
| 2026-09-09 17:02:27 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:25 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:12 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:11 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:11 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:10 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.060 |  |
| 2026-09-09 17:01:49 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 17:01:44 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:01:03 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.161 |  |
| 2026-09-09 17:00:26 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 17:01:49 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 17:02:52 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 17:03:23 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 17:07:50 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 17:15:06 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-09 17:02:11 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:00:26 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:49 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:57:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:03:33 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:16:01 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:05:04 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:13:08 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:03:03 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:25 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:03:05 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:03:55 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:11 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:03:40 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:27 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:01:44 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:03:52 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:10:39 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:02:12 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-09 17:04:20 | Ellagawa (Kalu Ganga) | 4.84 | 🟢 Normal | -0.010 |  |
| 2026-09-09 17:03:58 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | -0.016 |  |
| 2026-09-09 17:23:39 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.016 |  |
| 2026-09-09 17:03:55 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.019 |  |
| 2026-09-09 17:03:38 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.021 |  |
| 2026-09-09 17:11:53 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.028 |  |
| 2026-09-09 17:06:36 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.028 |  |
| 2026-09-09 17:07:40 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.029 |  |
| 2026-09-09 17:02:10 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.060 |  |
| 2026-09-09 17:09:25 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | -0.067 |  |
| 2026-09-09 17:07:59 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.076 |  |
| 2026-09-09 17:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | -0.116 |  |
| 2026-09-09 17:07:15 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.139 |  |
| 2026-09-09 17:01:03 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)