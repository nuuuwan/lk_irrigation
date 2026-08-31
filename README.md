# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_09:12:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **247,912 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 09:12:46 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | -0.019 |  |
| 2026-08-31 09:12:40 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.035 |  |
| 2026-08-31 09:10:02 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:07:36 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-08-31 09:07:23 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-08-31 09:07:06 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:06:08 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-31 09:05:46 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:05:42 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-31 09:05:11 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:05:02 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 09:04:59 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.061 |  |
| 2026-08-31 09:04:36 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.084 |  |
| 2026-08-31 09:04:33 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:04:06 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 09:03:40 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:03:12 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.021 |  |
| 2026-08-31 09:03:05 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-08-31 09:03:03 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.100 |  |
| 2026-08-31 09:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.218 |  |
| 2026-08-31 09:03:01 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:02:57 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-08-31 09:02:46 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:02:39 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:02:34 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-31 09:02:33 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.084 |  |
| 2026-08-31 09:02:02 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-31 09:02:02 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:01:53 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:01:48 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-08-31 09:01:45 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:01:41 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:01:39 | Ellagawa (Kalu Ganga) | 4.81 | 🟢 Normal | -0.010 |  |
| 2026-08-31 09:01:25 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:01:02 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:00:56 | Manampitiya (Mahaweli Ganga) | -0.49 | 🟢 Normal | -0.021 |  |
| 2026-08-31 09:00:42 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:00:37 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:00:14 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 09:02:02 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-31 09:02:34 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-31 09:05:42 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-31 09:06:08 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-31 09:04:06 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 09:05:02 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 09:02:39 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:00:37 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:01:02 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:02:02 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:03:01 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:01:45 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:02:46 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:10:02 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:05:46 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:04:33 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:01:41 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:03:40 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:05:11 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:07:06 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:01:25 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:01:53 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 09:02:57 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-08-31 09:07:23 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-08-31 09:03:05 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-08-31 09:01:39 | Ellagawa (Kalu Ganga) | 4.81 | 🟢 Normal | -0.010 |  |
| 2026-08-31 09:01:48 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-08-31 09:07:36 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-08-31 09:12:46 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | -0.019 |  |
| 2026-08-31 09:03:12 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.021 |  |
| 2026-08-31 09:00:56 | Manampitiya (Mahaweli Ganga) | -0.49 | 🟢 Normal | -0.021 |  |
| 2026-08-31 09:00:14 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.030 |  |
| 2026-08-31 09:12:40 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.035 |  |
| 2026-08-31 09:04:59 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.061 |  |
| 2026-08-31 09:02:33 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.084 |  |
| 2026-08-31 09:04:36 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.084 |  |
| 2026-08-31 09:03:03 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.100 |  |
| 2026-08-31 09:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.218 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)