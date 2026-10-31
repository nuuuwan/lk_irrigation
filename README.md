# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_16:18:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,123 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 16:18:25 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.017 |  |
| 2026-10-31 16:13:54 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:12:14 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:11:06 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:10:57 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.009 |  |
| 2026-10-31 16:08:46 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:06:57 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:06:48 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:06:35 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | -0.029 |  |
| 2026-10-31 16:06:23 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | -0.009 |  |
| 2026-10-31 16:06:18 | Galgamuwa (Mee Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:05:56 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.019 |  |
| 2026-10-31 16:05:05 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.051 |  |
| 2026-10-31 16:04:59 | Putupaula (Kalu Ganga) | 1.96 | 🟢 Normal | -0.041 |  |
| 2026-10-31 16:04:50 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:04:42 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.029 |  |
| 2026-10-31 16:04:41 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:04:39 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-31 16:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.61 | 🟢 Normal | -0.088 |  |
| 2026-10-31 16:04:06 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.031 |  |
| 2026-10-31 16:03:58 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:03:27 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | -0.059 |  |
| 2026-10-31 16:03:26 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:03:23 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-10-31 16:03:10 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | -0.036 |  |
| 2026-10-31 16:02:52 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-31 16:02:52 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | -0.081 |  |
| 2026-10-31 16:02:48 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:02:43 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | -0.011 |  |
| 2026-10-31 16:02:32 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-10-31 16:02:23 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-31 16:02:16 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:02:12 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:01:31 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-31 16:01:24 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-10-31 16:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-31 16:00:17 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:00:08 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:59:04 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 16:02:43 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | -0.011 |  |
| 2026-10-31 16:01:31 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-31 16:02:23 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-31 16:02:52 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-31 16:00:17 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:03:26 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:06:57 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:04:41 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:06:18 | Galgamuwa (Mee Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:02:48 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:13:54 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:02:16 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:03:58 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:08:46 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:06:48 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:11:06 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:12:14 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:02:12 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:04:50 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:10:57 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.009 |  |
| 2026-10-31 16:06:23 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | -0.009 |  |
| 2026-10-31 16:04:39 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-31 16:03:23 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-10-31 16:02:32 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:01:29 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-31 16:00:08 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-31 16:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-31 16:18:25 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.017 |  |
| 2026-10-31 16:05:56 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.019 |  |
| 2026-10-31 16:01:24 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-10-31 16:04:42 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.029 |  |
| 2026-10-31 16:06:35 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | -0.029 |  |
| 2026-10-31 16:04:06 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.031 |  |
| 2026-10-31 16:03:10 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | -0.036 |  |
| 2026-10-31 16:04:59 | Putupaula (Kalu Ganga) | 1.96 | 🟢 Normal | -0.041 |  |
| 2026-10-31 16:05:05 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.051 |  |
| 2026-10-31 16:03:27 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | -0.059 |  |
| 2026-10-31 16:02:52 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | -0.081 |  |
| 2026-10-31 16:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.61 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)