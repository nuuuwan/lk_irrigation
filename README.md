# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--15_05:38:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,213 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 05:38:20 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.034 |  |
| 2026-11-15 05:34:42 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:27:18 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.042 |  |
| 2026-11-15 05:17:20 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-15 05:11:11 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:10:49 | Moraketiya (Walawe Ganga) | 1.82 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-15 05:09:45 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:08:47 | Thanamalwila (Kirindi Oya) | 1.92 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-11-15 05:08:46 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-11-15 05:08:31 | Baddegama (Gin Ganga) | 2.89 | 🟢 Normal | -0.028 |  |
| 2026-11-15 05:07:08 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -0.018 |  |
| 2026-11-15 05:06:49 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.102 |  |
| 2026-11-15 05:06:47 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-11-15 05:06:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.019 |  |
| 2026-11-15 05:06:14 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-11-15 05:06:12 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-15 05:05:41 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.029 |  |
| 2026-11-15 05:05:37 | Panadugama (Nilwala Ganga) | 4.92 | 🟢 Normal | -0.070 |  |
| 2026-11-15 05:05:19 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 05:03:44 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.020 |  |
| 2026-11-15 05:03:13 | Hanwella (Kelani Ganga) | 2.54 | 🟢 Normal | -0.032 |  |
| 2026-11-15 05:03:09 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-11-15 05:02:58 | Thalgahagoda (Nilwala Ganga) | 1.88 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-15 05:02:56 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:02:49 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.010 |  |
| 2026-11-15 05:02:37 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:01:48 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:01:46 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.005 |  |
| 2026-11-15 05:01:42 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:01:37 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:01:33 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:01:30 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 05:01:08 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-11-15 05:01:05 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 04:59:51 | Thalgahagoda (Nilwala Ganga) | 1.88 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 05:02:58 | Thalgahagoda (Nilwala Ganga) | 1.88 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-15 05:08:47 | Thanamalwila (Kirindi Oya) | 1.92 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-11-15 05:06:12 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-15 05:01:30 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 18:01:52 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 05:17:20 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-15 05:10:49 | Moraketiya (Walawe Ganga) | 1.82 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-15 05:05:19 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 05:01:37 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:01:05 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:02:37 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:01:42 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:01:33 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:04:59 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:08:54 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:11:11 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:01:48 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:34:42 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:02:56 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-15 04:13:18 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:09:45 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-15 05:01:46 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.005 |  |
| 2026-11-15 05:02:49 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.010 |  |
| 2026-11-15 05:06:14 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-11-15 05:03:09 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-11-15 05:01:08 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:00:25 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-11-15 05:07:08 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -0.018 |  |
| 2026-11-15 05:06:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.019 |  |
| 2026-11-15 05:06:47 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-11-15 05:03:44 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.020 |  |
| 2026-11-15 05:08:31 | Baddegama (Gin Ganga) | 2.89 | 🟢 Normal | -0.028 |  |
| 2026-11-15 05:05:41 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.029 |  |
| 2026-11-15 05:03:13 | Hanwella (Kelani Ganga) | 2.54 | 🟢 Normal | -0.032 |  |
| 2026-11-15 05:38:20 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.034 |  |
| 2026-11-15 05:27:18 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.042 |  |
| 2026-11-15 04:12:19 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.044 |  |
| 2026-11-15 05:05:37 | Panadugama (Nilwala Ganga) | 4.92 | 🟢 Normal | -0.070 |  |
| 2026-11-15 05:06:49 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)