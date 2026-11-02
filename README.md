# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_10:03:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,686 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 10:03:22 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.070 |  |
| 2026-11-02 10:03:11 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.079 |  |
| 2026-11-02 10:03:03 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.039 |  |
| 2026-11-02 10:02:54 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.040 |  |
| 2026-11-02 10:02:53 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-02 10:02:52 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:02:47 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 10:02:37 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:02:30 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.041 |  |
| 2026-11-02 10:02:23 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.041 |  |
| 2026-11-02 10:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:02:00 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:01:46 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.039 |  |
| 2026-11-02 10:01:43 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:01:35 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:01:28 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 10:01:10 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 10:01:08 | Panadugama (Nilwala Ganga) | 4.61 | 🟢 Normal | -0.012 |  |
| 2026-11-02 10:00:54 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:00:25 | Weraganthota (Mahaweli Ganga) | -2.34 | 🟢 Normal | 0.632 | 🔺 Rising |
| 2026-11-02 10:00:08 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 09:03:56 | Thalgahagoda (Nilwala Ganga) | 1.41 | 🟡 Alert | 0.000 |  |
| 2026-11-02 10:00:25 | Weraganthota (Mahaweli Ganga) | -2.34 | 🟢 Normal | 0.632 | 🔺 Rising |
| 2026-11-02 09:02:49 | Ellagawa (Kalu Ganga) | 6.17 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-02 09:01:58 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-02 10:01:28 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 10:02:47 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 10:01:10 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 09:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:01:43 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:09:14 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:06:38 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-11-02 08:14:18 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:02:52 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:01:35 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:04:58 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:04:47 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:00:54 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:02:00 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:01:10 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:02:37 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:04:22 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:04:02 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-02 10:02:53 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-02 09:02:28 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-02 09:02:12 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-11-02 10:01:08 | Panadugama (Nilwala Ganga) | 4.61 | 🟢 Normal | -0.012 |  |
| 2026-11-02 10:00:08 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.021 |  |
| 2026-11-02 10:03:03 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.039 |  |
| 2026-11-02 10:01:46 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.039 |  |
| 2026-11-02 10:02:54 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.040 |  |
| 2026-11-02 10:02:23 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.041 |  |
| 2026-11-02 10:02:30 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.041 |  |
| 2026-11-02 10:03:22 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.070 |  |
| 2026-11-02 09:04:44 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.072 |  |
| 2026-11-02 10:03:11 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.079 |  |
| 2026-11-02 09:02:38 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.107 |  |
| 2026-11-02 09:05:19 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | -0.107 |  |
| 2026-11-02 09:03:13 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.267 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)