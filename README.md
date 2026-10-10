# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_09:08:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,916 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 09:08:37 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.028 |  |
| 2026-10-10 09:08:29 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:07:40 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.029 |  |
| 2026-10-10 09:07:29 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.018 |  |
| 2026-10-10 09:07:29 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-10-10 09:07:23 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-10-10 09:07:14 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:06:57 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:06:00 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | -0.029 |  |
| 2026-10-10 09:05:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | -0.057 |  |
| 2026-10-10 09:05:54 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.049 |  |
| 2026-10-10 09:05:24 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:04:42 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.021 |  |
| 2026-10-10 09:04:27 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:04:21 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -0.041 |  |
| 2026-10-10 09:03:40 | Glencourse (Kelani Ganga) | 11.27 | 🟢 Normal | -0.072 |  |
| 2026-10-10 09:03:14 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-10-10 09:03:06 | Moragaswewa (Deduru Oya) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-10-10 09:03:05 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-10 09:03:05 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.045 |  |
| 2026-10-10 09:03:03 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.080 |  |
| 2026-10-10 09:02:59 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:02:59 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.021 |  |
| 2026-10-10 09:02:58 | Hanwella (Kelani Ganga) | 3.63 | 🟢 Normal | -0.081 |  |
| 2026-10-10 09:02:54 | Urawa (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.022 |  |
| 2026-10-10 09:02:52 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:02:47 | Badalgama (Maha Oya) | 4.79 | 🟢 Normal | -0.039 |  |
| 2026-10-10 09:02:46 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-10 09:02:45 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:02:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-10 09:02:30 | Giriulla (Maha Oya) | 3.73 | 🟢 Normal | -0.120 |  |
| 2026-10-10 09:02:21 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:02:16 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-10-10 09:02:03 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-10 09:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 09:02:16 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-10-10 09:02:03 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-10 09:02:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-10 09:02:46 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-10 08:06:36 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-10 09:02:21 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:07:14 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:02:59 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:08:29 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:02:52 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:06:57 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:04:27 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:02:45 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:05:24 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:07:29 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-10-10 09:03:05 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-10 09:07:23 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-10-10 09:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-10 09:03:06 | Moragaswewa (Deduru Oya) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-10-10 09:07:29 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.018 |  |
| 2026-10-10 09:03:14 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-10-10 08:06:50 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-10-10 09:04:42 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.021 |  |
| 2026-10-10 09:02:59 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.021 |  |
| 2026-10-10 09:02:54 | Urawa (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.022 |  |
| 2026-10-10 09:08:37 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.028 |  |
| 2026-10-10 09:06:00 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | -0.029 |  |
| 2026-10-10 09:07:40 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.029 |  |
| 2026-10-10 09:02:47 | Badalgama (Maha Oya) | 4.79 | 🟢 Normal | -0.039 |  |
| 2026-10-10 09:04:21 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -0.041 |  |
| 2026-10-10 09:03:05 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.045 |  |
| 2026-10-10 09:05:54 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.049 |  |
| 2026-10-10 09:05:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | -0.057 |  |
| 2026-10-10 09:03:40 | Glencourse (Kelani Ganga) | 11.27 | 🟢 Normal | -0.072 |  |
| 2026-10-10 08:04:19 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.077 |  |
| 2026-10-10 09:03:03 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.080 |  |
| 2026-10-10 09:02:58 | Hanwella (Kelani Ganga) | 3.63 | 🟢 Normal | -0.081 |  |
| 2026-10-10 08:05:20 | Rathnapura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.116 |  |
| 2026-10-10 09:02:30 | Giriulla (Maha Oya) | 3.73 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)