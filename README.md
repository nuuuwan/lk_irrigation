# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_16:07:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,091 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 16:07:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.30 | 🟢 Normal | -0.038 |  |
| 2026-10-11 16:07:01 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.038 |  |
| 2026-10-11 16:06:35 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.116 |  |
| 2026-10-11 16:06:30 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-10-11 16:06:19 | Putupaula (Kalu Ganga) | 1.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-11 16:05:54 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.021 |  |
| 2026-10-11 16:05:35 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-11 16:05:17 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-11 16:05:08 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-10-11 16:05:07 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.092 |  |
| 2026-10-11 16:04:40 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-10-11 16:04:36 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-11 16:04:19 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-11 16:04:17 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-11 16:04:04 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-10-11 16:04:01 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | -0.064 |  |
| 2026-10-11 16:03:52 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | -0.020 |  |
| 2026-10-11 16:03:38 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.021 |  |
| 2026-10-11 16:03:31 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 16:03:06 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-10-11 16:02:48 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-11 16:02:44 | Hanwella (Kelani Ganga) | 2.77 | 🟢 Normal | -0.040 |  |
| 2026-10-11 16:02:38 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.041 |  |
| 2026-10-11 16:02:29 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 16:02:12 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | -0.062 |  |
| 2026-10-11 16:02:12 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-11 16:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-11 16:01:24 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-11 16:01:18 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | -0.012 |  |
| 2026-10-11 16:01:05 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-11 16:01:04 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-10-11 16:01:00 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 16:00:23 | Moragaswewa (Deduru Oya) | 2.36 | 🟢 Normal | -0.156 |  |
| 2026-10-11 16:00:19 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 16:06:30 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-10-11 16:04:36 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-11 16:04:19 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-11 16:02:48 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-11 16:01:24 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-11 16:06:19 | Putupaula (Kalu Ganga) | 1.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-11 16:04:17 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-11 16:05:17 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-11 16:00:19 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-11 16:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-11 16:02:29 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 16:01:00 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 16:03:31 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:05:45 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-11 16:01:05 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:07:03 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-11 16:05:08 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-10-11 16:05:35 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-11 16:04:04 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-10-11 16:02:12 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-11 16:04:40 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-10-11 16:03:06 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-10-11 16:01:04 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-10-11 16:01:18 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | -0.012 |  |
| 2026-10-11 15:06:26 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-10-11 16:03:52 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | -0.020 |  |
| 2026-10-11 16:05:54 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.021 |  |
| 2026-10-11 16:03:38 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.021 |  |
| 2026-10-11 16:07:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.30 | 🟢 Normal | -0.038 |  |
| 2026-10-11 16:07:01 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.038 |  |
| 2026-10-11 16:02:44 | Hanwella (Kelani Ganga) | 2.77 | 🟢 Normal | -0.040 |  |
| 2026-10-11 16:02:38 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.041 |  |
| 2026-10-11 15:03:44 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.057 |  |
| 2026-10-11 16:02:12 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | -0.062 |  |
| 2026-10-11 16:04:01 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | -0.064 |  |
| 2026-10-11 16:05:07 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.092 |  |
| 2026-10-11 16:06:35 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.116 |  |
| 2026-10-11 16:00:23 | Moragaswewa (Deduru Oya) | 2.36 | 🟢 Normal | -0.156 |  |
| 2026-10-11 15:06:21 | Magura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.257 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)