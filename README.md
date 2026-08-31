# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_15:11:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **248,155 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 15:11:57 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.048 |  |
| 2026-08-31 15:11:17 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:10:34 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:08:34 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:07:52 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-08-31 15:07:44 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:07:39 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:07:00 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.049 |  |
| 2026-08-31 15:06:52 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-31 15:06:20 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:06:07 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:05:49 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-08-31 15:05:27 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-31 15:04:53 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.022 |  |
| 2026-08-31 15:04:13 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:03:21 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.010 |  |
| 2026-08-31 15:03:09 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 15:03:03 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-31 15:03:01 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-08-31 15:02:49 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:02:34 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:02:32 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:02:29 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-08-31 15:02:13 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-08-31 15:02:08 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:01:53 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.055 |  |
| 2026-08-31 15:01:51 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:01:41 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:01:36 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:01:29 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:01:28 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:01:26 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-08-31 15:01:23 | Manampitiya (Mahaweli Ganga) | -0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:01:02 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:00:23 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:00:17 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-31 15:00:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.037 |  |
| 2026-08-31 15:00:14 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 15:02:13 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-08-31 14:14:43 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-08-31 15:00:17 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-31 15:05:27 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-31 15:06:52 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-31 15:03:03 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-31 15:03:09 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 15:01:51 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:00:23 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:00:14 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:02:32 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:01:29 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:06:07 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:07:39 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:08:34 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:07:44 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:10:34 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:01:41 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:02:49 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:06:20 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:01:28 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:02:08 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:02:34 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:01:23 | Manampitiya (Mahaweli Ganga) | -0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:04:13 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:01:36 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:11:17 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-31 15:05:49 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-08-31 15:03:01 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-08-31 15:01:26 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-08-31 15:02:29 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-08-31 15:03:21 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.010 |  |
| 2026-08-31 15:07:52 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-08-31 15:04:53 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.022 |  |
| 2026-08-31 15:00:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.037 |  |
| 2026-08-31 15:11:57 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.048 |  |
| 2026-08-31 15:07:00 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.049 |  |
| 2026-08-31 15:01:53 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.055 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)