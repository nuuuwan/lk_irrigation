# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_22:08:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,446 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 22:08:09 | Thaldena (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.221 |  |
| 2026-10-20 22:06:50 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-10-20 22:06:38 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-20 22:05:33 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.024 |  |
| 2026-10-20 22:04:45 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:03:58 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-20 22:03:54 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-10-20 22:03:53 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:03:53 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-10-20 22:03:50 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | -0.029 |  |
| 2026-10-20 22:03:27 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:03:23 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 22:03:12 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:03:02 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-20 22:02:55 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:02:40 | Panadugama (Nilwala Ganga) | 4.32 | 🟢 Normal | -0.020 |  |
| 2026-10-20 22:02:18 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 22:02:13 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:02:03 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:01:42 | Moragaswewa (Deduru Oya) | 1.70 | 🟢 Normal | 0.641 | 🔺 Rising |
| 2026-10-20 22:01:34 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-20 22:01:32 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 22:01:24 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-10-20 22:01:21 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | -0.040 |  |
| 2026-10-20 22:01:14 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-20 22:01:10 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-20 22:00:06 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.051 |  |
| 2026-10-20 21:36:21 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.330 |  |
| 2026-10-20 21:34:32 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.330 |  |
| 2026-10-20 21:27:57 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.330 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 21:02:31 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | -0.023 |  |
| 2026-10-20 18:02:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-10-20 22:01:42 | Moragaswewa (Deduru Oya) | 1.70 | 🟢 Normal | 0.641 | 🔺 Rising |
| 2026-10-20 22:06:50 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-10-20 22:06:38 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-20 22:03:02 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-20 22:01:14 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-20 22:03:58 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-20 22:03:23 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 22:01:32 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 18:04:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 22:02:18 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 21:03:16 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:02:55 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:03:12 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:03:53 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:02:03 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:03:27 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:04:45 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:12:00 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:02:13 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:01:34 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-20 21:04:36 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-20 22:01:10 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-20 22:01:24 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-10-20 21:15:15 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | -0.017 |  |
| 2026-10-20 21:08:25 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.019 |  |
| 2026-10-20 22:03:54 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-10-20 22:03:53 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-10-20 22:02:40 | Panadugama (Nilwala Ganga) | 4.32 | 🟢 Normal | -0.020 |  |
| 2026-10-20 22:05:33 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.024 |  |
| 2026-10-20 22:03:50 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | -0.029 |  |
| 2026-10-20 22:01:21 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | -0.040 |  |
| 2026-10-20 22:00:06 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.051 |  |
| 2026-10-20 21:02:42 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.178 |  |
| 2026-10-20 22:08:09 | Thaldena (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.221 |  |
| 2026-10-20 21:36:21 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.330 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)