# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_17:24:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,034 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 17:24:06 | Thawalama (Gin Ganga) | 2.44 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-08 17:15:34 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-08 17:12:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.034 |  |
| 2026-08-08 17:10:30 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:10:04 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-08-08 17:10:01 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:08:48 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.009 |  |
| 2026-08-08 17:08:30 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-08 17:06:43 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-08 17:06:28 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 1.636 | 🔺 Rising |
| 2026-08-08 17:06:22 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.028 |  |
| 2026-08-08 17:06:06 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 1.636 | 🔺 Rising |
| 2026-08-08 17:05:47 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:04:44 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.079 |  |
| 2026-08-08 17:04:43 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:04:43 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:04:39 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:04:37 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:04:36 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.040 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 17:06:28 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 1.636 | 🔺 Rising |
| 2026-08-08 17:03:10 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-08-08 17:10:04 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-08-08 17:02:47 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-08-08 17:08:30 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-08 17:03:41 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-08 17:04:36 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-08 17:06:43 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-08 17:24:06 | Thawalama (Gin Ganga) | 2.44 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-08 16:03:23 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-08 17:03:51 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-08 17:15:34 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-08 17:01:51 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:04:37 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:04:39 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:03:22 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:10:30 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:00:38 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:04:26 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:02:48 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:02:03 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:01:47 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:02:36 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:04:43 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:03:27 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:03:51 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:05:47 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:10:01 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:01:04 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:04:43 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:00:36 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-08 17:08:48 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.009 |  |
| 2026-08-08 17:01:16 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.010 |  |
| 2026-08-08 17:01:23 | Peradeniya (Mahaweli Ganga) | 3.68 | 🟢 Normal | -0.020 |  |
| 2026-08-08 17:02:51 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-08-08 17:04:01 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | -0.020 |  |
| 2026-08-08 17:06:22 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.028 |  |
| 2026-08-08 17:12:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.034 |  |
| 2026-08-08 17:04:44 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)