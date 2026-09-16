# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_16:23:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,592 measurements** from **39** stations.
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
| 2026-09-16 16:23:04 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:18:45 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-16 16:12:01 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-09-16 16:10:56 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:10:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.75 | 🟢 Normal | -0.045 |  |
| 2026-09-16 16:10:02 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-09-16 16:08:23 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-16 16:06:44 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:06:24 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-09-16 16:06:22 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-16 16:06:22 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-16 16:06:05 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-09-16 16:05:51 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:05:02 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | -0.079 |  |
| 2026-09-16 16:04:46 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:03:52 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-16 16:03:36 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | -0.081 |  |
| 2026-09-16 16:03:31 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-09-16 16:03:30 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:03:30 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.057 |  |
| 2026-09-16 16:03:10 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:03:02 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | -0.059 |  |
| 2026-09-16 16:02:50 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:02:42 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:02:35 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-09-16 16:02:28 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:02:16 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:02:09 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-16 16:02:02 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.010 |  |
| 2026-09-16 16:02:02 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-16 16:01:51 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-09-16 16:01:44 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:01:29 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.064 |  |
| 2026-09-16 16:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:01:11 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:01:10 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-09-16 16:01:02 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | -0.026 |  |
| 2026-09-16 16:00:51 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:00:37 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 16:10:02 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-09-16 16:01:51 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-09-16 16:02:09 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-16 16:02:02 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-16 16:06:22 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-16 16:18:45 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-16 16:08:23 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-16 16:03:52 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-16 16:06:22 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-16 16:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:01:44 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:04:46 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:00:51 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:02:42 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:02:16 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:02:50 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:06:44 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:01:11 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:02:28 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:03:10 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:10:56 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:05:51 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:23:04 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-16 15:05:13 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-16 16:12:01 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-09-16 16:02:02 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.010 |  |
| 2026-09-16 16:01:10 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-09-16 16:00:37 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-16 16:06:05 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-09-16 16:06:24 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-09-16 16:02:35 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-09-16 16:03:31 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-09-16 16:01:02 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | -0.026 |  |
| 2026-09-16 16:10:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.75 | 🟢 Normal | -0.045 |  |
| 2026-09-16 16:03:30 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.057 |  |
| 2026-09-16 16:03:02 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | -0.059 |  |
| 2026-09-16 16:01:29 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.064 |  |
| 2026-09-16 16:05:02 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | -0.079 |  |
| 2026-09-16 16:03:36 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)