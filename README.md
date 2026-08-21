# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_09:19:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **239,355 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 09:19:49 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:11:17 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:08:35 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:07:49 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:07:31 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-21 09:06:45 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:06:15 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-08-21 09:06:14 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-08-21 09:05:50 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | -0.031 |  |
| 2026-08-21 09:05:39 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:05:21 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:05:21 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.046 |  |
| 2026-08-21 09:04:33 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:04:27 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:04:09 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:03:55 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-08-21 09:03:39 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-21 09:03:37 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 09:03:09 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:02:59 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:02:58 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-08-21 09:02:52 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:02:49 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.19 | 🟢 Normal | -0.010 |  |
| 2026-08-21 09:02:46 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:02:43 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.042 |  |
| 2026-08-21 09:02:41 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:02:26 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 09:02:26 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-08-21 09:01:52 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-21 09:01:43 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:01:37 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.016 |  |
| 2026-08-21 09:01:26 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 09:01:23 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:01:20 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:01:07 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | -0.051 |  |
| 2026-08-21 09:00:58 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:00:30 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-08-21 09:00:11 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.035 |  |
| 2026-08-21 09:00:10 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 09:03:55 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-08-21 09:03:39 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-21 09:01:52 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-21 09:00:10 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-21 09:03:37 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 09:01:26 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 09:02:26 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 09:07:31 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-21 09:02:41 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:08:35 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:01:20 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:01:23 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:03:09 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:05:21 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:02:46 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:04:09 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:11:17 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:02:49 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:01:43 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:00:58 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:02:59 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:06:45 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:05:39 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:02:52 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:19:49 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:07:49 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:04:33 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.19 | 🟢 Normal | -0.010 |  |
| 2026-08-21 09:02:26 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-08-21 09:06:15 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-08-21 09:01:37 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.016 |  |
| 2026-08-21 09:06:14 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-08-21 09:00:30 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-08-21 09:02:58 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-08-21 09:05:50 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | -0.031 |  |
| 2026-08-21 09:00:11 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.035 |  |
| 2026-08-21 09:02:43 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.042 |  |
| 2026-08-21 09:05:21 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.046 |  |
| 2026-08-21 09:01:07 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)