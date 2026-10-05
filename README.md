# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_12:15:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,558 measurements** from **39** stations.
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
| 2026-10-05 12:15:48 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.036 |  |
| 2026-10-05 12:15:00 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:11:32 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.044 |  |
| 2026-10-05 12:08:06 | Panadugama (Nilwala Ganga) | 3.60 | 🟢 Normal | -0.088 |  |
| 2026-10-05 12:07:20 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-10-05 12:06:53 | Glencourse (Kelani Ganga) | 11.24 | 🟢 Normal | -0.089 |  |
| 2026-10-05 12:06:45 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:06:43 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.047 |  |
| 2026-10-05 12:06:16 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-10-05 12:05:52 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.040 |  |
| 2026-10-05 12:05:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.09 | 🟢 Normal | -0.086 |  |
| 2026-10-05 12:05:00 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-10-05 12:04:40 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.253 |  |
| 2026-10-05 12:04:30 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.070 |  |
| 2026-10-05 12:04:21 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.049 |  |
| 2026-10-05 12:04:19 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-05 12:04:19 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 12:04:09 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 12:04:02 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:03:48 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-05 12:03:31 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.049 |  |
| 2026-10-05 12:03:27 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.069 |  |
| 2026-10-05 12:03:20 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.061 |  |
| 2026-10-05 12:03:14 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:03:11 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-05 12:02:53 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.046 |  |
| 2026-10-05 12:02:53 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:02:44 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:02:32 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:02:30 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:02:17 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | -0.096 |  |
| 2026-10-05 12:01:58 | Dunamale (Aththanagalu Oya) | 2.35 | 🟢 Normal | -0.099 |  |
| 2026-10-05 12:01:39 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-05 12:01:36 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-10-05 12:01:33 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.010 |  |
| 2026-10-05 12:01:33 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:01:16 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:01:15 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:01:09 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:00:34 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 12:04:09 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 12:04:19 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 12:01:33 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:02:32 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:01:16 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:01:15 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:02:30 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:02:44 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:04:02 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:03:14 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:02:53 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:00:34 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:15:00 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:01:09 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 12:06:16 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-10-05 12:03:48 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-05 12:04:19 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-05 12:03:11 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-05 12:07:20 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-10-05 12:01:39 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-05 12:01:33 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.010 |  |
| 2026-10-05 12:01:36 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-10-05 12:05:00 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-10-05 12:15:48 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.036 |  |
| 2026-10-05 12:05:52 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.040 |  |
| 2026-10-05 12:11:32 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.044 |  |
| 2026-10-05 12:02:53 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.046 |  |
| 2026-10-05 12:06:43 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.047 |  |
| 2026-10-05 12:03:31 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.049 |  |
| 2026-10-05 12:04:21 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.049 |  |
| 2026-10-05 12:03:20 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.061 |  |
| 2026-10-05 12:03:27 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.069 |  |
| 2026-10-05 12:04:30 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.070 |  |
| 2026-10-05 12:05:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.09 | 🟢 Normal | -0.086 |  |
| 2026-10-05 12:08:06 | Panadugama (Nilwala Ganga) | 3.60 | 🟢 Normal | -0.088 |  |
| 2026-10-05 12:06:53 | Glencourse (Kelani Ganga) | 11.24 | 🟢 Normal | -0.089 |  |
| 2026-10-05 12:02:17 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | -0.096 |  |
| 2026-10-05 12:01:58 | Dunamale (Aththanagalu Oya) | 2.35 | 🟢 Normal | -0.099 |  |
| 2026-10-05 12:04:40 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.253 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)