# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--16_14:14:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,453 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 14:14:10 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:11:33 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.044 |  |
| 2026-11-16 14:09:53 | Thalgahagoda (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-11-16 14:09:43 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.152 |  |
| 2026-11-16 14:09:15 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-16 14:07:33 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:07:17 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-11-16 14:07:04 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:06:54 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-16 14:06:47 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:06:27 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.010 |  |
| 2026-11-16 14:04:59 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:04:54 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 14:04:30 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:04:14 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:03:25 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | -0.021 |  |
| 2026-11-16 14:03:23 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:03:18 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-16 14:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.87 | 🟢 Normal | -0.040 |  |
| 2026-11-16 14:02:51 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.011 |  |
| 2026-11-16 14:02:41 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-16 14:02:28 | Hanwella (Kelani Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-11-16 14:02:19 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-16 14:02:16 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:02:07 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-11-16 14:02:00 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-11-16 14:01:45 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:01:39 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:01:28 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:01:26 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:01:19 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:01:13 | Ellagawa (Kalu Ganga) | 5.31 | 🟢 Normal | -0.010 |  |
| 2026-11-16 14:01:10 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:01:04 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 14:06:54 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-16 14:09:15 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-16 14:04:54 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 14:01:45 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:01:39 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:02:16 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:04:14 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:01:04 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:01:19 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:02:41 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:07:33 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:03:23 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:04:59 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:07:04 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:06:47 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:01:10 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:21:52 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:01:26 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:14:10 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:04:30 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:01:28 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:12:37 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.008 |  |
| 2026-11-16 14:07:17 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-11-16 14:03:18 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-16 14:02:19 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-16 14:02:07 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-11-16 14:02:28 | Hanwella (Kelani Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-11-16 14:01:13 | Ellagawa (Kalu Ganga) | 5.31 | 🟢 Normal | -0.010 |  |
| 2026-11-16 13:00:27 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-16 14:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-16 14:06:27 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.010 |  |
| 2026-11-16 14:02:51 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.011 |  |
| 2026-11-16 14:09:53 | Thalgahagoda (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-11-16 13:09:48 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | -0.019 |  |
| 2026-11-16 14:02:00 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-11-16 14:03:25 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | -0.021 |  |
| 2026-11-16 14:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.87 | 🟢 Normal | -0.040 |  |
| 2026-11-16 14:11:33 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.044 |  |
| 2026-11-16 14:09:43 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)