# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_12:22:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,937 measurements** from **39** stations.
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
| 2026-10-11 12:22:08 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:10:34 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | -0.038 |  |
| 2026-10-11 12:10:28 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:09:33 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | -0.018 |  |
| 2026-10-11 12:09:19 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:08:18 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.029 |  |
| 2026-10-11 12:08:09 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:06:52 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.021 |  |
| 2026-10-11 12:06:37 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.131 |  |
| 2026-10-11 12:06:34 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:06:04 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.060 |  |
| 2026-10-11 12:05:11 | Hanwella (Kelani Ganga) | 2.89 | 🟢 Normal | -0.020 |  |
| 2026-10-11 12:04:45 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-10-11 12:04:38 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | -0.011 |  |
| 2026-10-11 12:04:36 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:04:27 | Giriulla (Maha Oya) | 2.49 | 🟢 Normal | -0.086 |  |
| 2026-10-11 12:04:25 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-10-11 12:04:21 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-10-11 12:03:40 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:03:35 | Dunamale (Aththanagalu Oya) | 2.84 | 🟢 Normal | -0.089 |  |
| 2026-10-11 12:03:30 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:03:19 | Badalgama (Maha Oya) | 3.73 | 🟢 Normal | -0.072 |  |
| 2026-10-11 12:03:14 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-10-11 12:03:12 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:03:07 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-11 12:03:07 | Ellagawa (Kalu Ganga) | 6.56 | 🟢 Normal | -0.020 |  |
| 2026-10-11 12:03:05 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.049 |  |
| 2026-10-11 12:02:49 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.074 |  |
| 2026-10-11 12:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.43 | 🟢 Normal | -0.020 |  |
| 2026-10-11 12:02:38 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.039 |  |
| 2026-10-11 12:02:28 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-10-11 12:02:14 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-10-11 12:01:58 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:01:50 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.060 |  |
| 2026-10-11 12:01:40 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:01:33 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:01:22 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.050 |  |
| 2026-10-11 12:01:14 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-11 12:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-11 12:00:39 | Moragaswewa (Deduru Oya) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 12:04:45 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-10-11 12:01:14 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-11 12:00:39 | Moragaswewa (Deduru Oya) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-11 12:01:40 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:04:36 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:03:30 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:08:09 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:03:12 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:06:34 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:01:33 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:03:40 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:01:58 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:22:08 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:10:28 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-11 12:03:07 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-11 12:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-11 12:02:28 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-10-11 12:04:38 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | -0.011 |  |
| 2026-10-11 12:09:33 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | -0.018 |  |
| 2026-10-11 12:05:11 | Hanwella (Kelani Ganga) | 2.89 | 🟢 Normal | -0.020 |  |
| 2026-10-11 12:02:14 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-10-11 12:03:07 | Ellagawa (Kalu Ganga) | 6.56 | 🟢 Normal | -0.020 |  |
| 2026-10-11 12:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.43 | 🟢 Normal | -0.020 |  |
| 2026-10-11 12:06:52 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.021 |  |
| 2026-10-11 12:04:21 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-10-11 12:08:18 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.029 |  |
| 2026-10-11 12:03:14 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-10-11 12:10:34 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | -0.038 |  |
| 2026-10-11 12:02:38 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.039 |  |
| 2026-10-11 12:04:25 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-10-11 12:03:05 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.049 |  |
| 2026-10-11 12:01:22 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.050 |  |
| 2026-10-11 12:01:50 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.060 |  |
| 2026-10-11 12:06:04 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.060 |  |
| 2026-10-11 12:03:19 | Badalgama (Maha Oya) | 3.73 | 🟢 Normal | -0.072 |  |
| 2026-10-11 12:02:49 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.074 |  |
| 2026-10-11 12:04:27 | Giriulla (Maha Oya) | 2.49 | 🟢 Normal | -0.086 |  |
| 2026-10-11 12:03:35 | Dunamale (Aththanagalu Oya) | 2.84 | 🟢 Normal | -0.089 |  |
| 2026-10-11 12:06:37 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)