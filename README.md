# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_18:13:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,305 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 18:13:45 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:12:47 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | -0.042 |  |
| 2026-10-20 18:09:41 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:07:57 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-10-20 18:07:09 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | -0.028 |  |
| 2026-10-20 18:04:56 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 18:04:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 18:04:26 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-10-20 18:04:09 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:03:56 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 18:03:42 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-10-20 18:03:27 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-20 18:03:16 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-10-20 18:03:15 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.012 |  |
| 2026-10-20 18:03:03 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | -0.040 |  |
| 2026-10-20 18:02:59 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-20 18:02:52 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-10-20 18:02:47 | Panadugama (Nilwala Ganga) | 4.42 | 🟢 Normal | -0.048 |  |
| 2026-10-20 18:02:47 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-20 18:02:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-10-20 18:02:35 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-10-20 18:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:02:12 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:02:10 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:02:09 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:02:02 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.321 | 🔺 Rising |
| 2026-10-20 18:01:55 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-20 18:01:52 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.040 |  |
| 2026-10-20 18:01:51 | Glencourse (Kelani Ganga) | 10.64 | 🟢 Normal | -0.052 |  |
| 2026-10-20 18:01:50 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | -0.010 |  |
| 2026-10-20 18:01:36 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:33 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | -0.030 |  |
| 2026-10-20 18:01:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:22 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:20 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.011 |  |
| 2026-10-20 18:01:07 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-10-20 18:01:03 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:00:33 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:00:09 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.044 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 18:01:50 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | -0.010 |  |
| 2026-10-20 18:02:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-10-20 18:02:02 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.321 | 🔺 Rising |
| 2026-10-20 18:03:16 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-10-20 18:02:59 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-20 18:01:55 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-20 18:03:27 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-20 18:04:56 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 18:04:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 18:03:56 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 18:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:36 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:02:09 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:13:45 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:04:09 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:02:12 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:22 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:00:33 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:02:10 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:09:41 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-10-20 17:09:39 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-10-20 18:07:57 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-10-20 18:02:47 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-20 18:01:07 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-10-20 18:03:42 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-10-20 18:02:52 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-10-20 18:01:20 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.011 |  |
| 2026-10-20 18:03:15 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.012 |  |
| 2026-10-20 18:04:26 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-10-20 18:07:09 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | -0.028 |  |
| 2026-10-20 18:01:33 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | -0.030 |  |
| 2026-10-20 18:03:03 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | -0.040 |  |
| 2026-10-20 18:01:52 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.040 |  |
| 2026-10-20 18:12:47 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | -0.042 |  |
| 2026-10-20 18:00:09 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.044 |  |
| 2026-10-20 18:02:47 | Panadugama (Nilwala Ganga) | 4.42 | 🟢 Normal | -0.048 |  |
| 2026-10-20 18:01:51 | Glencourse (Kelani Ganga) | 10.64 | 🟢 Normal | -0.052 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)