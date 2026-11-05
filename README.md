# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_17:27:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,691 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 17:27:48 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.030 |  |
| 2026-11-05 17:17:33 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-11-05 17:17:16 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-05 17:13:55 | Thalgahagoda (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-11-05 17:13:13 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:11:30 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-11-05 17:09:54 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:09:54 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.125 |  |
| 2026-11-05 17:08:59 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-11-05 17:08:46 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | -0.066 |  |
| 2026-11-05 17:08:12 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:07:56 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:07:37 | Dunamale (Aththanagalu Oya) | 2.47 | 🟢 Normal | -0.055 |  |
| 2026-11-05 17:07:00 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 17:06:30 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-05 17:06:05 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-05 17:06:04 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-11-05 17:06:02 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | -0.038 |  |
| 2026-11-05 17:05:48 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.012 |  |
| 2026-11-05 17:05:34 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:05:29 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 17:04:33 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 17:04:22 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | -0.039 |  |
| 2026-11-05 17:04:01 | Moragaswewa (Deduru Oya) | 3.33 | 🟢 Normal | -0.051 |  |
| 2026-11-05 17:03:54 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.029 |  |
| 2026-11-05 17:03:46 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:03:42 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:03:16 | Giriulla (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:03:13 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-05 17:03:05 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 17:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.98 | 🟢 Normal | -0.060 |  |
| 2026-11-05 17:02:52 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-05 17:02:28 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.005 |  |
| 2026-11-05 17:02:25 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-05 17:02:13 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-05 17:01:24 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-11-05 17:01:21 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.081 |  |
| 2026-11-05 17:00:47 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:00:44 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:00:41 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 17:11:30 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-11-05 17:06:04 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-11-05 17:03:13 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-05 17:17:16 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-05 17:02:25 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-05 17:06:30 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-05 17:06:05 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-05 17:05:29 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 17:03:05 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 17:04:33 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 17:07:00 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 17:00:44 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:02:13 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:05:34 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:03:16 | Giriulla (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:03:42 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:07:56 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:00:41 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:03:46 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:09:54 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:13:13 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:02:28 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.005 |  |
| 2026-11-05 17:17:33 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-11-05 17:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-05 17:02:52 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-05 17:05:48 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.012 |  |
| 2026-11-05 17:13:55 | Thalgahagoda (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-11-05 17:03:54 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.029 |  |
| 2026-11-05 17:01:24 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-11-05 17:27:48 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.030 |  |
| 2026-11-05 17:06:02 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | -0.038 |  |
| 2026-11-05 17:04:22 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | -0.039 |  |
| 2026-11-05 17:04:01 | Moragaswewa (Deduru Oya) | 3.33 | 🟢 Normal | -0.051 |  |
| 2026-11-05 17:07:37 | Dunamale (Aththanagalu Oya) | 2.47 | 🟢 Normal | -0.055 |  |
| 2026-11-05 17:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.98 | 🟢 Normal | -0.060 |  |
| 2026-11-05 17:08:59 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-11-05 17:08:46 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | -0.066 |  |
| 2026-11-05 17:01:21 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.081 |  |
| 2026-11-05 17:09:54 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)