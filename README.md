# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_19:19:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **248,305 measurements** from **39** stations.
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
| 2026-08-31 19:19:31 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.009 |  |
| 2026-08-31 19:12:08 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.043 |  |
| 2026-08-31 19:10:28 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-31 19:09:55 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.048 |  |
| 2026-08-31 19:09:40 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-31 19:09:23 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.028 |  |
| 2026-08-31 19:08:20 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:07:04 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:06:40 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:06:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.055 |  |
| 2026-08-31 19:06:22 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | -0.028 |  |
| 2026-08-31 19:06:00 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:05:55 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 19:05:33 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:04:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:03:43 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-08-31 19:03:39 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.159 |  |
| 2026-08-31 19:03:35 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-31 19:03:33 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:03:22 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:03:03 | Manampitiya (Mahaweli Ganga) | -0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:02:59 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-08-31 19:02:49 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-31 19:02:45 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-31 19:02:36 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:02:11 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:02:11 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-31 19:02:10 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:02:03 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-08-31 19:01:52 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | -0.537 |  |
| 2026-08-31 19:01:35 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:01:11 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:01:05 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:00:45 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -0.537 |  |
| 2026-08-31 19:00:20 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 19:03:43 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-08-31 19:02:03 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-08-31 19:02:11 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-31 19:03:35 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-31 19:02:45 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-31 19:05:55 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 19:10:28 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-31 19:09:40 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-31 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:00:20 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:01:05 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:06:00 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:04:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:03:22 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:04:51 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:02:10 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:03:33 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:08:20 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:02:36 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:01:35 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:05:33 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:07:04 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:06:40 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:03:03 | Manampitiya (Mahaweli Ganga) | -0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:00:47 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:01:11 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:02:11 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-31 19:19:31 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.009 |  |
| 2026-08-31 18:06:48 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-31 19:02:49 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-31 19:02:59 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-08-31 19:09:23 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.028 |  |
| 2026-08-31 19:06:22 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | -0.028 |  |
| 2026-08-31 19:12:08 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.043 |  |
| 2026-08-31 19:09:55 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.048 |  |
| 2026-08-31 19:06:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.055 |  |
| 2026-08-31 19:03:39 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.159 |  |
| 2026-08-31 19:01:52 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | -0.537 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)