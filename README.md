# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_12:22:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **230,532 measurements** from **39** stations.
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
| 2026-08-11 12:22:34 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:11:32 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.027 |  |
| 2026-08-11 12:11:27 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-08-11 12:09:40 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:07:47 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-11 12:07:33 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:07:05 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-08-11 12:06:36 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.028 |  |
| 2026-08-11 12:05:29 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:05:14 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-11 12:04:48 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-08-11 12:04:48 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:04:35 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.032 |  |
| 2026-08-11 12:04:32 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:04:25 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.032 |  |
| 2026-08-11 12:03:59 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-08-11 12:03:51 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:03:51 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 20.329 | 🔺 Rising |
| 2026-08-11 12:03:25 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:03:23 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:03:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-11 12:03:01 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-08-11 12:02:49 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:02:32 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:02:30 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-11 12:02:26 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 20.329 | 🔺 Rising |
| 2026-08-11 12:02:07 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:02:01 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:01:53 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:01:40 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:01:30 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-11 12:01:29 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.025 |  |
| 2026-08-11 12:01:25 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-08-11 12:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:00:21 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:00:13 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:00:10 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:00:09 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 12:03:51 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 20.329 | 🔺 Rising |
| 2026-08-11 12:01:25 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-08-11 12:03:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-11 12:01:30 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-11 12:02:30 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-11 12:07:47 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-11 12:05:14 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-11 12:02:07 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:00:09 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:02:49 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:22:34 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:00:21 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:01:40 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:05:29 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:03:23 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:04:32 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:03:51 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:03:25 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:00:13 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:04:48 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:03:01 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:02:32 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:02:01 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:00:10 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:06:23 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:09:40 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:12:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 12:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-08-11 12:04:48 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-08-11 12:07:05 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-08-11 12:11:27 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-08-11 12:03:59 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-08-11 12:01:29 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.025 |  |
| 2026-08-11 12:11:32 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.027 |  |
| 2026-08-11 12:06:36 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.028 |  |
| 2026-08-11 12:04:25 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.032 |  |
| 2026-08-11 12:04:35 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.032 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)