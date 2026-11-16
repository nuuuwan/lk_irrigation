# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--16_16:24:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,536 measurements** from **39** stations.
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
| 2026-11-16 16:24:16 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:15:53 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.009 |  |
| 2026-11-16 16:14:23 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.005 |  |
| 2026-11-16 16:13:18 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-16 16:13:10 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-11-16 16:10:49 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.017 |  |
| 2026-11-16 16:10:45 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | -0.010 |  |
| 2026-11-16 16:08:56 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-11-16 16:08:34 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:08:20 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.055 |  |
| 2026-11-16 16:07:26 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-16 16:06:53 | Thalgahagoda (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.018 |  |
| 2026-11-16 16:06:42 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-11-16 16:06:05 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:05:12 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:04:50 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:04:09 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-16 16:03:34 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-16 16:03:33 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.021 |  |
| 2026-11-16 16:03:26 | Hanwella (Kelani Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-11-16 16:03:11 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:02:48 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | -0.030 |  |
| 2026-11-16 16:02:37 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:02:26 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 16:02:20 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:02:20 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-11-16 16:02:13 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:02:10 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 16:02:08 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:02:05 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-16 16:02:05 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:02:04 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-16 16:01:49 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-16 16:01:39 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-11-16 16:01:25 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-16 16:01:01 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:00:38 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 16:01:25 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-16 16:07:26 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-16 16:13:18 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-16 16:03:34 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-16 16:01:49 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-16 16:02:26 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 16:02:10 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 16:02:13 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:02:20 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:02:37 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:00:38 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:02:48 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:06:05 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:01:01 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:24:16 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:05:12 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:03:11 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:04:50 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:02:04 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:08:34 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:02:08 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:02:05 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-16 16:14:23 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.005 |  |
| 2026-11-16 16:15:53 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.009 |  |
| 2026-11-16 16:13:10 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-11-16 16:08:56 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-11-16 16:10:45 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | -0.010 |  |
| 2026-11-16 16:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-16 16:06:42 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-11-16 16:02:05 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-16 16:01:39 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-11-16 16:02:20 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-11-16 16:04:09 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-16 16:10:49 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.017 |  |
| 2026-11-16 16:06:53 | Thalgahagoda (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.018 |  |
| 2026-11-16 16:03:26 | Hanwella (Kelani Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-11-16 16:03:33 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.021 |  |
| 2026-11-16 16:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | -0.030 |  |
| 2026-11-16 16:08:20 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.055 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)