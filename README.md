# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_23:09:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,250 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Urawa — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 23:09:13 | Baddegama (Gin Ganga) | 2.40 | 🟢 Normal | -0.020 |  |
| 2026-10-12 23:08:00 | Pitabeddara (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2026-10-12 23:06:55 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-10-12 23:06:50 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-12 23:06:48 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-10-12 23:06:33 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.064 |  |
| 2026-10-12 23:06:28 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-10-12 23:06:06 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-12 23:06:02 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-12 23:05:57 | Thawalama (Gin Ganga) | 3.39 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-10-12 23:04:42 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.029 |  |
| 2026-10-12 23:04:25 | Magura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-12 23:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.16 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-12 23:03:57 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-12 23:03:56 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-12 23:03:44 | Urawa (Nilwala Ganga) | 3.07 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-10-12 23:03:12 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.032 |  |
| 2026-10-12 23:03:12 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-12 23:03:09 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-12 23:02:33 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-12 23:02:28 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-12 23:02:14 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-12 23:02:04 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-12 23:01:56 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-12 23:01:53 | Thalgahagoda (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-12 23:01:49 | Ellagawa (Kalu Ganga) | 6.86 | 🟢 Normal | -0.020 |  |
| 2026-10-12 23:01:38 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-12 23:00:58 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | -0.011 |  |
| 2026-10-12 23:00:47 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 23:00:10 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:22:03 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.134 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 22:09:56 | Panadugama (Nilwala Ganga) | 5.61 | 🟡 Alert | 0.187 | 🔺 Rising |
| 2026-10-12 23:03:44 | Urawa (Nilwala Ganga) | 3.07 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-10-12 23:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.16 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-12 23:08:00 | Pitabeddara (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2026-10-12 23:06:48 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-10-12 23:05:57 | Thawalama (Gin Ganga) | 3.39 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-10-12 23:06:55 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-10-12 22:08:07 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-12 23:03:56 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-12 23:04:25 | Magura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-12 23:06:50 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-12 23:02:04 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-12 23:01:38 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-12 23:02:33 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-12 23:03:09 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-12 23:03:57 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-12 23:01:53 | Thalgahagoda (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-12 23:06:06 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-12 23:03:12 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-12 18:02:58 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.000 |  |
| 2026-10-12 23:00:10 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-12 23:01:56 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:01:47 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 23:00:47 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 23:02:14 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:08:31 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 23:06:02 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-12 23:02:28 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:38 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:04:59 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-12 23:00:58 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | -0.011 |  |
| 2026-10-12 23:01:49 | Ellagawa (Kalu Ganga) | 6.86 | 🟢 Normal | -0.020 |  |
| 2026-10-12 23:09:13 | Baddegama (Gin Ganga) | 2.40 | 🟢 Normal | -0.020 |  |
| 2026-10-12 23:04:42 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.029 |  |
| 2026-10-12 23:03:12 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.032 |  |
| 2026-10-12 23:06:33 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.064 |  |
| 2026-10-12 22:06:03 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | -0.070 |  |
| 2026-10-12 22:05:39 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)