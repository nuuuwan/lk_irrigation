# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_13:09:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,104 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 13:09:39 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:08:47 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.027 |  |
| 2026-10-20 13:07:09 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.009 |  |
| 2026-10-20 13:06:29 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-10-20 13:06:13 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:05:24 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-10-20 13:05:20 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.038 |  |
| 2026-10-20 13:04:53 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.020 |  |
| 2026-10-20 13:04:52 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-10-20 13:04:42 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:04:37 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:04:33 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.048 |  |
| 2026-10-20 13:04:15 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 13:04:09 | Thalgahagoda (Nilwala Ganga) | 1.66 | 🟡 Alert | -0.011 |  |
| 2026-10-20 13:04:02 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | -0.030 |  |
| 2026-10-20 13:04:00 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:03:57 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-10-20 13:03:44 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.029 |  |
| 2026-10-20 13:03:10 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:03:02 | Ellagawa (Kalu Ganga) | 6.22 | 🟢 Normal | -0.049 |  |
| 2026-10-20 13:03:00 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:02:46 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:02:45 | Hanwella (Kelani Ganga) | 2.78 | 🟢 Normal | -0.040 |  |
| 2026-10-20 13:02:43 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-10-20 13:02:27 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.050 |  |
| 2026-10-20 13:02:18 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-10-20 13:02:17 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.051 |  |
| 2026-10-20 13:02:09 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-20 13:01:33 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-20 13:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-20 13:01:23 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-20 13:01:15 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.030 |  |
| 2026-10-20 13:01:10 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:01:07 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.131 |  |
| 2026-10-20 13:00:46 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.032 |  |
| 2026-10-20 12:37:43 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 13:04:09 | Thalgahagoda (Nilwala Ganga) | 1.66 | 🟡 Alert | -0.011 |  |
| 2026-10-20 13:04:52 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-10-20 13:04:15 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 13:01:10 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:02:17 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:04:00 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:02:43 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:04:37 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:03:10 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:02:46 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:06:13 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:03:00 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:01:22 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-10-20 13:09:39 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-20 12:10:58 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-10-20 13:07:09 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.009 |  |
| 2026-10-20 13:02:43 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-10-20 13:02:18 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-10-20 13:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-20 13:01:33 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-20 13:02:09 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-20 13:03:57 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-10-20 13:06:29 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-10-20 13:01:23 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-20 12:02:59 | Panadugama (Nilwala Ganga) | 4.57 | 🟢 Normal | -0.020 |  |
| 2026-10-20 13:05:24 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-10-20 13:04:53 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.020 |  |
| 2026-10-20 13:08:47 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.027 |  |
| 2026-10-20 13:03:44 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.029 |  |
| 2026-10-20 13:04:02 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | -0.030 |  |
| 2026-10-20 13:01:15 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.030 |  |
| 2026-10-20 13:00:46 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.032 |  |
| 2026-10-20 13:05:20 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.038 |  |
| 2026-10-20 13:02:45 | Hanwella (Kelani Ganga) | 2.78 | 🟢 Normal | -0.040 |  |
| 2026-10-20 13:04:33 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.048 |  |
| 2026-10-20 13:03:02 | Ellagawa (Kalu Ganga) | 6.22 | 🟢 Normal | -0.049 |  |
| 2026-10-20 13:02:27 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.050 |  |
| 2026-10-20 13:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.051 |  |
| 2026-10-20 13:01:07 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)