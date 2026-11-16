# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--16_11:13:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,340 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 11:13:06 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | -0.029 |  |
| 2026-11-16 11:12:39 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:11:02 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-11-16 11:10:09 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -0.034 |  |
| 2026-11-16 11:08:13 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | -0.010 |  |
| 2026-11-16 11:07:53 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:07:22 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:06:52 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:06:31 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:06:29 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-11-16 11:06:08 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-11-16 11:05:56 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:05:26 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | -0.046 |  |
| 2026-11-16 11:05:01 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-11-16 11:04:58 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-11-16 11:04:56 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:04:42 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:04:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:04:16 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:03:59 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-11-16 11:03:33 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-11-16 11:03:11 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.011 |  |
| 2026-11-16 11:02:56 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 11:02:37 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 11:02:37 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-11-16 11:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-16 11:02:25 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.079 |  |
| 2026-11-16 11:02:11 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-16 11:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:02:08 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 11:02:07 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:02:06 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | -0.011 |  |
| 2026-11-16 11:02:04 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 11:01:52 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:01:48 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.032 |  |
| 2026-11-16 11:01:40 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:01:39 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-16 11:01:25 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-16 11:01:12 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:00:57 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 11:05:26 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | -0.046 |  |
| 2026-11-16 11:01:25 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-16 11:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-16 11:02:08 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 11:02:37 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 11:02:04 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 11:02:56 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 11:01:52 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:04:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:06:31 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:02:07 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:01:40 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:04:56 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:04:42 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:05:56 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:07:53 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:07:22 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:04:16 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:12:39 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:01:12 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-16 11:11:02 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-11-16 11:08:13 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | -0.010 |  |
| 2026-11-16 11:03:33 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-11-16 11:03:59 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-11-16 11:04:58 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-11-16 11:01:39 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-16 11:02:11 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-16 11:06:08 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-11-16 11:02:37 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-11-16 11:02:06 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | -0.011 |  |
| 2026-11-16 11:03:11 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.011 |  |
| 2026-11-16 11:00:57 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-11-16 11:05:01 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-11-16 11:13:06 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | -0.029 |  |
| 2026-11-16 11:06:29 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-11-16 11:01:48 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.032 |  |
| 2026-11-16 11:10:09 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -0.034 |  |
| 2026-11-16 11:02:25 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)