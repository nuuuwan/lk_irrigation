# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_23:07:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,765 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Holombuwa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 23:07:32 | Holombuwa (Kelani Ganga) | 3.08 | 🟡 Alert | -0.039 |  |
| 2026-10-07 23:07:31 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-10-07 23:06:02 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-07 23:05:53 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:05:45 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:05:19 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-07 23:05:13 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -21.670 |  |
| 2026-10-07 23:04:44 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.062 |  |
| 2026-10-07 23:04:28 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-10-07 23:04:19 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:04:05 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-10-07 23:03:57 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-07 23:03:47 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.059 |  |
| 2026-10-07 23:03:42 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-07 23:03:35 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-07 23:03:33 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-07 23:03:30 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | -21.670 |  |
| 2026-10-07 23:03:27 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-10-07 23:03:13 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-10-07 23:03:07 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-10-07 23:02:54 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-10-07 23:02:41 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-07 23:02:35 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:02:27 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:02:19 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | -0.021 |  |
| 2026-10-07 23:02:12 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-10-07 23:01:57 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:01:38 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 23:01:13 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-10-07 23:01:10 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:00:35 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:31:12 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 23:07:32 | Holombuwa (Kelani Ganga) | 3.08 | 🟡 Alert | -0.039 |  |
| 2026-10-07 22:07:15 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | 0.476 | 🔺 Rising |
| 2026-10-07 23:02:12 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-10-07 23:02:54 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-10-07 23:03:35 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-07 23:02:41 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-07 23:05:19 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-07 23:03:33 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-07 18:03:09 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-07 23:03:57 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-07 23:03:42 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-07 23:01:38 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 23:04:19 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:05:45 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:01:57 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:03:15 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:00:32 | Panadugama (Nilwala Ganga) | 4.72 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:02:27 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:00:35 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:05:53 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:09:53 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:08:22 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:01:10 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:02:35 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-07 23:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:31:12 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -0.007 |  |
| 2026-10-07 23:07:31 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-10-07 23:03:27 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-10-07 23:03:13 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-10-07 23:03:07 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-10-07 23:01:13 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-10-07 23:04:28 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-10-07 22:03:57 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.019 |  |
| 2026-10-07 23:06:02 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-07 23:04:05 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-10-07 23:02:19 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | -0.021 |  |
| 2026-10-07 23:03:47 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.059 |  |
| 2026-10-07 23:04:44 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.062 |  |
| 2026-10-07 23:05:13 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -21.670 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)