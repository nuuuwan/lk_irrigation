# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_10:20:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,609 measurements** from **39** stations.
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
| 2026-11-22 10:20:21 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-22 10:16:55 | Giriulla (Maha Oya) | 1.87 | 🟢 Normal | -0.025 |  |
| 2026-11-22 10:15:22 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:14:10 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | -0.031 |  |
| 2026-11-22 10:09:02 | Moragaswewa (Deduru Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:07:49 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.098 |  |
| 2026-11-22 10:07:16 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.027 |  |
| 2026-11-22 10:07:11 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:06:53 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-22 10:06:47 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.075 |  |
| 2026-11-22 10:06:30 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:06:17 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | -0.029 |  |
| 2026-11-22 10:06:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-22 10:05:45 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:05:37 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.009 |  |
| 2026-11-22 10:05:22 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:05:19 | Moragaswewa (Deduru Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:05:16 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:05:15 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.049 |  |
| 2026-11-22 10:04:54 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-22 10:04:14 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:04:09 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.080 |  |
| 2026-11-22 10:03:28 | Rathnapura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.106 |  |
| 2026-11-22 10:03:07 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:55 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:54 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:34 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:32 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-22 10:02:22 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.021 |  |
| 2026-11-22 10:02:14 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:04 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.029 |  |
| 2026-11-22 10:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:01:49 | Manampitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.835 | 🔺 Rising |
| 2026-11-22 10:01:43 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:01:05 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:00:10 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:00:09 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 10:01:49 | Manampitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.835 | 🔺 Rising |
| 2026-11-22 10:02:32 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-22 10:06:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-22 10:04:54 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-22 10:06:53 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-22 10:20:21 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-22 10:00:10 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:07:11 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:05:45 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:09:02 | Moragaswewa (Deduru Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:01:43 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:01:05 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:00:09 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:15:22 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:05:16 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:04:14 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:08:16 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-11-22 10:05:37 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.009 |  |
| 2026-11-22 10:05:22 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:34 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:54 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:03:07 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:55 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:14 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:22 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:06:30 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.021 |  |
| 2026-11-22 10:16:55 | Giriulla (Maha Oya) | 1.87 | 🟢 Normal | -0.025 |  |
| 2026-11-22 10:07:16 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.027 |  |
| 2026-11-22 10:06:17 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | -0.029 |  |
| 2026-11-22 10:02:04 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.029 |  |
| 2026-11-22 10:14:10 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | -0.031 |  |
| 2026-11-22 10:05:15 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.049 |  |
| 2026-11-22 10:06:47 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.075 |  |
| 2026-11-22 10:04:09 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.080 |  |
| 2026-11-22 10:07:49 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.098 |  |
| 2026-11-22 10:03:28 | Rathnapura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)