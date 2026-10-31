# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_05:36:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,690 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 05:36:43 | Pitabeddara (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.012 |  |
| 2026-10-31 05:29:11 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-31 05:13:16 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:12:03 | Panadugama (Nilwala Ganga) | 4.96 | 🟢 Normal | -0.029 |  |
| 2026-10-31 05:07:48 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.039 |  |
| 2026-10-31 05:06:46 | Baddegama (Gin Ganga) | 2.80 | 🟢 Normal | -54.000 |  |
| 2026-10-31 05:06:44 | Baddegama (Gin Ganga) | 2.83 | 🟢 Normal | -54.000 |  |
| 2026-10-31 05:06:18 | Urawa (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-31 05:06:18 | Rathnapura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-10-31 05:05:49 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:05:37 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.039 |  |
| 2026-10-31 05:05:35 | Putupaula (Kalu Ganga) | 2.78 | 🟢 Normal | -0.067 |  |
| 2026-10-31 05:05:24 | Hanwella (Kelani Ganga) | 2.78 | 🟢 Normal | -6.968 |  |
| 2026-10-31 05:05:19 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-31 05:04:53 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -6.968 |  |
| 2026-10-31 05:04:38 | Ellagawa (Kalu Ganga) | 7.23 | 🟢 Normal | -0.146 |  |
| 2026-10-31 05:04:35 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.041 |  |
| 2026-10-31 05:04:13 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-31 05:03:50 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.020 |  |
| 2026-10-31 05:03:46 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:03:25 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:03:23 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:03:22 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:03:14 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.030 |  |
| 2026-10-31 05:02:50 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:02:13 | Thanamalwila (Kirindi Oya) | 1.56 | 🟢 Normal | -0.040 |  |
| 2026-10-31 05:02:10 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.021 |  |
| 2026-10-31 05:02:05 | Padiyathalawa (Maduru Oya) | 1.11 | 🟢 Normal | -0.043 |  |
| 2026-10-31 05:01:43 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-10-31 05:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:01:02 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-31 05:00:53 | Magura (Kalu Ganga) | 2.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-31 05:00:52 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-31 05:00:42 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 05:00:52 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-31 03:05:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | -3.130 |  |
| 2026-10-31 05:29:11 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-31 05:05:19 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-31 05:04:13 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-31 05:00:53 | Magura (Kalu Ganga) | 2.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-31 04:00:56 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:03:25 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:03:46 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:02:50 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:07 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:03:23 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 03:10:35 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:03:22 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:05:49 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:13:16 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:01:10 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-31 05:06:18 | Urawa (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-31 05:06:18 | Rathnapura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-10-31 05:01:02 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-31 05:01:43 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-10-31 05:36:43 | Pitabeddara (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.012 |  |
| 2026-10-31 05:03:50 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.020 |  |
| 2026-10-30 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.021 |  |
| 2026-10-31 05:02:10 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:00:42 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-31 05:12:03 | Panadugama (Nilwala Ganga) | 4.96 | 🟢 Normal | -0.029 |  |
| 2026-10-31 05:03:14 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.030 |  |
| 2026-10-31 05:07:48 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.039 |  |
| 2026-10-31 05:05:37 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.039 |  |
| 2026-10-31 05:02:13 | Thanamalwila (Kirindi Oya) | 1.56 | 🟢 Normal | -0.040 |  |
| 2026-10-31 05:04:35 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.041 |  |
| 2026-10-31 05:00:42 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.041 |  |
| 2026-10-31 05:02:05 | Padiyathalawa (Maduru Oya) | 1.11 | 🟢 Normal | -0.043 |  |
| 2026-10-31 05:05:35 | Putupaula (Kalu Ganga) | 2.78 | 🟢 Normal | -0.067 |  |
| 2026-10-31 05:04:38 | Ellagawa (Kalu Ganga) | 7.23 | 🟢 Normal | -0.146 |  |
| 2026-10-31 05:05:24 | Hanwella (Kelani Ganga) | 2.78 | 🟢 Normal | -6.968 |  |
| 2026-10-31 05:06:46 | Baddegama (Gin Ganga) | 2.80 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)