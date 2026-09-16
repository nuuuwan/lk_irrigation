# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_15:12:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,552 measurements** from **39** stations.
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
| 2026-09-16 15:12:16 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:09:46 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.019 |  |
| 2026-09-16 15:09:14 | Baddegama (Gin Ganga) | 3.05 | 🟢 Normal | -0.010 |  |
| 2026-09-16 15:08:29 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:08:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-16 15:06:06 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:05:48 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:05:13 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:05:05 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.050 |  |
| 2026-09-16 15:05:02 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:04:55 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:04:47 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-16 15:04:41 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.071 |  |
| 2026-09-16 15:04:37 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 15:04:34 | Glencourse (Kelani Ganga) | 9.59 | 🟢 Normal | -0.040 |  |
| 2026-09-16 15:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.062 |  |
| 2026-09-16 15:03:24 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-09-16 15:03:22 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 15:02:55 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:02:43 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.041 |  |
| 2026-09-16 15:02:27 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.051 |  |
| 2026-09-16 15:02:19 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:02:18 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-09-16 15:02:17 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:02:09 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 15:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-09-16 15:02:08 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | -0.070 |  |
| 2026-09-16 15:02:07 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-09-16 15:01:59 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.400 | 🔺 Rising |
| 2026-09-16 15:01:49 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-09-16 15:01:24 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-09-16 15:01:23 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-16 15:01:18 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.062 |  |
| 2026-09-16 15:01:16 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:00:43 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-09-16 15:00:40 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:00:32 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 15:00:18 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 15:01:59 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.400 | 🔺 Rising |
| 2026-09-16 15:01:24 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-09-16 15:08:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-16 15:01:23 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-16 15:04:47 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-16 15:00:32 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 15:03:22 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 15:02:09 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 15:04:37 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 15:12:16 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:00:18 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:00:40 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:08:29 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:02:55 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:05:48 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:06:06 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:02:17 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:02:19 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:04:55 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:05:02 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:01:16 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-16 14:00:44 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:05:13 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:09:14 | Baddegama (Gin Ganga) | 3.05 | 🟢 Normal | -0.010 |  |
| 2026-09-16 15:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-09-16 15:00:43 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-09-16 15:02:07 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-09-16 15:02:18 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-09-16 15:01:49 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-09-16 15:09:46 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.019 |  |
| 2026-09-16 15:03:24 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-09-16 15:04:34 | Glencourse (Kelani Ganga) | 9.59 | 🟢 Normal | -0.040 |  |
| 2026-09-16 15:02:43 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.041 |  |
| 2026-09-16 15:05:05 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.050 |  |
| 2026-09-16 15:02:27 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.051 |  |
| 2026-09-16 15:01:18 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.062 |  |
| 2026-09-16 15:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.062 |  |
| 2026-09-16 15:02:08 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | -0.070 |  |
| 2026-09-16 15:04:41 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)