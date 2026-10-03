# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_16:08:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,892 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 16:08:55 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-10-03 16:08:00 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | -0.021 |  |
| 2026-10-03 16:07:09 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-03 16:07:01 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | -0.056 |  |
| 2026-10-03 16:06:27 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-03 16:05:25 | Ellagawa (Kalu Ganga) | 6.08 | 🟢 Normal | -0.077 |  |
| 2026-10-03 16:05:12 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.009 |  |
| 2026-10-03 16:05:08 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:05:05 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:04:50 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-10-03 16:04:36 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:04:31 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-03 16:04:28 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-03 16:04:08 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 16:04:06 | Hanwella (Kelani Ganga) | 2.14 | 🟢 Normal | -0.049 |  |
| 2026-10-03 16:03:54 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:03:50 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-10-03 16:03:42 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:02:42 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-03 16:02:33 | Manampitiya (Mahaweli Ganga) | -0.31 | 🟢 Normal | -0.020 |  |
| 2026-10-03 16:02:30 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.042 |  |
| 2026-10-03 16:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.040 |  |
| 2026-10-03 16:02:22 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:02:18 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-10-03 16:02:16 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-03 16:02:06 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-03 16:01:49 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.021 |  |
| 2026-10-03 16:01:37 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.054 |  |
| 2026-10-03 16:01:35 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:01:34 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | -0.010 |  |
| 2026-10-03 16:01:14 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:00:57 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:00:08 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 16:06:27 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-03 16:04:28 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-03 16:02:42 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-03 16:02:06 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-03 16:04:08 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 16:07:09 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-03 16:02:22 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 15:01:22 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:01:35 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 15:00:10 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:04:36 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-03 15:24:52 | Panadugama (Nilwala Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:01:14 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:05:08 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:03:42 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:05:05 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:00:57 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:03:54 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-03 16:08:55 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-10-03 16:05:12 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.009 |  |
| 2026-10-03 16:02:16 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-03 16:04:50 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-10-03 16:00:08 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-10-03 16:01:34 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | -0.010 |  |
| 2026-10-03 16:04:31 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-03 15:01:48 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-10-03 16:02:18 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-10-03 15:11:33 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-10-03 16:02:33 | Manampitiya (Mahaweli Ganga) | -0.31 | 🟢 Normal | -0.020 |  |
| 2026-10-03 16:01:49 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.021 |  |
| 2026-10-03 15:01:54 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.021 |  |
| 2026-10-03 16:08:00 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | -0.021 |  |
| 2026-10-03 16:03:50 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-10-03 16:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.040 |  |
| 2026-10-03 16:02:30 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.042 |  |
| 2026-10-03 16:04:06 | Hanwella (Kelani Ganga) | 2.14 | 🟢 Normal | -0.049 |  |
| 2026-10-03 16:01:37 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.054 |  |
| 2026-10-03 16:07:01 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | -0.056 |  |
| 2026-10-03 16:05:25 | Ellagawa (Kalu Ganga) | 6.08 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)