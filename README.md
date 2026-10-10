# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_08:09:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,881 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 08:09:39 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.035 |  |
| 2026-10-10 08:08:26 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-10-10 08:07:42 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-10-10 08:07:41 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:07:21 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:07:08 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:07:05 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.040 |  |
| 2026-10-10 08:06:50 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-10-10 08:06:38 | Holombuwa (Kelani Ganga) | 1.27 | 🟢 Normal | -0.033 |  |
| 2026-10-10 08:06:36 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-10 08:05:25 | Panadugama (Nilwala Ganga) | 4.49 | 🟢 Normal | -0.039 |  |
| 2026-10-10 08:05:20 | Rathnapura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.116 |  |
| 2026-10-10 08:05:16 | Moragaswewa (Deduru Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-10-10 08:05:12 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.085 |  |
| 2026-10-10 08:05:04 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:05:01 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | -0.019 |  |
| 2026-10-10 08:04:50 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-10-10 08:04:45 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-10 08:04:19 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.077 |  |
| 2026-10-10 08:04:06 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | -0.031 |  |
| 2026-10-10 08:03:54 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.028 |  |
| 2026-10-10 08:03:53 | Hanwella (Kelani Ganga) | 3.71 | 🟢 Normal | -0.091 |  |
| 2026-10-10 08:03:34 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 08:03:28 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-10-10 08:03:20 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 08:03:14 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.039 |  |
| 2026-10-10 08:03:00 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 08:02:40 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.84 | 🟢 Normal | -0.031 |  |
| 2026-10-10 08:02:29 | Giriulla (Maha Oya) | 3.85 | 🟢 Normal | -0.168 |  |
| 2026-10-10 08:02:18 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:02:00 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.021 |  |
| 2026-10-10 08:01:57 | Badalgama (Maha Oya) | 4.83 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-10 08:01:39 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | -0.012 |  |
| 2026-10-10 08:01:29 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-10-10 08:01:15 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:00:56 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:00:47 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:00:44 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-10 07:49:12 | Manampitiya (Mahaweli Ganga) | -0.33 | 🟢 Normal | 0.156 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 08:03:28 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-10-10 08:00:44 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-10 08:01:57 | Badalgama (Maha Oya) | 4.83 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-10 08:04:45 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-10 08:06:36 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-10 08:03:20 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 08:03:34 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 08:03:00 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 08:02:18 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:00:47 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:05:04 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:01:15 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:02:40 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:07:08 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:00:56 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:07:21 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:07:41 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 08:04:50 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-10-10 08:05:16 | Moragaswewa (Deduru Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-10-10 08:01:39 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | -0.012 |  |
| 2026-10-10 08:05:01 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | -0.019 |  |
| 2026-10-10 08:06:50 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-10-10 08:01:29 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-10-10 08:02:00 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.021 |  |
| 2026-10-10 08:03:54 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.028 |  |
| 2026-10-10 08:07:42 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-10-10 08:08:26 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-10-10 08:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.84 | 🟢 Normal | -0.031 |  |
| 2026-10-10 08:04:06 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | -0.031 |  |
| 2026-10-10 08:06:38 | Holombuwa (Kelani Ganga) | 1.27 | 🟢 Normal | -0.033 |  |
| 2026-10-10 08:09:39 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.035 |  |
| 2026-10-10 08:05:25 | Panadugama (Nilwala Ganga) | 4.49 | 🟢 Normal | -0.039 |  |
| 2026-10-10 08:03:14 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.039 |  |
| 2026-10-10 08:07:05 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.040 |  |
| 2026-10-10 08:04:19 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.077 |  |
| 2026-10-10 08:05:12 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.085 |  |
| 2026-10-10 08:03:53 | Hanwella (Kelani Ganga) | 3.71 | 🟢 Normal | -0.091 |  |
| 2026-10-10 08:05:20 | Rathnapura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.116 |  |
| 2026-10-10 08:02:29 | Giriulla (Maha Oya) | 3.85 | 🟢 Normal | -0.168 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)