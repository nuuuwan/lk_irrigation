# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--16_22:29:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,756 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 22:29:18 | Thalgahagoda (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:24:05 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:18:42 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.017 |  |
| 2026-11-16 22:16:50 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-11-16 22:16:19 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:15:48 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.035 |  |
| 2026-11-16 22:10:06 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:08:44 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:07:24 | Hanwella (Kelani Ganga) | 2.09 | 🟢 Normal | -0.019 |  |
| 2026-11-16 22:07:01 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2026-11-16 22:06:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | -0.024 |  |
| 2026-11-16 22:06:04 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:05:33 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-16 22:05:05 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-11-16 22:04:53 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | -0.050 |  |
| 2026-11-16 22:04:45 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-16 22:04:43 | Panadugama (Nilwala Ganga) | 4.23 | 🟢 Normal | -0.031 |  |
| 2026-11-16 22:03:58 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 22:03:53 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:03:37 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-11-16 22:03:36 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-11-16 22:03:20 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:03:16 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:03:10 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:03:07 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:02:53 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.050 |  |
| 2026-11-16 22:02:43 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-11-16 22:02:17 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:02:17 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:01:58 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-11-16 22:01:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | -0.030 |  |
| 2026-11-16 22:01:43 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:01:02 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:00:43 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 22:05:05 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-11-16 22:05:33 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-16 22:03:58 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 22:00:43 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:24:05 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:01:02 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-16 18:04:42 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:10:06 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:16:19 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:03:10 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:02:17 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:03:20 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:01:43 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:03:16 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-16 21:00:49 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:02:17 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:03:53 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:06:04 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-16 18:00:40 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:08:44 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:29:18 | Thalgahagoda (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:03:07 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:16:50 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-11-16 22:04:45 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-16 22:02:43 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-11-16 22:03:36 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-11-16 22:18:42 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.017 |  |
| 2026-11-16 22:07:24 | Hanwella (Kelani Ganga) | 2.09 | 🟢 Normal | -0.019 |  |
| 2026-11-16 22:03:37 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-11-16 22:06:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | -0.024 |  |
| 2026-11-16 22:01:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | -0.030 |  |
| 2026-11-16 22:01:58 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-11-16 22:04:43 | Panadugama (Nilwala Ganga) | 4.23 | 🟢 Normal | -0.031 |  |
| 2026-11-16 22:15:48 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.035 |  |
| 2026-11-16 21:03:00 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.039 |  |
| 2026-11-16 18:02:17 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | -0.041 |  |
| 2026-11-16 22:02:53 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.050 |  |
| 2026-11-16 22:04:53 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | -0.050 |  |
| 2026-11-16 22:07:01 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)