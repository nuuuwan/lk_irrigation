# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_13:18:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,209 measurements** from **39** stations.
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
| 2026-08-24 13:18:18 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-24 13:17:22 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.008 |  |
| 2026-08-24 13:11:47 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-08-24 13:09:33 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:09:03 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:07:48 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:06:55 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.028 |  |
| 2026-08-24 13:06:19 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:05:59 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-08-24 13:05:48 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:05:40 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:05:16 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:05:16 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:05:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-08-24 13:04:47 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | -0.010 |  |
| 2026-08-24 13:04:41 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 13:04:39 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.115 |  |
| 2026-08-24 13:03:51 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-24 13:03:41 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-08-24 13:03:24 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:02:52 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-24 13:02:26 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-08-24 13:02:15 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:02:12 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:02:08 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:02:02 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:02:01 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.041 |  |
| 2026-08-24 13:01:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:01:32 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:01:23 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:01:22 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | -0.013 |  |
| 2026-08-24 13:01:13 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-08-24 13:01:00 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:00:59 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:00:53 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:00:52 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-24 13:00:48 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-08-24 13:00:07 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 13:00:48 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-08-24 13:03:51 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-24 13:18:18 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-24 12:02:35 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-24 13:00:52 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-24 13:04:41 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 13:02:02 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:02:15 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:01:23 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:02:12 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:07:48 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:00:59 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:01:32 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:09:33 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:00:07 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:01:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:00:53 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:09:03 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:03:24 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:02:08 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:06:19 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:05:16 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:05:40 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:05:16 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:05:48 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:01:00 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 13:17:22 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.008 |  |
| 2026-08-24 13:05:59 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-08-24 13:04:47 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | -0.010 |  |
| 2026-08-24 13:11:47 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-08-24 13:02:26 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-08-24 13:03:41 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-08-24 13:02:52 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-24 13:01:13 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-08-24 13:01:22 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | -0.013 |  |
| 2026-08-24 13:06:55 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.028 |  |
| 2026-08-24 13:05:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-08-24 13:02:01 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.041 |  |
| 2026-08-24 13:04:39 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.115 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)