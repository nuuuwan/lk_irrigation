# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_18:25:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,076 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Norwood — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 18:25:59 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-12 18:18:13 | Panadugama (Nilwala Ganga) | 4.82 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-10-12 18:14:12 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:13:35 | Norwood (Kelani Ganga) | 1.66 | 🟡 Alert | 0.587 | 🔺 Rising |
| 2026-10-12 18:08:30 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-12 18:08:18 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.020 |  |
| 2026-10-12 18:07:58 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.121 |  |
| 2026-10-12 18:07:20 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:07:14 | Dunamale (Aththanagalu Oya) | 2.47 | 🟢 Normal | -0.029 |  |
| 2026-10-12 18:05:43 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.740 | 🔺 Rising |
| 2026-10-12 18:05:30 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:04:27 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-10-12 18:04:27 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | -0.051 |  |
| 2026-10-12 18:04:09 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-12 18:03:38 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-12 18:03:22 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.040 |  |
| 2026-10-12 18:03:08 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-10-12 18:03:04 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.021 |  |
| 2026-10-12 18:02:58 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:46 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-12 18:02:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:32 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:15 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-12 18:02:13 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.040 |  |
| 2026-10-12 18:02:08 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-10-12 18:02:06 | Glencourse (Kelani Ganga) | 11.62 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-10-12 18:02:05 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.039 |  |
| 2026-10-12 18:02:05 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 18:01:55 | Badalgama (Maha Oya) | 3.21 | 🟢 Normal | -0.043 |  |
| 2026-10-12 18:01:52 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:44 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-10-12 18:01:44 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:39 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:38 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:31 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:29 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 18:01:22 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-12 18:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-12 18:00:50 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 18:00:39 | Putupaula (Kalu Ganga) | 1.82 | 🟢 Normal | 0.023 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 18:13:35 | Norwood (Kelani Ganga) | 1.66 | 🟡 Alert | 0.587 | 🔺 Rising |
| 2026-10-12 18:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-12 18:05:43 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.740 | 🔺 Rising |
| 2026-10-12 18:18:13 | Panadugama (Nilwala Ganga) | 4.82 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-10-12 18:04:27 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-10-12 18:03:08 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-10-12 18:02:06 | Glencourse (Kelani Ganga) | 11.62 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-10-12 18:03:38 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-12 18:02:46 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-12 18:08:30 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-12 18:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-12 18:00:39 | Putupaula (Kalu Ganga) | 1.82 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-12 18:00:50 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 18:01:29 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 18:25:59 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-12 18:02:05 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 18:02:08 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-10-12 18:02:58 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:52 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:39 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:32 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:04:09 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:05:30 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:44 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:38 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:14:12 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:15 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-12 18:01:22 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-12 18:01:44 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-10-12 18:08:18 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.020 |  |
| 2026-10-12 18:03:04 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.021 |  |
| 2026-10-12 18:07:14 | Dunamale (Aththanagalu Oya) | 2.47 | 🟢 Normal | -0.029 |  |
| 2026-10-12 18:02:05 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.039 |  |
| 2026-10-12 18:03:22 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.040 |  |
| 2026-10-12 18:02:13 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.040 |  |
| 2026-10-12 18:01:55 | Badalgama (Maha Oya) | 3.21 | 🟢 Normal | -0.043 |  |
| 2026-10-12 18:04:27 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | -0.051 |  |
| 2026-10-12 18:07:58 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)