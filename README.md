# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--10_09:07:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **256,925 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-10 09:07:58 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-10 09:07:42 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-09-10 09:06:47 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:06:39 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:06:32 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-10 09:06:20 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-09-10 09:06:19 | Glencourse (Kelani Ganga) | 9.14 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-10 09:05:52 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:05:52 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.062 |  |
| 2026-09-10 09:05:49 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-09-10 09:04:20 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.005 |  |
| 2026-09-10 09:04:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.071 |  |
| 2026-09-10 09:04:06 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.060 |  |
| 2026-09-10 09:03:38 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.098 |  |
| 2026-09-10 09:03:30 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:03:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-10 09:02:36 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.010 |  |
| 2026-09-10 09:02:33 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:02:33 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-09-10 09:02:33 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-09-10 09:02:14 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-09-10 09:02:13 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:02:07 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:02:06 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-09-10 09:01:52 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:01:44 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-10 09:01:44 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:01:42 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:01:41 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:01:20 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-09-10 09:01:18 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:01:11 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 09:01:02 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:00:58 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.118 |  |
| 2026-09-10 09:00:19 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-10 09:01:20 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-09-10 09:03:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-10 08:01:42 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-10 09:06:19 | Glencourse (Kelani Ganga) | 9.14 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-10 09:02:33 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-09-10 09:06:32 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-10 09:01:11 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 09:04:20 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.005 |  |
| 2026-09-10 08:07:11 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:01:41 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:00:19 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:03:30 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:05:52 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:02:13 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:06:39 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:01:44 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 08:09:15 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:01:18 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:01:02 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:01:52 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:02:07 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:02:33 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:06:47 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:01:42 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:01:44 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-10 09:07:58 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-10 09:02:36 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.010 |  |
| 2026-09-10 09:02:06 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-09-10 09:06:20 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-09-10 09:07:42 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-09-10 09:05:49 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-09-10 09:02:14 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-09-10 09:02:33 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-09-10 09:04:06 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.060 |  |
| 2026-09-10 09:05:52 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.062 |  |
| 2026-09-10 09:04:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.071 |  |
| 2026-09-10 09:03:38 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.098 |  |
| 2026-09-10 09:00:58 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)